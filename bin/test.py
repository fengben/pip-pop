import os
from docopt import docopt
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session

requests = session()


class Requirements(object):                     #Requitement(r1)
    def __init__(self, reqfile=None):
        super(Requirements, self).__init__()
        self.path = reqfile                             #self.path=a.txt
        self.requirements = []                          #self.requirements=[]

        if reqfile:                                             #True
            self.load(reqfile)                                  #self.load(a.txt)

    def __repr__(self):
        return '<Requirements \'{}\'>'.format(self.path)

    def load(self, reqfile):
        if not os.path.exists(reqfile):                                         #pass
            raise ValueError('The given requirements file does not exist.')

        finder = PackageFinder([], [], session=requests)                        #object finder= new Class PackageFinder
        for requirement in parse_requirements(reqfile, finder=finder, session=requests): #guess : yield lines
            if requirement.req:
                if not getattr(requirement.req, 'name', None):
                    # Prior to pip 8.1.2 the attribute `name` did not exist.
                    requirement.req.name = requirement.req.project_name
                self.requirements.append(requirement.req)                       #self.requirements=[] + 'requirement.req'


    def diff(self, requirements, ignore_versions=False, excludes=None):
        r1 = self
        r2 = requirements
        results = {'fresh': [], 'stale': []}

        # Generate fresh packages.
        other_reqs = (
            [r.name for r in r1.requirements]
            if ignore_versions else r1.requirements
        )

        for req in r2.requirements:
            r = req.name if ignore_versions else req

            if r not in other_reqs and r not in excludes:
                results['fresh'].append(req)

        # Generate stale packages.
        other_reqs = (
            [r.name for r in r2.requirements]
            if ignore_versions else r2.requirements
        )

        for req in r1.requirements:
            r = req.name if ignore_versions else req

            if r not in other_reqs and r not in excludes:
                results['stale'].append(req)

        return results


def diff(r1, r2, include_fresh=False, include_stale=False, excludes=None):
    include_versions = True if include_stale else False     #False
    excludes = excludes if len(excludes) else []             #[]

    try:
        r1 = Requirements(r1)                                       #
        r2 = Requirements(r2)                                       #
    except ValueError:
        print('There was a problem loading the given requirements files.')
        exit(os.EX_NOINPUT)

    results = r1.diff(r2, ignore_versions=True, excludes=excludes)

    if include_fresh:
        for line in results['fresh']:
            print(line.name if include_versions else line)

    if include_stale:
        for line in results['stale']:
            print(line.name if include_versions else line)


def main():
    #args = docopt(__doc__, version='pip-diff')

    # kwargs = {
    #         'r1': args['<reqfile1>'],
    #         'r2': args['<reqfile2>'],
    #         #'r1': args['a.txt'],
    #         #'r1': args['b.txt'],
    #         'include_fresh': args['--fresh'],
    #         'include_stale': args['--stale'],
    #         'excludes': args['<package>']
    #     }

    diff('a.txt','b,txt',True,)

if __name__ == '__main__':
    main()
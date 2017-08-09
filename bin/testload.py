import os
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session

requests=session()

class Requirements(object):                     #Requitement(r1)
    def __init__(self, reqfile=None):
        super(Requirements, self).__init__()
        self.path = reqfile                             #self.path=a.txt
        self.requirements = []                          #self.requirements=[]
        print(type(self.requirements))

        if reqfile:                                             #True
            self.load(reqfile)
    def load(self, reqfile):
        if not os.path.exists(reqfile):  # pass
            raise ValueError('The given requirements file does not exist.')

        finder = PackageFinder([], [], session=requests)  # object finder= new Class PackageFinder
        for requirement in parse_requirements(reqfile, finder=finder, session=requests):  # guess : yield lines
            if requirement.req:  # requirement.req=abc    req.name=content
                if not getattr(requirement.req, 'name', None): #grtattr(x,'y')==x.y
                    # Prior to pip 8.1.2 the attribute `name` did not exist.
                    requirement.req.name = requirement.req.project_name
                self.requirements.append(requirement.req)

if __name__=='__main__':
    instance = Requirements('a.txt')
    #str=instance.requirements
    #print(str[1])              #instance.requirements[0]='abc'  len=line   each line is an element
    # print(type(instance.requirements)) #type=list
    # print(type(instance.requirements[0]))
    # for r in instance.requirements:
    #     print(type(r))
    #     print(r.name)
    # a=['abc','def']
    # for l in a:
    #     print(type(l))
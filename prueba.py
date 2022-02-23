from statistics import variance


class animal:
    pass
class vaca(animal):
    pass
class  becerro(vaca):
    pass
print (becerro.__bases__)
print (animal.__subclasses__())
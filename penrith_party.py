import os
import random


class Person:

    def __init__(self,id=0,vaccinated=True,diseased=False):
        self.__id = id
        self.__vaccinated = vaccinated
        self.__diseased = diseased

    @property
    def id(self):
        return self.__id

    @property
    def vaccinated(self):
        return self.__vaccinated

    @vaccinated.setter
    def vaccinated(self,value):
        self.__vaccinated = value

    @property
    def diseased(self):
        return self.__diseased

    @diseased.setter
    def diseased(self,value:bool):
        self.__diseased = value


class Location:

    def __init__(self,name='Penrith',population_size=10000):
        self.__name = name
        self.__population_size= population_size
        self.__population = []

        i=0
        while i<self.__population_size:
            vaccinated = False
            diseased = False
            if random.uniform(0,1) < 0.1:
                vaccinated = True
            if random.uniform(0,1) < 0.002:
                diseased = True
            self.__population.append(Person(vaccinated=vaccinated,diseased=diseased))
            i+=1

    @property
    def name(self):
        return self.__name

    @property
    def population_size(self):
        return self.__population_size

def run_model():

    location = Location()


if __name__=='__main__':
    run_model()
import random
import numpy as np



class school:
    course_list = {}

    r


class student(school):

    taken_courses = {}
    name = ""
    gender = ""
    age = ""

    def __init__(self, name, age):
            self.name = name
            self.age = age

    def addclass(self, class_topic, teacher_name):
        if class_topic in self.course_list:
            self.taken_courses[class_topic]= teacher_name
            self.course_list[class_topic][teacher_name].append(self.name)
    






class teacher(school):
    teaches_courses =[]
    name = ""
    gender = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age


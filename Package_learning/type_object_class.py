#   Zuqing xie
#   Uni Stuttgart
#   developing time 2021/7/22 15:40
print(type(type))
print(type(int))
class person:
    pass
a = person()
print(type(a))
print(type(person))
#结论：person这个类是由type这个方法生成的对象，和int，str概念一样

print(person.__base__)
#结论，如果没有特殊说明继承关系的话，
# 所有的类都会继承object类。而且object是最顶层的基类
#type也是一个类，但是同时也是一个对象
print(type.__base__)
print(type(object))
print(object.__base__)




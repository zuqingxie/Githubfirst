#   Zuqing xie
#   Uni Stuttgart
#   developing time 2021/7/22 13:27

##函数也是可以成为变量的
def ask(name = "boby"):
    print(name)
myname = ask
myname("abc")
#
# #类也是变量，也可以赋值给别人！！！
class person:
    def __init__(self):
        print("this is a person")

def decorater():
    print("dec start")
    return ask
#
# Teacher = person
#
#Teacher_Tom = Teacher()

obj_list= []
obj_list.append(ask)
obj_list.append(person)
obj_list.append(decorater)
for a in obj_list:
    print(a())
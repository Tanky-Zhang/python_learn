# 类和对象


class Student():

    # __init__是一个特殊方法用于在创建对象时进行初始化操作,就是Java中的构造方法
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 学习函数
    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age <= 18:
            print('%s只能观看《熊出没》' % self.name)
        else:
            print('%s正在观看大电影' % self.name)


if __name__ == '__main__':
    stu1 = Student('小明', 80)
    stu1.study('Java')
    stu1.watch_movie()

    stu2 = Student('hhh', 10)
    stu2.study('hhh')
    stu2.watch_movie()

print('------------------------------------------------------------------------------------------------')


# 可见行问题

# Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则仍然可以访问到它们，下面的代码就可以验证这一点

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()

'''
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻，
关于这一点可以看看我的《Python - 那些年我们踩过的那些坑》文章中的讲解。
'''
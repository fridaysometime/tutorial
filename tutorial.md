# Tutorials

## Git

Download [Git](https://git-scm.com/)

Online interactive git tutorial: [Try git](https://try.github.io/levels/1/challenges/1)  

Codecademy git course: <https://www.codecademy.com/learn/learn-git>

Git tutorial:

-   vogella: <http://www.vogella.com/tutorials/Git/article.html#gitdefintion_localrepositories>  

-   atlassian: <https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud>

Config username and email before commit: <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com

## Fiddler

Download [Fiddler](http://www.telerik.com/fiddler)

[Youtube fiddler tutorial](https://www.youtube.com/watch?v=gujBKFGwjd4&index=1&list=PLvmaC-XMqeBbw72l2G7FG7CntDTErjbHc)  

[Capture mobile web traffic with fiddler](http://www.cantoni.org/2013/11/06/capture-android-web-traffic-fiddler)  

## Charles proxy

Download [Charles](https://www.charlesproxy.com/download/)

-   Crack Link: <http://pan.baidu.com/s/1i59mEcX> password: zuyu  

-   Backup `charles.jar` and copy crack to installation folder(C:\\Program Files\\Charles\\lib)

iOS devices SSL Certificates configuration: [official doc](https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/)

-   Set your iOS device to use Charles as its HTTP proxy in the Settings app > Wifi settings.

-   Open Safari and browse to <https://chls.pro/ssl>. Safari will prompt you to install the SSL certificate.  

-   If you are on iOS 10.3 or later, open the Settings.app and navigate to General > About > Certificate Trust

Settings, and find the Charles Proxy certificate, and switch it on to enable full trust for it.  

Charles tutorial: <https://www.raywenderlich.com/154244/charles-proxy-tutorial-ios>

## Selenium

## Appium

## python Unittest & pytest

    Design test framework and cases  
    Data driven test case  

### Unittest

-   Create python unittest in pycharm
-   Create run configuration as Python tests --> Uniitests
-   Select Target as Path and specify a folder if run all tests
-   Or Select Python if run specific test
-   e.g:&lt;test_file_name>.&lt;test_class_name>.\[&lt;test_method>]
-   Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be modules or packages importable from the top-level directory of the project (this means that their filenames must be valid identifiers).
-   Run unittest:  
    ```python
    python -m unittest discover
    ```

-   [Improve Your Python: Understanding Unit Testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)

### pytest

The `pytest` framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
[official website](https://docs.pytest.org/en/latest/)

## URL RESTful

parse URL:  

```python
from urlparse import urlsplit, parse_qsl
url = "http://www.example.org/default.html?user=admin&password=Bdclab123"
query = urlsplit(url).query
params = parse_qsl(query)
print query
print dict(params)
```

## Python OOP
[Improve Your Python: Python Classes and Object Oriented Programming](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)

### Inheritance

What's the difference?
> `SomeBaseClass.__init__(self)`

means to call SomeBaseClass's `__init__`. while

> `super(Child, self).__init__()` or `super(self.__class__,self).__init__()`

means to call a bound `__init__` from the parent class that follows Child in the instance's method resolution order.

source code [link](/src/inheritance.py)

```python
class Person(object):
    def __init__(self, name):
        self.name = name
        self.age = 18

    def print_bio(self):
        print "bio..."
        for k, v in vars(self).iteritems():
            print "{}: {}".format(k, v)


class Customer(Person):
    def __init__(self, name, rank):
        # call super __init__() before self __init__()
        super(Customer, self).__init__(name)
        # super(self.__class__, self).__init__(name)
        self.rank = rank


class Staff(Person):
    def __init__(self):
        name = 'new staff'
        Person.__init__(self, name) # call base class __init__() method
        self.staff_no = 10086

    def print_bio(self):
        # override base class method
        print "override super method, print bio:"
        print "staff no: ", self.staff_no
        print "staff name: ", self.name


def print_person_bio(*persons):
    for p in persons:
        p.print_bio()
        print "-" * 20


if __name__ == '__main__':
    person = Person('person1')
    customer = Customer('vip customer', 9)
    staff = Staff()

    person.print_bio()
    print "-" * 20
    customer.print_bio()
    print "-" * 20
    staff.print_bio()


    # polymorphism
    # print_person_bio(person,customer,staff)
```
### module, packages

```python
if __name__ == '__main__':
  main()
```

### @staticmethod, @classmethod, instance method (self)  

[The definitive guide on how to use static, class or abstract methods in Python](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

[why self? & \__init__() is not a constructor](https://www.programiz.com/article/python-self-why)

@classmethod: used as overloading constraction methods
@staticmethod: for better organization within class
```python
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def display_date(self):
        print "{}/{}/{}".format(self.month, self.day, self.year)

    @classmethod
    def from_string(cls, date_as_string):
        """
        as a factory method to instantiate Date instance  

        :param date_as_string: 'dd-MM-yyyy'
        :return: Date instance
        """
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_valid_date(date_string):
        day, month, year = map(int, date_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == '__main__':
    class_attr = set(dir(Date))

    date_str1 = '6-26-2017'
    date_str2 = '16-26-2017'
    print Date.is_valid_date(date_str2)
    date1 = Date.from_string(date_str1)

    # print dir(date1)
    for attr in [x for x in dir(date1) if not x.startswith('__')]:
        print "attribute: {}-->{}, if callable: {}".format(attr, getattr(date1, attr), callable(getattr(date1, attr)))

    # only date attributes
    print date1.__dict__
    for k, v in date1.__dict__.items():
        print k, getattr(date1, k)
```

### Data Hiding
```python
class BankAccount(object):
    __class_hiding_member = "I'm now hiding"
    total = 0

    def __init__(self):
        self.__amount = 0  # keep accessing from outside class
        self.sn = '0000-0000-0000'

    def deposit(self, money):
        # can access a hiding member within it's own class
        # provide getter, setter methods to interact hiding member from outside
        self.__amount += money

    def balance(self):
        return self.__amount

    def withdraw(self, money):
        # TODO: there might be a potential logic issue here try to fix it
        if self.balance() >= money:
            self.__amount -= money
            return money
        else:
            raise Exception("Not enough money!")

    def transfer(self):
        # implement this method
        pass


if __name__ == '__main__':
    acc1 = BankAccount()
    acc1.sn = '1234-5678-6666'
    print acc1.__amount
    acc1.__amount = 9999
    print "default balance: ", acc1.balance()
    acc1.deposit(100)
    print "deposit 100: ", "balance: ", acc1.balance()

    try:
        print "withdraw: ", acc1.withdraw(80), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(15), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(5), "balance: ", acc1.balance()
        print "withdraw: ", acc1.withdraw(-100), "balance: ", acc1.balance()
    except Exception as ex:
        print "[reason]", ex.message, "balance: ", acc1.balance()

    # can still access hiding member with vars()
    # print vars(acc1)
    # print vars(BankAccount)
    #
    # print acc1._DataHiding__amount
    # print acc1._DataHiding__class_hiding_member
```


## Regular expression

## Jekins

## Linux commands

-   wget  
-   rpm  
-   yum  
-   systemctl  

    -   modify firewall setting
    -   start stop service

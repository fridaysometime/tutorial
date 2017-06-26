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
        python -m unittest discover


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

## python OOP

oop <https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/>
class inheritance

### self

### module, packages

```python
if __name__ == '__main__':
  main()
```

### @staticmethod, @classmethod, instance method

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

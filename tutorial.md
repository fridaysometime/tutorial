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

[sample code link](/src/inheritance.py)

### module, packages

```python
if __name__ == '__main__':
  main()
```

### @staticmethod, @classmethod, instance method (self)

[The definitive guide on how to use static, class or abstract methods in Python](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

[why self? & \_\_init\_\_() is not a constructor](https://www.programiz.com/article/python-self-why)

@classmethod: used as overloading constraction methods
@staticmethod: for better organization within class

[sample code link](/src/class_method.py)

### Data Hiding

[sample code link](/src/BankAccount.py)

## Regular expression

## Jekins

## Linux commands

-   wget  
-   rpm  
-   yum  
-   systemctl  

    -   modify firewall setting
    -   start stop service

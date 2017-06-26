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

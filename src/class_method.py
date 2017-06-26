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
    # iterate object attributes
    for attr in [x for x in dir(date1) if not x.startswith('__')]:
        print "attribute: {}-->{}, if callable: {}".format(attr, getattr(date1, attr), callable(getattr(date1, attr)))

    # only data member attributes
    print vars(date1)

    for k, v in date1.__dict__.iteritems():
        print k, getattr(date1, k), type(getattr(date1, k))

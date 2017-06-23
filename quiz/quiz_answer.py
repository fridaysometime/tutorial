# quiz 1: reverse array
# define a function using given list(or string) as parameter and return a reversed list
list_to_reverse = [1, 2, 3, 4]
string_to_reverse = "abcd"
def get_reversed_list(given_list):
    reversed_iterator = reversed(given_list)
    # Note that reversed(...) does not return a list.
    print "r is type of {}".format(type(reversed_iterator))
    # You can get a reversed list using list(reversed(array)).
    reversed_list = list(reversed_iterator)
    return reversed_list


print get_reversed_list(list_to_reverse)
print get_reversed_list(string_to_reverse)
# #########################################################################################################

# quiz 2: immutable types are called by value
# define a function swaps 2 numbers. e.g use a=4,b=5 as 2 parameters, after calling the function a=5,b=4
# the easy way (a,b) = (b,a)
a = 4
b = 5

def swap_2_number(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    print "inside swap: num1={},num2={}".format(num1, num2)
    return num1, num2


print "before swap a={},b={}".format(a, b)
swap_2_number(a, b)
print "after  swap but without reassign a={},b={}".format(a, b)
a, b = swap_2_number(a, b)
print "after swap with reassign a={},b={}".format(a, b)

# #########################################################################################################




# quiz 3: string formatting
# wraps a given string with specific html tag
# output should look like below:
# <div>1st line wraps with div</div>
# <p>2nd line wraps with p</p>
# <a>3rd line wraps with a</a>
html_tags = ['a', 'p', 'div']
text_to_wrap = ['1st line wraps with div', '2nd line wraps with p', '3rd line wraps with a']

def get_html_string(tag, text):
    return "<{tag}>{text}</{tag}>".format(tag=tag, text=text)

print(map(get_html_string, reversed(html_tags), text_to_wrap))

# or use lambda expression
print map(lambda tag, text: "<{tag}>{text}</{tag}>".format(tag=tag, text=text), reversed(html_tags), text_to_wrap)

# #########################################################################################################




# quiz 4: string manipulation
str1 = "    remove only tailing white spaces and print its string representation     "
# expected result: '    remove only tailing white spaces and print its string representation'

str2 = "print the index of 'target'?"  # 19
# expected result: 19

str3 = "https://www.userinfo.com/login?username=admin&password=Bdclab123"  # filter out username and password
# expected result: {username:'admin',password:'Bdclab123'}

print "str1 result: ", repr(str1.rstrip())
print "str2 result: ", str2.index("'target'")
temp_userinfo_list = str3[str3.index('?') + 1:].split('&')
username_list = temp_userinfo_list[0].split('=')
password_list = temp_userinfo_list[1].split('=')
print "str3 result: ", dict([tuple(username_list), tuple(password_list)])  # init a dict passing a list with 2 tuples

# #########################################################################################################



# quiz 5: built-in method range to create a list then
# use this list as stack to push an item in the end, then pop the last one.
int_array = [x for x in range(10)]
print int_array

int_array.append(10) # append to the last position
poped = int_array.pop() # pop the last one
print poped
print int_array

# #########################################################################################################


# quiz 6: function returns another function then calling the returned function
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def get_func(operator):
    op_map = {'+': add, '-': minus}
    return op_map[operator]


n1 = 10
n2 = 2
print get_func('+')(n1, n2)
print get_func('-')(n1, n2)

# #########################################################################################################


# quiz 7: data encapsulation
kms_object = dict()
kms_object['network_id'] = 20480
kms_object['system_ids'] = [1572, 1573]
# iterate each item in dict as tuple
for each_item in kms_object.iteritems():
    print each_item

# access property within dict

sca_sys_id = kms_object['system_ids'][0]
cca_sys_id = kms_object['system_ids'][1]

print sca_sys_id, cca_sys_id


# ####################  The End ########################

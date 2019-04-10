

input = """
4
BaseException
Exception : BaseException
LookupError : Exception 
KeyError : LookupError
2
BaseException
KeyError
"""

test_input = """
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
"""


def foo(error):
    raise error

# def main():
#     try:
#         foo()
#     except ZeroDivision:
#         print("ZeroDivision")
#     except OSError:
#         print("OSError")
#     except ArithmeticError:
#         print("ArithmeticError")
#     except FileNotFoundError:
#         print("FileNotFoundError")
#
# main()


errors = {}
data = input.split(' : ')
if len(data) == 1:
    data.append("")
errors[data[0]] = data[1].split()
for j in errors[data[0]]:
    if j not in errors:
        errors[j] = []

print(errors)

catched = []


def been_catched(error):
    if error in catched:
        return True
    if len(errors[error]):
        return any(map(lambda x: been_catched(x), errors[error]))
    return False


for i in range(4):
    error = input
    if been_catched(error):
        print(error)
    else:
        catched.append(error)

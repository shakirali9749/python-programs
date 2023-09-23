




# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()  

# def divide(a, b):
#     return a/b

# print(divide(12,1))


def trace_dispatch(frame, event, arg):
    if event == 'line':
        record_line_execution(frame)

sys.settrace(trace_dispatch)


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2)

import sys


def interactive_module_function(arg0, arg1, args):
    print(f"Running {'/'.join(arg0.split('/')[-3:])} as a script")
    print(f"The 1st argument is: {arg1}")
    print(f"Other arguments are: {args}")


if __name__ == '__main__':
    args = sys.argv

    interactive_module_function(args[0], args[1], args[2:])

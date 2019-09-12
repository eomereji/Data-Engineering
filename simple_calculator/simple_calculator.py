
# simple python calculator program


import argparse


def main():
    parser = argparse.ArgumentParser(description="calculator")
    parser.add_argument("-operation", type=str,
                        help="Which operation do you want to perform? Choose add, sub, mul or div?")
    parser.add_argument("x", type=int, help="You need to enter a number")
    parser.add_argument(
        "y", type=int, help="You need to enter a second number")

    args = parser.parse_args()
    print(calc(args))


def calc(args):
    if args.operation == "add":
        return "{} + {} = {}".format(args.x, args.y, args.x + args.y)
    elif args.operation == "sub":
        return "{} - {} = {}".format(args.x, args.y, args.x - args.y)
    elif args.operation == "mul":
        return "{} * {} = {}".format(args.x, args.y, args.x * args.y)
    elif args.operation == "div":
        return "{} / {} = {}".format(args.x, args.y, args.x / args.y)
    else:
        return "You have chosen an invalid opearation"


if __name__ == "__main__":
    main()


def func(no):
    if (no > 0):
        func(no - 1)
        print(no)
        func(no - 2)


if __name__ == "__main__":
    func(3)
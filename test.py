def func():
    print("Hello world")

    if __name__ == "__main__":
        print("This runs only when file is run directly")

    print("Thank you")

func()
print(__name__)
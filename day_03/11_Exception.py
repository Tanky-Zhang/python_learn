# py中的异常处理


def main():
    try:
        a = 1 / 0
    except Exception as e:
        print(e)
    finally:
        print("finally excute!")


if __name__ == '__main__':
    main()

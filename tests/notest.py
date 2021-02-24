from friendlydb import Friendly


def main():
    with Friendly(path="./test.json") as friend:
        pass


if __name__ == '__main__':
    main()

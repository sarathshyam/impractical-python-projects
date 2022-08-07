import sys
import random


def main():
    first_names = ('boby', 'mob', 'charlie', 'rick')
    last_names = ('nick', 'fury', 'rig', 'max')

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press ENTER else n to quit)\n")

        if try_again.lower() == "n":
            break
    input("\nPress ENTER to exit.")


if __name__ == "__main__":
    main()
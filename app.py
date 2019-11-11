from classes.battlefield import Battlefield


def main():
    battlefield = Battlefield.create_battlefield_from_config()
    battlefield.battle()


if __name__ == '__main__':
    main()

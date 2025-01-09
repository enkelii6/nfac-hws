from argparse import ArgumentParser


def main(word):
    print(word)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('word', type=str)
    args = parser.parse_args()

    main(args.word)

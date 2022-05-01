import random


def get_superlatives():
    superlatives = set()

    with open("./data/superlatives", 'r') as f:
        for word in f:
            superlatives.add(word.strip())

    return superlatives


def print_spam(superlatives):
    for row in range(2):
        for spam in range(4):
            print("SPAM", end=' ')
        print()

    random.shuffle(list(superlatives))
    print(f"{superlatives.pop().upper()} SPAM {superlatives.pop().upper()} SPAM")


def main():
    s = get_superlatives()
    print_spam(s)


if __name__ == '__main__':
    main()

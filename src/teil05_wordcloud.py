# imports as needed
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def alice():
    with open("./data/Teil_05_Alice_in_wonderland.txt", 'r') as f:
        wonderland = f.read()

    return wonderland


def wort_wolke(alice_text):
    my_wordcloud = WordCloud(width=1920, height=1200)

    STOPWORDS.add('said')
    STOPWORDS.add('illustration')

    my_wordcloud.generate(text=alice_text)

    plt.imshow(my_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    alice_text = alice()
    # print(len(alice_text))
    wort_wolke(alice_text)


if __name__ == '__main__':
    main()

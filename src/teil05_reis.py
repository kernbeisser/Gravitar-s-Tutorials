# imports as needed

def reis1():
    print(f"{2**0:27,} Reiskorn")
    for feld in range(1, 65):
        print(f"{2**feld:27,} Reiskörner")

def reis2():
    return 2**64-1

def gewicht(reis):
    gramm = reis * 0.02
    tonnen = gramm / 1000 / 1000
    return tonnen

def main():
    reis1()
    print()
    # print(f"{reis2():27,}")
    print(f"Gewicht aller Reiskörner: {gewicht(reis2()):15,.0f}")

if __name__ == '__main__':
    main()

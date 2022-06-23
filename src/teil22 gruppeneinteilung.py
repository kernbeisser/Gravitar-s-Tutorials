import random
import faker


def teilnehmer() -> list:
    fake = faker.Faker()
    teilnehmer = []
    for _ in range(99):

        teilnehmer.append(fake.name())

    # return "Constantin Peter Jan Simone Jörg Daniela Klaus Dirk Heike Elke".split()
    return teilnehmer


def mischen(teilnehmer: list) -> list:
    random.seed()
    random.shuffle(teilnehmer)
    return teilnehmer


def gruppenbildung(teilnehmer: list, gruppen_groesse: int) -> list:
    for n in range(0, len(teilnehmer), gruppen_groesse):
        yield teilnehmer[n : n + gruppen_groesse]


def main():
    tn = teilnehmer()
    tn_shuffled = mischen(tn)
    for i, gruppe in enumerate(gruppenbildung(tn_shuffled, 3)):
        print(f"Gruppe {i+1:3}: {gruppe[0]}, {gruppe[1]}, {gruppe[2]}")


if __name__ == "__main__":
    main()

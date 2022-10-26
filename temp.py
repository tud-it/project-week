from tabulate import tabulate


def table():
    tabellle = [
        ["one", "two", "three"],
        ["four", "five", "six"],
        ["seven", "eight", "nine"],
    ]

    print(tabulate(tabellle, tablefmt="html"))

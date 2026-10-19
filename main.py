import csv
from SupportCase import SupportCase

def read_cases():
    cases = []

    with open('supportarenden.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if row:
                case = SupportCase(
                    case_id=row[0],
                    customer=row[1],
                    category=row[2],
                    priority=row[3],
                    status=row[4]
                )
                cases.append(case)

    return cases


def main():
    cases = read_cases()

    for case in cases:
        if case.id != "id":
            case.describe()


main()

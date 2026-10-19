import csv


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


class SupportCase:
    def __init__(self, case_id, customer, category, priority, status):
        self.id = case_id
        self.customer = customer
        self.category = category
        self.priority = priority
        self.status = status


    def describe(self):
        print(
            f"id: \t\t{self.id}\n"
            + f"customer: \t{self.customer}\n"
            + f"category: \t{self.category}\n"
            + f"priority: \t{self.priority}\n"
            + f"status: \t{self.status}\n"
        )


def main():
    cases = read_cases()

    for case in cases:
        if case.id != "id":
            case.describe()


main()

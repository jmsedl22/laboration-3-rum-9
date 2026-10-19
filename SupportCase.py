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

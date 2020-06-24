# OOP (Object Oriented Programming)


class TroubleTicket:
    def __init__(self,
                 number,
                 symptom="",
                 severity="service_impacted",
                 urgency="P3",
                 mean_time=0
                 ):
        self.number = number
        self.symptom = symptom
        self.severity = severity
        self.urgency = urgency
        self.mean_time = mean_time

    def __str__(self):
        return f"#{self.number} {self.symptom}"


class PowerTicket(TroubleTicket):
    # Constructor
    def __init__(self, number):
        self.power_type = "PPP"
        # Call Parent or Base Class
        super().__init__(number, symptom="power")


data = [
    PowerTicket(123),
    TroubleTicket(222, "power", "service_impacted", "P1"),
    TroubleTicket(333, "transport", "service_impacted", "P1"),
    TroubleTicket(333, "unknown", "service_impacted", "P1"),
]

for ticket in data:
    if "power" == ticket.symptom:
        print(f"email group one {ticket}")
    elif "transport" == ticket.symptom:
        print(f"email group two {ticket}")
    else:
        print(f"email group X {ticket}")

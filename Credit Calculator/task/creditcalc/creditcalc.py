import math
import argparse


class CreditCalculator:

    def __init__(self):
        self.credit_principal = None
        self.operation_type = None
        self.count_of_periods = None
        self.credit_interest = None
        self.monthly_payment = None
        self.interest_rate = None
        self.differentiate_payment = None
        self.overpayment = None
        self.annuity_payment = None
        self.credit_principal = None
        self.main()

    def active_args(self):
        initialised = 0
        if interest is None:
            self.incorrect_parameters()
        for item in arguments:
            if item is not None:
                initialised += 1
        if initialised < 4:
            self.incorrect_parameters()

    def incorrect_parameters(self):
        print('Incorrect parameters')
        exit()

    def main(self):
        self.active_args()
        self.operation_type_chooser()
        self.calculation_chooser()

    def operation_type_chooser(self):
        self.operation_type = type

    def calc_annuity_monthly_payment(self):
        if payment is None:
            if int(principal) < 0 or int(periods) < 0 or float(interest) < 0:
                self.incorrect_parameters()
            self.credit_principal = int(principal)
            self.count_of_periods = int(periods)
            self.credit_interest = float(interest)
            self.interest_rate = self.credit_interest / 1200
            self.annuity_payment = self.credit_principal * (
                    (self.interest_rate * math.pow(1 + self.interest_rate, self.count_of_periods)) / (
                    math.pow(1 + self.interest_rate, self.count_of_periods) - 1))
            print(f"Your annuity payment = {math.ceil(self.annuity_payment)}!")
            self.overpayment = math.ceil(self.annuity_payment) * self.count_of_periods - self.credit_principal
            print('Overpayment =', math.ceil(self.overpayment))
        elif principal is None:
            self.calc_credit_principal()
        elif periods is None:
            self.calc_count_of_month()

    def calc_count_of_month(self):

        self.interest_rate = float(interest) / 1200
        number_of_periods = self.calc_number_of_periods()
        if number_of_periods % 12 == 0:
            print(f"You need {math.ceil(number_of_periods / 12)} years to repay this credit!")
        elif number_of_periods < 12:
            print(f'You need {math.ceil(number_of_periods)} months to repay this credit!')
        else:
            print(f'You need {math.ceil(number_of_periods // 12)} years and {math.ceil(number_of_periods % 12)} months to repay this credit!')
        self.overpayment = number_of_periods * self.monthly_payment - self.credit_principal
        print('Overpayment = ', self.overpayment)

    def calc_number_of_periods(self):
        if int(payment) < 0 or int(principal) < 0:
            self.incorrect_parameters()
        self.monthly_payment = int(payment)
        self.credit_principal = int(principal)
        return math.ceil(
            math.log(self.monthly_payment / (self.monthly_payment - self.interest_rate * self.credit_principal),
                     1 + self.interest_rate))

    def calc_credit_principal(self):
        if int(payment) < 0 or int(periods) < 0 or float(interest) < 0:
            self.incorrect_parameters()
        self.monthly_payment = int(payment)
        self.count_of_periods = int(periods)
        self.interest_rate = float(interest) / 1200
        self.credit_principal = self.monthly_payment / (
                (self.interest_rate * math.pow(1 + self.interest_rate, self.count_of_periods)) / (math.pow(
            self.interest_rate + 1, self.count_of_periods) - 1))
        self.overpayment = self.monthly_payment * self.count_of_periods - int(self.credit_principal)
        print(f'Your credit principal = {int(self.credit_principal)}!')
        print('Overpayment = ', self.overpayment)

    def calculation_chooser(self):
        if self.operation_type == 'annuity':
            self.calc_annuity_monthly_payment()
        elif self.operation_type == 'diff':
            if payment is None:
                self.calc_differentiate_payment()
            else:
                self.incorrect_parameters()

    def calc_differentiate_payment(self):
        if int(principal) < 0 or int(periods) < 0 or float(interest) < 0:
            self.incorrect_parameters()
        self.count_of_periods = int(periods)
        self.interest_rate = float(interest) / (12 * 100)
        self.credit_principal = int(principal)
        self.overpayment = 0
        for i in range(1, self.count_of_periods + 1):
            self.differentiate_payment = (self.credit_principal / self.count_of_periods) + self.interest_rate * (
                    self.credit_principal - ((self.credit_principal * (i - 1)) / self.count_of_periods))
            print('Month ' + str(i) + ': paid out', math.ceil(self.differentiate_payment))
            self.overpayment += math.ceil(self.differentiate_payment) - self.credit_principal / self.count_of_periods
        print()
        print('Overpayment =', int(self.overpayment))


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
type = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
arguments = [type, principal, periods, interest, payment]

CreditCalculator()

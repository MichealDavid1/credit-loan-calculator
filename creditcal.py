import math
import argparse
parser = argparse.ArgumentParser(description="This is a credit calculator")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()

if not args.type:
    print("Incorrect parameters.")
elif args.type == "annuity":
    if args.payment and args.principal and args.interest:
        principal = args.principal
        payment = args.payment
        interest = args.interest
        i = interest / (12 * 100)
        b = payment - i * principal
        c = payment / b
        d = 1 + i
        n = math.log(c, d)
        n = math.ceil(n)
        a = int(n / 12)
        b = n % 12
        overpay = (payment * n) - principal
        if b > 1 and a > 1:
            print("It will take", a, "years and", b, "months to repay this loan")
        elif b == 0 and a > 1:
            print("It will take", a, "years to repay this loan")
        elif b == 0 and a == 1:
            print("It will take", a, "year to repay this loan")
        elif b == 1 and a == 1:
            print("It will take", a, "year and", b, "month to repay this loan")
        elif b == 1 and a == 0:
            print("It will take", b, "month to repay this loan")
        elif b == 1 and a > 1:
            print("It will take", a, "years and", b, "month to repay this loan")
        print("Overpayment = " + str(int(overpay)))
    elif args.payment and args.periods and args.interest:
        annuity = args.payment
        periods = args.periods
        interest = args.interest
        i = (interest / 100) * (1 / 12)
        a = i + 1
        b = pow(a, periods)
        c = i * b
        d = b - 1
        e = c / d
        principal = annuity / e
        principal = math.floor(principal)
        annuity = math.ceil(annuity)
        overpay = (annuity * periods) - principal
        print("Your loan principal = " + str(principal) + "!")
        print("Overpayment = " + str(overpay))
    elif args.principal and args.periods and args.interest:
        principal = args.principal
        periods = args.periods
        interest = args.interest
        i = (interest / 100) * (1 / 12)
        a = i + 1
        b = pow(a, periods)
        c = i * b
        d = b - 1
        e = c / d
        annuity = principal * e
        annuity = math.ceil(annuity)
        overpay = (annuity * periods) - principal
        print("Your annuity payment = " + str(annuity) + "!")
        print("Overpayment = " + str(int(overpay)))
    else:
        print("Incorrect parameters.")
elif args.type == "diff":
    if args.principal and args.periods and args.interest:
        p = args.principal
        n = args.periods
        interest = args.interest
        i = (interest / 100) * (1/12)
        m = n
        f = 1
        list_ = []
        while f <= n:
            a = p + (i * n)
            b = a / n
            c = (n * p) + ((-p * f) + p)
            e = (c * i) + p
            diff = e / n
            v = math.ceil(diff)
            list_.append(v)
            print("Month " + str(f) + ":" + " payment is " + str(math.ceil(diff)))
            f += 1
            m -= 1
        a = sum(list_)
        overpay = a - p
        print()
        print("Overpayment = " + str(math.ceil(overpay)))
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")

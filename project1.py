import math

list_op = ['log', 'sin', 'cos', 'tan', 'fac', 'sqrt']


def calculator(num1, num2, op):

    match(op):
        case '+':
            return f"sum={num1+num2}"
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            if (num2 == 0):
                return "errro"
            else:
                return num1/num2
        case '//':
            if (num2 == 0):
                return "error"
            else:
                return num1//num2
        case '**':
            return num1**num2
        case '%':
            if (num2 != 0):
                return num1 % num2
            else:
                return "errro"
        case 'abs':
            return (abs(num1), abs(num2))
        case 'pow':
            return pow(num1, num2)
        case 'max':
            return max(num1, num2)
        case'min':
            return min(num1, num2)
        case 'sqrt':
            return math.sqrt(num1)
        case 'sin':
            return round(math.sin(math.radians(num1)))
        case 'cos':
            # این کلمه ابتدا برای این است که تا دو قم اعشار نشون بده
            return round(math.cos(math.radians(num1)))
        case 'tan':
            # برای تانژانت باید این رو بنویسی تا به درجه حساب منه نه رادیان
            return round(math.tan(math.radians(num1)), 2)
        case 'cot':
            return round(1/math.tan(math.radians(num1)), 2)
        case 'log':
            return round(math.log10(num1), 2)
        case 'fac':
            return math.factorial(num1)
        case 'bmm':
            return math.gcd(num1, num2)
        case 'prime':
            if (num1 < 2):
                return "no prime"

            for i in range(2, int(num1**0.5)+1):
                if num1 % i == 0:
                    return "no prime"
            return "prime"
        case 'cmm':
            return math.lcm(num1, num2)
        case 'ave':
            return (num1+num2)/2
        case _:
            return "other"


while True:
    try:

        op = input("enter operator=")

        if op == "exite":
            break
        num1 = int(input("enter number1="))

        if op not in list_op:
            num2 = int(input("num2="))
        else:
            num2 = None

    except Exception as e:
        print(f"error={e}")
        continue

    print(calculator(num1, num2, op))
    print("-" * 80)

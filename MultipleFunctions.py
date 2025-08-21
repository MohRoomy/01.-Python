class Calculator():
    def OddEven():
        num = int(input("Enter the Number: "))
        if ((num%2)==0):
            message = "EVEN"
        else:
            message = "ODD"
        return message
    def Addition(num1,num2):
        add = num1+num2
        return add
    def Subst(num1,num2):
        sub= num1-num2
        return sub
    def Mult(num1,num2):
        mul= num1*num2
        return mul
    def Devid(num1,num2):
        dev = num1/num2
        return dev
    def BMI():
        BMI = float(input("Enter The Your BMI Index : "))
        if BMI < 16:
            text = ("Your Severe Thinness")
        elif BMI < 17:
            text = ("Your Moderate Thinness")
        elif BMI < 18.5:
            text = ("Your Mild Thinness")
        elif BMI < 25:
            text = ("Your Normal Weight")
        elif BMI < 30:
            text = ("Your Overweight")
        else:
            text = ("Your Very Overweight")
        return text
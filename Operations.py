class Fraction():
    ##Atributo##
    denominator = 1
    numerator = 0
    
    ##Fin atributo##

    ##Metodos##

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def print(self):
        print(self.numerator,"/",self.
        denominator)

    ##Multiplicacion##

    def multiply(self,def_multiplication):
        Res_numerator = self.numerator*def_multiplication.numerator
        Res_denominator = self.denominator*def_multiplication.denominator
        Res_multiply = Fraction(Res_numerator,Res_denominator)
        print("El producto de las fracciones es:", Res_numerator,"/",Res_denominator)
        return Res_multiply

    ##Fin multiplicacion##

    ##Divicion##
    def division(self,def_division):
        Res_numerator = self.numerator*def_division.denominator
        Res_denominator = self.denominator*def_division.numerator
        Res_division = Fraction(Res_numerator,Res_denominator)
        print("El cociente de las fracciones es:", Res_numerator,"/",Res_denominator)
        return Res_division

    ##Fin division##

    ##Suma##
    def suma(self,def_suma):
        multiplication_one = self.denominator*numerator_two
        multiplication_two = self.numerator*denominator_two
        Res_denominator = self.denominator*def_suma.denominator
        Res = multiplication_one + multiplication_two
        Res_suma = Fraction(Res,Res_denominator)
        print("El resultado de la suma de fracciones es:", Res,"/",Res_denominator)
        return Res_suma

    ##Fin suma##

    ##Resta##

    def resta(self,def_resta):
        multiplication_one = self.denominator*numerator_two
        multiplication_two = self.numerator*denominator_two
        result_denominator = self.denominator*def_resta.denominator
        result = multiplication_one-multiplication_two
        result_suma = Fraction(result,result_denominator)
        print("El resultado de la resta de fracciones es:", result,"/",result_denominator)
        return result_suma

    ##Fin resta##

print("Ingrese el valor del primer numerador")
numerator_one = int(input())
print("Ingrese el valor del primer denominador")
denominator_one = int(input())
result_one = Fraction (numerator_one,denominator_one)

Fraction_one = Fraction(numerator_one,denominator_one)


print("ingrese el valor del segundo numerador")
numerator_two = int(input())
print("ingrese el valor del segundo denominador")
denominator_two = int(input())
result_two = Fraction (numerator_two,denominator_two)

Fraction_two = Fraction(numerator_two,denominator_two)


Res_multiply = Fraction_one.multiply(Fraction_two)
Res_multiply.print

result_division = Fraction_one.division(Fraction_two)
result_division.print

result_suma = Fraction_one.suma(Fraction_two)
result_suma.print

result_resta = Fraction_one.resta(Fraction_two)
result_resta.print

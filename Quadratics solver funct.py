import math
import fractions
a = float(input("a: "))
while a:
        b = float(input("b: "))
        c = float(input("c: "))
        y = float(input("y: "))
        c1= c-y
        
        print (f'{y}={a}x^2+({b})x+({c})')
        print(f'∴0={a}x^2+({b})x+({c})-({y})')
        print(f'∴0={a}x^2+({b})x+({c1})')
        'SUM, PROD AND DIS'
        sum= -b/a
        prod= c/a
        dis= (b**2) - (4*a*c1)
        print(f'Δ=(b^2)-(4ac)\n={b**2}-(4*{a}*{c1})\n={dis}')
        print ("\n")
        'SOLUTIONS'
        if dis>0:
                x1=( -b + math.sqrt(dis))/(2*a)
                x2=( -b - math.sqrt(dis))/(2*a)

                print('x=(-b+-√Δ)/2a')
                print(f'x\\1=({-b}+√{dis})/(2*{a})\n={x1}')
                print(f'x\\2=({-b}-√{dis})/(2*{a})\n={x2}')
                print(f'Dis > 0. ∴ two real roots: x={x1} and {x2}')
                print('\n')

                sum1 = x1 + x2
                print(f'sum = x\\1 + x\\2\n = {x1} + {x2}\n = {sum1}')
                print('\n')

                prod1 = x1 * x2
                print(f'prod = x\\1 * x\\2\n = {x1} * {x2}\n = {prod1}')
                print('\n')


        elif dis==0:
                x1=( -b + math.sqrt(dis))/(2*a)
                x2=( -b - math.sqrt(dis))/(2*a)

                print('x=(-b+-√Δ)/2a')
                print(f'x\\1=({-b}+√{dis})/(2*{a})\n={x1}')
                print(f'x\\2=({-b}-√{dis})/(2*{a})\n={x2}')
                print(f'Dis = 0. ∴ repeated roots: x={x1} and {x2}')
                print('\n')

                sum1 = x1 + x2
                print(f'sum = x\\1 + x\\2\n = {x1} + {x2}\n = {sum1}')
                print('\n')

                prod1 = x1 * x2
                print(f'prod = x\\1 * x\\2\n = {x1} * {x2}\n = {prod1}')
                print('\n')

        else:print('Dis < 0. ∴ no real roots')


        'OTHER BS'
        xv= (-b/(2*a))
        yv= (a*xv**2)+(b*xv)+c
        print (f'Axis of sym: x =-b/ 2 * a\n    =-{b}/ 2 * {a}\ ={xv}')
        print('\n')
        print(f'Vertex =(({xv}) , (a * {xv}^2 + b *{xv}+c))\n =(({xv}),({a} * {xv}^2 + {b}*{xv}+{c1}))\n =({xv},{yv})')
        print('\n')

        a = float(input("a: "))
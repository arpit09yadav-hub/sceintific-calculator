name=input('Please Enter your name :')
print('Nice to meet you,',name)
print('Choose a Function from the following --->\n \nAlgebraic--> \nAddition, Subtraction, Multiplication, Division, Random number generator.')
print('\nScientific--> \nExponential, Logarithim, Factorial, Fibonacchi, sine(), cosine(), tangent(), cosecant(), secant(), cotangent().')
print('\nData Visualization--> \nNumerical Line Graph, Bar Graph, Pie Chart.')
from numpy import *
from scipy import *
import math 
import random
import numpy as np
import matplotlib.pyplot as plt
ans=[]
while ans!=['']:
    ans=input()
    if ans=='Addition'or ans=='addition':
        break
    elif ans=='Subtraction'or ans=='subtraction':
        break
    elif ans=='Multiplication'or ans=='multiplication':
        break
    elif ans=='Division'or ans=='division':
        break
    elif ans=='Factorial'or ans=='factorial':
        break
    elif ans=='Fibonacchi'or ans=='fibonacchi':
        break
    elif ans=='Exponential'or ans=='exponential':
        break
    elif ans=='Logarithim'or ans=='logarithim':
        break
    elif ans=='sine()'or ans=='sine':
        break
    elif ans=='cosine()'or ans=='cosine':
        break
    elif ans=='tangent()'or ans=='tangent':
        break
    elif ans=='cosecant()'or ans=='cosecant':
        break
    elif ans=='secant()'or ans=='secant':
        break
    elif ans=='cotangent()'or ans=='cotangent':
        break
    elif ans=='Numerical Line Graph'or ans=='numerical line graph':
        break
    elif ans=='Bar Graph' or ans=='bar graph':
        break
    elif ans=='Pie Chart' or ans=='pie chart':
        break
    elif ans=='Random number generator' or ans=='random number generator':
        break
    print('Please enter a valid function.')

if ans=='Addition'or ans=='addition':
    num1=float(input('Enter first number:'))
    num2=float(input('Enter second number:'))
    sum=num1+num2
    print('The sum of the given numbers is:', sum)

elif ans=='Subtraction'or ans=='subtraction':
    n1=float(input('Enter first number:'))
    n2=float(input('Enter second number:'))
    diff=n1-n2
    print('The difference of the two given numbers is: ',diff)

elif ans=='Division'or ans=='division':
    n1=float(input('Enter the Numerator:'))
    n2=float(input('Enter the Denominator:'))
    divi=n1/n2
    print('The required Quotient is:',divi)

elif ans=='Multiplication'or ans=='multiplication':
    n1=float(input('Enter the first number:'))
    n2=float(input('Enter the second number:'))
    multip=n1*n2
    print('The required multiplication is:',multip)

elif ans=='Factorial'or ans=='factorial':
    n=int(input('Enter the Number:'))
    fact=1
    cnt=1
    while cnt<=n:
        fact=fact*cnt
        cnt=cnt+1
    print('The factorial of the given number is:',fact)

elif ans=='Fibonacchi'or ans=='fibonacchi':
    n=int(input('Enter the number of terms you would like to see:'))
    a=0
    b=1
    cnt=1
    next=1 
    while cnt<=n:
        print(a,end=', ')
        next=a+b
        a,b=b,next
        cnt+=1
    print()

elif ans=='Exponential' or ans=='exponential':
    p=float(input('Enter the exponent of (e):'))
    b=math.e**p
    print('The Eulers number (e) raised to the power',p, 'is', b)

elif ans=='Logarithim' or ans=='logarithim':
    a1=int(input('Enter the argument of logarithim (+ve real no.):'))
    a2=int(input('Enter the base of logarithim (+ve real no. other than 1):'))
    a3=math.log(a1,a2)
    print('The Logarithim of', a1,'with the base',a2,'is',a3)

elif ans=='sine()' or ans=='sine':
    ang_degrees=float(input('Enter the argument of sine (Degrees):'))
    ang_radians=np.radians(ang_degrees)
    sin_ang_radians=math.sin(ang_radians)
    print('The value of sine',ang_degrees,'degrees is',sin_ang_radians)

elif ans=='cosine' or ans=='cosine()':
    ang_degrees=float(input('Enter the argument of cosine (Degrees):'))
    ang_radians=math.radians(ang_degrees)
    cos_ang_radians=math.cos(ang_radians)
    print('The value of cosine',ang_degrees,'degrees is',cos_ang_radians)

elif ans=='tangent' or ans=='tangent()':
    ang_degrees=float(input('Enter the argument of tangent (Degrees):'))
    ang_radians=math.radians(ang_degrees)
    tan_ang_radians=math.tan(ang_radians)
    print('The value of tangent',ang_degrees,'degrees is',tan_ang_radians)

elif ans=='cosecant' or ans=='cosecant()':
    ang_degrees=float(input('Enter the argument of cosecant (Degrees):'))
    ang_radians=math.radians(ang_degrees)
    cosec_ang_radians=1/(math.sin(ang_radians))
    print('The value of cosecant',ang_degrees,'degrees is',cosec_ang_radians)

elif ans=='secant' or ans=='secant()':
    ang_degrees=float(input('Enter the argument of secant (Degrees):'))
    ang_radians=math.radians(ang_degrees)
    sec_ang_radians=1/(math.cos(ang_radians))
    print('The value of secant',ang_degrees,'degrees is',sec_ang_radians)

elif ans=='cotangent' or ans=='cotangent()':
    ang_degrees=float(input('Enter the argument of cotangent (Degrees):'))
    ang_radians=math.radians(ang_degrees)
    cot_ang_radians=1/(math.tan(ang_radians))
    print('The value of cotangent',ang_degrees,'degrees is',cot_ang_radians)

elif ans=='Numerical Line Graph' or ans=='numerical line graph':
    title=input('Enter the title of the line graph:')
    x_label=input('Enter the x axis label:')
    y_label=input('Enter the y axis label:')
    print('\n The number of x-axis values must be equal to the number of y-axis values')
    print('Enter the',x_label,'values')
    x_values=list(map(int,input('Please separate the values by a space only.').split()))
    print('\n Enter the',y_label,'values:')
    y_values=list(map(int,input('Please separate the values by a space only.').split()))
    plt.plot(x_values,y_values,marker='o',linestyle='-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

elif ans=='Bar Graph' or ans=='bar graph':
    title=input('Enter the title of the Bar Graph:')
    x_label=input('Enter the x axis Label:')
    y_label=input('Enter the y axis label:')
    print('\n The number of x-axis labels must be equal to the number of y-axis values')
    print('Enter the',x_label,'labels:')
    x_values=list(map(str,input('Please separate the categories by a space and use hyphens between words in one category.').split()))
    print('\n Enter the',y_label,'values:')
    y_values=list(map(int,input('Please separate the values by a space.').split()))
    plt.bar(x_values,y_values,color='blue')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

elif ans=='Pie Chart' or ans=='pie chart':
    title=input('Enter the title of the Pie chart.')
    print('\n Enter the lables of the pie chart.')
    names=list(map(str,input('Separate the labels by a space only').split()))
    print('\n The number of size values should be equal to the number of labels.')
    sizes=list(map(int,input('Enter the values of sizes sepatated by a space only.').split()))
    print('\n Enter the colors of the labels')
    colors=list(map(str,input('Separate the colors by a space only.').split()))
    plt.pie(sizes,labels=names,autopct='%1.1f%%',startangle=140,colors=colors)
    plt.title(title)
    plt.show()

elif ans=='Random number generator' or ans=='random number generator':
    lower_limit=float(input('The random number should be greater than:'))
    upper_limit=float(input('The random number should be lesser than:'))
    if lower_limit>upper_limit:
        print('The lower limit, cannot be greater than the upper limit of the range. Please re-enter the values.')
    elif lower_limit<upper_limit:
        random_num=random.uniform(lower_limit,upper_limit)
        print('The random number is:',random_num)

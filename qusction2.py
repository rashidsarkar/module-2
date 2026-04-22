def compute(a,b):
    fastCal= a**2 + b**2
    secCal= a-b

    try:
       result = fastCal/secCal
       return result
    except ZeroDivisionError:
      print("Division not possible")

compute(5,5)
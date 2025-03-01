try:
    print(10/0)
except:
    print("Error 발생")



try:
    print(10/0)

except ZeroDivisionError as z :
    print("ZeroDivisionError 발생")

except:
    print("Error 발생")
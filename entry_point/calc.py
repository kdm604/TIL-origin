def my_add(num1, num2):
    return num1 + num2

def my_BBA(num1, num2):
    return num1 - num2
    
def my_multi(num1, num2):
    return num1 * num2

def my_divi(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as err:
        return('{}, 0으로는 나눌 수 없습니다.'.format(err))
    else:
        return result
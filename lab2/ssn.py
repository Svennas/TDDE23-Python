import numbers

def sum_num(num):   
    if (num > 9):
        print("Returning: {}".format((num // 10) + (num % 10)))
        return ((num // 10) + (num % 10))   
    else:
        print("Returning: {}".format(num))
        return num  
    
    

def count_pnr(ssn):
    sum = 0
    for i in range (len(ssn)):
        if (i % 2 == 0):
            sum += sum_num(ssn[i] * 2)
        else:
            sum += sum_num(ssn[i])
        print("sum = {}".format(sum))
    return sum
            
    
def con_num(sum):
    close = 0   
    if (sum % 10 == 0):
        close = sum
    else:
        close = (sum // 10) * 10 + 10
    
    return (close - sum)


def check_pnr(ssn):  
    sum = count_pnr(ssn)
    if (con_num(sum) == ssn[-1]):
        return True
    else: 
        return False
    
    
#([9, 5, 0, 9, 0, 8, 5, 5, 5, 2])
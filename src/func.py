from datetime import datetime as d
from time import time

def calc_logger(done_):
    
    time = d.now().strftime('%Y-%m-%d %H:%M')
    path = r'log.csv'
    with open (path,'a') as f:
        f.write(f'{time},  {done_}')

def search_number(s):
    s = s+' '
    digit = ['0','1','2','3','4','5','6','7','8','9']
    op = ['(',')','i','*','/','+','-']
    a=[]
    i = 0
    while i<len(s)-1:
        if s[i] in digit:
            first_i = i
            while (s[i] in digit)and (i<len(s)-1):
                i += 1
            a.append((s[first_i:i]))
        if s[i] in op:
            a.append(s[i])
        i +=1
    a.append(' ')
    return(a)

def remove_(a,pos_op):
    for j in range(2):
        k = pos_op-1
        while k < len(a)-1:
            a[k] = a[k+1] 
            k +=1
    return(a)

def remove_parenth(a,open_,close_):
    for j in range(close_ - open_):
        k = open_+1
        while k < len(a)-1:
            a[k] = a[k+1] 
            k +=1
    return(a)     
    
def mult_div(a):
    i = 0
    while a[i] != ' ':
        while (a[i] != '*')and(a[i] != '/')and(a[i] != ' '):
            i +=1
        if a[i] != ' ':    
            pos_op = i
            if a[pos_op] == '*':
                a[pos_op+1] = str(float(a[pos_op-1])*float(a[pos_op+1]))
            else:
                a[pos_op+1] = str(float(a[pos_op-1])/float(a[pos_op+1]))
            remove_(a,pos_op)
    return(a)

def sum_sub(a):
    i = 0
    while a[i] != ' ':
        while (a[i] != '+')and(a[i] != '-')and(a[i] != ' '):
            i +=1
        if a[i] != ' ':    
            pos_op = i    
            if a[i] == '+':
                a[pos_op+1] = str(float(a[pos_op-1])+float(a[pos_op+1]))
            else:
                a[pos_op+1] = str(float(a[pos_op-1])-float(a[pos_op+1]))
            remove_(a,pos_op)
    return(a)

def search_parenths(a):
    i = 0
    open_ = 0
    close_= 0
    while close_== 0:
        if a[i] == '(':
            open_ = i
        if a[i] == ')':
            close_ = i
        i +=1    
    return(open_,close_)


def perform_parenths(b,open_,close_):
    a = b[open_:close_+1]
    a[-1] = ' '
    while '*' in a:
        a = mult_div(a)
    while '/' in a:
        a = mult_div(a)
    a = sum_sub(a)    
    return a[1]    

def calc_(s):
    a = []
    # s = '17 +234-1+10'
    # s = '17-2*4+20/5-52/26'
    # s = '17-2*4+20/5-2*4+52/26+1'
    # s ='4*6/3'
    # s = '1+(4*5+(7-6/2))-4'
    # s = '(1+(4*5+(7-6/2))-4)-(2*3/6-1)+3 '
    a = search_number(s)
    
    while '(' in a:
        open_, close_ = search_parenths(a)
        a[open_] = perform_parenths(a,open_,close_)
        a = remove_parenth(a,open_,close_)

    while '*' in a:
        a = mult_div(a)
    while '/' in a:
        a = mult_div(a)
    a = sum_sub(a)
    
    result = str(a[0])
    calc_logger(s+'='+result+'\n')    
    return result
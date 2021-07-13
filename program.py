formula = '(((1+1+1+2+3+1234+234+9)/3)+8*23-2342+234)/1+1*(3)+(3+1+3*2/10)='

for _ in range(int(formula.count('('))):

    origin =  formula[formula[0:formula.find(')')].rfind('('):formula.find(')')+1]
    tmp_formula = origin.replace('(', '').replace(')', '')
    sub_flg = False
    div_flg = False
    tmp_num = ''
    tmp_lst = []
    counter = 0

    for index, item in enumerate(list(tmp_formula)):

        if sub_flg == True:
            sub_flg = False
            tmp_lst.append(f'-{item}')
            continue

        if div_flg == True:
            if item == '+' or item == '-' or item == '/' or item == '*':
                tmp_lst.append(str(float(1/int(tmp_num))))
                div_flg = False
            else:
                if index+1 == len(list(tmp_formula)):
                    if tmp_num == '':
                        tmp_lst.append(str(float(1/int(item))))
                    else:
                        tmp_num += item
                        tmp_lst.append(str(float(1/int(tmp_num))))
                        tmp_num = ''
                    div_flg = False
                else:
                    tmp_num += item
                    counter += 1
            continue

        if item == '-':
            tmp_lst.append('+')
            sub_flg = True
        elif item == '/':
            tmp_lst.append('*')
            div_flg = True
        elif sub_flg == False and div_flg == False and counter == 0:
            tmp_lst.append(item)
            
    tmp_formula = ''.join(tmp_lst)

    multicount = tmp_formula.find('*')
    sumcount = tmp_formula.find('+')
    oneback_item = ''

    if multicount > 0 and sumcount > 0:
        cal_flg = False
        for item in tmp_formula.split('*'):
            if cal_flg == True:
                if item.find('+') == -1:
                    tmp_num = item
                else:
                    tmp_num = item[:item.find('+')]
                tmp_formula = tmp_formula.replace(f'{oneback_item}*{tmp_num}', str(float(oneback_item)*float(tmp_num)))
                oneback_item = str(float(oneback_item)*float(tmp_num))
            else:
                if item.find('+') != 0:
                    oneback_item = item[item.rfind('+')+1:]
                else:
                    oneback_item = item
                cal_flg = True
        tmp_formula = str(sum(list(map(float, tmp_formula.split('+')))))

    elif multicount > 0:
        answer = 1
        for item in tmp_formula.split('*'):
            answer *= float(item)
        tmp_formula = str(answer)

    elif sumcount > 0:
        tmp_formula = str(sum(list(map(int, tmp_formula.split('+')))))

    else:
        tmp_formula = tmp_formula

    formula = formula.replace(origin, tmp_formula)

print(formula)
formula = formula[:formula.find('=')]
tmp_list = []
tmp_num = ''
div_flg = False
 
for index, item in enumerate(list(formula)):
    if div_flg == False:
        if item == '/':
            tmp_list.append(tmp_num)
            tmp_num = ''
            tmp_list.append('*')
            div_flg = True
        else:
            if item == '*' or item == '+':
                tmp_list.append(tmp_num)
                tmp_num = ''
                tmp_list.append(item)
            else:
                tmp_num += item
            if len(list(formula)) == index+1:
                tmp_list.append(tmp_num)
        continue
    else:
        if item == '+' or item == '*':
            tmp_list.append(str(1/float(tmp_num)))
            tmp_num = ''
            tmp_list.append(item)
            div_flg = False
        else:
            tmp_num += item
        continue
 
formula = ''.join(tmp_list)
 
for index, item in enumerate(formula.split('*')):
 
    number = item
    if item.find('+') != -1:
        number = item[:item.find('+')]
 
    if index != 0:
        cal_num = str(float(oneback_item) * float(number))
        formula = formula.replace(f'{oneback_item}*{number}', cal_num)
 
    if item.find('+') == -1:
        oneback_item = item
    else:
        oneback_item = item[item.rfind('+')+1:]
 
answer = sum(map(float, formula.split('+')))
print(answer)



formula = '(((1+1+1+2+3+1234+234+9)/3)+8*23-2342+234)/1+1*(3)+(3+1+3*2/10)='

for _ in range(int(formula.count('('))):

    tmp_formula = formula[formula[0:formula.find(')')].rfind('('):formula.find(')')+1]
    formula = formula.replace(tmp_formula, str(eval(tmp_formula.replace('(', '').replace(')', ''))))

print(eval(formula.replace('=', '')))

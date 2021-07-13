formula = '(((1+1+1+2+3+1234+234+9)/3)+8*23-2342+234)/1+1*(3)+(3+1+3*2/10)='

def cal_formula(formula):
    
    tmp_list = []
    tmp_num = ''
    div_flg = False
    sub_flg = False
    
    for index, item in enumerate(list(formula)):

        if sub_flg == True:
            tmp_num += f'-{item}'
            sub_flg = False
            continue

        if div_flg == False:
            if item == '/':
                tmp_list.append(tmp_num)
                tmp_num = ''
                tmp_list.append('*')
                div_flg = True
            else:
                if item == '-':
                    if index != 0:
                        tmp_list.append(tmp_num)
                        tmp_num = ''
                        tmp_list.append('+')
                        sub_flg = True
                    else:
                        tmp_num += item
                    continue
                elif item == '*' or item == '+':
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
                if len(list(formula)) == index+1:
                    tmp_list.append(str(1/float(tmp_num)))
            continue
    
    formula = ''.join(tmp_list)
    flg = False
    for index, item in enumerate(formula.split('*')):
        cal_num = ''
        number = item
        if item.find('+') != -1:
            number = item[:item.find('+')]
    
        if index != 0:
            cal_num = str(float(oneback_item) * float(number))
            formula = formula.replace(f'{oneback_item}*{number}', cal_num)
            if item.find('+') == -1:
                flg = True

        if flg == True:
            oneback_item = cal_num
        else:
            if item.find('+') == -1:
                oneback_item = item
            else:
                oneback_item = item[item.rfind('+')+1:]
    
    return str(sum(map(float, formula.split('+'))))


formula = '(((1+1+1+2+3+1234+234+9)/3)+8*23-2342+234)/1+1*(3)+(3+1+3*2/10)='
formula = formula.replace('=','')

for _ in range(int(formula.count('('))):
    calculate_formula = formula[formula[0:formula.find(')')].rfind('('):formula.find(')')+1]
    tmp_formula = cal_formula(calculate_formula.replace('(', '').replace(')', ''))
    formula = formula.replace(calculate_formula, tmp_formula)
print(float(cal_formula(formula)))

print(eval(formula.replace('=', '')))

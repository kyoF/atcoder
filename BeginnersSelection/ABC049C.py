s = input()
if 'eraser' in s or 'erase' in s:
    s = s.replace('eraser', '').replace('erase', '')
s = s.replace('dreamer', '').replace('dream', '')
print('YES') if s=='' else print('NO')
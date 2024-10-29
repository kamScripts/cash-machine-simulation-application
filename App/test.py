import os.path
width, height = os.get_terminal_size()
def display_note(*args):
    len(args)
    output = ''
    line = '******** ' * len(args)
    middle_line=''
    for arg in args:       
        middle_line+='*'+ f'{arg:^6}' + '* '
    middle_line=middle_line.center(width)

   
    output = line.center(width) + '\n'+ middle_line + '\n'+line.center(width)
    return output
def withdraw_notes(amount_to_withdraw):
    notes = []
    if amount_to_withdraw % 20 == 0:
        for times in range(amount_to_withdraw//20):
            notes.append(20)
    else:
        notes.append(10)
        if amount_to_withdraw != 10:
            for times in range((amount_to_withdraw-10)//20):
                notes.append(20)
    print(notes)           
    output = ''
    line = '******** ' * len(notes)
    middle_line=''
    for note in notes:       
        middle_line+='*'+ f'{note:^6}' + '* '
    middle_line=middle_line.center(width)        
    output = line.center(width) + '\n'+ middle_line + '\n'+line.center(width)
    return output

check_path = os.path.isfile('App\\333666.csv')
print(check_path)

print(len('| £ 300.'))
print(width)

import os
width, height = os.get_terminal_size()

def yellow(text):
    return f"\033[1;33;12m {text} \033[0m "
def red(text):
    return f"\033[1;31;12m {text} \033[0m "
def green(text):
    return f"\033[1;32;12m {text} \033[0m "
def center_input(length, height):
    output ='\n'+ green('*') * length
    output += '\n' * ((height//2)-8)
    print(output)
def withdraw_notes(amount_to_withdraw):
    notes = []
    output = ''
    middle_line=''
    if not isinstance(amount_to_withdraw, int):
        amount_to_withdraw = int(amount_to_withdraw)
    if amount_to_withdraw % 20 == 0:
        for _ in range(amount_to_withdraw//20):
            notes.append(20)
    elif amount_to_withdraw>=30:
        notes.append(10)
        for _ in range((amount_to_withdraw-10)//20):
              notes.append(20)
    else:
          notes.append(10)
    line = '******** ' * len(notes)
    print(repr(line))
    for note in notes:
        middle_line+='*'+ f'{ "£"+str(note):^6}' + '* '
        
    output = green(f'\n{line.lstrip()}\n{middle_line}\n{line}\ntake your notes and continue.')
    return output
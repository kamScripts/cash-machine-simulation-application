def green(text):
    return f"\033[1;32;40m {text} \033[0m "
def red(text):
    return f"\033[1;31;40m {text} \033[0m "
def yellow(text):
    return f"\033[1;33;12m {text} \033[0m "
def red_no_background(text):
    return f"\033[1;31;12m {text} \033[0m "
def green_no_background(text):   
    return f"\033[1;32;12m {text} \033[0m "
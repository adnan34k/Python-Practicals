def pattern(num):
    if num<1:
        print('Please enter a positive number')
        return
    if num!=int(num):
        print('Please enter an integer value')
        return
    # Upper part 
    spaces = num*2 + 2
    nextspace = 3
    for i in range(num):
        if i == 0:
            print(' '*spaces + '+' + ' '*spaces)
            spaces -= 2
        elif i == num-1:
            print(' '*spaces + '+' + ' '*(nextspace // 2) + '*' + ' '*(nextspace // 2) + '+')
            spaces -= 2
            nextspace += 4
        else:
            print(' '*spaces + '+' + ' '*nextspace + '+')
            spaces -= 2
            nextspace += 4
    # Lower part
    spaces = 2
    nextspaces =(num*2 - 1)*2
    for i in range(num):
        if i == num - 1:
            spaces += 2
            print(' '*spaces + '-' + ' '*nextspaces)
        else:
            print(' '*spaces + '+' + ' '*nextspaces + '+')
            spaces += 2
            nextspaces -= 3

num = int(input('Enter number\n'))
pattern(num)


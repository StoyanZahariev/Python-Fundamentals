def palindrome_integers():
    number = input().split(', ')
    for digits in number:
        if str(digits) == str(digits)[::-1]:
            print('True')
        else:
            print('False')


palindrome_integers()

from func import pedro_isa, random_value

def main():
    decoding = pedro_isa()
    num = random_value()
    if decoding['pedro'] == num:
        print('pedro')
    elif decoding['isa'] == num:
        print('isa')

main()

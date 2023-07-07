import jumpcut as Jumpcut
import spread as Spread

def main():
    r = '1'
    l = '2'
    type = 'png'

    #Jumpcut.jumpcut(r, type)
    #Jumpcut.jumpcut(l, type)
    Spread.spread(r, l, type)

    return 'SUCCESS'

if __name__ == "__main__":
    main()
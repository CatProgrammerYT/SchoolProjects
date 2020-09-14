

# Some useless variables
roshen = 1.5
lykas = 2
priceRoshen = float(input("Ціна перших цукерок: "))
priceLykas = float(input("Ціна других цукерок: "))


# Some useless functions
def calc():
    calc1 = roshen * priceRoshen
    calc2 = lykas   * priceLykas
    calc3 = calc1 + calc2


    print("Вартість перших цукерок: " + str(calc1) + ". Вартість других цукерок: " + str(float(calc2)))
    print("Всього заплатили: " + str(float(calc3)))


calc()

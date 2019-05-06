import open1
print("{}".format("WELCOME TO COM PLOT"))
input()
year_list = list()
worth_list = list()
m = None
while m != "end":
    while True:
        c = input("ENTER THE YEAR AND WORTH WITH (,) BETWEEN THEM")
        d = c.split(",")
        try:
            if open1.intigercheck(d[1]) and open1.intigercheck(d[0]):
                break
                pass
        except:
            print("give both of them")
        print("are you joking give numbers")
    year_list.append(int(d[0]))
    worth_list.append(int(d[1]))
    m = input("for next enter anything to end the stream enter (""end"")")
    pass
print(year_list)
print(worth_list)
open1.complot(year_list,worth_list)
def asal_test(p_control):
    """Bir sayının asallığını test eden fonksiyon"""
    div_nums = list()
    num = 2
    while num < p_control:
        if p_control % num == 0:
            div_nums.append(num)
        num = num + 1
    if div_nums == list():
        print("Girdiğiniz sayı asal.")
    else:
        print("Girdiğiniz sayı asal değil!"
              + " Bu sayıyı bölen sayıların listesi aşağıda:")
        print(div_nums)



def ebob_bulma(num1, num2):
    """İki sayının EBOB'unu bulan fonksiyon"""
    div_num_1 = list()
    div_num_2 = list()
    num = 1
    while num < num1:
        if num1 % num == 0:
            div_num_1.append(num)
        num = num + 1
    num = 1
    while num < num2:
        if num2 % num == 0:
            div_num_2.append(num)
        num = num + 1
    intersection = set(div_num_1).intersection(set(div_num_2))
    intersection_list = list(intersection)
    print(f"Girdiğiniz iki sayı için EBOB({num1},{num2}) = {max(intersection_list)} ")
    if max(intersection_list) == 1:
        print(f"\nBu sebeple girdiğiniz {num1} ve {num2} sayıları aralarında asaldır.")
    else:
        print(f"Girdiğiniz {num1} ve {num2} sayıları aralarında asal değildir.")
        print("1 dışında ortak bölenleri:")
        intersection_list.pop(0)
        print(intersection_list)


def iki_sayi_arasi_asallar(num1, num2):
    """İki sayı arasındaki asalları bulen fonksiyon"""
    p_list = list()
    if num1 < num2:
        for i in range(num1, num2 + 1):
            div_num_i = list()
            num = 2
            while num < i:
                if i % num == 0:
                    div_num_i.append(num)
                num = num + 1
            if div_num_i == list():
                p_list.append(i)
        if p_list == list():
            print("Girdiğiniz iki sayı arasında asal sayı bulunmuyor.")
        else:
            print(f"Girdiğiniz iki sayı arasındaki asalların listesi:"
                  + "\n")
            print(p_list)
    else:
        for i in range(num2, num1 + 1):
            div_num_i = list()
            num = 2
            while num < i:
                if i % num == 0:
                    div_num_i.append(num)
                num = num + 1
            if div_num_i == list():
                p_list.append(i)
        if p_list == list():
            print("Girdiğiniz iki sayı arasında asal sayı bulunmuyor.")
        else:
            print(f"Girdiğiniz iki sayı arasındaki asalların listesi:"
                  + "\n")
            print(p_list)


def ekok_bulma(num1, num2):
    div_num_1 = list()
    div_num_2 = list()
    num = 1
    while num < num1:
        if num1 % num == 0:
            div_num_1.append(num)
        num = num + 1
    num = 1
    while num < num2:
        if num2 % num == 0:
            div_num_2.append(num)
        num = num + 1
    intersection = set(div_num_1).intersection(set(div_num_2))
    intersection_list = list(intersection)
    ebob = int(max(intersection_list))
    ekok = int(ebob * (num1 / ebob) * (num2 / ebob))
    print(f"Girdiğiniz iki sayı için EKOK({num1},{num2}) = {ekok} ")


run_0 = True
while run_0:

    intro_0 = ("\nHangi işlemi yapmak istersiniz?"
               "\n-Bir sayının asallığını test etmek için 'z' girin."
               "\n-İki sayı arasındaki asalları bulmak için 'x' girin."
               "\n-İki sayının EBOB'unu bulmak için 'c' girin."
               "\n-İki sayının EKOK'unu bulmak için 'v' girin."
               "\n-Çıkmak için 'q' girin."
               "\n")

    enter_0 = input(intro_0)
    intro_enter_list = ["z", "x", "c", "v", "q",
                        "Z", "X", "C", "V", "Q"]

    run_1 = True
    while run_1:
        if enter_0.lower() not in intro_enter_list:
            enter_0 = input("\nBelirtilen bir değer girmelisiniz!"
                            " Çıkmak istiyorsanız 'q' girmelisiniz." + "\n")
        else:
            run_1 = False

    if enter_0.lower() == "q":
        print("\nİYİ GÜNLER!")
        quit()

    if enter_0.lower() == "z":
        run = True
        while run:
            intro_z = ("\nAsallığını kontrol etmek istediğiniz sayıyı girin."
                       " (Çıkmak için 'q' geri gelmek için 'g' girin.)" + "\n")
            enter_z = input(intro_z)
            try:
                enter_z_num = int(enter_z)
                asal_test(enter_z_num)
            except ValueError:
                if enter_z.lower() == "q":
                    print("\nİYİ GÜNLER!")
                    quit()
                elif enter_z.lower() == "g":
                    run = False
                else:
                    print("\nBelirtilen bir değer girmediniz."
                          " Tekrar deneyin.")

    if enter_0.lower() == "x":
        run = True
        while run:
            intro_x = ("Hangi iki sayı arasındaki asalları bulmak istiyorsanız,"
                       " bu iki sayıdan ilkini girin."
                       "(Çıkmak için 'q' geri gelmek için 'g' girin.)")

            enter_x_1 = input(intro_x)

            try:
                enter_x_1_num = int(enter_x_1)
                enter_x_2 = input("İkinci sayıyı girin")
                try:
                    enter_x_2_num = int(enter_x_2)
                    iki_sayi_arasi_asallar(enter_x_1_num, enter_x_2_num)
                except ValueError:
                    print("\nBelirtilen bir değer girmediniz."
                          " Tekrar deneyin.")
            except ValueError:
                if enter_x_1.lower() == "q":
                    print("\nİYİ GÜNLER!")
                    quit()
                elif enter_x_1.lower() == "g":
                    run = False
                else:
                    print("\nBelirtilen bir değer girmediniz. Tekrar deneyin.")

    if enter_0.lower() == "c":
        run = True
        while run:
            intro_c = ("Hangi iki sayının EBOB'unu bulmak istiyorsanız,"
                       " bu iki sayıdan ilkini girin."
                       "(Çıkmak için 'q' geri gelmek için 'g' girin.)")

            enter_v_1 = input(intro_c)

            try:
                enter_c_1_num = int(enter_v_1)
                enter_v_2 = input("İkinci sayıyı girin")
                try:
                    enter_c_2_num = int(enter_v_2)
                    ebob_bulma(enter_c_1_num, enter_c_2_num)
                except ValueError:
                    print("\nBelirtilen bir değer girmediniz."
                          " Tekrar deneyin.")
            except ValueError:
                if enter_v_1.lower() == "q":
                    print("\nİYİ GÜNLER!")
                    quit()
                elif enter_v_1.lower() == "g":
                    run = False
                else:
                    print("\nBelirtilen bir değer girmediniz. Tekrar deneyin.")

    if enter_0.lower() == "v":
        run = True
        while run:
            intro_v = ("Hangi iki sayının EBOB'unu bulmak istiyorsanız,"
                       " bu iki sayıdan ilkini girin."
                       "(Çıkmak için 'q' geri gelmek için 'g' girin.)")

            enter_v_1 = input(intro_v)

            try:
                enter_v_1_num = int(enter_v_1)
                enter_v_2 = input("İkinci sayıyı girin")
                try:
                    enter_v_2_num = int(enter_v_2)
                    ekok_bulma(enter_v_1_num, enter_v_2_num)
                except ValueError:
                    print("\nBelirtilen bir değer girmediniz."
                          " Tekrar deneyin.")
            except ValueError:
                if enter_v_1.lower() == "q":
                    print("\nİYİ GÜNLER!")
                    quit()
                elif enter_v_1.lower() == "g":
                    run = False
                else:
                    print("\nBelirtilen bir değer girmediniz. Tekrar deneyin.")

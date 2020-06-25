"""a'den b'ye kadar olan sayılardan, x'e tam bölünenlerin toplamını veren bir fonksiyon yazınız."""

mod_list = []

def divide_Funtion(initial_range, end_range, mod):
    total = 0
    for num in range(initial_range, end_range):
        if(num % mod == 0):
            mod_list.append(num)
        for i in range(len(mod_list)):
            total += mod_list[i]
    print(mod, "Değerine tam bölünenlerin toplamı ..: ", total)


def main():
    initial_value = input("Baslangic degerini giriniz..:")
    end_value = input("bitis degerini giriniz..:")
    mod_value = input("Bölme değerlerini giriniz..:")
    divide_Funtion(int(initial_value), int(end_value), int(mod_value))


main()

"""Elemanları interger olan bir array içerisinde birbirine komşu olmayan elemanlarından oluşan alt kümeler oluşturularak bu alt kümeler arasındak toplamı en büyük olan alt kümeyi bulunuz. """


toplam_in = 0
toplam_out = 0
toplam_out_list = []
temp_list = []
int_list = []


def subset_Print(received_value):
    toplam_in_func = 0
    for i in range(received_value, len(int_list), 2):
        if i+2 < len(int_list):
            temp_list.append(int_list[i+2])
            for i in range(len(temp_list)):
                toplam_in_func += temp_list[i]
            toplam_out_list.append(toplam_in_func)
    print(temp_list, " ", toplam_in_func)
    toplam_in_func = 0
    temp_list.clear()


def main(len_value):
    count = 0
    if(len_value <= 2):
        print("2 ve 1 elemanlı dizilerde komşuluk yoktur.")
    elif(len_value >= 3):
        while count < len_value:
            list_num = input("Dizi elemanlarını giriniz ..:")
            int_list.append(int(list_num))
            count += 1
        print("ALT KÜME", " ", "Toplam")
        for i in range(len_value):
            for k in range(i, len_value):
                if i == k or i+1 == k or i == k+1:
                    continue
                else:
                    toplam_out = int_list[k]+int_list[i]
                    toplam_out_list.append(toplam_out)
                    print("[{:>2}, {:>2}] ".format(
                        int_list[i], int_list[k]), " ", toplam_out)
                    if k+2 < len(int_list):
                        temp_list.append(int_list[i])
                        temp_list.append(int_list[k])
                        subset_Print(k)
        print("En büyük değer..: ", max(toplam_out_list))
    else:
        print("Yanlış değer girdiniz")


len_list_value = int(input("Dizi kaç elemandan oluşacak..:"))
main(len_list_value)

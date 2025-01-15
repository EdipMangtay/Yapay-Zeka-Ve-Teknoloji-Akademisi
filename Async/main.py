import time

def my_func_1():
    print("1. fonksiyon başlıyor");
    time.sleep(5);
    print("birinciis bitiyor");


def my_func_2():
    print("2. fonksiyon başlıyor");
    time.sleep(4);
    print("ikinciis bitiyor");

if __name__ == "__main__":
    my_func_1();
    my_func_2();

import threading
import time

def wite_words(word_count, file_name):
    file = open(file_name, "a",  encoding='utf-8')
    for i in range(word_count):
        file.write(f"Какое-то слово № {i+1} \n")
        time.sleep(0.1)
    file.close()
    print(f"Завершилась запись в файла {file_name} ")

start_time1 = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(f"Время выполнения функции: {elapsed_time1} секунд")

start_time2 = time.time()

thread_first = threading.Thread(target=wite_words, args=(10,"example1.txt" ))
thread_second = threading.Thread(target=wite_words, args=(30,"example1.txt" ))
thread_third = threading.Thread(target=wite_words, args=(200,"example1.txt" ))
thread_fourth = threading.Thread(target=wite_words, args=(100,"example1.txt" ))

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourth.start()

thread_first.join()
thread_second.join()
thread_third.join()
thread_fourth.join()

end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print(f"Время выполнения потока: {elapsed_time2} секунд")

conclusion =elapsed_time1 - elapsed_time2

print(f"Скорость потоков быстрее функций на {conclusion} секунд")
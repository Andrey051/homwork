from multiprocessing import Pool
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            read = f.readline()
            all_data.append(read)
            if not read:
                break


files = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]
start = datetime.datetime.now()

for f in files:
    print(f)
    read_info(f)

end = datetime.datetime.now()
time1 = end - start

print(f"Время линейного выполнения программы: {time1}")

# start = datetime.datetime.now()
# if __name__ == "__main__":
#     with Pool(4) as p:
#         p.map(read_info, files)
#     end = datetime.datetime.now()
#     time2 = end - start

#     print(f"Время  многопроцессорного выполнения программы: {time2}")

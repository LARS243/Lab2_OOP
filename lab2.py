import xml.etree.ElementTree as ET
#C:\Users\g\source\repos\Lab2\Lab2\address.csv

import csv
import time
import os

class csv_file:
    def __init__(self, file): # конструктор класса
        self.file = file;
        self.data = self.csv_parser();
        self.repeats, self.floor_counter = self.data_processor();
        
    def csv_parser(self):
        with open(self.file, mode='r', encoding='utf-8') as file: # открываем файл
            matrix = list(); # создаем массив
            csv_file = csv.DictReader(file, delimiter=';'); # парсим csv файл
            for element in csv_file: # проходимся по файлу
                matrix.append((element['city'], element['street'], element['house'], element['floor'])); # добавляем значения в массив
            return matrix; # возвращаем массив
        
    def data_processor(self):# обработка данных
        repeats = dict(); # словарь повтарений
        floor_counter = dict(); # словарь количества зданий
        for element in self.data:
            if ((element[0], element[1], element[2]) in repeats):
                repeats[(element[0], element[1], element[2])] += 1; # если повторение добавляем единицу
            else:
                repeats[(element[0], element[1], element[2])] = 0; # если новый элемент, то добавляем в массив
            if (element[0] in floor_counter):
                floor_counter[element[0]][int(element[3])-1] += 1; # если существует массив по ключу, то прибавляем единицу
            else:
                floor_counter[element[0]] = list(); # если массива нет, то создаем ключ
                for i in range(5):
                    floor_counter[element[0]].append(0) # запалняем массив по ключу нулями
        return repeats, floor_counter;
    
    def print_resualts(self):
        print("Повторения: ");
        for element in self.repeats:
            if (self.repeats[element] > 0):
                print(element[0], element[1], element[2], "\nКоличество упоминаний:", self.repeats[element]+1);
        print("Подсчет домов по этажности:")
        for element in self.floor_counter:
            print("Город:", element);
            for i in range(5):
                print("Домов с максимальным этажем", str(i+1) + ":", self.floor_counter[element][i]);

class xml_file:
    def __init__(self, file): # конструктор класса
        self.file = file;
        self.data = self.xml_parser();
        self.repeats, self.floor_counter = self.data_processor();
        
    def xml_parser(self):
        data = list();
        tree = ET.parse(self.file)
        root = tree.getroot()
        for item in root.findall('item'):
            data.append((item.get('city'), item.get('street'), item.get('house'), item.get('floor')))   

        return data;
        
    def data_processor(self):# обработка данных
        repeats = dict(); # словарь повтарений
        floor_counter = dict(); # словарь количества зданий
        for element in self.data:
            if ((element[0], element[1], element[2]) in repeats):
                repeats[(element[0], element[1], element[2])] += 1; # если повторение добавляем единицу
            else:
                repeats[(element[0], element[1], element[2])] = 0; # если новый элемент, то добавляем в массив
            if (element[0] in floor_counter):
                floor_counter[element[0]][int(element[3])-1] += 1; # если существует массив по ключу, то прибавляем единицу
            else:
                floor_counter[element[0]] = list(); # если массива нет, то создаем ключ
                for i in range(5):
                    floor_counter[element[0]].append(0) # запалняем массив по ключу нулями
        return repeats, floor_counter;
    
    def print_resualts(self):
        print("Повторения: ");
        for element in self.repeats:
            if (self.repeats[element] > 0):
                print(element[0], element[1], element[2], "\nКоличество упоминаний:", self.repeats[element]+1);
        print("Подсчет домов по этажности:")
        for element in self.floor_counter:
            print("Город:", element);
            for i in range(5):
                print("Домов с максимальным этажем", str(i+1) + ":", self.floor_counter[element][i]);

def user_interface():
    aplication_work = True;
    print('Введите директорию файла или "exit" для завершения работы')
    while (aplication_work):
        file_name = input()
        if (file_name == "exit"):
            aplication_work = False;
        elif not os.path.exists(file_name):
            print("Файл не найден")
        else:
            start_time = time.time();
            
            if file_name.endswith('.xml'):
                fil = xml_file(file_name);
                print("Время выполнения программы:", time.time() - start_time);
                fil.print_resualts();
                aplication_work = False;    
                
            elif file_name.endswith('.csv'):
                fil = csv_file(file_name);
                print("Время выполнения программы:", time.time() - start_time);
                fil.print_resualts();
                aplication_work = False;    
            else:
                print("Файл недопустимого формата")

user_interface();
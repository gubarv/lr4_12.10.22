import pickle
class Biblioteka(): # Сoздание библиотеки с переменными: отдел, кол-во книг
    def __init__(self, chapter, book_in):
        self.chapter = chapter
        self.book_in = book_in

    # Конструктор
    def books(self): # Вывод информации о количестве всех книг в отделах библиотеки
        b = b1.book_in + b2.book_in + b3.book_in + b4.book_in
        print("Вы находитесь в отделе " + self.chapter + '.' + 'Сумарное количество книг во всех отделах библиотеки равно ' + str(b))

    def test(self): # unittest
        b = b1.book_in + b2.book_in + b3.book_in + b4.book_in
        return b

    # Сериализация
    def serialize(self):
        with open('hhh.pkl', 'wb') as f:
            pickle.dump(self.book_in, f)
        f.closed

    # Десериализация
    def deserialize(self):
        with open('hhh.pkl', 'rb') as f:
            Biblioteka = pickle.load(f)
        f.closed
        return Biblioteka
    #print(Biblioteka)

    #Деструктор
    #def __del__(self): # Уничтожение экземпляра
    #print("Стелаж" + self.chapter + "не находиться в нашей библиотеке")

#Наследование
class Aftor(Biblioteka): #Дочериний класс авторы
    def __init__(self,chapter, book_in, name_aftor):
        super().__init__(chapter, book_in)
        self.name_aftor = name_aftor
    def aftor_chapter(self): #На каком слаже данный автор
        print("Автор " + self.name_aftor + "находится на стелаже " + self.chapter + '.')

    #Полиморфизм
    def bookss(self):
        print("Количество книг на этом стелаже: " + str(self.book_in))

b1 = Biblioteka("Психология", 115)
b2 = Biblioteka("Наука", 33)
b3 = Biblioteka("История", 54)
b4 = Biblioteka("Художественная литература", 211)
#b1.books()

b1 = Aftor( b1.chapter, b1.book_in, "Иванов ")
b1.aftor_chapter()
b1.bookss()

b1.serialize()
#print(b1.deserialize())
b2.serialize()
#print(b2.deserialize())
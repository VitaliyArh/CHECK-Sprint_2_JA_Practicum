from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    
# МОИ ТЕСТЫ НАЧИНАЮТСЯ ОТСЮДА


    def test_init_books_rating_empty_dict_true(self):
        collector = BooksCollector()                    # создаем экземпляр (объект) класса BooksCollector
        assert collector.books_rating == {}             # проверяем что словарь есть и он пустой

    def test_init_favorites_empty_list_true(self):
        collector = BooksCollector()                    # создаем экземпляр (объект) класса BooksCollector
        assert collector.favorites == []                # проверяем что список есть и он пустой

# --------------------

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()                      # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                 # добавляем в словарь одну книгу
        assert len(collector.get_books_rating()) == 1     # проверяем что книга добавилась в словарь


    def test_add_new_book_checking_rating_of_the_add_book_true(self):
        collector = BooksCollector()                      # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                 # добавляем в словарь одну книгу
        assert collector.books_rating == {'Золушка' : 1}  # удостоверяемся что у добавленной книги рейтинг 1


    def test_add_new_book_cannot_add_book_twice(self):
        collector = BooksCollector()                     # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                # добавляем в словарь одну книгу с ключом 'Золушка'
        collector.add_new_book('Золушка')                # добавляем в словарь второй раз такую же книгу
        assert len(collector.get_books_rating()) == 1    # проверяем что второй раз книга с таким же название не добавилась

# -----------------------

    def test_set_book_rating_cant_set_rating_less_than_one(self):   # нельзя рейтинг сделать меньше 1
        collector = BooksCollector()                                # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                           # добавляем в словарь одну книгу
        collector.set_book_rating('Золушка', 0)                     # присваиваем книге 'Золушка' рейтинг '0'
        assert collector.books_rating == {'Золушка' : 1}            # вызвали метод с параметром рейтинг книги в словаре не поменялся

# -----------------------

    def test_get_book_rating_book_rating_by_name(self):           # получение рейтинга по имени книги
        collector = BooksCollector()                               # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                          # добавляем в словарь одну книгу
        assert collector.get_book_rating('Золушка') == 1           # вызвали метод с параметром


    def test_get_book_rating_no_book_no_rating(self):              # нет книги - нет рейтинга
        collector = BooksCollector()                               # создаем экземпляр (объект) класса BooksCollector
        assert collector.get_book_rating(None) != range(1, 11)     # вызвали метод с параметром

# -----------------------

    def test_get_books_with_specific_rating_list_books_specified_rating(self):  # получение списка книг с указанным рейтингом
        collector = BooksCollector()                                            # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                                       # добавляем в словарь одну книгу
        collector.set_book_rating('Золушка', 8)                                 # меняем рейтинг по умолчанию на 8
        assert collector.get_books_with_specific_rating(8) == ['Золушка']       # вызвали метод класса с параметром

# -----------------------

    def test_get_books_rating_get_current_dict(self):                  # получаем текущий словарь с ДАННЫМИ
        collector = BooksCollector()                                   # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                              # добавляем в словарь одну книгу
        assert collector.get_books_rating() == {'Золушка' : 1}         # вызвали метод класса - вывели текущий словарь с данными


    def test_get_books_rating_get_current_zero_dict(self):             # получаем ПУСТОЙ текущий словарь
        collector = BooksCollector()                                   # создаем экземпляр (объект) класса BooksCollector
        assert collector.get_books_rating() == {}                      # вызвали метод класса - вывели текущий словарь без данных

# -----------------------

                              # добавляет книгу в избранное. Повторно добавить книгу в избранное нельзя.
    def test_add_book_in_favorites_book_added_to_favorites_can_not_be_added_again(self):
        collector = BooksCollector()                 # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')            # добавляем в словарь одну книгу
        collector.add_book_in_favorites('Золушка')   # обращаемся к словарю по параметру, и добавляем книгу в избранное
        collector.add_book_in_favorites('Золушка')   # добавляем ту же книгу повторно
        assert len(collector.favorites) == 1         # вызываем список "Избранное" проверяем количество книг в нём

# -----------------------
    # delete_book_from_favorites — удаляет книгу из избранного, если она там есть.

    def test_delete_book_from_favorites_book_removed_from_favorites(self):  # удаляем книгу из избранного если она там есть
        collector = BooksCollector()                                        # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                                   # добавляем в словарь одну книгу
        collector.add_book_in_favorites('Золушка')
        collector.delete_book_from_favorites('Золушка')                     # с помощью метода удаляем данные из списка избранное
        assert len(collector.favorites) == 0

# -----------------------



    def test_get_list_of_favorites_books_gets_a_list_of_favorite_books(self):   # получаем список избранных книг
        collector = BooksCollector()                                            # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Золушка')                                       # добавляем в словарь одну книгу
        collector.add_book_in_favorites('Золушка')                              # обращаемся к словарю по параметру, и добавляем книгу в избранное
        assert collector.get_list_of_favorites_books() == ['Золушка']           #

# -----------------------






# Нельзя добавить книгу в избранное, если её нет в словаре books_rating.


    def test_add_book_in_favorites_cannot_book_added_to_favorites_if_no_in_dictionary(self):
        collector = BooksCollector()                 # создаем экземпляр (объект) класса BooksCollector
        collector.add_book_in_favorites('Золушка')   # обращаемся к словарю по параметру, и добавляем книгу в избранное
        assert len(collector.favorites) == 1         # вызываем список "Избранное" проверяем количество книг в нём


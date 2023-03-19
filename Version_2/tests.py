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




    def test_init_books_rating_empty_dict_true(self):
        collector = BooksCollector()
        assert collector.books_rating == {}


    def test_init_favorites_empty_list_true(self):
        collector = BooksCollector()
        assert collector.favorites == []


    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        assert len(collector.get_books_rating()) == 1


    def test_add_new_book_checking_rating_of_the_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        assert collector.books_rating == {'Бродяга' : 1}


    def test_add_new_book_cannot_add_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        collector.add_new_book('Бродяга')
        assert len(collector.get_books_rating()) == 1


    def test_set_book_rating_cant_set_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        collector.set_book_rating('Бродяга', 0)
        assert collector.books_rating == {'Бродяга' : 1}


    def test_get_book_rating_book_rating_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        assert collector.get_book_rating('Бродяга') == 1


    def test_get_book_rating_no_book_no_rating(self):
        collector = BooksCollector()
        assert collector.get_book_rating(None) != range(1, 11)


    def test_get_books_with_specific_rating_list_books_specified_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        collector.set_book_rating('Бродяга', 8)
        assert collector.get_books_with_specific_rating(8) == ['Бродяга']


    def test_get_books_rating_get_current_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        assert collector.get_books_rating() == {'Бродяга' : 1}


    def test_get_books_rating_get_current_zero_dict(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == {}


    def test_add_book_in_favorites_book_added_to_favorites_can_not_be_added_again(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        collector.add_book_in_favorites('Бродяга')
        collector.add_book_in_favorites('Бродяга')
        assert len(collector.favorites) == 1


    def test_delete_book_from_favorites_book_removed_from_favorites(self):
        collector =BooksCollector()
        book_name = 'Бродяга'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites


    def test_get_list_of_favorites_books_gets_a_list_of_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Бродяга')
        collector.add_book_in_favorites('Бродяга')
        assert collector.get_list_of_favorites_books() == ['Бродяга']



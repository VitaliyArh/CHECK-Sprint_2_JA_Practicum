from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector :

	# пример теста:
	# обязательно указывать префикс test_
	# дальше идет название метода, который тестируем add_new_book_
	# затем, что тестируем add_two_books - добавление двух книг
	def test_add_new_book_add_two_books(self) :
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

	def test_init_books_rating_empty_dictionary_true(self) :
		collector = BooksCollector()
		# assert collector.books_rating == {}

		assert len(collector.books_rating) == 0  # правка

	def test_init_favorites_empty_list_true(self) :
		collector = BooksCollector()
		# assert collector.favorites == []

		assert len(collector.favorites) == 0  # правка

	def test_add_new_book_add_one_book_true(self) :
		collector = BooksCollector()
		book_name = 'Три поросёнка'
		collector.add_new_book(book_name)
		# assert len(collector.get_books_rating()) == 1

		assert collector.books_rating[book_name] == 1  # правка

	def test_add_new_book_check_rating_of_the_add_book_true(self) :
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		# assert collector.books_rating == {'Три поросёнка': 1}

		assert collector.books_rating['Три поросёнка'] == 1  # правка

	def test_add_new_book_cannot_add_book_twice_true(self) :
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		collector.add_new_book('Три поросёнка')
		# assert len(collector.get_books_rating()) == 1

		assert 'Три поросёнка' in collector.books_rating  # правка

	def test_set_book_rating_cant_set_rating_less_than_one_error(self):    # устанавливаем рейтинг книге (от 1 до 10)
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		collector.set_book_rating('Три поросёнка', 0)
		# assert 'Три поросёнка' in collector.books_rating and collector.books_rating['Три поросёнка'] != 0

		assert collector.books_rating['Три поросёнка'] in range(1, 11)  # правка

	def test_get_book_rating_book_rating_by_name(self) :
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		assert collector.get_book_rating('Три поросёнка') == collector.books_rating['Три поросёнка']  # правка

	def test_get_book_rating_no_book_no_rating(self) :
		collector = BooksCollector()
		book_name = 'Три поросёнка'
		# assert collector.get_book_rating(book_name) != in range(1, 11)

		assert collector.get_book_rating(book_name) == None  # правка

	def test_get_books_with_specific_rating_list_books_specified_rating(self) :
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		collector.add_new_book('Красная шапочка')
		collector.add_new_book('Колобок')
		collector.set_book_rating('Три поросёнка', 7)
		collector.set_book_rating('Красная шапочка', 7)
		# assert collector.get_books_with_specific_rating(7) == ['Три поросёнка']

		assert collector.get_books_with_specific_rating(7) == ['Три поросёнка', 'Красная шапочка']  # правка

	def test_get_books_rating_get_current_dict_true(self) :
		collector = BooksCollector()
		collector.add_new_book('Три поросёнка')
		collector.add_new_book('Красная шапочка')
		collector.add_new_book('Колобок')
		collector.set_book_rating('Три поросёнка', 7)
		collector.set_book_rating('Красная шапочка', 7)

		assert collector.get_books_rating() == {'Три поросёнка' : 7, 'Красная шапочка' : 7, 'Колобок' : 1}  # правка

	def test_add_book_in_favorites_book_add_to_favorites_true(self) :
		collector = BooksCollector()
		book_name = 'Три поросёнка'
		collector.add_new_book(book_name)
		collector.add_book_in_favorites(book_name)
		assert book_name in collector.favorites

	def test_add_book_to_favorites_book_add_to_favorites_twice_cannot_be(self) :
		collector = BooksCollector()
		book_name = 'Три поросёнка'
		collector.add_new_book(book_name)
		collector.add_book_in_favorites(book_name)
		collector.add_book_in_favorites(book_name)
		# assert len(collector.favorites) == 1

		assert collector.favorites.count(book_name) == 1  # ыполнили

	def test_delete_book_from_favorites_book_remove_from_favorites(self) :
		collector = BooksCollector()
		book_name = 'Три поросёнка'
		collector.add_new_book(book_name)
		collector.add_book_in_favorites(book_name)
		collector.delete_book_from_favorites(book_name)
		# assert book_name not in collector.favorites

		# assert not (book_name in collector.favorites)
		assert collector.favorites.count(book_name) == 0  # выполнили

	def test_get_list_of_favorites_books_list_favorite_books_true(self) :
		collector = BooksCollector()
		# book_name = 'Три поросёнка'
		collector.add_new_book('Три поросёнка')
		collector.add_new_book('Красная шапочка')
		collector.add_new_book('Колобок')

		collector.add_book_in_favorites('Красная шапочка')
		collector.add_book_in_favorites('Колобок')

		# print(collector.get_list_of_favorites_books())
		assert collector.get_list_of_favorites_books() == ['Красная шапочка', 'Колобок']




 qa_python

1) test_init_books_rating_empty_dict_true 
               ---- проверяем что словарь books_rating есть и он пустой

2) test_init_favorites_empty_list_true  
               ---- проверяем что список favorites есть и он пустой

3) test_add_new_book_add_one_book 
               ---- проверяем что книга добавилась в словарь

4) test_add_new_book_checking_rating_of_the_add_book_true 
               ---- удостоверяемся что у добавленной книги по умолчании рейтинг 1

5) test_add_new_book_cannot_add_book_twice 
               ---- проверяем что второй раз книга с таким же названием не не добавляется

6) test_set_book_rating_cant_set_rating_less_than_one 
              ---- нельзя рейтинг сделать меньше еденицы "1"

7) test_get_book_rating_book_rating_by_name 
              ---- получение рейтинга по имени книги

8) test_get_book_rating_no_book_no_rating 
              ---- у несуществующей книги (не добавленной) нет рейтинга

9) test_get_books_with_specific_rating_list_books_specified_rating 
              ---- получение списка книг с определённым рейтингом "8"

10) test_get_books_rating_get_current_dict 
              ---- получаем текущий словарь с данными

11) test_get_books_rating_get_current_zero_dict 
              ---- получаем пусто текущий словарь

12) test_add_book_in_favorites_book_added_to_favorites_can_not_be_added_again 
              ---- добавляем книгу в список избранное (favorites) из словаря books_rating. 
                   Повторно добавить книгу нельзя.

13) test_delete_book_from_favorites_book_removed_from_favorites 
              ---- удаляем книгу из списка избранных (favorites)

14) test_get_list_of_favorites_books_gets_a_list_of_favorite_books 
              ---- получаем список избранных книг



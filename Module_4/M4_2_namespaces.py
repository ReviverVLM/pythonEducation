def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()
"""
Функция inner_function() находится в локальном пространстве имён test_function(),
поэтому извне её вызвать нельзя, но в самой test_function() она видна и там её
можно использовать. У глобального пространства нет доступа к внутреннему, в то время,
как внутреннее может обращаться на более высокие уровни
"""

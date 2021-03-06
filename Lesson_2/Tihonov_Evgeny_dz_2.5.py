# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

prices = [57.80, 46.51, 97, 42.8, 9, 8.11, 68.39, 79.50, 2.77, 39, 12.78, 73.6, 79.07]

for i in prices:
    rub, kop = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {kop} коп", end=", ")

print(f"\n\nID в списке до сорт: {id(prices)} - {prices}")
prices.sort()
print(f"ID измененное: {id(prices)} - {prices}")

prices.reverse()
print(prices[0:5])
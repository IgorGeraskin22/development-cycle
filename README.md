# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 4 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – strike всегда 20 очков
#   «4/» - spare всегда 15 очков
#   «34» – сумма 3+4=7
#   «-4» - сумма 0+4=4
# То есть для игры «Х4/34-4» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.


# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state

# You were hired by a young startup. The idea of ​​a startup is to provide a service for calculating the results of games.
# Decided to start with bowling, a simplified version.
#
# Rules such.
#
# Total 10 pins. The game consists of 10 frames. In one frame up to 2 throws, the goal is to knock down all the pins.
# Frame results are written as:
# "X" - "strike", all 10 pins knocked down by the first throw
# "<number>/", for example "4/" - "spare", 4 pins knocked down on the first throw, the rest on the second
# "<number><number>", for example, "34" - 3 pins are knocked down on the first throw, 4 pins on the second.
# instead of <number> there can be a dash "-", for example "-4" - not a single pin was knocked down for the first throw
# The result of the game is a string with a record of the results of frames. There are no separator characters between frames.
# For example, for a 4-frame game, the result record might look like this:
# "Х4/34-4"
# A simplified way of calculating the number of points is proposed:
# "X" - strike is always 20 points
# "4/" - spare always 15 points
# "34" - sum 3+4=7
# "-4" - sum 0+4=4
# That is, for the game "X4/34-4" the sum of points is 20+15+7+4=46
#
# We need to write a python module (named bowling) that provides an API for calculating the number of points:
# a get_score function that takes a game_result parameter. The function must throw exceptions,
# when game_result contains invalid data. Use standard exceptions to the maximum,
# if not enough - create your own.
#
# Be sure to write tests for this module. Place in the tests folder.

# From the current file, make a console utility for determining the number of points using the argparse package
# The script should take the --result parameter and print to the console:
# Number of points for results XXX - uuu.

# TODO here is your code

# When writing code, remember that the customer may want improvements and new features...
# And you might want to use the "State" design pattern,
# see https://clck.ru/Fudd8 and https://refactoring.guru/ru/design-patterns/state

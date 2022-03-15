# -*- coding: utf-8 -*-
import pandas as pd
from collections import Counter
from prettytable import PrettyTable


class Records:
    mytable = PrettyTable()

    def __init__(self, tour_results, winner, count, output):
        self.tour_results = tour_results
        self.winner = winner
        self.count = count
        self.output = output

    def print_result(self):
        count_tour = pd.Series(self.count)
        count_tour = count_tour.to_string(index=False)  # удаляю индексы

        game_data = pd.Series(self.tour_results)
        game_data = game_data.to_string(index=True)  # удаляю индексы

        winner = pd.Series(self.winner)
        winner = winner.to_string(index=False)  # удаляю индексы

        with open(self.output, "a", encoding='utf8') as file:
            file.write(f'### Tour {count_tour}\n{game_data}\nwinner is {winner}\n\n')


# Вывод результатов на консоль
def console_output(output):
    mytable = PrettyTable()
    wins_matches = []
    # имена полей таблицы
    mytable.field_names = ["Игрок ", "сыграно матчей", "всего побед"]
    players = []  # Все игроки
    winner = []  # список победителей
    player_data = []
    with open(output, 'r', encoding='utf8') as file:
        for line in file:
            if len(line) > 15:
                if 'winner' not in line:
                    players.append(line.split(' ')[0])  # собираю в список всех игроков
                if 'winner' in line:
                    string_winner = line.split(' ')[2:3]  # вырезаю из строки имя победителя
                    if 'Ошибка' in string_winner:  # если строка содержит не корректный счет,то беру следующую строку
                        continue
                    # if 'winner' in string_winner: # что бы не попала в список
                    #     continue

                    winner.append(string_winner[0].replace('\n', ''))  # удаляю \n и добавляю в список имя победителя

        number_wins = dict(Counter(winner))  # словарь подсчета количества побед игроков
        number_matches = dict(Counter(players))  # словарь подсчета количество сыграных матчей

        player_wins = list(number_wins.items())  # преобразование словаря количества побед игроков в список
        player_matches = list(number_matches.items())  # преобразование словаря сыграных матчей в список

        merger = sorted(player_wins + player_matches)  # слияние и сортировка  списков

        for i in merger:  # избавляюсь от скобок в списке
            wins_matches.extend(i)

        for player_results in wins_matches:  # сбор данных игроков
            player_data.append(player_results)  # добавляю данные в список

            if len(player_data) == 4:
                player_name, played_matches, victories = player_data[0], str(player_data[3]), str(player_data[1])  # выборка данных
                player_data.clear()
                # формируется список для вывода на консоль
                player_data.append(player_name)
                player_data.append(played_matches)
                player_data.append(victories)
                mytable.add_row(player_data)
                player_data.clear()
    print(mytable)
   

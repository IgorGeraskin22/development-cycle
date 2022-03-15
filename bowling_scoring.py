# -*- coding: utf-8 -*-
import logging
from tournament_record import Records
import collections


class Logger:
    def __init__(self):
        self.file_handler = logging.FileHandler('bowling.log',
                                                encoding='utf8')
        self.log = logging.getLogger('bowling')  # имя логера

    def configure_logging(self):
        self.file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s %(lineno)d %(message)s',
                              datefmt='%d.%m.%Y %H:%M'))
        self.log.setLevel(logging.DEBUG)
        if self.log.hasHandlers():
            self.log.handlers.clear()

        self.log.addHandler(self.file_handler)
        self.file_handler.setLevel(logging.DEBUG)


class PlayerScoring(Logger):
    def __init__(self, players, count_tour, output):
        super().__init__()
        self.frame_list = None
        self.results_game_dict = None
        self.records = None
        self.output = output
        self.winner = None
        self.line_number = None
        self.line_numbers = []
        self.error = None
        self.value = None
        self.clue = None
        self.meaning = None
        self.tour_results = None
        self.player_data = None
        self.correct_account = {}
        self.name_glasses = {}
        self.frame_res = {}
        self.results_one_round = {}
        self.check = {}
        self.count = count_tour
        self.players = players
        self.complete = 0
        self.account_error = ''
        self.player_frame = {}
        self.player_value = None
        self.all_results = {}
        self.all_results2 = {}
        self.list_players_frames = []
        self.players_account = []
        self.results_game = []
        self.player_line_number = None

    def scoring(self):
        self.name_glasses.clear()

        for self.clue, self.player_value in self.players.items():  # Цикл происходит один раз
            self.frame_res.clear()
            clue_meaning = list(self.players.get(self.clue))
            self.meaning = clue_meaning[0]
            self.players_account.append(self.meaning)
            self.line_number = clue_meaning[1]

            # Делю на фреймы. start=1 - начинаю со второго индекса т.е. с 1
            for key, self.value in enumerate(zip(self.meaning.replace('X', 'X-')[0::2],
                                                 self.meaning.replace('X', 'X-')[1::2]), start=1):
                self.frame_res[key] = self.value  # создаю словарь из фреймов
                self.all_results.clear()
                self.all_results[self.clue] = self.frame_res
            self.list_players_frames.append(str(self.all_results))  # составляю список игроков фреймов
            self.line_numbers.append(self.line_number)  # составляю список номеров строк
            # self.all_results.clear()

    def domestic_market(self):
        f = self.line_numbers
        for self.player_number_frames, self.meaning, self.player_line_number in zip(self.list_players_frames, self.players_account,
                                                                                    self.line_numbers):
            v = self.player_line_number
            self.complete = 0
            for self.player_name in eval(self.player_number_frames):  # получаю имя игрока
                self.frame_list = eval(self.player_number_frames).get(self.player_name)  # получаю список фреймов
                for key, value in self.frame_list.items():  # перебор фреймов
                    if self.possible_errors(value, len(self.frame_list)):  # если есть ошибки в счете
                        self.error = 'Ошибка. Смотри лог'  # вместо суммы очков записываю сообщение
                        self.account_error = self.clue, self.meaning, self.error  # запись игрока с ошибкой счета
                        self.frame_res.clear()
                        break

                    if 'X' in value:
                        self.complete += 20
                    elif '/' in value:
                        self.complete += 15
                    elif '-' in value:
                        index_number = value.index('-')
                        if index_number == 1:
                            if value[0].isnumeric():
                                self.complete += int(value[0])
                        else:
                            if value[1].isnumeric():
                                self.complete += int(value[1])

                    else:
                        self.complete += int(value[0]) + int(value[1])  #

                if 'Ошибка. Смотри лог' in self.account_error:
                    self.complete = self.error
                    self.player_data = f'{self.player_name}  {self.meaning}'
                    self.results_one_round[self.player_data] = self.complete
                    self.account_error = ''  # очищаю переменную

                else:
                    self.player_data = f'{self.player_name}  {self.meaning} '
                self.results_one_round[self.player_data] = self.complete
        self.results_game.append(self.results_one_round)
        self.results_game_dict = (self.results_game[0])
        self.data_output()

    def world_market(self):
        self.complete = 0  # Проверить необходимость
        for self.player_number_frames, self.meaning, self.player_line_number in zip(self.list_players_frames, self.players_account,
                                                                                    self.line_numbers):

            self.complete = 0  # Проверить необходимость

            for self.player_name in eval(self.player_number_frames):  # получаю имя игрока
                self.frame_list = eval(self.player_number_frames).get(self.player_name)  # получаю список фреймов
                for self.key, value in self.frame_list.items():  # перебор фреймов
                    if self.possible_errors(value, len(self.frame_list)):  # если есть ошибки в счете
                        self.error = 'Ошибка. Смотри лог'  # вместо суммы очков записываю сообщение
                        self.account_error = self.clue, self.meaning, self.error  # запись игрока с ошибкой счета
                        self.frame_res.clear()  # TODO проверить нужно или нет
                        self.clue = None  # TODO проверить нужно или нет
                        break
                    if self.key < 9:
                        if 'X' in self.frame_list[self.key] and 'X' in self.frame_list[self.key + 1] \
                                and 'X' in self.frame_list[self.key + 2]:
                            self.complete += 30
                            continue

                    if self.key < 9:
                        if 'X' in self.frame_list[self.key] and 'X' in self.frame_list[self.key + 1]:
                            self.complete += 20
                            if self.frame_list[self.key + 2][0].isdigit():
                                self.complete += int(self.frame_list[self.key + 2][0])
                                continue

                            if self.frame_list[self.key + 2][1].isnumeric():
                                self.complete += int(self.frame_list[self.key + 2][1])
                                continue

                    if 'X' in self.frame_list[self.key]:
                        self.complete += 10
                        if self.key < 9:
                            if self.frame_list[self.key + 1][0].isdigit() and self.frame_list[self.key + 1][1].isdigit():
                                self.complete += int(self.frame_list[self.key + 1][0])
                                self.complete += int(self.frame_list[self.key + 1][1])
                                continue

                            else:
                                if self.frame_list[self.key + 1][0].isnumeric():
                                    self.complete += int(self.frame_list[self.key + 1][0])
                                    continue

                                elif self.frame_list[self.key + 1][1].isnumeric():
                                    self.complete += int(self.frame_list[self.key + 1][1])
                                    continue

                    if '/' in self.frame_list[self.key]:
                        self.complete += 10

                        if self.key < 10:
                            if 'X' in self.frame_list[self.key + 1]:
                                self.complete += 10
                                continue

                            if self.frame_list[self.key + 1][0].isdigit():
                                self.complete += int(self.frame_list[self.key + 1][0])
                                continue

                    elif '-' in self.frame_list[self.key]:
                        if self.frame_list[self.key][0].isdigit():
                            self.complete += int(self.frame_list[self.key][0])
                        nn = self.frame_list[self.key][1]
                        if self.frame_list[self.key][1].isdigit():
                            self.complete += int(nn)

                        else:
                            continue

                    elif self.frame_list[self.key][0].isdigit() and self.frame_list[self.key][1].isdigit():
                        self.complete += int(self.frame_list[self.key][0])
                        self.complete += int(self.frame_list[self.key][1])
                    else:
                        self.complete += int(self.frame_list[self.key][0]) or int(self.frame_list[self.key][1])
                if 'Ошибка. Смотри лог' in self.account_error:
                    self.complete = self.error
                    self.player_data = f'{self.player_name}  {self.meaning}'
                    self.results_one_round[self.player_data] = self.complete
                    self.account_error = ''  # очищаю переменную

                else:
                    self.player_data = f'{self.player_name}  {self.meaning} '
                self.results_one_round[self.player_data] = self.complete
        self.results_game.append(self.results_one_round)
        self.results_game_dict = (self.results_game[0])

        self.data_output()

    def data_output(self):
        for player_score, sum_points in self.results_game_dict.items():
            sum_points = str(sum_points)
            if sum_points.isdigit():  # если число
                self.correct_account[player_score] = int(sum_points)

            self.check[player_score] = sum_points

        if not self.correct_account:
            self.winner = 'Ошибка данных'
        else:
            round_winner = max(self.correct_account, key=self.correct_account.get)
            self.winner = round_winner[0:round_winner.find(' ')]  # беру имя победителя из строки
        self.tour_results = {**self.check, **self.correct_account, }  # вывод результатов в файл

        self.records = Records(self.tour_results, self.winner, self.count, self.output)

        self.records.print_result()
        # self.scoring()

    def possible_errors(self, value, len_frame_res):  # возможные ошибки
        if len_frame_res != 10:
            self.log.debug(f'→ Cтрока №{self.player_line_number} "{self.meaning}" Неправильное  количество фреймов!')
            return True

        elif '0' in value:
            self.log.debug(
                f'→ Cтрока №{self.player_line_number} "{self.meaning}" фрейм- "{value[0]}{value[1]}"  Введено неправильное значение')
            return True

        elif '/' in value[0]:
            self.log.debug(
                f'→ Cтрока №{self.player_line_number} "{self.meaning}" фрейм- "{value[0]}{value[1]}" Spare не может быть на первом броске')
            return True

        elif 'X' in value[1]:
            self.log.debug(
                f'→ Cтрока №{self.player_line_number} "{self.meaning}" фрейм- "{value[0]}{value[1]}"  Strike не может быть на втором броске'
            )
            return True

        elif value[0].isdigit() and value[1].isdigit() and int(value[0]) + int(value[1]) >= 10:
            self.log.debug(
                f'→ Cтрока №{self.player_line_number}  "{self.meaning}" фрейм- "{value[0]}{value[1]}"  Сумма одного фрейма не может быть '
                f'больше 9 очков, если не Spare ')
            return True

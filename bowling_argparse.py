# -*- coding: utf-8 -*-
import argparse


class Bowling:
    def __init__(self, game_result):
        self.game_result = game_result
        self.frame_res = {}
        self.complete = 0
        self.total = 0

    def get_score(self):
        for _ in self.game_result:
            for key, value in enumerate(
                    zip(self.game_result.replace('X', 'X-')[0::2], self.game_result.replace('X', 'X-')[1::2]),
                    start=1):  # разобьем на фреймы. start=1 - начинаю со второго индекса т.е. с 1

                self.frame_res[key] = value  # создадим словарь из фреймов

    def domestic_market(self):
        for self.key, self.value in self.frame_res.items():
            self.possible_errors(self.value, len(self.frame_res))
            if 'X' in self.value:
                self.complete += 20
            elif '/' in self.value:
                self.complete += 15
            elif '-' in self.value:
                index_number = self.value.index('-')
                if index_number == 1:
                    if self.value[0].isnumeric():
                        self.complete += int(self.value[0])
                else:
                    if self.value[1].isnumeric():
                        self.complete += int(self.value[1])

            else:
                self.complete += int(self.value[0]) + int(self.value[1])  # складываем очки за 2 броска

        print('domestic_market - ', self.game_result, '-', self.complete)

    def world_market(self):
        self.complete = 0
        for self.key, self.value in self.frame_res.items():
            self.possible_errors(self.value, len(self.frame_res))
            if self.key < 9:
                if 'X' in self.value and 'X' in self.frame_res[self.key + 1] and 'X' in self.frame_res[self.key + 2]:
                    self.complete += 30
                    continue

            if self.key < 9:
                if 'X' in self.value and 'X' in self.frame_res[self.key + 1]:
                    self.complete += 20
                    if self.frame_res[self.key + 2][0].isdigit():
                        self.complete += int(self.frame_res[self.key + 2][0])
                        continue

                    if self.frame_res[self.key + 2][1].isnumeric():
                        self.complete += int(self.frame_res[self.key + 2][1])
                        continue
                    else:
                        self.complete += 10
                        continue

            if 'X' in self.value:
                self.complete += 10
                if self.key < 9:
                    if self.frame_res[self.key + 1][0].isdigit() and self.frame_res[self.key + 1][1].isdigit():
                        self.complete += int(self.frame_res[self.key + 1][0])
                        self.complete += int(self.frame_res[self.key + 1][1])

                    else:
                        if self.frame_res[self.key + 1][0].isnumeric():
                            self.complete += int(self.frame_res[self.key + 1][0])

                        elif self.frame_res[self.key + 1][1].isnumeric():
                            self.complete += int(self.frame_res[self.key + 1][1])

            if '/' in self.value:
                self.complete += 10
                if self.key < 10:
                    if 'X' in self.frame_res[self.key + 1][0]:
                        self.complete += 10
                        continue

                    if self.frame_res[self.key + 1][0].isdigit():
                        self.complete += int(self.frame_res[self.key + 1][0])
                        continue
                    else:
                        if self.frame_res[self.key + 1][1].isdigit():
                            self.complete += int(self.frame_res[self.key + 1][1])
                        continue

            if '-' in self.value:
                if self.value[0].isdigit():
                    self.complete += int(self.value[0])
                else:
                    if self.value[1].isdigit():
                        self.complete += int(self.value[1])
            else:
                if self.value[0].isdigit() and self.value[1].isdigit():
                    self.complete += int(self.value[0])
                    self.complete += int(self.value[1])
                else:
                    self.complete += int(self.value[0]) or int(self.value[1])

        print('world_market - ', self.game_result, '-', self.complete)

    def possible_errors(self, value, len_frame_res):  # возможные ошибки
        if len_frame_res != 10:
            raise ValueError('Не правильно указано  количество фреймов!')
        if '0' in value:
            raise ValueError('Введено неправильное значение')
        elif '/' in value[0]:
            raise ValueError('Spare не может быть на первом броске')
        elif 'X' in value[1]:
            raise ValueError('Strike не может быть на втором броске')
        if value[0].isdigit() and value[1].isdigit() and int(value[0]) + int(value[1]) >= 10:
            raise ValueError('Введено неправильное значение, сумма одного фрейма не может быть больше 9 очков если не '
                             'Spare ')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--INPUT', type=str)
        args = parser.parse_args()
        bouling_argparse = Bowling(args.INPUT)
        bouling_argparse.get_score()
        bouling_argparse.domestic_market()
        bouling_argparse.world_market()
    except Exception as ex:
        result = '4-3/7/3/8/X711627-5'
        bowling = Bowling(result)
        bowling.get_score()
        bowling.domestic_market()
        bowling.world_market()

# Команда запуска программы  
# python bowling_argparse.py --INPUT 4-3/7/3/8/X711627-5

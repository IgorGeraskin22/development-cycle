# -*- coding: utf-8 -*-
from bowling_scoring import PlayerScoring, Logger
import tournament_record
import argparse

INPUT = 'input.txt'
OUTPUT = 'output.txt'


class Treatment:
    def __init__(self, entry, output):
        self.players = {}
        self.entry = entry
        self.output = output
        self.count_tour = 0

    def main(self):  # выборка имени игрока от его счета
        with open(self.entry, 'r', encoding='utf8') as file:
            for line_number, line in enumerate(file, start=1):  # номер строки и сама строка
                line = line.replace('\n', '')  # заменяю символ \n на пустоту
                line = line.split('\t', )  # разбиваю строку на части, используя разделитель  '\t' и возвращаю эти
                # части списком

                if 'winner' in line[0]:
                    logger = Logger()
                    logger.configure_logging()
                    self.count_tour += 1
                    playerscoring = PlayerScoring(self.players, self.count_tour, self.output)
                    playerscoring.scoring()

                    # Внутренняя версия
                    #playerscoring.domestic_market()

                    # Международная версия
                    playerscoring.world_market()

                    self.players.clear()

                if len(line) > 1:
                    self.players[line[0]] = line[1], line_number


def run():
    treatment = Treatment(INPUT, OUTPUT)
    treatment.main()


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        if parser.add_argument('--INPUT') and parser.add_argument('--OUTPUT'):
            args = parser.parse_args()
            treatment_argparse = Treatment(args.INPUT, args.OUTPUT)
            treatment_argparse.main()
    except Exception as ex:
        run()
        tournament_record.console_output('output.txt')

# Команда запуска программы:
# python tournament_launch.py --INPUT input.txt --OUTPUT output.txt

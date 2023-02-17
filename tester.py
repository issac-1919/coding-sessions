import logging
import datetime
import greedy

def init_logs():
    logging.basicConfig(filename='coding_practice_session_logs.logs',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("\nCoding Session on {}".format(datetime.datetime.now()))

def main():
    # logging.info(greedy.coin_change_problem_2())
    logging.info(greedy.coin_change_problem_2())


if __name__ == '__main__':
    init_logs()
    main()
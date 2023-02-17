import logging
import datetime
import greedy, fun, graphs, trees, linked_lists

def init_logs():
    logging.basicConfig(filename='coding_practice_session_logs.logs',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("\nCoding Session on {}".format(datetime.datetime.now()))

def main():
    obj = linked_lists.singly_node()
    logging.info(obj.node(10))
    logging.info(obj.node(14))
    logging.info(obj.node(12))
    logging.info(obj.get_data())
    logging.info(obj.has_next())
    logging.info(obj.display_singly())

if __name__ == '__main__':
    init_logs()
    main()
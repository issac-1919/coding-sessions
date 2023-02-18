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
    obj = linked_lists.singly_llist()
    obj.set_at_front(10)
    obj.set_at_front(21)
    obj.set_at_front(512)
    obj.set_at_rear(52)
    logging.info(obj.display_singly())
    
if __name__ == '__main__':
    init_logs()
    main()
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
    user_network = [
        ('samuel','elen'),
        ('elen', 'karen'),
        ('brock', 'lesnar'),
        ('karen', 'samuel'),
        ('lesnar', 'karen'),
        ('karen', 'brock'),
        ('karen', 'elen')
    ]
    graph_ob = graphs.graph(user_network)
    logging.info(graph_ob)
if __name__ == '__main__':
    init_logs()
    main()
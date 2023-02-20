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
        ('elen','brock'),
        ('sandra', 'brock'),
        ('elen', 'sandra'),
        ('sandra', 'samuel'),
        ('brock', 'sandra')
    ]
    graph_ob = graphs.graph(user_network)
    logging.info(graph_ob.display_graph())
    
    org = "samuel"
    dest = "brock"
    logging.info((f"Path from {org} to {dest}:", graph_ob.get_paths(org, dest)))

if __name__ == '__main__':
    init_logs()
    main()
# create log file at C:\Users\Nikodem\Documents\Embarcadero\Studio\Projects\Multiple Threads\test.log with 'test works' in it

import logging
import sys; 
import time


logname = 'C:\\Users\\Nikodem\\Documents\\Embarcadero\\Studio\\Projects\\Multiple_Threads\\test.log'

logging.basicConfig(filename=logname,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Logging working")
logging.info(sys.version)



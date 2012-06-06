# -*- coding: utf-8 -*-
import time
import logging
log = logging.getLogger(__name__)

def log_duration(func_to_decorate):
    '''Logs the time it takes to execute a function'''
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func_to_decorate(*args, **kwargs)
        elapsed = (time.time() - start)
        
        #print("[TIMING]:%s - %s" % (func_to_decorate.__name__, elapsed))
        log.debug("[TIMING]:%s - %s" % (func_to_decorate.__name__, elapsed))
            
        return result
    wrapper.__doc__ = func_to_decorate.__doc__
    wrapper.__name__ = func_to_decorate.__name__
    return wrapper

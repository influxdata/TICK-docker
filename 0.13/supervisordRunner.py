#!/usr/bin/python

####################################################################
# This is a runner which starts supervisord. Supervisord picks 
# it's config from /etc/supervisor/conf.d/ 
#
# Even after the listener exits, the process group influxdb keeps on
# generating log events as stdout_events_enabled is set to true. 
# So once telegraf starts, the subcribers need to be cleared. 
# Process group influxdblistener is the only subscriber, hence 
# it is safe to clear the callbacks.
#
# @see events.py https://github.com/Supervisor/supervisor 
####################################################################

from supervisor.supervisord import main
from supervisor.events import clear as clearCallbacks
from subprocess import check_output
import threading, re

def clearEventCallbacks():
    while True:
        # wait till telegraf starts
        output = check_output(["ps", "-ef"])
        if re.search(r'telegraf', output):
            # HACK:: Supervisord still keeps on sending events to a listener
            # even if the listener process has exited.
            # Clear the callbacks so no more events are handled, and Error 
            # messgaes are not logged
            clearCallbacks()
            return

if __name__ == '__main__':
    threading.Thread(target=clearEventCallbacks).start()
    main()
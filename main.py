# *************************************************************************** #
#                                                                              #
#    main.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/12/21 17:02:20 by Widium                                    #
#    Updated: 2023/12/21 17:02:20 by Widium                                    #
#                                                                              #
# **************************************************************************** #

from logger import AdvancedLogger

logger = AdvancedLogger(
    log_directory="logs"
)

with logger.logging_context() as tracker:
    print("This message will be logged.")
    print("This message have multiple lines\nThis is the second line\nThis is the third line")

print(tracker.log_path)
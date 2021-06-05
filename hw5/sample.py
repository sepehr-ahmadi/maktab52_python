from person import Person
import logging
logging.basicConfig(force="True")
sub_logger=logging.getLogger("sub")
sub_stream_handler=logging.StreamHandler()
sub_file_handler = logging.FileHandler('sample.log', 'a', encoding='utf-8')
sub_log_format = logging.Formatter("%(asctime)s,-%(name)-10s -%(levelname)-16s -%(msecs)s -%(message)s")
sub_stream_handler.setLevel(logging.INFO)
sub_stream_handler.setFormatter(sub_log_format)
sub_file_handler.setLevel(logging.INFO)
sub_file_handler.setFormatter(sub_log_format)
sub_logger.addHandler(sub_stream_handler)
sub_logger.addHandler(sub_file_handler)


def sub(a, b):

    if b != 0:
        sub_logger.log(logging.DEBUG, "a/b=" + str(a / b))
        return a / b

    #logging.error("Divide by zero!")
    sub_logger.log(logging.ERROR,"Divide by zero!")
    # logging.info("Divide by zero!") this log is error not info


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

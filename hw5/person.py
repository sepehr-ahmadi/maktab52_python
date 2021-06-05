import logging

logging.basicConfig()
person_logger = logging.getLogger("person")
person_stream_handler = logging.StreamHandler()
person_file_handler = logging.FileHandler('person.log', 'a', encoding='utf-8')
person_log_format = logging.Formatter("%(asctime)s,-%(name)-10s -%(levelname)-16s -%(message)s")
person_stream_handler.setLevel(logging.DEBUG)
person_stream_handler.setFormatter(person_log_format)
person_file_handler.setLevel(logging.DEBUG)
person_file_handler.setFormatter(person_log_format)
person_logger.addHandler(person_stream_handler)
person_logger.addHandler(person_file_handler)


class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        person_logger.addHandler(person_stream_handler)
        person_logger.addHandler(person_file_handler)
        # logging.warning("Person created! {} {}".format(self.name, self.family)) initial of class is not warning its just info logging
        person_logger.log(logging.INFO, "thist is info log")
        # logging.info("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            # logging.critical("Invalid age!") its error not critical event
            person_logger.log(logging.ERROR, "invalid age!")
        self._age = 0

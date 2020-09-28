class TextParser(object):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def check_deletion_id_if_exists(message):
        # ex. Delete task id: 1234
        if "Delete task id" in message:
            return message.split(":")[1].strip()

        return None


def get_deletion_id(text_body):
    parser = TextParser(text_body)
    return parser.check_deletion_id_if_exists(text_body)




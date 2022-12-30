class Validator:
    @staticmethod
    def raise_if_str_is_empty_or_whitespace(value, error_message):
        if value == '' or value.isspace():
            raise ValueError(error_message)
""" Validators module for checking integers """


def validate_integer(
        arg_name, arg_value, min_value=None, max_value=None,
        custom_min_message=None, custom_max_message=None
):
    """ validates 'arg_value' is an integer, and optionally falls within specific
        bounds.
        A custom override error message can be provided when min/max are exceeded.

    Args:
        arg_name(str): the name of the argument(used in deult error message)
        arg_value(obj): the value being validated
        max_value(int): optional, specifies the minimum value(inclusive)
        min_value(int): optional, specifies the maximum value(inclusive)
        custom_min_message(str):optional, custom message when the value is smaller
                                than minimum
        custom_max_message(str): optional, custom message when the value is greater
                                than maximum

    Returns: None if the validation passes else to raise an error
    Raises: TypeError if arg_value is not an integer
            ValueError if arg_value does not satisfy the bounds

    """

    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} is not an integer")

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f"{arg_name} cannot be less than {min_value}")

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f"{arg_name} cannot be greater than {max_value}")


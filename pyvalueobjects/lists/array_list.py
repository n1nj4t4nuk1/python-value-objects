from __future__ import annotations

from typing import TypeVar

from pyvalueobjects.abstract.valueobject import ValueObject
from pyvalueobjects.errors.ValueObjectError import ValueObjectError

T = TypeVar('T')


def ArrayList(cls):
    """
    Dynamically creates a value object class for a list of values of a specific type.
    This function returns a class that validates and encapsulates a list of values, ensuring each value is of the specified type.

    :param cls: The class type for the elements in the list.
    :return: A new class _ArrayList that inherits from ValueObject and validates a list of values of type cls.
    """
    class _ArrayList(ValueObject):
        """
        A value object representing a list of values of a specific type. Inherits from ValueObject and validates that the input is a list of the specified type.
        """

        def __init__(self, values: list[cls]):
            """
            Initialize the _ArrayList object with the given list of values.
            :param values: A list of values of type cls.
            """
            super().__init__(values)
            self._sub_value_objects = [cls(value) for value in values]

        def _validate(self, value):
            """
            Validate that the given value is a list.
            :param value: The value to validate.
            :raises: ValueObjectError if the value is not a list.
            """
            super()._validate(value)
            input_type = type(value)
            if input_type != list:
                raise ValueObjectError(f'Input type should be: list.')

    return _ArrayList

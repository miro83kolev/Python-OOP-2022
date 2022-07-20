#open for extension/inheritance/ and closed for modifications

class NumbersValidator:
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f'Value is outside the range [{self.min_value}, {self.max_value}]')


class NegativeNumbersValidator:
    min_value = -1024
    max_value = 0

validators = [
    NumbersValidator(),
    NegativeNumbersValidator()
]

numbers = [-1, 1]
for validator in validators:
    




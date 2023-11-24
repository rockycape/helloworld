from pydantic import BaseModel, ValidationError, validator

class BaseConversionInput(BaseModel):
    number: str
    from_base: int
    to_base: int

    @validator('from_base', 'to_base')
    def check_base_range(cls, value):
        if not (2 <= value <= 36):
            raise ValueError("Base must be between 2 and 36")
        return value

def convert_base(input_data: BaseConversionInput) -> str:
    decimal_number = int(input_data.number, input_data.from_base)

    result = ""
    while decimal_number > 0:
        remainder = decimal_number % input_data.to_base
        result = str(remainder) + result
        decimal_number //= input_data.to_base

    return result if result else "0"

if __name__ == "__main__":
    try:
        # Get input from the user using Pydantic model
        input_data = BaseConversionInput.parse_obj({
            "number": input("Enter the number: "),
            "from_base": int(input("Enter the base of the input number (2-36): ")),
            "to_base": int(input("Enter the base to convert to (2-36): "))
        })

        # Convert to the specified base
        converted_number = convert_base(input_data)

        # Display the result
        print(f"The {input_data.from_base}-based representation of {input_data.number} is: {converted_number} in base {input_data.to_base}")

    except ValidationError as e:
        print(f"Input validation error: {e}")

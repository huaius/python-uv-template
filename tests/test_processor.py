import pytest

from my_uv_template.processor import Processor

@pytest.mark.parametrize("number1,number2,result", [
    ("2","3",5),
    ("10","13",23),
    ("15","3",18),
])
def test_processor(number1, number2, result):
    processor = Processor(number1, number2)
    output = processor.run()
    assert result == output

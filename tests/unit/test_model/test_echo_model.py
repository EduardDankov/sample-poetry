from pydantic import ValidationError

from dkvsample.model.echo_model import EchoModel

SAMPLE_STR_VALUE_1: str = 'SampleValue1'
SAMPLE_STR_VALUE_2: str = 'SampleValue2'
SAMPLE_INT_VALUE: int = 1

class TestEchoModel:
    def test_model_valid_different_parameters(self):
        model = EchoModel(
            skey1=SAMPLE_STR_VALUE_1,
            skey2=SAMPLE_STR_VALUE_2
        )
        assert model.skey1 != model.skey2 and model.skey1 is not None

    def test_model_valid_identical_parameters(self):
        model = EchoModel(
            skey1=SAMPLE_STR_VALUE_1,
            skey2=SAMPLE_STR_VALUE_1
        )
        assert model.skey1 == model.skey2 and model.skey1 is not None 

    def test_model_valid_single_parameter(self):
        model = EchoModel(
            skey1=SAMPLE_STR_VALUE_1
        )
        assert model.skey1 is not None and model.skey2 is None

    def test_model_no_parameters(self):
        model = EchoModel()
        assert model.skey1 is None and model.skey2 is None

    def test_model_invalid_parameter_type(self):
        try:
            model = EchoModel(
                skey1=SAMPLE_INT_VALUE
            )
        except ValidationError as err:
            assert err.error_count() == 1 and 'Input should be a valid string' in err.errors()[0]['msg']

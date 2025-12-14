import pydantic
import pytest
from pyvote.candidates.candidate import Candidate


class TestCandidate:

    def test_constructor_when_given_arguments_expect_to_work(self):
        name = "Ted Robert"
        popularity = 0.001

        candidate = Candidate(name=name, popularity=popularity)

        assert candidate.name == name
        assert candidate.popularity == popularity

    @pytest.mark.parametrize("popularity", (-0.1, 1.1))
    def test_constructor_when_given_invalid_popularity_expect_error(self, popularity):
        with pytest.raises(ValueError):
            Candidate(name="Ted Robert", popularity=popularity)

    def test_change_name_expect_error(self):
        candidate = Candidate(name="Ted Robert", popularity=0.001)
        with pytest.raises(pydantic.ValidationError):
            candidate.name = "Robert Gurtner"

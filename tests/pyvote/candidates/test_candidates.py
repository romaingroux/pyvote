import pytest

from pyvote.candidates.candidate import Candidate


@pytest.fixture
def candidate() -> Candidate:
    """Returns a candidate."""
    candidate = Candidate(name="Candidate 1", popularity=1)
    candidate.get_vote()
    return candidate


@pytest.fixture
def candidate_name(candidate) -> Candidate:
    """Changes the name of candidate fixture and returns it."""
    candidate._name = "Brah"
    return candidate


@pytest.fixture
def candidate_popularity(candidate) -> Candidate:
    """Changes the popularity of candidate fixture and returns it."""
    candidate._popularity = 999
    return candidate


@pytest.fixture
def candidate_votes(candidate) -> Candidate:
    """Changes the votes of candidate fixture and returns it."""
    candidate._votes = 999
    return candidate


class TestCandidate:
    """A test suite for the Candidate class."""

    def test_constructor_when_given_arguments_expect_to_work(self):
        name = "Ted Robert"
        popularity = 0.001

        candidate = Candidate(name=name, popularity=popularity)

        assert candidate.name == name
        assert candidate.popularity == popularity

    def test_constructor_when_given_invalid_popularity_expect_error(self):
        with pytest.raises(ValueError, match=r"popularity must be >= 0 \(-0.1\)"):
            Candidate(name="Ted Robert", popularity=-0.1)

    def test_set_popularity_when_given_invalid_popularity_expect_error(self):

        candidate = Candidate(name="Ted Robert", popularity=0)

        with pytest.raises(ValueError, match=r"popularity must be >= 0 \(-0.1\)"):
            candidate.popularity = -0.1

    def test_equal_when_equal_expect_true(self, candidate):
        assert candidate == candidate  # noqa: PLR0124

    @pytest.mark.parametrize(
        "candidate_1,candidate_2",
        [
            (candidate, candidate_name),
            (candidate, candidate_popularity),
            (candidate, candidate_votes),
        ],
    )
    def test_equal_when_unequal_expect_false(self, candidate_1, candidate_2):
        assert not candidate_1 == candidate_2  # noqa: SIM201

    def test_unequal_when_equal_expect_false(self, candidate):
        assert not candidate != candidate  # noqa: SIM202, PLR0124

    @pytest.mark.parametrize(
        "candidate_1,candidate_2",
        [
            (candidate, candidate_name),
            (candidate, candidate_popularity),
            (candidate, candidate_votes),
        ],
    )
    def test_unequal_when_unequal_expect_true(self, candidate_1, candidate_2):
        assert candidate_1 != candidate_2

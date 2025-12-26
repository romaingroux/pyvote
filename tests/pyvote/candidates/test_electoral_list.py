import pytest

from pyvote.candidates.candidate import Candidate
from pyvote.candidates.electoral_list import ElectoralList


@pytest.fixture
def candidates() -> list[Candidate]:
    """Returns a list of 3 candidate."""
    candidate1 = Candidate(name="Candidate 1", popularity=1)
    candidate2 = Candidate(name="Candidate 2", popularity=1)
    candidate3 = Candidate(name="Candidate 3", popularity=1)
    return [candidate1, candidate2, candidate3]


class TestElectoralList:
    """A test suite for the ElectoralList class."""

    def test_constructor_when_given_non_empty_list_expect_to_work(self, candidates):

        electoral_list = ElectoralList(candidates)

        assert electoral_list._candidates == candidates
        assert electoral_list._candidates_dict == {
            candidate: candidate for candidate in candidates
        }

    def test_constructor_when_list_is_empty_expect_error(self):
        with pytest.raises(ValueError, match="empty candidate list"):
            ElectoralList([])

    @pytest.mark.parametrize("n_candidates,expected_len", ((1, 1), (2, 2), (3, 3)))
    def test_len_expect_number_of_candidates(
        self, n_candidates, expected_len, candidates
    ):
        assert len(ElectoralList(candidates[:n_candidates])) == expected_len

    @pytest.mark.parametrize("candidate_idx", (0, 1, 2))
    def test_get_vote_candidate_expect_candidate_and_list_get_vote(
        self, candidate_idx, candidates
    ):
        candidate: Candidate = candidates[candidate_idx]

        electoral_list = ElectoralList(candidates)
        electoral_list.get_vote_candidate(candidate)

        assert electoral_list._candidates[candidate_idx].votes == 1
        assert electoral_list.votes == 1

    # TODO
    @pytest.mark.parametrize(
        "proportion, n_candidates",
        (
            (0.0, 0),
            (0.33, 0),
            (1.0 / 3.0, 1),
            (0.66, 1),
            (2.0 / 3.0, 2),
            (0.99, 2),
            (1.0, 3),
        ),
    )
    def test_get_top(self, proportion, n_candidates, candidates):

        expected_candidates = candidates[:n_candidates]

        electoral_list = ElectoralList(candidates)

        assert electoral_list.get_top(proportion) == expected_candidates

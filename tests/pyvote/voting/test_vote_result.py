import pytest

from pyvote.candidates.candidate import Candidate
from pyvote.voting.vote_result import VoteResult


@pytest.fixture
def candidates() -> list[Candidate]:
    """Returns a list of Candidates for test usage."""

    candidate_1 = Candidate(name="Teddy Bear", popularity=1)
    candidate_2 = Candidate(name="Winnie the Poo", popularity=2)
    candidate_3 = Candidate(name="Mickey Mouse", popularity=3)

    candidate_1.get_vote()

    candidate_2.get_vote()
    candidate_2.get_vote()

    candidate_3.get_vote()
    candidate_3.get_vote()
    candidate_3.get_vote()

    return [candidate_1, candidate_2, candidate_3]


class TestVoteResult:

    def test_constructor_when_given_all_arguments_expect_to_work(self, candidates):

        result = VoteResult(winners=candidates[1:], candidates=candidates)

        # they are sorted by decreasing number of votes
        assert result._winners == [candidates[2], candidates[1]]
        assert result._candidates == candidates

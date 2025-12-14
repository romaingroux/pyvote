from pyvote.candidates.candidate import Candidate
from pyvote.voting.vote_result import VoteResult


class TestVoteResult:

    candidates = [
        Candidate(name="Teddy Bear", popularity=1.0),
        Candidate(name="Winnie the Poo", popularity=1.0),
    ]

    def test_constructor_when_given_all_arguments_expect_to_work(self):
        statistics = dict.fromkeys(TestVoteResult.candidates, 1)

        result = VoteResult(winners=TestVoteResult.candidates, statistics=statistics)

        assert result.winners == TestVoteResult.candidates
        assert result.statistics == statistics

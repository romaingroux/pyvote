from pyvote.voting.vote_result import VoteResult
from pyvote.candidates.candidate import Candidate

class TestVoteResult:

    candidates = [
        Candidate(name="Teddy Bear", popularity=1.),
        Candidate(name="Winnie the Poo", popularity=1.),
    ]

    def test_constructor_when_given_all_arguments_expect_to_work(self):
        statistics = {candidate:1 for candidate in TestVoteResult.candidates}
        
        result = VoteResult(
            winners=TestVoteResult.candidates,
            statistics=statistics
        )

        assert result.winners == TestVoteResult.candidates
        assert result.statistics == statistics

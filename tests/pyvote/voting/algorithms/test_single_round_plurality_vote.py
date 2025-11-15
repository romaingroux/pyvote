from pyvote.candidates.candidate import Candidate
from pyvote.voting.context import Context
from pyvote.voting.vote_result import VoteResult
from pyvote.voting.algorithms.single_round_plurality_vote import SingleRoundPluralityVote


class TestSingleRoundPluralityVote:

    context = Context(population_size=1000, seed=1234)
    candidates = [
        Candidate(name="Ted", popularity=1.),
        Candidate(name="Winnie", popularity=1.)
    ]

    def test_constructor_when_given_all_arguments_expect_to_work(self):
        voting = SingleRoundPluralityVote(
            TestSingleRoundPluralityVote.candidates, 
            TestSingleRoundPluralityVote.context
        )

        assert voting._candidates == TestSingleRoundPluralityVote.candidates
        assert voting._candidates[0].popularity == 0.5
        assert voting._candidates[1].popularity == 0.5
        assert voting._context == TestSingleRoundPluralityVote.context
    
    def test_vote_when_given_seed_expect_precise_results(self):
        
        results_exp = VoteResult(
            winners=[Candidate(name='Winnie', popularity=0.5)],
            statistics={
                Candidate(name='Ted', popularity=0.5): 484, 
                Candidate(name='Winnie', popularity=0.5): 516
            }
        )

        voting = SingleRoundPluralityVote(
            TestSingleRoundPluralityVote.candidates, 
            TestSingleRoundPluralityVote.context
        )

        results = voting.vote()

        assert results == results_exp

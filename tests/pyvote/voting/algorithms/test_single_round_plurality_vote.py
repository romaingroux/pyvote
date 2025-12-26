import pytest

from pyvote.candidates.candidate import Candidate
from pyvote.voting.algorithms.single_round_plurality_vote import (
    SingleRoundPluralityVote,
)
from pyvote.voting.context import Context
from pyvote.voting.vote_result import VoteResult


@pytest.fixture
def candidates() -> list[Candidate]:
    """Returns a list of Candidates for test usage."""

    return [
        Candidate(name="Teddy Bear", popularity=3),
        Candidate(name="Winnie the Poo", popularity=2),
        Candidate(name="Mickey Mouse", popularity=0),
    ]


@pytest.fixture
def context() -> Context:
    return Context(population_size=1000, seed=1234)


class TestSingleRoundPluralityVote:

    def test_constructor_when_given_all_arguments_expect_to_work(
        self, candidates, context
    ):
        voting = SingleRoundPluralityVote(candidates, context)

        # popularities are normalized in constructor
        candidates[0].popularity = 0.6  # noqa: PLR2004
        candidates[1].popularity = 0.4  # noqa: PLR2004
        candidates[2].popularity = 0.0  # noqa: PLR2004

        assert voting._candidates == candidates
        assert voting._context == context

    def test_vote_when_given_seed_expect_precise_results(self, candidates, context):

        results_exp = VoteResult(
            winners=[candidates[0]],
            candidates=[candidates[0], candidates[1], candidates[2]],
        )

        # popularities are normalized and votes added
        results_exp.winners[0]._votes = 593
        results_exp.winners[0]._popularity = 0.6
        results_exp.candidates[0]._popularity = 0.6
        results_exp.candidates[0]._votes = 593.0
        results_exp.candidates[1]._popularity = 0.4
        results_exp.candidates[1]._votes = 407
        results_exp.candidates[2]._popularity = 0.0
        results_exp.candidates[2]._votes = 0.0

        voting = SingleRoundPluralityVote(candidates, context)
        results = voting.vote()

        assert results.winners == results_exp.winners
        assert results.candidates == results_exp.candidates

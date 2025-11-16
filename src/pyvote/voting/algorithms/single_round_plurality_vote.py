import random

from pyvote.candidates.candidate import Candidate
from pyvote.voting.algorithms.ivoting_system import IVotingSystem
from pyvote.voting.context import Context
from pyvote.voting.vote_result import VoteResult


class SingleRoundPluralityVote(IVotingSystem):
    """The SingleRoundPlurality implements a single round plurality voting system. Under
    this regime, each voter selects a single candidate from the list. The candidate who
    gets the most votes after a single turn wins the election.

    :param candidates: the list of candidates to vote for.
    :param context: the election parameters.
    """

    def __init__(self, candidates: list[Candidate], context: Context) -> None:
        super().__init__(candidates=candidates, context=context)

    def vote(self) -> VoteResult:
        """Runs the vote and returns its results.

        :returns: the election result.
        """
        statistics = dict.fromkeys(self._candidates, 0)
        weights = [candidate.popularity for candidate in self._candidates]

        for _ in range(self._context.population_size):
            vote = random.choices(self._candidates, weights=weights, k=1)[  # nosec B311
                0
            ]
            statistics[vote] += 1

        winner = max(statistics, key=lambda c: statistics[c])
        return VoteResult(winners=[winner], statistics=statistics)

    def _normalize_popularities(self) -> None:
        """Normalizes the popularity of the different candidates such that they sum up
        to 1."""
        total = 0.0

        for candidate in self._candidates:
            total += candidate.popularity

        for candidate in self._candidates:
            candidate.popularity = candidate.popularity / total

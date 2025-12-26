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

        # turn popularities into probabilities
        self._normalize_popularities()

    def vote(self) -> VoteResult:
        """Runs the vote and returns its results.

        :returns: the election result.
        """
        # set seed
        if self._context.seed:
            random.seed(self._context.seed)

        # set votes to 0 (in case)
        for candidate in self._candidates:
            candidate.reset()

        probs = [candidate.popularity for candidate in self._candidates]
        for _ in range(self._context.population_size):
            voted_for: Candidate = random.choices(  # nosec B311
                self._candidates, weights=probs, k=1
            )[0]
            voted_for.get_vote()

        winner = max(self._candidates, key=lambda c: c.votes)
        return VoteResult([winner], self._candidates)

    def _normalize_popularities(self) -> None:
        """Normalizes the popularity of the different candidates such that they sum up
        to 1."""
        popularity_tot = 0.0

        for candidate in self._candidates:
            popularity_tot += candidate.popularity

        for candidate in self._candidates:
            candidate.popularity = candidate.popularity / popularity_tot

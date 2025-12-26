import copy

from pyvote.candidates.candidate import Candidate


class VoteResult:
    """The VoteResult class models the result of an election.

    :param winners: the list of candidate elected.
    :param candidates: the ensemble of candidates which participated in the election.
    """

    def __init__(self, winners: list[Candidate], candidates: set[Candidate]) -> None:
        self._winners: list[Candidate] = copy.deepcopy(winners)
        """The list of candidate elected."""
        self._candidates: set[Candidate] = copy.deepcopy(candidates)
        """The ensemble of candidates which participated in the election."""

        # sort best elected 1st
        self._winners.sort(reverse=True, key=lambda c: c.votes)

    @property
    def winners(self) -> list[Candidate]:
        """Returns the list of winners."""
        return self._winners

    @property
    def candidates(self) -> set[Candidate]:
        """Returns the ensemble of the candidates."""
        return self._candidates

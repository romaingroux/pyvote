import abc
import copy

from pyvote.candidates.candidate import Candidate
from pyvote.voting.context import Context
from pyvote.voting.vote_result import VoteResult


class IVotingSystem(abc.ABC):
    """The IVotingSystem defines an interface for all classes implementing a voting
    system.

    :param candidates: the list of candidates voters can vote for.
    :param context: the vote parameters.
    """

    def __init__(self, candidates: list[Candidate], context: Context) -> None:
        self._candidates: list[Candidate] = copy.deepcopy(candidates)
        """The list of candidates to the election."""
        self._context: Context = context
        """The election parameters."""

    @abc.abstractmethod
    def vote(self) -> VoteResult:
        """Must run the voting simulation and returns it result.

        Returns:
            A dictionary containing the number of votes (value) per candidate
            (key).
        """

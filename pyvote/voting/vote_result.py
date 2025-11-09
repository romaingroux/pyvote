import pydantic

from pyvote.candidates.candidate import Candidate


class VoteResult(pydantic.BaseModel):
    """The VoteResult class models the result of an election.

    :param winners: the list of candidate elected.
    :param statistics: the per candididate number of votes.
    """

    winners: list[Candidate]
    """The list of candidate elected."""
    statistics: dict[Candidate, int]
    """The in-detail election statistics."""

import pydantic


class Candidate(pydantic.BaseModel):
    """The Candidate class models a candidate to an election.

    :param name: the candidate's name.
    :param popularity: the candidate popularity, expressed as the
        probability that an elector vote for it.
    """

    name: str = pydantic.Field(frozen=True)
    """The candidate's name."""
    popularity: float = pydantic.Field(ge=0.0, le=1.0)
    """The probability that an elector vote for this candidate.

    It may be normalized when facing other candidates.
    """

    def __hash__(self) -> int:
        return hash(self.name)

from pyvote.candidates.eligible_base import EligibleBase


class Candidate(EligibleBase):
    """The Candidate class models a candidate to an election.

    :param name: the candidate's name.
    :param popularity: the candidate popularity, expressed as the probability that an
        elector vote for it.
    """

    def __init__(self, name: str, popularity: float) -> None:

        super().__init__()

        self._name: str = name
        """The candidate's name."""
        self.popularity = popularity  # sets self._popularity

    def __hash__(self) -> int:
        """Returns the hash of the candidate.

        The hash is based on the candidate name.
        """
        return hash(self._name)

    def __eq__(self, other: object) -> bool:
        """Compare two instances field wise and returns if they are identical."""
        if not isinstance(other, Candidate):
            return NotImplemented
        else:
            return (
                self.name == other.name
                and self.popularity == other.popularity
                and self.votes == other.votes
            )

    def __ne__(self, other: object) -> bool:
        """Compares two instances field wise and returns if they differ."""
        return not self == other

    def __repr__(self) -> str:
        """Returns a string representation of the instance."""
        return f"<name:{self.name}, popularity:{self.popularity}, votes:{self.votes}>"

    @property
    def popularity(self) -> float:
        """Returns the candidate popularity."""
        return self._popularity

    @popularity.setter
    def popularity(self, value: float) -> None:
        """Sets the popularity.

        :param value: The new popularity value. Must be >= 0.
        :raises: ValueError if the popularity is not >= 0.
        """
        if value < 0.0:
            msg = f"popularity must be >= 0 ({value})"
            raise ValueError(msg)

        self._popularity = value
        """The candidate popularity.

        It will be used by voting systems to compare candidates. It may be normalized
        when facing other candidates.
        """

    @property
    def name(self) -> str:
        """Returns the candidate's name."""
        return self._name

class EligibleBase:
    """The EligibleBase class defines a base class for something or somebody that can be
    voted for and receives voices."""

    def __init__(self) -> None:
        self._votes: int = 0
        """The number of votes collected so far."""

    def get_vote(self) -> None:
        """Adds a vote."""
        self._votes += 1

    def reset(self) -> None:
        """Resets number of votes to 0."""
        self._votes = 0

    @property
    def votes(self) -> int:
        """Returns the number of votes collected so far."""
        return self._votes

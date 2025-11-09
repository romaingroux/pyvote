import pydantic


class Context(pydantic.BaseModel):
    """The Context class models an election context. It is used to pass
    paramters to the election.

    :param population_size: the number of voters participating to the
        vote.
    """

    seed: int | None = None
    """A seed for the random number generator"""

    population_size: int = pydantic.Field(gt=0)
    """The number of voters."""

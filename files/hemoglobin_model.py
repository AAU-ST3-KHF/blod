import numpy as np


def hemoglobin_model(
    Hb0: float, t: np.ndarray | float, k: float, S: float
) -> np.ndarray:
    """
    Total hemoglobin Hb(t) [g], the solution of

        dHb/dt = -k Hb + S,   Hb(0) = Hb0

    Implement your solution from question B here.
    """
    raise NotImplementedError("Implement your solution Hb(t) from question B")

import numpy as np


def hemoglobin_model(
    Hb0: float, t: np.ndarray | float, k: float, S: float
) -> np.ndarray:
    """
    dHb/dt = -k Hb + S
    """
    Hbinf = S / k
    Hb = Hbinf + (Hb0 - Hbinf) * np.exp(-k * t)
    return Hb


if __name__ == "__main__":
    N = 100
    t_max = 365.0
    t = 100.0  # days
    k = 1.0 / 120.0  # fractional turnover rate, uddrivelsesraten / dag
    Hb0 = 500
    S = 6.3  # rate of hemoglobin production gHb / dag
    Hb_after_100_days = float(hemoglobin_model(Hb0=500, t=100.0, k=k, S=S))
    print(f"{Hb_after_100_days=}")
    # Plot

import numpy as np

def concentration(x: np.ndarray, L_axial: float, v: float, D: float, C0: float):
    transit_time = L_axial / v
    lambda_eff = np.sqrt(2 * D * transit_time)
    C = C0 * np.exp(-x / lambda_eff)
    return C


def flux(x: np.ndarray, C: np.ndarray, v: float, D: float):
    dCdx = np.gradient(C, x)
    Jd = -D * dCdx
    Jc = v * C
    Js = Jd + Jc

    return Js


def peclet(L: float | np.ndarray, D: float, v: float):
    Pe = L * v / D
    return Pe


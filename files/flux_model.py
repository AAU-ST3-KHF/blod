import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes

L_axial = 0.1  # mm
L = 0.1  # mm
C0 = 1.0  # mol/mm^3
x = np.linspace(0.01 * L, L, 101)  # mm

conditions = {
    "Normal": {"v": 0.1, "D": 1.8e-3},
    "Valsalva": {"v": 0.3, "D": 1.8e-3},  # Increased velocity
    "Fibrosis": {"v": 0.1, "D": 0.9e-3},  # Reduced diffusion
    "Valsalva+Fibrosis": {
        "v": 0.3,
        "D": 0.9e-3,
    },  # Increased velocity, Reduced diffusion
}


def concentration(x, L_axial, v, D, C0):
    transit_time = L_axial / v
    lambda_eff = np.sqrt(2 * D * transit_time)
    C = C0 * np.exp(-x / lambda_eff)
    return C


def flux(
    x: np.ndarray,
    C: np.ndarray,
    v: float,
    D: float,
):

    Jd = -D * np.gradient(C, x)
    Jc = v * C
    Js = Jd + Jc

    return Js


def peclet(L, D, v):
    Pe = L * v / D
    return Pe


# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 8))
axs: list[matplotlib.axes.Axes]  # Denne linje giver bare typehints (liv==lettere)

for i, (label, params) in enumerate(conditions.items()):
    v = params["v"]
    D = params["D"]

    # Flux components
    C = concentration(x, L_axial, v, D, C0)
    Js = flux(x, C, v, D)
    Pe = peclet(x, D, v)

    # Plot fluxes
    axs[0].plot(x * 1e3, Js, label=label)

    # Plot concentration
    axs[1].plot(x * 1e3, C, label=label)

    # Plot peclet
    axs[2].plot(x * 1e3, Pe * np.ones_like(x), label=label)

axs[0].set_title("Flux")
axs[0].set_xlabel("Tissue barrier thickness (μm)")
axs[0].set_ylabel("Flux [mol/mm²/s]")
axs[0].set_xscale("log")
axs[0].grid(True)
axs[0].legend()
axs[1].set_title("Concentration")
axs[1].set_xlabel("Tissue barrier thickness (μm)")
axs[1].set_ylabel("Concentration [mol/mm³]")
axs[1].set_xscale("log")
axs[1].grid(True)
axs[1].legend()

axs[2].plot(
    x * 1e3, np.ones_like(x), label="Diff./Conv. Barrier", linestyle="--", color="k"
)
axs[2].set_title("Peclet's Number")
axs[2].set_xlabel("Tissue barrier thickness (μm)")
axs[2].set_ylabel("Peclet Number")
axs[2].set_xscale("log")
axs[2].set_yscale("log")
axs[2].grid(True)
axs[2].legend()
plt.tight_layout()
plt.show()

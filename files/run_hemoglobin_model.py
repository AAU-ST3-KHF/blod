import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("QtAgg")  # or "QtAgg" if Qt is installed

from hemoglobin_model import hemoglobin_model

if __name__ == "__main__":
    N = 100
    t_max = 365.0
    t = np.linspace(0, t_max, 100)  # days
    k = 1 / 120  # fractional turnover rate, uddrivelsesraten / dag
    S = 6.3  # rate of hemoglobin production gHb / dag
    Hb0_steadystate = S / k  # g total hemoglobin in blood at t0
    Hb_steadystate = hemoglobin_model(Hb0=Hb0_steadystate, t=t, k=k, S=S)
    Hb_bloodloss = hemoglobin_model(Hb0=500, t=t, k=k, S=S)

    # Plot
    plt.figure(figsize=(6, 4))
    plt.plot(t, Hb_steadystate, label="Hemoglobin (Steady State)")
    plt.plot(t, Hb_bloodloss, label="Hemoglobin (Blood Loss)", linestyle="--")
    plt.xlabel("Time after blood loss (days)")
    plt.ylabel("Total Hemoglobin (g Hb)")
    plt.title("Total Hemoglobin over time")
    plt.legend()
    plt.grid(True)
    plt.show()

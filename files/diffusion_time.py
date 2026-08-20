import math

D = 0.0018  # mm^2/s, same as 1.8e-5 cm^2s^-1
x1 = 0.001
x2 = 1

# Solution
t1 = x1**2 / (2 * D)
t2 = x2**2 / (2 * D)
print(f"1 µm: {t1:10.6f} s  (≈ {t1 * 1e3:.3f} ms)")
print(f"1 mm: {t2:10.0f} s  (≈ {t2 / 60:.2f} min)")

x_2ms = math.sqrt(2 * D * 2e-3) * 1000
print(f"Diffusion is no longer viable when x is > {x_2ms:.1f} μm")

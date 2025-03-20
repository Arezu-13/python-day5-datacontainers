from scipy.stats import poisson
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# a
# Random descrete variable with poissonian distribution
# with average rate, mu=4
rv_p = poisson(mu=4)

# Number of discrete events
x = np.arange(0, 15)

# PMF, CDF values 
pmf_val_p = rv_p.pmf(x)
cdf_val_p = rv_p.cdf(x)

# Generate 1000 random samples
samples = rv_p.rvs(size=1000)

# Create subplots side by side
fig, axs = plt.subplots(2, 3, figsize=(18, 14))
ax1, ax2, ax3, ax4, ax5, ax6 = axs.flatten()
plt.subplots_adjust(hspace=0.4)  # hspace controls vertical spacing between rows


# Plot PMF
ax1.stem(x, pmf_val_p, basefmt=" ")
ax1.set_title("Poisson PMF (μ = 4)")
ax1.set_xlabel("Number of events (k)")
ax1.set_ylabel("P(X = k)")
ax1.grid(True)

# Plot CDF
ax2.step(x, cdf_val_p, where='post')
ax2.set_title("Poisson CDF (μ = 4)")
ax2.set_xlabel("Number of events (k)")
ax2.set_ylabel("P(X ≤ k)")
ax2.grid(True)

# Histogram of 1000 realizations (sprobability not freq)
ax3.hist(samples, bins=np.arange(-0.5, 15.5, 1), density=True, edgecolor='black', alpha=0.9)
ax3.set_title("Histogram of 1000 random realizations")
ax3.set_xlabel("Number of events")
ax3.set_ylabel("Relative frequency")
ax3.grid(True, linestyle=':', alpha=0.3)

# b :
# Continuous random variable with normal distribution
# mean = 0, standard deviation = 1
rv_n = norm(loc=0, scale=1)

# Number of events
x = np.linspace(-4, 4, 1000)

# PDF, CDF values 
pdf_val_n = rv_n.pdf(x)
cdf_val_n = rv_n.cdf(x)

# Generate 1000 random samples
samples = rv_n.rvs(size=1000)

# Plot PMF
ax4.plot(x, pdf_val_n, color="blue")
ax4.set_title("Normal PDF (μ=0, σ=1)")
ax4.set_xlabel("x")
ax4.set_ylabel("Probability Density")
ax4.grid(True)

# Plot CDF
ax5.plot(x, cdf_val_n, color="blue")
ax5.set_title("Normal CDF (μ=0, σ=1)")
ax5.set_xlabel("x")
ax5.set_ylabel("P(X ≤ x)")
ax5.grid(True)

# Histogram of 1000 realizations (shows the probability not freq)
ax6.hist(samples, bins=30, density=True, edgecolor='black', alpha=0.5, color="blue")
ax6.set_title("Histogram of 1000 random realizations")
ax6.set_xlabel("x")
ax6.set_ylabel("Density")
ax6.grid(True, linestyle=':', alpha=0.3)

plt.show()

# c :
# Poisson samples (discrete)
poisson = rv_p.rvs(size=1000)

# Normal samples (continuous, mean=0)
normal = rv_n.rvs(size=1000)

# Perform two-sample t-test (Welch’s t-test)
t_stat, p_val = ttest_ind(poisson, normal, equal_var=False)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_val}")

if p_val < 0.05:
    print("Samples come from different distributions (reject H0).")
else:
    print("Samples could come from the same distribution (fail to reject H0).")

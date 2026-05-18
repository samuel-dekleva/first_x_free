# This is a model comparing the money paid by an insurance company when a deductible:
# a. is the first $X paid by the insured
# b. is the second $X paid by the insured
# c. is $X paid by the insured after $Y is paid by the company.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Variables: 
# 1. Policyholders and expected accidents per policyholder per year.
policyholders = 80000
accident_prob = 0.09

# 2. Mean and standard deviation of the accident cost distribution. Note that values of sigma over 1.5 are highly chaotic.
avg_cost = 1500
sigma_est = 0.8

# 3. The set of deductibles to test, as well as the set X of "first X is on us!"
deductibles = [500, 1000, 1500, 3000, 10000]
offsets = [0, 500, 1000, 1500, 3000, 10000]

policyholders_list = np.random.poisson(size=policyholders, lam=accident_prob)

accident_cost = np.zeros(policyholders)
for i in range(policyholders):
    if policyholders_list[i] == 0:
        accident_cost[i] = 0
    else:
        for _ in range(policyholders_list[i]):
            accident_cost[i] = accident_cost[i] + np.random.lognormal(mean=np.log(avg_cost) - sigma_est**2 / 2, sigma=sigma_est)

accident_cost = np.sort(accident_cost)
o_tvar_95 = np.mean(accident_cost[int(0.95*policyholders):])
o_tvar_99 = np.mean(accident_cost[int(0.99*policyholders):])

def sim_run(offset):
    ded_scenario = np.where(
        accident_cost > deductible + offset,
        accident_cost - deductible,
        np.where(
            accident_cost > offset,
            offset,
            accident_cost
        )
    )
    ded_scenario = np.sort(ded_scenario)
    tvar_95 = np.mean(ded_scenario[int(0.95*policyholders):])
    tvar_99 = np.mean(ded_scenario[int(0.99*policyholders):])
    return ded_scenario, tvar_95, tvar_99


def deductible_variance(deductible):
    summary_table = {
        "Scenario": ["No Deductible"],
        "Mean": [
            f"${np.mean(accident_cost):.2f}",
        ],
        "Total": [
            f"${np.sum(accident_cost):,.2f}",
        ],
        "TVaR 95": [
            f"${o_tvar_95:.2f}",
        ],
        "TVaR 99": [
            f"${o_tvar_99:.2f}",
        ],
            "LER": [
            f"{0:.2f}%",
        ]
    
    }
    for offset in offsets:
        losses,pct95,pct99 = sim_run(offset)
        summary_table["Scenario"].append( f"Offset by ${offset}")
        summary_table["Mean"].append(f"${losses.mean():.2f}")
        summary_table["Total"].append(f"${losses.sum():,.2f}")
        summary_table["TVaR 95"].append(f"${pct95:.2f}")
        summary_table["TVaR 99"].append(f"${pct99:.2f}")
        summary_table["LER"].append(f"{(accident_cost.mean() - losses.mean()) / accident_cost.mean() * 100:.2f}%")
    
    summary = pd.DataFrame(summary_table)
    
    print(summary)



def survival_curve(losses, x_grid):
    sorted_losses = np.sort(losses)
    n = len(sorted_losses)

    survival_probs = np.array([
        np.mean(sorted_losses > x) for x in x_grid
    ])

    return x_grid, survival_probs

def plot(deductible):
    plt.figure(figsize=(10,3))

    x_grid = np.linspace(0, np.max(accident_cost), 1000)

    for offset in offsets:
        losses, _, _ = sim_run(offset)
        x, y = survival_curve(losses, x_grid)
        plt.plot(x, y, label=f"Offset ${offset}")

    plt.xlabel("Insurer Payment")
    plt.ylabel("P(X > x)")
    if sigma_est > 1.5:
        plt.xscale("log")
    plt.yscale("log")
    plt.title(f"Survival Curves with ${deductible} Deductible")
    plt.legend()
    plt.show()

for deductible in deductibles:
    print(f"Running the simulation with a deductible of ${deductible}.")
    deductible_variance(deductible)
    plot(deductible)
    print()
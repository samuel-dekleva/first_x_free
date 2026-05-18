# First X Free

This repository studies how corridor deductible structures affect insurer payouts and tail risk.

## About

Corridor deductibles are deductible structures in which the insurer initially covers losses up to a threshold, 
after which the insured absorbs a specified layer of losses before insurer coverage resumes.
For instance, the insurance company may begin by paying the first $500, after which the policyholder pays a deductible of $1000 before the company pays the rest.

This model evaluates the merits of these corridor deductibles and how they affect the average and total payouts of the insurance company.

The model operates using a one-year simulation of an adjustable number of policyholders. The accident frequency and severity are likewise adjustable.
Deductibles and stratifications in a list are then tested and compared. 
The output is a summary table of each offset for each deductible and a survival plot for each offset.
The information included in each summary table is as follows:
* Mean paid out per policyholder: The average payment to each policyholder.
* Total: Total money paid out by the company.
* Tail Value at Risk (TVaR) 95: The average of all policies which paid in the 95th percentile or higher.
* Tail Value at Risk (TVaR) 99: The average of all policies which paid in the 99th percentile or higher.
* Loss Elimination Ratio (LER): The percentage reduction in the company's payouts given the corridor deductible plan.

## Explicit Model Assumptions

* Throughout, we assume independence of claims.
* The frequency of claims for each policyholder is modeled using a Poisson distribution with adjustable parameter lambda.
* We assume the cost of each claim is modeled by a lognormal distribution with adjustable mean and standard deviation.
* Importantly, we also assume claims for each policyholder are aggregated prior to applying any corridor deductibles.

## Example Model Output

This image shows what happens in the case where a deductible of $3,000 is applied and it is offset by varying amounts.
The initial conditions were:
* 80,000 policyholders, each with a frequency probability of 0.09.
* Claim severities are modeled using a lognormal distribution calibrated to a target expected severity (in this case $1,500) and adjustable variance parameter (in this case 0.8).

![here](https://imgur.com/NMDNCUH.png)

## Insights

While the body of the distribution is varied based on the offset of the deductible being triggered, after a certain point,
the graphs rejoin. This indicates the tail behavior is not affected strongly by the offsetting, and large payouts occur in similar frequencies.

For some claim frequencies and severities, especially when the mean payment is high, the corridor deductible plan yields roughly the same total payouts
as the standard deductible plan. 
From a consumer perspective, policies that provide immediate partial coverage may appear more attractive than standard deductible structures, 
even when expected insurer payouts are similar.

## How To Run

You can use the file seen [here](First_X_Free.py) to run the code!

The parameters are adjustable and comments are left to explain which variables can be edited.

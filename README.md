# First X Free

This repo is a study of how changing corridor deductible structure changes the overall cost to an insurance company.

## About

Corridor deductibles are deductibles which are applied after the insurance company already pays a certain amount.
For instance, the insurance company may begin by paying the first $500, after which the policyholder pays a deductible of $1000 before the company pays the rest.

This model evaluates the merits of these corridor deductibles and how they affect the average and total payouts of the insurance company.

The model operates using a one-year simulation of an adjustable number of policyholders. The accident frequency and severity are likewise adjustable.
Deductibles and stratifications in a list are then tested and compared. 
The output is a summary table of each offset for each deductible and a survival plot for each offset.

## Explicit Model Assumptions

* Throughout, we assume independence of claims.
* The frequency of claims for each policyholder is modeled using a Poisson distribution with adjustable parameter lambda.
* We assume the cost of each claim is modeled by a lognormal distribution with adjustable mean and standard deviation.
* We also assume claims for each policyholder are aggregated prior to applying any corridor deductibles.

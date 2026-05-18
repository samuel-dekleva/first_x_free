# First X Free

This repo is a study of how changing corridor deductible structure changes the overall cost to an insurance company.

## About

Corridor deductibles are deductibles which are applied after the insurance company already pays a certain amount.
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
* 

## Explicit Model Assumptions

* Throughout, we assume independence of claims.
* The frequency of claims for each policyholder is modeled using a Poisson distribution with adjustable parameter lambda.
* We assume the cost of each claim is modeled by a lognormal distribution with adjustable mean and standard deviation.
* Importantly, we also assume claims for each policyholder are aggregated prior to applying any corridor deductibles.

## Example Model Output

This image shows what happens in the case where a deductible of $3,000 is applied and it is offset by varying amounts.
The initial conditions were:
* 80,000 policyholders, each with a frequency probability of 0.09.
* Each accident follows a lognormal distribution with modified mean $1,500 and standard deviation 0.8. (Note that anything over 1.5 swings very wildly.)

![here](https://imgur.com/NMDNCUH.png)

## How To Run

You can use the file seen [here](First_X_Free.py) to run the code!

## 

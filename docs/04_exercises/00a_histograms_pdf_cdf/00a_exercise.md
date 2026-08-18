# Exercise 00a - Water Demand Distribution and Capacity Analysis

## Assignment

A municipal water utility is reviewing historical operating data for one of its water distribution service areas.

The utility has observed continued development within the service area and is beginning preliminary planning for future water-supply and pumping improvements.

Before developing demand projections or performing detailed hydraulic modeling, the engineering team wants to better understand the **existing distribution of system demand**.

You have been provided with one year of historical operating data.

Your responsibility is to:

* Understand the supplied data
* Evaluate data quality
* Characterize historical water demand
* Evaluate the distribution of observed demand
* Estimate the frequency with which selected demand thresholds were exceeded
* Interpret the results in the context of existing system capacity
* Identify limitations that should be considered before using the results for infrastructure planning

The objective is not simply to calculate statistics.

The objective is to determine:

> **What does the historical operating record tell us about normal, high, and unusually high system demand?**

---

# Engineering Background

The **Riverview Water Utility** operates a municipal water system serving residential, commercial, and light industrial customers.

The service area is supplied by a water treatment and pumping facility with a nominal finished-water production capacity of:

$$
Q_{capacity} = 6.0 \text{ MGD}
$$

Historical operating records indicate that demand varies substantially throughout the year.

Operations staff report that demand is generally influenced by:

* Time of day
* Day of week
* Seasonal conditions
* Outdoor water use
* Weather
* Normal customer variability

The utility is beginning to evaluate whether existing capacity provides sufficient operating margin during higher-demand conditions.

This exercise represents an **initial statistical evaluation**.

It is not a complete capacity analysis or water-supply planning study.

---

# Primary Engineering Question

The primary question for this assignment is:

> **How frequently does system demand approach or exceed selected portions of the existing 6.0-MGD production capacity?**

Your analysis should characterize the complete historical demand distribution rather than evaluating only the single largest observed value.

---

# Supporting Questions

As part of the investigation, consider:

* What demand levels are most commonly observed?
* What portion of observations represent relatively high-demand conditions?
* Is the demand distribution symmetric or skewed?
* How frequently does demand exceed selected thresholds?
* How frequently does demand approach the nominal production capacity?
* Are extreme observations isolated or part of recognizable operating patterns?
* Are there data-quality concerns that could materially affect the analysis?

These questions are intended to help frame the investigation.

They do not prescribe a specific sequence of calculations.

---

# Information Provided

## System Information

The following system information has been provided:

| Parameter                   |                            Value |
| --------------------------- | -------------------------------: |
| System                      |          Riverview Water Utility |
| Facility                    | Central Water Treatment Facility |
| Nominal Production Capacity |                          6.0 MGD |
| Service Type                |                        Municipal |
| Data Period                 |                One Calendar Year |
| Nominal Data Frequency      |                           Hourly |

The production-capacity value represents nominal available production capacity for the purposes of this exercise.

Do not assume that this value alone establishes the utility's actual firm, permitted, hydraulic, or reliable capacity.

---

# Data Provided

The dataset is located at:

```text
data/raw/water_distribution/00a_water_demand/
```

The following files are provided:

```text
README.md
system_metadata.csv
hourly_operations.csv
```

Treat these files as original source data.

**Do not modify the raw files.**

---

# Dataset Type

> **Simulated Operational Data**

The dataset is synthetic and was generated to represent realistic municipal water-system operating behavior.

It does not contain records from an actual utility.

The dataset intentionally includes normal operational variability and may contain data-quality conditions requiring investigation.

---

# Data Description

## `system_metadata.csv`

This file contains general information about the system and monitoring period.

Potential information includes:

* System identifier
* Facility identifier
* Nominal production capacity
* Observation period
* Nominal recording interval

Review the file before beginning the analysis.

---

## `hourly_operations.csv`

This file contains the historical operating record.

Each row represents a recorded hourly observation.

The file includes operational and contextual variables associated with water demand.

Do not assume that every variable is necessary for the primary analysis.

Part of the assignment is determining which information is relevant.

---

# Your Role

Approach the assignment as an engineer performing an initial review of utility operating data.

You have not been provided with:

* Expected statistical results
* Known anomaly locations
* A list of invalid observations
* A predetermined conclusion
* A completed analysis
* A solution notebook
* An answer key

Your conclusions should be developed from the supplied evidence.

---

# Part 1 - Understand the Assignment

Before performing calculations, summarize the assignment in your own words.

Document:

1. What engineering system is being evaluated?
2. Why is the analysis being performed?
3. What is the primary engineering question?
4. What does the 6.0-MGD value represent?
5. What does it **not necessarily represent**?
6. What additional information would eventually be required for a complete capacity evaluation?

Do not begin by calculating probabilities.

Understand the engineering question first.

---

# Part 2 - Data Inventory

Review every file provided with the exercise.

Create a data inventory containing, at minimum:

| File | Purpose | Records | Key Fields | Time Period | Notes |
| ---- | ------- | ------: | ---------- | ----------- | ----- |
|      |         |         |            |             |       |

Determine:

* What does each file contain?
* What does each row represent?
* What identifiers are available?
* What is the observation period?
* What is the expected observation frequency?
* What units are used?
* Which variables appear relevant to the capacity question?

---

# Part 3 - Initial Data Inspection

Load the supplied data using Python.

Inspect:

* Shape
* Column names
* Data types
* Beginning and ending records
* Timestamp coverage
* Missing values
* Duplicate records
* Numerical ranges

Do not modify the raw files.

Document any initial observations or concerns.

---

# Part 4 - Data Quality Assessment

Before analyzing the demand distribution, determine whether the historical record is suitable for analysis.

Investigate:

* Missing observations
* Duplicate timestamps
* Irregular time intervals
* Missing demand measurements
* Physically questionable demand values
* Unexpected discontinuities
* Other conditions that could influence the analysis

For material issues, document:

| Issue | Evidence | Potential Impact | Treatment |
| ----- | -------- | ---------------- | --------- |
|       |          |                  |           |

Do not automatically remove unusual observations.

Determine whether there is evidence that an observation is invalid before excluding it.

---

# Part 5 - Initial Statistical Characterization

Characterize the historical demand record using appropriate descriptive statistics.

At minimum, your analysis should allow you to describe:

* Typical demand
* Variability
* Observed range
* High-demand conditions

You may use concepts introduced in Lesson 00 and other statistical measures you already understand.

Avoid producing statistics that do not contribute to understanding the engineering problem.

---

# Part 6 - Histogram

Create a histogram of the observed hourly water demand.

Select an appropriate number of bins.

Evaluate:

* Where most observations occur
* Overall shape
* Spread
* Possible skewness
* Presence of multiple concentrations
* Unusually high or low observations

Then answer:

> **What does the histogram tell you about how this system normally operates?**

Do not describe only the appearance of the plot.

Interpret its engineering meaning.

---

# Part 7 - Probability Density

Estimate and visualize the probability density of historical hourly demand.

Compare the probability density with the histogram.

Consider:

* Which demand ranges appear most common?
* Which demand ranges are relatively uncommon?
* Does the distribution appear to have one dominant operating range?
* Are there secondary patterns that may deserve investigation?
* Does the density appear approximately symmetric?

Explain what the probability density adds to your understanding of the system.

---

# Part 8 - Empirical Cumulative Distribution

Construct an empirical cumulative distribution function for hourly demand.

Use the empirical CDF to evaluate the historical probability that demand was less than or equal to selected thresholds.

Evaluate at least the following:

$$
P(Q \leq 4.0 \text{ MGD})
$$

$$
P(Q \leq 4.5 \text{ MGD})
$$

$$
P(Q \leq 5.0 \text{ MGD})
$$

$$
P(Q \leq 5.5 \text{ MGD})
$$

$$
P(Q \leq 6.0 \text{ MGD})
$$

Interpret each important result in plain engineering language.

---

# Part 9 - Exceedance Probability

Convert the cumulative probabilities into exceedance probabilities.

Evaluate:

$$
P(Q > 4.0 \text{ MGD})
$$

$$
P(Q > 4.5 \text{ MGD})
$$

$$
P(Q > 5.0 \text{ MGD})
$$

$$
P(Q > 5.5 \text{ MGD})
$$

$$
P(Q > 6.0 \text{ MGD})
$$

For each threshold, determine what the result means operationally.

For example, distinguish between statements such as:

> "The probability of exceeding 5.5 MGD was X."

and:

> "X percent of the recorded hourly observations exceeded 5.5 MGD."

Consider whether those statements are equivalent for this particular analysis and what assumptions are implicit when describing the empirical record probabilistically.

---

# Part 10 - Capacity Utilization

Express the selected demand thresholds as percentages of nominal production capacity.

For example:

$$
\text{Capacity Utilization}
===========================

\frac{Q}{Q_{capacity}}
\times 100
$$

Evaluate the historical frequency with which demand exceeded:

* Approximately 67% of capacity
* 75% of capacity
* Approximately 83% of capacity
* Approximately 92% of capacity
* 100% of capacity

Develop a concise table summarizing the results.

Suggested structure:

| Demand Threshold | Capacity Utilization | Observations Exceeding | Empirical Exceedance Probability |
| ---------------: | -------------------: | ---------------------: | -------------------------------: |
|          4.0 MGD |                      |                        |                                  |
|          4.5 MGD |                      |                        |                                  |
|          5.0 MGD |                      |                        |                                  |
|          5.5 MGD |                      |                        |                                  |
|          6.0 MGD |                      |                        |                                  |

---

# Part 11 - Investigate High-Demand Observations

A probability distribution describes frequency, but it does not tell you **when** events occurred.

Investigate observations representing unusually high demand.

Determine:

* When did the highest-demand observations occur?
* Were they isolated?
* Did they occur in clusters?
* Were they concentrated during particular portions of the year?
* Were they concentrated during particular times of day?
* Do any contextual variables appear related?

Do not assume that every relationship observed is causal.

The objective is to determine whether the distribution contains temporal or operational structure that is hidden when the data are viewed only as a histogram or CDF.

---

# Part 12 - Compare Distribution and Time

Compare what you learned from:

1. The histogram
2. The probability density
3. The empirical CDF
4. The chronological operating record

Discuss what each representation reveals that the others do not.

In particular, consider:

> **Could two water systems have nearly identical demand distributions but very different operational behavior through time?**

Explain why or why not.

---

# Part 13 - Validation

Validate important analytical results.

At minimum, independently verify selected empirical probabilities using the underlying observations.

For a threshold $q$:

$$
P(Q > q)
========

\frac{\text{Number of observations where }Q>q}
{\text{Number of valid observations}}
$$

Compare this calculation with the result obtained from the empirical CDF.

The two approaches should be consistent.

If they are not, investigate the difference.

---

# Part 14 - Engineering Interpretation

Return to the primary engineering question:

> **How frequently does system demand approach or exceed selected portions of the existing 6.0-MGD production capacity?**

Use the analysis to describe:

* Typical operating conditions
* Higher-demand conditions
* Frequency of operation near capacity
* Frequency of operation above nominal capacity, if any
* Important temporal patterns
* Important uncertainty or data limitations

Separate observed evidence from engineering interpretation.

---

# Part 15 - Capacity Discussion

Based on the historical record, discuss whether the data suggest:

* Substantial available capacity
* Periodic operation near capacity
* Frequent operation near capacity
* Potential capacity concerns requiring further investigation

Do **not** make a final determination regarding facility adequacy using this dataset alone.

Explain why historical hourly demand and nominal production capacity are insufficient for a complete capacity determination.

Consider additional factors such as:

* Firm production capacity
* Largest unit out of service
* Storage
* Pumping limitations
* Treatment-process constraints
* Permitted capacity
* Fire-flow requirements
* Peak-day demand
* Peak-hour demand
* Demand growth
* Equipment reliability
* Operational redundancy

You are not required to analyze these factors in this exercise.

You should recognize their importance.

---

# Part 16 - Limitations

Identify limitations that materially affect the analysis.

Consider:

* Length of historical record
* Observation frequency
* Missing observations
* Data quality
* Whether the year was representative
* Weather conditions
* Growth
* Changes in system operation
* Use of historical frequency as an estimate of future probability

For each significant limitation, consider:

> **Could this materially change the engineering conclusion?**

---

# Part 17 - Engineering Conclusion

Prepare a concise conclusion addressing:

> **What does the historical record tell us about the distribution of system demand and the frequency with which demand approaches the nominal production capacity?**

Your conclusion should distinguish among:

* What is directly supported by the data
* What is suggested by the data
* What cannot be determined from the available information

---

# Part 18 - Recommendation

Recommend appropriate next steps for the utility.

Recommendations should follow from your findings.

Potential next steps may involve:

* Continued monitoring
* Additional historical data
* Peak-day analysis
* Demand forecasting
* Capacity evaluation
* Hydraulic modeling
* Firm-capacity analysis
* Evaluation of storage
* Review of operational redundancy

Do not recommend infrastructure expansion solely because demand occasionally approaches a nominal capacity value.

---

# Required Deliverables

## 1. Analysis Notebook

Complete the analysis in:

```text
notebooks/00a_water_demand_distribution/
└── workspace.ipynb
```

The notebook should execute successfully from beginning to end.

---

## 2. Processed Data

Store any material processed datasets under:

```text
data/processed/water_distribution/00a_water_demand/
```

Do not modify the original files.

---

## 3. Figures

Provide, at minimum:

* Histogram of hourly demand
* Histogram with estimated probability density
* Empirical CDF
* At least one visualization investigating the timing of high-demand observations

Additional figures should be created only when they contribute meaningfully to the analysis.

---

## 4. Capacity Threshold Table

Provide a table summarizing:

* Demand threshold
* Capacity utilization
* Number of valid observations
* Number of exceedances
* Empirical exceedance probability

---

## 5. Engineering Summary

Prepare a concise engineering summary containing:

### Issue

Why was the analysis performed?

### Data

What information was evaluated?

### Analysis

How was the historical demand record evaluated?

### Findings

What are the most important results?

### Limitations

What prevents stronger conclusions?

### Conclusion

What does the available evidence support?

### Recommendation

What should the utility evaluate next?

---

# Use of Lesson 00

This exercise builds directly upon:

**Lesson 00 - Histograms, Probability Density Functions, and Cumulative Distribution Functions**

You should be comfortable with:

* Histograms
* Probability density
* Empirical cumulative probability
* Exceedance probability
* Basic descriptive statistics
* Python data analysis
* Basic visualization

Return to Lesson 00 when you need to review a concept.

The lesson explains the methods.

This exercise requires you to decide how to use them.

---

# Getting Help

If you become stuck, preserve the analytical challenge whenever possible.

## Level 1 - Conceptual Review

Review Lesson 00.

## Level 2 - Directional Guidance

Ask what statistical concept may help answer a specific question.

## Level 3 - Method Guidance

Ask how a method works without requesting the result for this dataset.

## Level 4 - Debugging

Provide your code and explain what you intended it to calculate.

## Level 5 - Separate Example

Request a demonstration using a different dataset.

Avoid requesting completed calculations for the exercise dataset unless you have exhausted the earlier levels.

---

# Final Reflection

After completing the exercise, answer the following:

1. Which visualization gave you the best understanding of normal system demand?

2. Which visualization gave you the best understanding of capacity risk?

3. What did the CDF tell you that the histogram did not?

4. What did the chronological data reveal that neither the histogram nor CDF showed?

5. Which data-quality decision had the greatest potential to affect your results?

6. What additional dataset would most improve the capacity evaluation?

7. If the utility gave you five additional years of hourly data, how would that change your confidence in the analysis?

8. What conclusion from this exercise would you be least comfortable presenting as definitive?

---

# Completion Standard

The exercise is complete when you can explain:

> **How demand is distributed, how frequently important demand thresholds are exceeded, when high-demand conditions occur, how reliable those estimates are, and what the results mean for further engineering evaluation.**

The objective is not to prove that the facility is adequate or inadequate.

The objective is to use historical observations to develop a defensible understanding of existing system demand.

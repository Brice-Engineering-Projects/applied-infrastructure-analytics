# Lesson 00 - Histograms, Probability Distribution Functions (PDF), and Cumulative Distribution Functions (CDF)

## Purpose

One of the most common challenges engineers face is understanding uncertainty.

Unlike deterministic calculations, natural systems rarely produce the same result twice. Annual rainfall changes from year to year, peak streamflow varies with storm intensity, groundwater elevations fluctuate seasonally, and water demands continually evolve over time.

Probability provides engineers with tools to describe this uncertainty.

This lesson introduces three of the most fundamental concepts in applied statistics:

- Histograms
- Probability Distribution Functions (PDF)
- Cumulative Distribution Functions (CDF)

Rather than beginning with mathematical equations, this lesson starts with observed hydrologic data and develops an intuitive understanding of what these tools represent.

The goal is to understand **what these plots tell us about a dataset** and **how engineers use them to make decisions.**

---

# Scenario

A stream gaging station has recorded the annual maximum discharge of a small watershed over the past twenty years.

A transportation department is considering replacing an aging culvert at a roadway crossing.

Before hydraulic modeling begins, the engineering team would like to better understand the historical streamflow data.

As a junior engineer on the project, you have been asked to perform an exploratory statistical analysis of the annual peak flow record.

Your objective is **not** to perform a complete flood frequency analysis.

Instead, your objective is to understand how probability distributions describe observed data and how cumulative probabilities can be used to evaluate engineering risk.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Load and inspect a dataset using Pandas.
- Compute basic descriptive statistics.
- Create and interpret a histogram.
- Explain what a Probability Distribution Function represents.
- Explain what a Cumulative Distribution Function represents.
- Estimate exceedance probabilities from a CDF.
- Relate statistical results to an engineering design decision.

---

# Dataset

The dataset consists of twenty years of annual peak streamflow observations.

Each record contains:

- Year
- Annual Maximum Streamflow (cfs)

The dataset has intentionally been kept small so that calculations can be verified manually if desired.

---

# Assignment

## Part 1 – Exploratory Data Analysis

Load the dataset.

Determine:

- Number of observations
- Mean
- Median
- Minimum
- Maximum
- Range
- Standard deviation

Document your observations.

Questions to consider:

- Does the dataset appear reasonable?
- Are there any obvious outliers?
- Are values evenly distributed?

---

## Part 2 – Histogram

Create a histogram of the annual peak flows.

Use an appropriate number of bins.

Answer the following questions:

- Where do most observations occur?
- Is the data approximately symmetric?
- Does the distribution appear skewed?
- Are high-flow events common or rare?

Record your observations before continuing.

---

## Part 3 – Probability Density Function (PDF)

Estimate the Probability Density Function for the observed data.

Overlay the PDF on the histogram.

Without using mathematical definitions, answer:

- What does the PDF tell you about the streamflow record?
- Which flow values appear most likely?
- Which flow values appear least likely?

Think about how this differs from the histogram.

---

## Part 4 – Cumulative Density Function (CDF)

Construct the empirical CDF.

Using the CDF, estimate:

- P(Flow ≤ 600 cfs)
- P(Flow ≤ 700 cfs)
- P(Flow > 700 cfs)
- P(Flow > 800 cfs)

Describe what each probability means in plain English.

---

## Part 5 – Engineering Interpretation

A proposed culvert has a hydraulic capacity of **700 cfs**.

Using only the observed record:

Determine:

- Probability that annual peak flow does not exceed the culvert capacity.
- Probability that annual peak flow exceeds the culvert capacity.

Discuss:

- Does the observed record suggest the culvert capacity is adequate?
- What limitations exist when using only twenty years of data?
- What additional information would you request before making a final design recommendation?

---

# Deliverables

Upon completion, your project should produce:

- Summary statistics table
- Histogram
- Histogram with estimated PDF
- Empirical CDF
- Short engineering discussion interpreting the results

---

# Stretch Goal

Suppose an engineer with no background in statistics asks:

> "Why do I need both a PDF and a CDF? Aren't they showing the same thing?"

Write a brief explanation answering this question without using equations.

If you can explain the difference clearly to another engineer, you have likely developed a solid conceptual understanding of both tools.

---

# Looking Ahead

In future lessons, this project will build upon these concepts by introducing:

- Common probability distributions
- Return periods
- Exceedance probability
- Flood frequency analysis
- Reliability analysis
- Monte Carlo simulation
- Bayesian statistics
- Markov chains
- Time series analysis

Each lesson will continue to use realistic engineering datasets and practical infrastructure problems rather than purely academic examples.

# Applied Exercise

You have now used a small hydrologic dataset to learn how histograms,
probability density functions, cumulative distribution functions, and
exceedance probabilities describe observed uncertainty.

The next exercise removes much of the instructional scaffolding.

In **Exercise 00a - Water Demand Distribution and Capacity Analysis**, you
will receive one year of simulated municipal water-system operating data.

Unlike this lesson, the applied exercise requires you to:

- inspect the supplied files,
- evaluate data quality,
- determine which variables are relevant,
- apply the statistical concepts from this lesson,
- validate your results,
- and develop an engineering interpretation.

The exercise introduces an important distinction that will become more
significant later in the curriculum:

> **A probability distribution describes how frequently values occur,
> but it does not describe when they occur.**

The applied exercise is located at:

`docs/04_exercises/00a_water_demand_distribution/exercise.md`

The associated raw data are located at:

`data/raw/water_distribution/leson_00/00a_water_demand/`

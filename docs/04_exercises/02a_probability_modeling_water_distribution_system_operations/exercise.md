# Exercise 02a - Probability Modeling of Water Distribution System Operations

## Purpose

A utility rarely receives a dataset labeled with the probability distribution that should be used for each variable.

Instead, engineers receive operational records containing different types of measurements and events:

- pressures,
- flows,
- equipment runtimes,
- failure counts,
- repair durations,
- alarms,
- maintenance records,
- and environmental conditions.

Some variables may be reasonably represented by theoretical probability distributions.

Others may not.

The purpose of this exercise is to investigate a realistic water distribution system dataset and determine which probability models, if any, provide useful representations of the observed uncertainty.

Unlike the instructional examples in Lesson 02, you will **not** be told which distribution to apply to each variable.

You must make and defend those decisions.

---

# Engineering Scenario

## Background

A municipal water utility operates a distribution system serving approximately 48,000 customers.

The system includes:

- approximately 420 miles of water main,
- three high-service pump stations,
- four elevated storage tanks,
- pressure monitoring locations throughout the distribution system,
- and a mixture of residential, commercial, and industrial customers.

The utility has accumulated several years of operational and maintenance data.

Historically, these records have primarily been used for:

- regulatory reporting,
- responding to customer complaints,
- investigating individual failures,
- and documenting maintenance activities.

The utility would now like to use the historical data more systematically.

Engineering staff are particularly interested in understanding the uncertainty associated with:

- system demand,
- pressure,
- equipment operation,
- water-main failures,
- and repair activities.

The utility has asked you to perform an initial probability analysis of the available records.

---

# Engineering Objective

Your assignment is to determine whether selected operational and maintenance variables can be reasonably represented using theoretical probability distributions.

The utility is interested in questions such as:

- What constitutes unusually high system demand?
- How frequently might low-pressure conditions occur?
- What range of pump operating conditions should normally be expected?
- How variable are monthly water-main failures?
- How likely are unusually high monthly failure counts?
- How variable are repair durations?
- Are extreme repair durations unusual or simply part of the underlying distribution?
- Can historical event frequencies reasonably support future probability estimates?

Your objective is **not** to find a probability distribution for every column.

Your objective is to determine where probability modeling is useful and where it is not.

---

# Available Data

The exercise dataset represents multiple years of simulated utility operating records.

The dataset may contain information related to:

- water demand,
- distribution-system pressure,
- pump operation,
- storage conditions,
- water-main failures,
- repair activities,
- alarms,
- weather or seasonal conditions,
- asset characteristics,
- and maintenance history.

Not every variable should necessarily be analyzed using the same methods.

Some variables may be:

- discrete,
- continuous,
- binary,
- categorical,
- timestamps,
- identifiers,
- cumulative measurements,
- or derived quantities.

Part of the assignment is determining which variables represent meaningful random variables for probability analysis.

---

# Important Data Note

The provided files should be treated as **raw utility data**.

Do not assume that:

- every record is valid,
- every field is complete,
- timestamps are perfectly continuous,
- units are automatically obvious,
- duplicate records are impossible,
- sensors always report physically reasonable values,
- operational conditions remain constant throughout the record,
- or every file covers exactly the same period.

Do not modify the raw files manually.

If cleaning or transformation is necessary, preserve the original data and create processed datasets separately.

---

# Assignment

## Part 1 - Data Inventory

Begin by examining all files provided with the exercise.

For each file, determine:

- number of records,
- number of columns,
- observation period,
- timestamp resolution where applicable,
- available variables,
- units,
- missing values,
- duplicate records,
- and obvious data-quality concerns.

Create a concise data inventory.

Do not begin fitting distributions yet.

The first task is to understand what you actually received.

---

# Part 2 - Data Quality Assessment

Evaluate the data before performing probability analysis.

Investigate conditions such as:

- missing observations,
- duplicate timestamps,
- missing timestamps,
- impossible values,
- suspiciously extreme values,
- inconsistent equipment states,
- sensor values outside reasonable physical ranges,
- cumulative meters that decrease or reset,
- and inconsistent units or data types.

Document each issue you identify.

For each issue, classify your response as one of the following:

```text
Retain
Correct
Exclude
Flag for further investigation
```

Explain your reasoning.

Do not remove an observation simply because it appears unusual.

An extreme observation may represent:

- bad data,
- a sensor problem,
- an actual operational event,
- an equipment failure,
- or an important system condition.

Engineering context matters.

---

# Part 3 - Identify Candidate Random Variables

Review the available variables and identify those that may be useful for probability analysis.

For each candidate variable, classify it as:

```text
Discrete
Continuous
Binary
Categorical
Not appropriate for probability modeling
```

Create a table similar to:

| Variable | Classification | Candidate for Modeling? | Reason |
| --- | --- | --- | --- |
| Example Variable | Continuous | Yes | Represents variable operational measurement |
| Example Identifier | Categorical | No | Identifier rather than random quantity |

Do not use the example classifications as answers for the actual dataset.

---

# Part 4 - Exploratory Distribution Analysis

For each variable selected for further analysis, examine its empirical behavior.

Depending on the variable, useful methods may include:

- summary statistics,
- frequency tables,
- histograms,
- empirical PMFs,
- empirical CDFs,
- box plots,
- percentiles,
- skewness,
- mean-to-variance comparisons,
- and time-series plots.

Do not immediately fit a theoretical distribution.

First determine what the observations actually look like.

For each selected variable, describe:

- center,
- spread,
- symmetry or skewness,
- range,
- unusual observations,
- physical limits,
- and any patterns that may affect probability modeling.

---

# Part 5 - Evaluate Candidate Probability Distributions

Using the concepts introduced in Lesson 02, identify plausible probability distributions for selected variables.

Available models from the lesson include:

- Bernoulli
- Binomial
- Poisson
- Normal
- Lognormal
- Exponential

You are **not required to use all six distributions**.

You are also not required to force every selected variable into one of these models.

For each candidate model, explain:

1. What random variable is being modeled?
2. Is the variable discrete or continuous?
3. Why is the distribution physically plausible?
4. What assumptions does the distribution require?
5. Which assumptions appear reasonable?
6. Which assumptions may be questionable?

Document your reasoning **before** evaluating the quality of the fit.

---

# Part 6 - Parameter Estimation

Estimate the required parameters for the distributions you selected.

Depending on the model, these may include:

$$
p
$$

$$
n
$$

$$
\lambda
$$

$$
\mu
$$

$$
\sigma
$$

or other parameters required by the selected distribution.

Document:

- the parameter,
- its estimated value,
- how it was estimated,
- its units where applicable,
- and its physical interpretation.

Do not report parameters without explaining what they mean.

---

# Part 7 - Empirical vs. Theoretical Comparison

Compare the selected theoretical distributions with the observed data.

For discrete variables, consider comparing:

- empirical relative frequencies,
- theoretical PMFs,
- empirical CDFs,
- theoretical CDFs.

For continuous variables, consider comparing:

- histograms,
- theoretical PDFs,
- empirical CDFs,
- theoretical CDFs.

Your plots should allow the empirical and theoretical behavior to be compared directly.

Do not judge the model solely by whether two curves appear reasonably close.

Consider the underlying engineering assumptions as well.

---

# Part 8 - Probability Questions

Use your selected probability models to answer engineering questions about the system.

Develop at least **five probability questions** based on the dataset.

Your questions should include a mixture of:

- probability below a threshold,
- probability above a threshold,
- probability within a range,
- probability of an exact discrete count,
- probability of multiple events,
- or probability associated with waiting time.

At least one question should involve an **exceedance probability**.

At least one question should involve a **discrete random variable**.

At least one question should involve a **continuous random variable**.

For every calculation, state the question in plain engineering language before presenting the mathematical result.

---

# Part 9 - Empirical Probability vs. Model Probability

Select at least two of your probability questions and calculate the probability using both:

1. the empirical observations,
2. the theoretical probability model.

For example, conceptually:

$$
P(X>x)
$$

can be estimated from the observed data as:

$$
\hat{P}_{empirical}
=
\frac{
\text{Number of observations greater than }x
}{
\text{Total number of valid observations}
}
$$

The same probability can then be estimated from the theoretical distribution.

Compare the results.

Discuss:

- How close are the estimates?
- Why might they differ?
- Which estimate would you be more comfortable using?
- Does the answer depend on the engineering decision being made?

---

# Part 10 - Investigate Time Dependence

Probability distributions describe uncertainty, but many simple probability models implicitly assume that observations arise from a stable process.

Infrastructure systems may not behave that way.

Investigate whether at least one modeled variable changes with:

- time of day,
- day of week,
- month,
- season,
- weather,
- equipment operating state,
- or another available operational condition.

Determine whether treating the entire dataset as one probability distribution hides important structure.

For example, a variable may have one distribution during:

```text
Normal operating conditions
```

and another during:

```text
Peak-demand conditions
```

Do not assume that one fitted distribution represents every operating regime.

---

# Part 11 - Investigate Event Independence

For any event-count model you develop, consider whether events appear independent.

Investigate whether events:

- cluster in time,
- occur during particular seasons,
- follow unusual operational conditions,
- occur near other failures,
- or correspond with environmental conditions.

If events appear clustered, discuss what this means for a simple constant-rate probability model.

You are not expected to develop a more advanced model yet.

The objective is to recognize the limitation.

---

# Part 12 - Engineering Interpretation

Prepare a short engineering assessment of your findings.

Address the following questions.

## System Behavior

- Which variables were reasonably represented by theoretical probability distributions?
- Which were not?
- What operational conditions produced the greatest variability?
- Were any distributions substantially skewed?
- Were any extreme events operationally significant?

## Model Suitability

- Which probability model appeared most useful?
- Which model had the weakest assumptions?
- Which model required the strongest assumptions?
- Did any model fit the observations reasonably well but still appear physically questionable?

## Risk

- What conditions appear unusual based on the historical record?
- Which conditions could affect system reliability?
- What events might warrant additional investigation by utility staff?

## Limitations

Discuss limitations such as:

- observation period,
- missing data,
- sensor accuracy,
- changing operating conditions,
- seasonal behavior,
- asset heterogeneity,
- event dependence,
- maintenance activities,
- and the assumption that historical behavior represents future conditions.

---

# Part 13 - Engineering Recommendation

Assume your analysis will be reviewed by the utility's engineering manager.

Prepare a brief recommendation describing:

1. which probability models you would be comfortable using,
2. what engineering questions those models can reasonably support,
3. which models you would **not** recommend relying upon,
4. what additional data you would request,
5. and what additional analysis should be performed before using the models for operational or capital-planning decisions.

Do not simply state:

> "More data are needed."

Specify **what data** and **why**.

---

# Required Deliverables

Your completed exercise should include:

## Data Assessment

- Data inventory
- Data-quality assessment
- Documentation of cleaning decisions
- Identification of candidate random variables

## Statistical Analysis

- Descriptive statistics
- Empirical distributions
- Candidate theoretical distributions
- Estimated distribution parameters
- Empirical vs. theoretical comparisons
- Probability calculations
- Investigation of temporal behavior

## Visualizations

At minimum:

- One discrete probability comparison
- One continuous probability comparison
- One empirical vs. theoretical CDF comparison
- One time-based visualization
- Additional plots required to support your analysis

## Engineering Documentation

- Distribution-selection reasoning
- Assumption assessment
- Engineering interpretation
- Model limitations
- Final recommendation

---

# Code Requirements

Your analysis should follow the project Python standards.

Use:

- Python 3.12+
- Pandas
- NumPy
- Matplotlib
- SciPy
- Type hints for reusable functions

Separate:

```text
Data loading
Data validation
Data transformation
Statistical analysis
Visualization
Engineering interpretation
```

where practical.

Do not write one enormous script that performs the entire analysis from top to bottom with every operation living at module scope.

Reusable functionality should be extracted where doing so provides actual value.

---

# Data Preservation

Raw data must remain unchanged.

Use the project structure:

```text
data/
├── raw/
│   └── water_distribution/
│
└── processed/
```

Original utility-style files belong under:

```text
data/raw/water_distribution/
```

Any cleaned, aggregated, or derived datasets should be written to:

```text
data/processed/
```

Your analysis should be reproducible from the original raw files.

---

# Analytical Constraints

For this exercise:

- Do not use machine learning.
- Do not use automated distribution-selection packages.
- Do not select distributions solely using goodness-of-fit scores.
- Do not discard extreme observations without investigation.
- Do not assume normality without justification.
- Do not treat correlation as evidence of causation.
- Do not modify raw data manually.

The objective is to develop statistical and engineering reasoning, not to ask a library to make the decisions.

---

# Questions to Consider

As you work through the analysis, continually ask:

> What physical process generated this variable?

> Is this variable actually random, or is it largely controlled by operations?

> Is the process stationary enough for one distribution to be meaningful?

> Are observations independent?

> Are extreme values errors or real events?

> Does the theoretical model permit physically impossible values?

> Does a reasonable statistical fit imply a reasonable engineering model?

> What decision could this probability estimate actually support?

These questions are more important than obtaining a beautifully fitted curve.

---

# Stretch Goal

Suppose the engineering manager asks:

> "Which distribution fits the data best?"

Prepare a response explaining why that question alone is insufficient.

Then propose a better question for evaluating the probability models.

Your response should distinguish between:

- statistical fit,
- physical plausibility,
- model assumptions,
- and usefulness for engineering decisions.

---

# Final Deliverable

Prepare a short engineering memorandum summarizing your analysis.

The memorandum should be written for a technically knowledgeable engineering manager who understands the water distribution system but does not specialize in statistics.

Recommended structure:

```text
1. Objective
2. Available Data
3. Data Quality
4. Statistical Approach
5. Probability Models Evaluated
6. Key Findings
7. Engineering Interpretation
8. Limitations
9. Recommendations
```

Do not fill the memorandum with equations or raw statistical output.

The detailed analysis supports the recommendation.

The memorandum communicates what the analysis means.

---

# Completion Criteria

Exercise 02a is complete when you can defend:

- why you selected each random variable,
- why you selected each candidate distribution,
- how you estimated its parameters,
- what assumptions the model makes,
- whether the observed data support those assumptions,
- what the resulting probabilities mean,
- and whether those probabilities are useful for an engineering decision.

A technically correct SciPy call is not sufficient.

The objective is to move from:

```text
Here is a probability distribution.
```

to:

```text
Here is the uncertainty I observed,
here is the model I used to represent it,
here is why I selected that model,
here are the assumptions I made,
and here is what the result means for the infrastructure system.
```

That is the analytical skill this exercise is intended to develop.
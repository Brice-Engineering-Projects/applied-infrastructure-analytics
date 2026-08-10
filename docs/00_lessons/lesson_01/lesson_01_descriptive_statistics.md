# Lesson 01 - Descriptive Statistics for Infrastructure Data

## Purpose

Infrastructure engineers routinely work with datasets containing measurements that vary over time and space.

Examples include:

- Streamflow
- Rainfall
- Water demand
- Wastewater flow
- Pump runtime
- Pressure
- Groundwater elevation
- Pipe age
- Failure frequency
- Construction cost

Before applying probability models, regression, machine learning, or simulation, an engineer should first understand the basic characteristics of the available data.

Descriptive statistics provide a compact way to summarize a dataset and answer questions such as:

- What is a typical value?
- How much does the data vary?
- Are unusually high or low observations present?
- Is the mean representative of the dataset?
- How widely are observations distributed around the center?
- Does the dataset contain characteristics that deserve further investigation?

This lesson develops those concepts using an infrastructure dataset and focuses on interpreting statistics rather than simply calculating them.

---

# Scenario

A municipal utility operates a water distribution system supplied by a water treatment facility.

The utility has collected daily water-demand measurements and wants to better understand how demand varies.

The engineering team is beginning an evaluation of system capacity and future capital improvements.

Before performing forecasting or probabilistic analysis, the team needs a statistical summary of historical water demand.

As an engineer supporting the analysis, you have been asked to characterize the dataset and identify features that may affect future engineering analysis.

Your objective is **not** to determine whether the system has adequate capacity.

Your objective is to determine:

> What does the historical dataset tell us about the magnitude, variability, and distribution of water demand?

---

# Learning Objectives

After completing this lesson, you should be able to:

- Load and inspect an engineering dataset using Pandas.
- Distinguish between a sample and a population.
- Calculate measures of central tendency.
- Calculate measures of dispersion.
- Explain variance and standard deviation conceptually.
- Calculate and interpret percentiles and quartiles.
- Calculate the interquartile range.
- Identify potential outliers.
- Explain why the mean alone may poorly characterize an engineering dataset.
- Compare mean and median to identify possible skewness.
- Interpret descriptive statistics in an engineering context.
- Build reusable Python functions for descriptive statistical analysis.

---

# Dataset

The dataset contains historical daily water-demand measurements from a municipal water system.

Each observation contains at minimum:

- Date
- Daily Water Demand (MGD)

Additional variables may be introduced if appropriate.

The dataset should contain enough observations to demonstrate meaningful variation while remaining easy to inspect and visualize.

---

# 1. Population vs. Sample

Before calculating statistics, determine what your dataset represents.

A **population** contains every observation relevant to the question being studied.

A **sample** contains only some observations from a larger population or process.

For example, suppose a utility has recorded daily demand for one year. Those 365 observations represent the complete record for that particular year.

However, if the engineering question concerns:

> What water demands might this system experience over the next 30 years?

those 365 measurements are only a **sample of the underlying demand process**.

This distinction matters because many statistical calculations differ depending on whether the data represent a sample or an entire population.

### Engineering Question

Consider the dataset used in this lesson.

Is it:

- A population?
- A sample?
- Potentially either, depending on the engineering question?

Explain your reasoning.

---

# 2. Initial Data Inspection

Load the dataset using Pandas.

Before calculating statistics, inspect the data.

Determine:

- Number of observations
- Column names
- Data types
- Missing values
- Duplicate observations
- Minimum and maximum dates
- Whether the units are clearly defined

Do not immediately calculate statistics. First determine whether the dataset appears suitable for analysis.

### Questions

- Are any observations missing?
- Are there duplicate dates?
- Are any values physically impossible?
- Are units consistent?
- Does the time period appear complete?
- Are there suspicious values that deserve investigation?

Document your observations.

---

# 3. Measures of Central Tendency

Measures of central tendency describe where observations tend to concentrate.

The three most common measures are:

- Mean
- Median
- Mode

## 3.1 Mean

The arithmetic mean is calculated as:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

where:

- $x_i$ = individual observation
- $n$ = number of observations
- $\bar{x}$ = sample mean

Calculate the mean daily water demand.

### Interpretation

Do not simply report:

> Mean demand = X MGD.

Explain what the value represents.

Consider:

- Does this appear representative of a typical day?
- Could unusually high-demand days influence the mean?
- Would designing infrastructure solely around mean demand be appropriate?

## 3.2 Median

The median represents the middle observation after the values are sorted.

Half of the observations fall below the median and half fall above it.

Calculate the median daily demand.

Compare:

$$
\text{Mean}
$$

with:

$$
\text{Median}
$$

### Questions

- Are the mean and median approximately equal?
- If not, which is larger?
- What might this suggest about the distribution?
- Could extreme observations be influencing the mean?

## 3.3 Mode

The mode is the most frequently occurring value.

Calculate the mode if one exists.

### Engineering Question

Consider whether the mode provides useful information for a continuous engineering variable such as daily water demand.

Explain why the mode may be more or less useful depending on:

- Measurement precision
- Rounding
- Data resolution
- Type of variable

---

# 4. Measures of Dispersion

Knowing the center of a dataset is not enough.

Consider two systems:

```text
System A:
9.9, 10.0, 10.0, 10.1, 10.0

System B:
5.0, 7.5, 10.0, 12.5, 15.0
```

Both systems have approximately the same mean. However, their behavior is clearly different.

System A is relatively stable. System B experiences substantial variability.

Infrastructure design often depends as much on **variability** as it does on the average.

---

# 5. Range

The range is:

$$
\text{Range} = x_{\max} - x_{\min}
$$

Calculate:

- Minimum demand
- Maximum demand
- Range

### Questions

- How large is the range relative to the mean?
- Does the maximum appear unusually high?
- Does the minimum appear unusually low?
- What operational conditions might explain these extremes?

### Limitation

The range depends entirely on two observations: the minimum and maximum.

It therefore provides very little information about how the remaining observations are distributed.

---

# 6. Variance

Variance measures how far observations tend to spread around the mean.

For a sample:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Conceptually, the calculation performs the following steps:

1. Calculate the mean.
2. Determine the distance between each observation and the mean.
3. Square those distances.
4. Add the squared distances.
5. Divide by the appropriate number of degrees of freedom.

### Why Square the Differences?

If we simply added deviations from the mean:

$$
x_i-\bar{x}
$$

positive and negative deviations would cancel.

Squaring the deviations prevents this cancellation and gives greater weight to observations farther from the mean.

## Sample vs. Population Variance

Population variance commonly uses:

$$
\sigma^2 = \frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

Sample variance commonly uses:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

The $n-1$ denominator is known as **Bessel's correction**.

It compensates for the tendency of a sample to underestimate the variability of the population from which it was drawn.

### Python Investigation

Determine what default behavior Pandas uses when calculating:

```python
series.var()
```

Identify the `ddof` parameter and determine why it matters.

---

# 7. Standard Deviation

Standard deviation is the square root of variance:

$$
s = \sqrt{s^2}
$$

Standard deviation is generally easier to interpret because it has the same units as the original variable.

If demand is measured in MGD:

```text
Variance           -> MGD²
Standard deviation -> MGD
```

Calculate the standard deviation of daily demand.

### Interpretation

Do not stop at:

> Standard deviation = X MGD.

Instead ask:

- Is variability small or large relative to average demand?
- Does the system appear relatively stable?
- Are occasional extreme demands responsible for much of the variability?
- Would this variability matter when evaluating system capacity?

---

# 8. Coefficient of Variation

Standard deviation provides absolute variability.

Sometimes we want to understand variability **relative to the magnitude of the data**.

The coefficient of variation is:

$$
CV = \frac{s}{\bar{x}}
$$

It is often expressed as a percentage:

$$
CV(\%) = \frac{s}{\bar{x}}\times100
$$

For example:

```text
System A:
Mean = 2 MGD
Standard Deviation = 1 MGD
CV = 50%

System B:
Mean = 20 MGD
Standard Deviation = 1 MGD
CV = 5%
```

Both have the same standard deviation, but the variability has very different significance relative to normal system demand.

Calculate the coefficient of variation for the dataset.

### Engineering Question

Does the CV change your interpretation of the standard deviation?

---

# 9. Percentiles

Percentiles describe the value below which a specified percentage of observations occur.

For example:

$$
P_{90}
$$

represents the value at or below which approximately 90% of observations occur.

Calculate:

- 10th percentile
- 25th percentile
- 50th percentile
- 75th percentile
- 90th percentile
- 95th percentile

### Questions

- How does the 50th percentile compare with the median?
- How far is the 95th percentile above the mean?
- What does the 90th percentile tell you about high-demand conditions?

---

# 10. Quartiles

Quartiles divide the observations into four portions.

$$
Q_1 = \text{25th percentile}
$$

$$
Q_2 = \text{50th percentile} = \text{median}
$$

$$
Q_3 = \text{75th percentile}
$$

Calculate Q1, Q2, and Q3.

Interpret each value in plain engineering language.

---

# 11. Interquartile Range

The interquartile range is:

$$
IQR = Q_3-Q_1
$$

The IQR describes the spread of the middle 50% of observations.

Unlike the full range, it is less sensitive to extreme values.

Calculate the IQR.

Compare:

- Range
- Standard deviation
- IQR

### Question

What does each measure tell you that the others do not?

---

# 12. Potential Outliers

A common exploratory method for identifying potential outliers uses the IQR.

Calculate:

$$
\text{Lower Fence} = Q_1 - 1.5(IQR)
$$

and:

$$
\text{Upper Fence} = Q_3 + 1.5(IQR)
$$

Observations outside these limits may be flagged for further investigation.

### Important Engineering Warning

An outlier is **not automatically bad data**.

A high water-demand observation could represent:

- Extreme weather
- Major irrigation demand
- Fire flow
- Operational changes
- A large industrial demand
- Metering error
- Data-entry error
- A legitimate extreme event

Statistical identification should therefore lead to **investigation**, not **automatic deletion**.

Engineering context determines whether an observation is credible.

---

# 13. Visualization

Create a box plot of daily water demand.

The box plot should display:

- Median
- First quartile
- Third quartile
- Interquartile range
- Potential outliers

Compare the box plot with the descriptive statistics.

### Questions

- Does the distribution appear symmetric?
- Are potential outliers visible?
- Is one side of the distribution more spread out than the other?
- Does the visualization support your interpretation of the mean and median?

---

# 14. Build a Reusable Descriptive Statistics Function

Create a Python function that calculates descriptive statistics for a numeric Pandas Series or DataFrame column.

The function should calculate at minimum:

- Number of observations
- Mean
- Median
- Minimum
- Maximum
- Range
- Variance
- Standard deviation
- Q1
- Q3
- IQR
- Coefficient of variation

Consider an interface similar to:

```python
def descriptive_statistics(data: pd.Series) -> dict[str, float]:
    ...
```

Think about:

- Input validation
- Missing values
- Empty datasets
- Numeric data types
- Return types
- Sample vs. population statistics

---

# 15. Validate the Function

Do not assume that a function is correct merely because Python executed it without complaining.

Create a small dataset where the expected results can be calculated manually.

For example:

```python
data = [2, 4, 6, 8, 10]
```

Calculate selected statistics manually.

Compare those values with the results returned by your function.

Then compare your function with appropriate Pandas or NumPy calculations.

### Questions

- Do the values agree?
- If variance or standard deviation differs, are both methods using the same degrees of freedom?
- How should missing values be handled?

---

# 16. Engineering Interpretation

Prepare a short engineering discussion based on the statistical analysis.

### Typical Demand

What value best represents typical daily demand?

Consider the mean and median. Explain your choice.

### Variability

How much does daily demand vary?

Discuss:

- Range
- Standard deviation
- IQR
- Coefficient of variation

### Extreme Observations

Are potential outliers present?

If so:

- Are they necessarily errors?
- What additional information would you investigate?
- Could they represent important operational conditions?

### Capacity

Does the dataset contain evidence that system capacity should be investigated?

Do **not** determine whether the system is adequately sized.

Explain what additional engineering information would be required before making that determination.

---

# 17. Engineering Judgment

Suppose the dataset has:

```text
Mean Demand       = 8.2 MGD
Median Demand     = 7.6 MGD
95th Percentile   = 11.8 MGD
Maximum Demand    = 15.1 MGD
```

An engineer proposes using:

```text
Design Demand = Mean Demand = 8.2 MGD
```

because:

> "The average represents normal system operation."

Evaluate this reasoning.

Consider:

- What happens during high-demand periods?
- What information is hidden by the mean?
- What consequences could occur if infrastructure were designed only around average conditions?
- Does the maximum automatically represent the correct design condition?
- What additional criteria should influence the engineering decision?

The objective is not to identify one correct design flow.

The objective is to understand why **statistical summaries support engineering judgment rather than replace it**.

---

# Deliverables

Upon completion, the lesson should produce:

- Data-quality summary
- Descriptive statistics table
- Mean and median comparison
- Range
- Sample variance
- Sample standard deviation
- Coefficient of variation
- Percentile table
- Quartiles and IQR
- Potential-outlier analysis
- Box plot
- Reusable descriptive-statistics Python function
- Unit tests for the function
- Short engineering interpretation

---

# Stretch Goal 1 - Mean vs. Median

Create two small datasets.

The first should have:

```text
Mean ≈ Median
```

The second should contain an extreme high value that causes:

```text
Mean > Median
```

Compare the results and explain why the median is more resistant to extreme values.

---

# Stretch Goal 2 - Standard Deviation

Create two datasets with approximately the same mean but substantially different standard deviations.

Plot both datasets.

Explain what standard deviation reveals that the mean cannot.

---

# Stretch Goal 3 - Remove an Outlier

Identify the largest potential outlier in the water-demand dataset.

Calculate descriptive statistics:

1. With the observation included.
2. With the observation temporarily excluded.

Compare:

- Mean
- Median
- Standard deviation
- Range
- IQR

Do **not** permanently remove the observation.

Explain which statistics changed the most and why.

Then answer:

> Does the fact that removing an observation improves the statistical appearance of the dataset justify removing it?

---

# Stretch Goal 4 - Connect to Lesson 00

Recall the concepts from Lesson 00:

- Histogram
- PDF
- CDF

Compare the descriptive statistics with the distribution plots.

Consider:

- Where does the mean fall on the histogram?
- Where does the median fall?
- Can you identify the median using the empirical CDF?
- How does standard deviation relate to the apparent spread?
- Do the descriptive statistics alone reveal skewness as clearly as the histogram?
- Can a few summary statistics fully describe the shape of a distribution?

Explain why numerical summaries and visualizations should generally be used together.

---

# Key Concepts to Remember

## Mean

> Where is the arithmetic center of the data?

## Median

> What value divides the observations in half?

## Range

> How far apart are the minimum and maximum observations?

## Variance

> How much squared deviation exists around the mean?

## Standard Deviation

> How much variability exists around the mean in the original units?

## Coefficient of Variation

> How large is the variability relative to the mean?

## Percentile

> What value is greater than or equal to a specified percentage of the observations?

## IQR

> How widely spread is the middle 50% of the data?

## Potential Outlier

> Which observations are statistically unusual enough to deserve investigation?

---

# Looking Ahead

Descriptive statistics tell us what the observed data looks like.

They do not yet tell us whether an observed pattern represents the broader process from which the data originated.

That leads to the next lesson:

# Lesson 02 - Common Probability Distributions

The next lesson will investigate:

- Random variables
- Discrete vs. continuous variables
- Distribution parameters
- Normal distribution
- Lognormal distribution
- Exponential distribution
- Extreme-value distributions
- Distribution fitting
- Goodness of fit
- Engineering interpretation

These concepts will allow us to move from:

> **What did we observe?**

toward:

> **What probability model might reasonably describe the process generating those observations?**

That distinction becomes essential when analyzing rare events, infrastructure reliability, and engineering risk.

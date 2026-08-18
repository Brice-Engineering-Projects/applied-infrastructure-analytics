# Lesson 01 - Descriptive Statistics

## Purpose

Engineering datasets often contain hundreds, thousands, or millions of observations.

Before performing probability analysis, regression, forecasting, reliability analysis, or other statistical methods, an engineer needs to understand the basic characteristics of the data.

Descriptive statistics provide tools for answering fundamental questions such as:

- What is a typical value?
- How much do observations vary?
- What range of conditions has been observed?
- Are extreme observations present?
- Is the distribution concentrated or widely dispersed?
- Do different measures of "typical" tell the same story?

These questions appear throughout infrastructure engineering.

Examples include:

- What is typical daily water demand?
- How variable is pump runtime?
- What is the typical groundwater elevation?
- How widely do construction bid prices vary?
- What is the typical number of annual water-main failures?
- How variable are wastewater influent flows?

This lesson introduces the descriptive statistics commonly used to answer these questions.

The central idea is:

> **No single statistic adequately describes a dataset.**

Descriptive statistics should be interpreted together and in the context of the engineering system that produced the observations.

---

# Engineering Motivation

A municipal utility operates a wastewater pump station serving an established residential service area.

Operations staff periodically review pump runtime to identify changes in station operation and support maintenance planning.

The station contains two pumps operating in a lead-lag configuration.

For this introductory analysis, the engineering team has extracted a small sample of **daily total station runtime** observations.

Before investigating trends, equipment performance, or reliability, the engineer needs to understand what normal runtime looks like and how much it varies from day to day.

This creates several basic analytical questions:

> **What is a typical daily runtime?**

> **How much does runtime vary?**

> **What range of operating conditions occurred during the observation period?**

Descriptive statistics provide the first tools for answering these questions.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Explain the purpose of descriptive statistics.
- Distinguish measures of central tendency from measures of dispersion.
- Calculate and interpret the mean.
- Calculate and interpret the median.
- Understand when the mode is useful.
- Calculate minimum, maximum, and range.
- Explain variance conceptually and mathematically.
- Calculate and interpret standard deviation.
- Distinguish sample variance from population variance.
- Calculate and interpret percentiles and quartiles.
- Explain the interquartile range.
- Create and interpret a box plot.
- Recognize how extreme observations affect different statistics.
- Calculate descriptive statistics using Python.
- Validate library calculations using direct implementations.
- Interpret descriptive statistics in an engineering context.

---

# Prerequisites

Before beginning this lesson, you should be familiar with:

- Basic algebra
- Python variables and functions
- Python lists or NumPy arrays
- Basic Pandas operations
- Histograms
- Probability density
- Cumulative probability

The probability concepts were introduced in:

**Lesson 00 - Histograms, Probability Density Functions, and Cumulative Distribution Functions**

No advanced statistical background is required.

---

# Engineering Scenario

## Background

A municipal wastewater utility operates **Pump Station PS-17**, which serves an established residential basin.

The station contains two submersible pumps operating in a lead-lag configuration.

Daily station runtime varies because influent wastewater flow changes from day to day.

Potential influences include:

- Customer water use
- Day of week
- Rainfall
- Groundwater conditions
- Pump sequencing
- Normal operational variability

Operations staff want an initial statistical description of daily station runtime before performing more detailed operational analysis.

For this lesson, a small sample has been selected so that the statistical calculations can be inspected and verified manually.

---

## Engineering Question

The primary engineering question is:

> **What do the observed daily runtimes tell us about typical pump-station operation and day-to-day variability?**

This lesson does not attempt to determine why runtime varies.

The objective is first to learn how that variability can be described.

---

# Dataset

## Dataset Description

The instructional dataset contains **15 daily observations** of total station pump runtime.

Each observation represents the combined number of hours that the station pumps operated during one calendar day.

Because two pumps are installed, total station runtime can exceed 24 hours if both pumps operate during portions of the same day.

The dataset is intentionally small and controlled.

It is designed for conceptual understanding and manual verification rather than to reproduce the complexity of a complete SCADA export.

---

## Observations

| Day | Total Pump Runtime (hr/day) |
| ---: | ---: |
| 1 | 9.8 |
| 2 | 10.4 |
| 3 | 10.1 |
| 4 | 11.0 |
| 5 | 10.7 |
| 6 | 9.9 |
| 7 | 10.5 |
| 8 | 10.2 |
| 9 | 11.3 |
| 10 | 10.6 |
| 11 | 10.0 |
| 12 | 10.8 |
| 13 | 9.7 |
| 14 | 10.3 |
| 15 | 14.2 |

Notice that one observation is substantially larger than most of the others.

Do not assume that it is an error.

It is an observed value that requires interpretation.

---

# Initial Data Inspection

Before calculating statistics, inspect the observations.

Ask:

- What does each row represent?
- What units are being used?
- What range of values appears typical?
- Is there an observation that stands out?
- Does the dataset appear approximately symmetric?
- Would one number be sufficient to describe these observations?

A quick visual inspection suggests that most daily runtimes are concentrated around approximately 10 to 11 hours per day.

Day 15 appears different.

That observation gives us an opportunity to examine how different descriptive statistics respond to an unusually high value.

---

# Measures of Central Tendency

Measures of central tendency attempt to describe where observations tend to be located.

Three common measures are:

- Mean
- Median
- Mode

They answer related questions, but they are not interchangeable.

---

# Concept 1 - Mean

## Conceptual Understanding

The arithmetic mean is what is commonly called the **average**.

It combines all observations into a single measure representing the center of the dataset.

Every observation contributes to the mean.

This is both useful and important to remember.

Because every value contributes, unusually large or unusually small observations can influence the mean substantially.

---

## Engineering Interpretation

For the pump-station dataset, the mean answers:

> **If the observed runtime were distributed equally among all 15 days, how many hours of runtime would each day contain?**

The mean provides one measure of typical station operation.

It does not describe how much daily runtime varies.

---

# Mathematical Foundation

For observations:

$$
x_1, x_2, \ldots, x_n
$$

the sample mean is:

$$
\bar{x}
=
\frac{1}{n}
\sum_{i=1}^{n} x_i
$$

where:

- $x_i$ = individual observation
- $n$ = number of observations
- $\bar{x}$ = sample mean

---

## What the Equation Is Doing

The calculation has two steps:

1. Add all observations.
2. Divide the total by the number of observations.

For the pump-station data:

$$
\bar{x}
=
\frac{
9.8+10.4+10.1+\cdots+14.2
}{15}
$$

The sum of the observations is:

$$
158.5
$$

Therefore:

$$
\bar{x}
=
\frac{158.5}{15}
$$

$$
\bar{x}
=
10.567 \text{ hr/day}
$$

The mean daily station runtime is approximately:

$$
\boxed{10.57 \text{ hr/day}}
$$

---

## Units

The observations are measured in:

$$
\text{hr/day}
$$

Therefore, the mean is also expressed in:

$$
\text{hr/day}
$$

---

# Concept 2 - Median

## Conceptual Understanding

The median is the middle observation after the values have been arranged from smallest to largest.

Unlike the mean, the median depends primarily on the **position** of observations rather than their magnitude.

This makes the median less sensitive to unusually large or small observations.

---

## Engineering Interpretation

The median answers a slightly different question:

> **What value divides the observed days so that approximately half have lower runtime and half have higher runtime?**

This can be particularly useful when the dataset contains extreme observations or is strongly skewed.

---

# Mathematical Foundation

For an odd number of observations, the median occurs at position:

$$
\frac{n+1}{2}
$$

For:

$$
n=15
$$

the median is the:

$$
\frac{15+1}{2}
=
8^\text{th}
$$

ordered observation.

Sorting the runtimes gives:

$$
9.7,\,
9.8,\,
9.9,\,
10.0,\,
10.1,\,
10.2,\,
10.3,\,
10.4,\,
10.5,\,
10.6,\,
10.7,\,
10.8,\,
11.0,\,
11.3,\,
14.2
$$

The eighth observation is:

$$
\boxed{10.4 \text{ hr/day}}
$$

Therefore:

$$
\text{Median}
=
10.4 \text{ hr/day}
$$

---

# Mean vs. Median

The calculated values are:

| Statistic | Runtime (hr/day) |
| --- | ---: |
| Mean | 10.57 |
| Median | 10.40 |

The mean is slightly larger than the median.

Why?

The unusually high observation of:

$$
14.2 \text{ hr/day}
$$

pulls the mean upward.

The median changes much less because its value depends on the ordering of observations rather than the magnitude of the largest observation.

This illustrates an important distinction:

> **The mean is sensitive to extreme values. The median is more resistant to them.**

Neither statistic is automatically better.

The appropriate interpretation depends on the engineering question and the distribution of the data.

---

# Concept 3 - Mode

## Conceptual Understanding

The mode is the most frequently occurring value.

A dataset may have:

- One mode
- Multiple modes
- No mode

For continuous engineering measurements, exact repeated values may be uncommon.

As a result, the mode is often less useful than the mean or median for continuous sensor measurements.

---

## Engineering Interpretation

In this dataset, every runtime value is unique.

Therefore, there is no mode.

That is not a problem with the dataset.

It simply means that no exact runtime occurred more frequently than another.

Mode becomes more useful for categorical or discrete engineering data.

Examples include:

- Most common pipe material
- Most common failure type
- Most common pump alarm
- Most common asset condition rating
- Most common number of pumps operating

---

# Measures of Dispersion

Central tendency tells us where observations are centered.

It does **not** tell us how much they vary.

Consider two hypothetical stations:

### Station A

```text
10.0, 10.1, 9.9, 10.0, 10.0
```

### Station B

```text
5.0, 8.0, 10.0, 12.0, 15.0
```

Both have a mean of:

$$
10.0
$$

Yet their operating behavior is obviously very different.

This is why measures of dispersion are necessary.

Common measures include:

- Minimum and maximum
- Range
- Variance
- Standard deviation
- Interquartile range

---

# Concept 4 - Minimum, Maximum, and Range

## Minimum

The minimum is the smallest observed value.

For the pump-station dataset:

$$
x_{min}
=
9.7 \text{ hr/day}
$$

---

## Maximum

The maximum is the largest observed value.

$$
x_{max}
=
14.2 \text{ hr/day}
$$

---

## Range

The range is:

$$
R
=
x_{max}-x_{min}
$$

Therefore:

$$
R
=
14.2-9.7
$$

$$
\boxed{R=4.5 \text{ hr/day}}
$$

---

## Engineering Interpretation

The observed daily runtimes span:

$$
4.5 \text{ hr/day}
$$

from the lowest to highest observation.

The range is easy to understand but has an important limitation.

It depends entirely on **two observations**:

- The minimum
- The maximum

If the maximum changes substantially, the range changes substantially even if every other observation remains unchanged.

---

# Concept 5 - Variance

## Conceptual Understanding

Variance measures how far observations tend to be from the mean.

The basic idea is:

1. Determine the mean.
2. Measure how far each observation is from the mean.
3. Square those differences.
4. Combine them into an overall measure of spread.

Why square the differences?

If we simply added deviations from the mean, positive and negative differences would cancel.

Squaring prevents that cancellation.

It also gives larger deviations greater influence.

---

# Mathematical Foundation

For a sample, variance is:

$$
s^2
=
\frac{
\sum_{i=1}^{n}
(x_i-\bar{x})^2
}{
n-1
}
$$

where:

- $x_i$ = individual observation
- $\bar{x}$ = sample mean
- $n$ = number of observations
- $s^2$ = sample variance

---

# Why Divide by \(n-1\)?

This dataset is being treated as a **sample** of possible pump-station operating conditions rather than every operating condition the station could ever experience.

When estimating population variance from a sample, the sample mean has already been estimated from the same observations.

This removes one degree of freedom.

Therefore, sample variance uses:

$$
n-1
$$

rather than:

$$
n
$$

This correction prevents the sample variance from systematically underestimating population variability.

For now, the important distinction is:

### Population variance

$$
\sigma^2
=
\frac{
\sum_{i=1}^{N}(x_i-\mu)^2
}{
N
}
$$

### Sample variance

$$
s^2
=
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}{
n-1
}
$$

The appropriate denominator depends on what the observations represent.

---

# Manual Variance Example

Using the mean:

$$
\bar{x}
=
10.567
$$

calculate each deviation:

$$
x_i-\bar{x}
$$

and square it:

$$
(x_i-\bar{x})^2
$$

A few examples are:

| Runtime | Deviation from Mean | Squared Deviation |
| ---: | ---: | ---: |
| 9.8 | -0.767 | 0.588 |
| 10.4 | -0.167 | 0.028 |
| 10.1 | -0.467 | 0.218 |
| 11.0 | 0.433 | 0.188 |
| 14.2 | 3.633 | 13.201 |

Notice how strongly the 14.2-hour observation contributes to the total squared deviation.

For the complete dataset:

$$
\sum_{i=1}^{15}
(x_i-\bar{x})^2
\approx
19.793
$$

Therefore:

$$
s^2
=
\frac{19.793}{14}
$$

$$
\boxed{s^2 \approx 1.414 \text{ (hr/day)}^2}
$$

---

# Units of Variance

Variance has squared units.

Because runtime is measured in:

$$
\text{hr/day}
$$

variance is expressed in:

$$
(\text{hr/day})^2
$$

This makes variance mathematically useful but somewhat awkward to interpret directly as an engineering quantity.

Standard deviation addresses this problem.

---

# Concept 6 - Standard Deviation

## Conceptual Understanding

Standard deviation is the square root of variance.

$$
s
=
\sqrt{s^2}
$$

Because the square root reverses the squared units of variance, standard deviation is expressed in the **same units as the original observations**.

For the pump-station dataset:

$$
s
=
\sqrt{1.414}
$$

$$
\boxed{s \approx 1.19 \text{ hr/day}}
$$

---

## Engineering Interpretation

The mean daily runtime is approximately:

$$
10.57 \text{ hr/day}
$$

with a standard deviation of approximately:

$$
1.19 \text{ hr/day}
$$

Standard deviation provides a measure of how dispersed the observed runtimes are around the mean.

It should not automatically be interpreted as a fixed engineering tolerance.

Statements such as:

> "Most observations must occur within one standard deviation of the mean"

require additional assumptions about the distribution.

Standard deviation measures spread.

Its probabilistic interpretation depends on the underlying distribution.

---

# Effect of the Extreme Observation

The 14.2-hour observation affects several statistics:

- Mean
- Maximum
- Range
- Variance
- Standard deviation

It affects the median much less.

This does **not** mean the observation should be removed.

Before excluding an unusual observation, an engineer should ask:

- Is it physically possible?
- Was the sensor functioning?
- Was there rainfall?
- Was there unusual system operation?
- Was maintenance occurring?
- Was there an equipment problem?
- Is the value consistent with other records?

An observation should not be deleted simply because it makes the statistics inconvenient.

---

# Concept 7 - Percentiles

## Conceptual Understanding

A percentile identifies the value below which a specified percentage of observations occur.

For example, the 90th percentile represents a value such that approximately:

$$
90\%
$$

of observations occur at or below that value.

Percentiles are useful because they describe the **position of observations within a distribution** without requiring a particular probability distribution.

---

## Engineering Applications

Percentiles are frequently useful for infrastructure analysis.

Examples include:

- 90th-percentile water demand
- 95th-percentile pump runtime
- 10th-percentile pressure
- 95th-percentile wastewater flow
- Percentile-based construction costs
- Condition-score distributions

Percentiles can sometimes communicate operating conditions more intuitively than standard deviation.

---

# Quartiles

Quartiles divide the ordered data into four portions.

Common quartiles are:

### First Quartile

$$
Q_1
=
25^\text{th percentile}
$$

### Second Quartile

$$
Q_2
=
50^\text{th percentile}
=
\text{Median}
$$

### Third Quartile

$$
Q_3
=
75^\text{th percentile}
$$

For this dataset, percentile values should be calculated using Python.

Be aware that software libraries can use different interpolation methods when the desired percentile falls between observations.

That means percentile values from different tools may differ slightly even when both calculations are valid.

---

# Concept 8 - Interquartile Range

The interquartile range is:

$$
IQR
=
Q_3-Q_1
$$

The IQR describes the spread of the middle 50% of observations.

Because it does not depend directly on the minimum or maximum, it is less sensitive to extreme observations than the full range.

This makes the IQR particularly useful when distributions are skewed or contain unusual observations.

---

# Mean and Standard Deviation vs. Median and IQR

These statistics form useful pairs.

| Central Tendency | Dispersion |
| --- | --- |
| Mean | Standard Deviation |
| Median | Interquartile Range |

The first pair is sensitive to extreme values.

The second pair is more resistant to extreme values.

That does not make one pair universally superior.

The choice depends on:

- Distribution shape
- Presence of extreme observations
- Engineering question
- Intended interpretation

---

# Python Implementation

Now calculate the statistics using Python.

## Load the Data

For the lesson dataset, the observations may be represented directly:

```python
import numpy as np
import pandas as pd


runtime_hr = np.array(
    [
        9.8,
        10.4,
        10.1,
        11.0,
        10.7,
        9.9,
        10.5,
        10.2,
        11.3,
        10.6,
        10.0,
        10.8,
        9.7,
        10.3,
        14.2,
    ],
    dtype=float,
)
```

---

# Direct Implementation

Implement several statistics directly.

```python
observations = len(runtime_hr)

mean_runtime = runtime_hr.sum() / observations

minimum_runtime = runtime_hr.min()
maximum_runtime = runtime_hr.max()

runtime_range = maximum_runtime - minimum_runtime

squared_deviations = (runtime_hr - mean_runtime) ** 2

sample_variance = squared_deviations.sum() / (observations - 1)

sample_standard_deviation = np.sqrt(sample_variance)
```

This implementation closely follows the mathematical definitions.

---

# NumPy Implementation

Now calculate the same values using NumPy.

```python
mean_runtime = np.mean(runtime_hr)
median_runtime = np.median(runtime_hr)

minimum_runtime = np.min(runtime_hr)
maximum_runtime = np.max(runtime_hr)

runtime_range = np.ptp(runtime_hr)

sample_variance = np.var(runtime_hr, ddof=1)

sample_standard_deviation = np.std(runtime_hr, ddof=1)

q1 = np.percentile(runtime_hr, 25)
q3 = np.percentile(runtime_hr, 75)

iqr = q3 - q1
```

Notice:

```python
ddof=1
```

This instructs NumPy to calculate **sample** variance and sample standard deviation.

Without this parameter, NumPy defaults to population calculations.

---

# Pandas Implementation

The observations may also be represented using a Pandas Series.

```python
runtime = pd.Series(runtime_hr, name="runtime_hr")
```

Individual statistics can then be calculated using:

```python
runtime.mean()
runtime.median()
runtime.min()
runtime.max()
runtime.var()
runtime.std()
runtime.quantile(0.25)
runtime.quantile(0.75)
```

Pandas uses:

```text
ddof=1
```

by default for `Series.var()` and `Series.std()`.

Understanding library defaults matters.

Two libraries can appear to disagree simply because they are calculating different definitions.

---

# Descriptive Summary

Pandas provides:

```python
runtime.describe()
```

which returns statistics including:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum

This is convenient for initial exploration.

However:

> **Convenience does not remove the need to understand what the statistics mean.**

`describe()` is a summary tool, not an engineering conclusion generator.

Mercifully, Pandas has not yet added a `.tell_me_what_to_build()` method.

---

# Validation

Compare results obtained using different approaches.

Create a table similar to:

| Statistic | Direct Calculation | NumPy/Pandas |
| --- | ---: | ---: |
| Mean | | |
| Minimum | | |
| Maximum | | |
| Range | | |
| Sample Variance | | |
| Sample Standard Deviation | | |

The results should agree within normal floating-point precision.

If they do not, investigate the reason.

Pay particular attention to:

- Sample vs. population definitions
- `ddof`
- Percentile interpolation
- Rounding

---

# Visualization - Box Plot

A box plot provides a compact visualization of:

- Median
- Quartiles
- Interquartile range
- Overall spread
- Potential extreme observations

Create a box plot:

```python
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

ax.boxplot(runtime_hr)

ax.set_ylabel("Daily Station Runtime (hr/day)")
ax.set_title("PS-17 Daily Pump Runtime")

fig.tight_layout()
plt.show()
```

---

# Interpreting the Box Plot

Examine:

- Location of the median
- Width of the interquartile range
- Length of the whiskers
- Presence of observations plotted beyond the whiskers

Compare the visualization with the numerical statistics.

Ask:

> **Does the box plot reinforce what the mean, median, range, and standard deviation suggested?**

---

# Box Plot "Outliers"

Many box plots identify observations using a rule based on the interquartile range.

A common rule identifies observations outside:

$$
Q_1-1.5(IQR)
$$

or:

$$
Q_3+1.5(IQR)
$$

These observations are often called **outliers**.

That terminology can be misleading in engineering analysis.

The box plot is identifying observations that are unusual according to a statistical rule.

It is **not determining that the observation is erroneous**.

A statistically unusual pump runtime may represent:

- A storm event
- An equipment condition
- A maintenance event
- Increased influent flow
- A legitimate extreme operating day
- A sensor problem

The statistical method detects unusualness.

Engineering investigation determines meaning.

---

# Comparing the Statistics

At this point, several different characteristics of the same dataset can be described.

| Statistic | Describes |
| --- | --- |
| Mean | Arithmetic center |
| Median | Middle ordered observation |
| Mode | Most frequently occurring value |
| Minimum | Lowest observed value |
| Maximum | Highest observed value |
| Range | Total observed spread |
| Variance | Squared dispersion around the mean |
| Standard Deviation | Dispersion around the mean in original units |
| Percentile | Position within the ordered distribution |
| IQR | Spread of the middle 50% |

No individual statistic provides a complete description.

---

# Engineering Interpretation

Return to the original question:

> **What do the observed daily runtimes tell us about typical pump-station operation and day-to-day variability?**

The observations indicate that most recorded days are concentrated within a relatively narrow runtime range near 10 to 11 hours per day.

The mean is somewhat higher than the median because the 14.2-hour observation influences the arithmetic average.

The range and standard deviation are also affected by this observation.

The median and interquartile range provide measures that are less sensitive to it.

The appropriate conclusion is not:

> "14.2 hours is an outlier and should be deleted."

Instead:

> **The 14.2-hour observation is unusual relative to the remainder of the sample and would warrant additional investigation if this were an operational dataset.**

---

# Observation vs. Interpretation

## Observation

One day contains substantially more pump runtime than the remaining observations.

## Possible Interpretation

Potential explanations could include:

- Higher influent flow
- Rainfall-dependent inflow and infiltration
- Changed pump performance
- Different pump sequencing
- Maintenance activity
- Instrumentation problems

## Additional Evidence Needed

Useful additional information could include:

- Rainfall history
- Influent flow
- Wet-well levels
- Individual pump runtime
- Pump starts
- Alarm history
- Maintenance records
- Motor current
- Discharge pressure

The runtime observation alone cannot establish the cause.

---

# Engineering Judgment

Descriptive statistics identify characteristics of the observed data.

They do not explain the physical mechanisms that produced those characteristics.

For this dataset, an engineer could reasonably conclude that:

- Typical daily runtime is around 10 to 11 hours.
- Most observations are relatively concentrated.
- One observation differs substantially from the others.
- That observation materially affects some descriptive statistics.
- Additional operational information would be required to determine why that condition occurred.

This is the distinction between:

```text
Statistical Description
        ↓
Engineering Investigation
        ↓
Engineering Interpretation
```

---

# Limitations

This analysis has several important limitations.

## Small Sample

Only 15 days are represented.

This may not capture the complete range of station operation.

## Short Observation Period

Seasonal effects cannot be evaluated from this sample.

## Limited Variables

Only total daily station runtime is provided.

The dataset does not contain enough information to explain changes in runtime.

## Aggregated Data

Daily total runtime hides within-day operating behavior.

Two days with identical total runtime could have very different:

- Pump cycling
- Individual pump operation
- Peak wet-well levels
- Flow patterns

## Representativeness

The sample may not represent long-term station operation.

Descriptive statistics describe the supplied observations.

They do not automatically describe every future operating condition.

---

# Common Mistakes and Misinterpretations

## Mistake 1 - Treating Mean as the "Correct" Typical Value

The mean is one measure of central tendency.

For skewed datasets or datasets containing extreme observations, the median may describe the center differently.

Always consider the distribution.

---

## Mistake 2 - Removing Outliers Automatically

An unusual observation is not automatically an erroneous observation.

Investigate before excluding.

---

## Mistake 3 - Confusing Variance and Standard Deviation

Variance is expressed in squared units.

Standard deviation is expressed in the original units.

They describe related concepts but have different interpretations.

---

## Mistake 4 - Ignoring Sample vs. Population Definitions

Using:

```python
np.std(values)
```

and:

```python
pd.Series(values).std()
```

can produce different results.

NumPy defaults to population standard deviation.

Pandas defaults to sample standard deviation.

Neither library is broken.

They are answering slightly different mathematical questions because apparently one universal default would have made things too peaceful.

---

## Mistake 5 - Reporting Statistics Without Engineering Meaning

A statement such as:

> "Standard deviation = 1.19."

is incomplete.

A better statement is:

> "Observed daily station runtime had a sample standard deviation of approximately 1.19 hr/day."

Better still, discuss what that variability means relative to the system being evaluated.

---

## Mistake 6 - Excessive Precision

Reporting:

```text
Mean Runtime = 10.566666666666666 hr/day
```

does not make the analysis more accurate.

Presentation precision should reflect the measurement and engineering context.

---

# Reusable Python Component

Descriptive-statistics functionality may eventually belong under:

```text
src/applied_infrastructure_analytics/descriptive/
```

Potential modules include:

```text
central_tendency.py
dispersion.py
percentiles.py
```

For example:

```python
def calculate_range(values: np.ndarray) -> float:
    """Calculate the observed range of a numerical dataset."""
    if values.size == 0:
        raise ValueError("values must contain at least one observation")

    return float(np.max(values) - np.min(values))
```

Reusable functionality should be:

- Typed
- Tested
- General
- Independent of the PS-17 dataset

Do not create custom wrappers around every NumPy function merely to increase the number of files in the repository.

---

# Testing

Reusable functions should be validated using known values.

For example:

```python
import numpy as np
import pytest

from applied_infrastructure_analytics.descriptive.dispersion import (
    calculate_range,
)


def test_calculate_range_known_values() -> None:
    values = np.array([2.0, 4.0, 8.0])

    result = calculate_range(values)

    assert result == pytest.approx(6.0)
```

The purpose of testing is to validate reusable implementation.

It does not replace statistical validation or engineering interpretation.

---

# Knowledge Check

Answer these questions without running Python unless necessary.

1. Why can two datasets have the same mean but very different operating behavior?

2. Why is the median generally less sensitive to extreme observations than the mean?

3. Why does sample variance use squared deviations rather than ordinary deviations?

4. Why is standard deviation usually easier to interpret than variance in an engineering context?

5. If a box plot identifies an observation as an outlier, does that mean the observation should be removed? Why or why not?

6. What is the difference between range and interquartile range?

7. Why might the median and IQR be preferable to the mean and standard deviation for a strongly skewed dataset?

8. What additional information would you request before concluding that unusually high pump runtime indicates equipment deterioration?

---

# Explain It to an Engineer

A project manager asks:

> "If we already know the average pump runtime, why do we need all these other statistics?"

Explain the answer without equations.

Your explanation should address why two systems with the same average can exhibit very different operational behavior.

---

# Lesson Summary

After completing this lesson, you should understand:

- Mean
- Median
- Mode
- Minimum and maximum
- Range
- Variance
- Standard deviation
- Percentiles
- Quartiles
- Interquartile range
- Box plots
- Sample vs. population statistics
- Sensitivity to extreme observations

More importantly, you should understand that descriptive statistics answer **different questions about the same dataset**.

The central lesson is:

> **A useful statistical description requires both measures of where observations are centered and measures of how those observations vary.**

Neither should be interpreted without considering the engineering system that produced the data.

---

# Analytical Toolbox

This lesson adds the following tools to the analytical methods available for future exercises:

## Central Tendency

- Mean
- Median
- Mode

## Dispersion

- Range
- Variance
- Standard deviation
- Interquartile range

## Distribution Position

- Percentiles
- Quartiles

## Visualization

- Box plot

## Analytical Reasoning

- Comparing resistant and non-resistant statistics
- Investigating unusual observations
- Distinguishing statistical unusualness from data error
- Distinguishing observation from interpretation

These tools remain available throughout the remainder of the curriculum.

Future exercises may require their use without explicitly instructing you to calculate them.

---

# Transition to Applied Exercise

This lesson used:

- 15 controlled observations
- One primary variable
- Known units
- Guided calculations
- Manual verification
- Explicit statistical methods

The corresponding applied exercise will remove much of that structure.

In **Exercise 01a**, you will receive a substantially larger engineering dataset representing realistic infrastructure operations.

You will be responsible for:

- Understanding the supplied files
- Evaluating data quality
- Determining which variables matter
- Selecting appropriate descriptive statistics
- Investigating unusual observations
- Comparing operating conditions
- Developing an engineering interpretation

Unlike this lesson, the applied exercise will not tell you every statistic to calculate.

The objective will shift from:

> **Calculate these descriptive statistics.**

to:

> **Use descriptive statistics to investigate an engineering problem.**
# Dataset Documentation - Lesson 01: Descriptive Statistics

## Overview

This dataset contains one year of **synthetic daily municipal water-demand data** developed for Lesson 01 of the Applied Infrastructure Analytics project.

The dataset is intended to support hands-on exploration of descriptive statistics using a realistic civil and environmental engineering scenario.

It represents daily water demand for a hypothetical municipal water system over calendar year 2025.

The dataset is **synthetic**. It does not represent an actual utility, water treatment facility, municipality, or customer population.

---

## File

```text
lesson_01_daily_water_demand.csv
```

---

## Dataset Purpose

The dataset was created to support the following Lesson 01 concepts:

- Data inspection
- Data-quality review
- Mean
- Median
- Mode
- Minimum and maximum
- Range
- Variance
- Standard deviation
- Coefficient of variation
- Percentiles
- Quartiles
- Interquartile range
- Potential-outlier identification
- Box plots
- Engineering interpretation of statistical results

The objective is not merely to calculate statistics.

The dataset should be treated as though it were provided by a municipal utility for an initial engineering analysis.

The analyst should determine what the data reveals, identify observations that deserve further investigation, and distinguish statistical findings from engineering conclusions.

---

## Scenario

A municipal utility operates a water distribution system supplied by a water treatment facility.

The utility has provided one year of historical daily water-demand records as part of an initial evaluation of system demand and potential future capital improvements.

Before performing forecasting, capacity analysis, or probabilistic modeling, the engineering team wants to understand the characteristics of the historical demand record.

The primary question for this lesson is:

> **What does the historical dataset tell us about the magnitude, variability, and distribution of daily water demand?**

The dataset alone is not sufficient to determine whether the water system has adequate capacity.

---

## Data Dictionary

| Column | Data Type | Units | Description |
|---|---|---|---|
| `date` | Date | YYYY-MM-DD | Calendar date associated with the daily demand observation |
| `daily_water_demand_mgd` | Float | MGD | Total daily municipal water demand expressed in million gallons per day |

---

## Units

Water demand is reported in:

```text
MGD = million gallons per day
```

For example:

```text
8.25 MGD
```

represents an average daily flow rate equivalent to 8.25 million gallons delivered during that day.

---

## Time Period

The dataset covers:

```text
January 1, 2025 through December 31, 2025
```

with one observation per calendar day.

Expected number of observations:

```text
365
```

Students should verify the number and completeness of observations during their initial data-quality review rather than assuming the dataset is complete merely because this documentation says it should be. Documentation, like humans, occasionally lies.

---

## Nature of the Dataset

The dataset is designed to resemble municipal water-demand behavior rather than a collection of completely independent random values.

Several components influence the synthetic demand record.

### Baseline Demand

The system has an underlying typical daily demand around which individual observations vary.

This represents the general water-use requirements of the hypothetical service area.

### Seasonal Variation

Municipal water demand commonly changes throughout the year.

Potential causes include:

- Irrigation
- Temperature
- Rainfall
- Seasonal population changes
- Outdoor water use
- Commercial activity

The synthetic dataset contains a seasonal component intended to produce higher and lower demand periods during the year.

Students should determine whether this pattern is visible from the data rather than assuming its magnitude or importance.

### Short-Term Variation

Daily demand fluctuates even when the overall seasonal condition remains similar.

Potential real-world causes could include:

- Weather
- Day of week
- Irrigation behavior
- Commercial activity
- Operational conditions
- Random variation in customer usage

The dataset includes day-to-day variability to represent this behavior.

### Unusual Observations

The dataset contains a small number of observations that may appear unusual relative to the majority of the record.

These observations are intentionally included to support investigation of:

- Extreme values
- IQR-based outlier detection
- Sensitivity of the mean
- Sensitivity of standard deviation
- Engineering treatment of unusual observations

Students should **not automatically remove unusual observations**.

A statistically unusual observation is not necessarily erroneous.

In a real utility dataset, an unusual value could represent:

- A legitimate high-demand event
- Fire flow
- Extreme weather
- Major irrigation demand
- A large industrial or commercial demand
- Operational changes
- Metering problems
- Sensor problems
- Data-entry errors

Statistical analysis can identify an observation that deserves attention.

Engineering investigation determines what that observation actually means.

---

## Synthetic Data Disclaimer

This dataset was generated specifically for educational use.

It should not be interpreted as representing the statistical characteristics of any particular municipal water system.

The dataset is useful for learning analytical techniques because its behavior resembles patterns that may occur in engineering datasets.

However, conclusions drawn from this dataset should **not** be generalized into design criteria.

For example, the dataset should not be used to conclude that:

- A particular coefficient of variation is typical for all utilities.
- A particular peak-to-average demand ratio should be used for design.
- A specific percentile represents an appropriate design demand.
- Values identified by the IQR method should automatically be discarded.
- One year of demand data is sufficient for infrastructure planning.

Those questions require project-specific data, standards, operational information, and engineering judgment.

---

## Sample vs. Population

An important statistical question in this lesson is whether the dataset represents a **sample** or a **population**.

The answer depends on the engineering question.

If the question is:

> What was daily water demand during calendar year 2025?

and all 365 daily observations are available, the dataset can be considered the complete population for that narrowly defined period.

If the question is:

> What range of water demand might this system experience over its future operating life?

the same 365 observations should be viewed as a sample from a much larger underlying demand process.

This distinction becomes important when calculating and interpreting quantities such as variance and standard deviation.

---

## Expected Data-Quality Review

Before performing descriptive statistics, inspect the dataset.

At minimum, verify:

- Number of observations
- Column names
- Data types
- Date range
- Missing values
- Duplicate dates
- Negative demand values
- Physically suspicious values
- Unit consistency

Do not assume that a dataset is valid simply because it successfully loads into Pandas.

A successful `pd.read_csv()` call proves remarkably little about whether the data makes engineering sense.

---

## Suggested Initial Inspection

Typical Python operations may include:

```python
import pandas as pd

df = pd.read_csv("lesson_01_daily_water_demand.csv")

df.head()
df.tail()
df.info()
df.describe()
```

However, avoid relying entirely on `DataFrame.describe()`.

The purpose of the lesson is to understand what each statistic means and how it should be interpreted, not merely to ask Pandas to produce a table and admire its efficiency.

---

## Important Analytical Considerations

### Mean Does Not Equal Design Demand

The arithmetic mean describes the center of the observed data.

It does not automatically represent an appropriate infrastructure design condition.

A water system must often accommodate conditions substantially above average demand.

### Maximum Does Not Automatically Equal Design Demand

The maximum observation is also not automatically the correct design condition.

A maximum may represent:

- A legitimate system peak
- An unusual operational condition
- An error
- A rare event
- A condition that should be considered through separate design criteria

Engineering context is required.

### Outlier Does Not Mean Error

The IQR method provides a statistical rule for identifying unusual observations.

It does not determine whether those observations are invalid.

Deleting observations simply because they make a dataset inconvenient can remove exactly the events that matter most to infrastructure risk.

### Variability Matters

Two systems can have the same average demand while experiencing very different operating conditions.

For this reason, Lesson 01 emphasizes measures such as:

- Standard deviation
- IQR
- Range
- Coefficient of variation
- Percentiles

in addition to the mean.

---

## Relationship to Lesson 00

Lesson 00 introduced:

- Histograms
- Probability Density Functions
- Cumulative Distribution Functions
- Empirical exceedance probability

Lesson 01 approaches data from another direction.

Instead of initially asking:

> **How is probability distributed?**

the lesson asks:

> **How can a dataset be summarized numerically?**

The two approaches complement each other.

A histogram may reveal distribution shape that is hidden by summary statistics.

A descriptive-statistics table may quantify characteristics that are difficult to estimate visually.

Good exploratory analysis generally uses both.

---

## Future Use

This dataset is primarily intended for Lesson 01.

Later lessons may revisit the dataset when studying topics such as:

- Probability distributions
- Confidence intervals
- Hypothesis testing
- Regression
- Time-series analysis
- Monte Carlo simulation

When reused in later lessons, additional assumptions or modifications may be introduced as appropriate.

---

## Reproducibility

Because the dataset is synthetic, it should be treated as a fixed educational artifact once committed to the repository.

Regenerating the dataset with different random values would change:

- Descriptive statistics
- Percentiles
- Outlier identification
- Visualizations
- Expected test results
- Student conclusions

For reproducible analysis, the committed CSV should therefore serve as the canonical Lesson 01 dataset.

---

## Intended Use

This dataset is intended for:

- Education
- Statistical practice
- Python development
- Engineering analytics demonstrations
- Unit-testing exercises
- Portfolio demonstration

It is not intended for:

- Actual infrastructure design
- Regulatory analysis
- Utility planning
- Hydraulic model calibration
- Water-demand forecasting for a real system
- Establishing engineering design criteria

---

## Source

The dataset was synthetically generated for the **Applied Infrastructure Analytics** learning project.

No real customer, utility, municipality, or infrastructure system data is included.

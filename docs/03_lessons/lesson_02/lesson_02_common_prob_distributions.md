# Lesson 02 - Common Probability Distributions

## Purpose

Engineering systems operate under uncertainty.

Rainfall varies from storm to storm. Water demand changes throughout the day. Pump failures occur unpredictably. Construction costs vary between projects. Equipment lifetimes differ even among nominally identical assets.

Lessons 00 and 01 introduced methods for **describing observed data**:

- Histograms
- Probability density
- Cumulative distributions
- Mean and median
- Variance and standard deviation
- Percentiles and quartiles

Those methods tell us what happened in the observations we collected.

This lesson introduces the next step:

> **Using theoretical probability distributions to represent uncertain quantities beyond the observations themselves.**

A probability distribution is a mathematical model describing the possible values of a random variable and how probability is distributed among those values.

The objective is not to memorize a catalog of distributions.

The objective is to understand:

1. what type of process a distribution represents,
2. what assumptions it makes,
3. when those assumptions are reasonable,
4. and when the distribution should **not** be used.

---

# Engineering Motivation

Suppose a utility has recorded the number of water-main failures occurring each month for several years.

The historical record tells us what happened during those months.

But engineers often need to answer questions about conditions that have **not yet occurred**:

- What is the probability of zero failures next month?
- What is the probability of three or more failures?
- How unusual would five failures in one month be?
- How many failures should the utility expect during a typical month?

The empirical data alone provide some information.

A probability model can provide a mathematical representation of the underlying uncertainty.

But selecting a distribution merely because software can fit it is not sufficient.

The physical process matters.

---

# Learning Objectives

After completing this lesson, you should be able to:

- Explain the difference between empirical and theoretical distributions.
- Define a random variable.
- Distinguish discrete and continuous random variables.
- Explain the role of distribution parameters.
- Understand the Bernoulli distribution.
- Understand the binomial distribution.
- Understand the Poisson distribution.
- Understand the normal distribution.
- Understand the lognormal distribution.
- Understand the exponential distribution.
- Calculate probabilities using probability distributions.
- Use SciPy to evaluate probability distributions.
- Compare theoretical distributions with observed engineering data.
- Evaluate whether a distribution is physically reasonable for a particular variable.
- Recognize important assumptions and limitations of common distributions.

---

# Prerequisites

Before beginning this lesson, you should be familiar with:

- Histograms
- Probability density
- Cumulative distribution functions
- Exceedance probability
- Mean
- Variance
- Standard deviation
- Basic Python
- NumPy
- Pandas
- Matplotlib

These concepts were introduced in Lessons 00 and 01.

---

# Engineering Scenario

## Background

A municipal water utility maintains a distribution system containing several hundred miles of water main.

Operations staff maintain records of reported water-main failures.

For this lesson, the engineering team is examining the **monthly number of water-main failures** over a three-year period.

The objective is to determine whether a probability model can reasonably describe the observed monthly failure counts.

---

# Engineering Question

The primary question is:

> **Can the historical monthly failure record be represented by a probability distribution that allows us to estimate the likelihood of future failure counts?**

Before answering that question, we need to understand what probability distributions actually represent.

---

# Dataset

The instructional dataset contains 36 monthly water-main failure counts.

| Month | Failures |
| ---: | ---: |
| 1 | 2 |
| 2 | 1 |
| 3 | 3 |
| 4 | 2 |
| 5 | 0 |
| 6 | 2 |
| 7 | 4 |
| 8 | 1 |
| 9 | 2 |
| 10 | 3 |
| 11 | 1 |
| 12 | 2 |
| 13 | 2 |
| 14 | 3 |
| 15 | 1 |
| 16 | 2 |
| 17 | 4 |
| 18 | 2 |
| 19 | 1 |
| 20 | 3 |
| 21 | 2 |
| 22 | 2 |
| 23 | 0 |
| 24 | 1 |
| 25 | 3 |
| 26 | 2 |
| 27 | 1 |
| 28 | 4 |
| 29 | 2 |
| 30 | 3 |
| 31 | 2 |
| 32 | 1 |
| 33 | 5 |
| 34 | 2 |
| 35 | 3 |
| 36 | 1 |

The dataset is intentionally small so that calculations can be inspected and verified.

The applied exercise following this lesson will use a substantially larger infrastructure dataset.

---

# Concept 1 - Random Variables

A **random variable** represents a numerical outcome whose value is uncertain before it is observed.

Examples include:

- Number of water-main failures next month
- Peak flow during next year's largest storm
- Time until a pump fails
- Daily water demand
- Construction bid price
- Whether a valve fails during operation

Random variables are generally classified as:

- Discrete
- Continuous

---

# Discrete Random Variables

A discrete random variable takes distinct, countable values.

For example, monthly water-main failures could be:

```text
0
1
2
3
4
5
...
```

You cannot observe:

```text
2.37 water-main failures
```

Failure **counts** are therefore discrete.

---

# Continuous Random Variables

A continuous random variable can take any value within a range.

Examples include:

- Flow
- Pressure
- Temperature
- Runtime
- Rainfall depth
- Groundwater elevation
- Equipment lifetime

A measured flow might be:

```text
423.7 gpm
```

or:

```text
423.71 gpm
```

or any other value permitted by the physical system and measurement precision.

---

# Why the Distinction Matters

Different probability distributions describe different types of random variables.

| Variable | Type | Potential Distribution |
| --- | --- | --- |
| Pump starts during one hour | Discrete | Poisson |
| Component succeeds or fails | Discrete | Bernoulli |
| Number of failures among 20 components | Discrete | Binomial |
| Measurement error | Continuous | Normal |
| Positive skewed repair duration | Continuous | Lognormal |
| Time between independent events | Continuous | Exponential |

This does **not** mean the listed distribution is automatically correct.

It means the distribution might be worth considering based on the type of process involved.

---

# Empirical vs. Theoretical Distributions

Lesson 00 introduced the empirical CDF.

An empirical distribution is derived directly from observed data.

If 36 months have been observed, the empirical distribution describes those 36 observations.

A theoretical distribution instead defines probability mathematically.

This distinction is important.

## Empirical

```text
What did we observe?
```

## Theoretical

```text
What probability model might reasonably represent the process?
```

Theoretical distributions allow probability estimates between and beyond specific historical observations.

That additional capability comes with additional assumptions.

---

# Distribution Parameters

Probability distributions are controlled by **parameters**.

Parameters determine characteristics such as:

- center,
- spread,
- event rate,
- shape.

For example, a normal distribution is commonly described using:

$$
\mu
$$

and:

$$
\sigma
$$

where:

- $\mu$ = population mean
- $\sigma$ = population standard deviation

A Poisson distribution uses:

$$
\lambda
$$

where $\lambda$ represents the expected number of events within a specified interval.

Understanding the parameters is more useful than memorizing formulas without context.

---

# Concept 2 - Bernoulli Distribution

The Bernoulli distribution represents an experiment with exactly two possible outcomes.

Examples include:

```text
Pump starts successfully / Pump does not start
Valve operates / Valve fails to operate
Pipe fails / Pipe does not fail
Inspection passes / Inspection fails
```

The outcomes are commonly represented numerically as:

$$
X =
\begin{cases}
1 & \text{success} \\
0 & \text{failure}
\end{cases}
$$

If the probability of success is:

$$
p
$$

then the probability of failure is:

$$
1-p
$$

---

# Engineering Example

Suppose historical testing indicates that an emergency generator successfully starts during:

$$
p=0.98
$$

of tests.

Then:

$$
P(X=1)=0.98
$$

and:

$$
P(X=0)=0.02
$$

The Bernoulli distribution represents **one trial**.

This distinction becomes important when we consider multiple trials.

---

# Concept 3 - Binomial Distribution

The binomial distribution extends the Bernoulli process to multiple trials.

Suppose a utility operates 20 identical remote telemetry units.

Assume each unit has a:

$$
p=0.05
$$

probability of communication failure during a particular test period.

We might ask:

> What is the probability that exactly two units fail?

The binomial distribution can model the number of failures among a fixed number of trials.

---

# Mathematical Foundation

For:

$$
X \sim Binomial(n,p)
$$

the probability of exactly $k$ successes is:

$$
P(X=k)
=
\binom{n}{k}
p^k
(1-p)^{n-k}
$$

where:

- $n$ = number of trials
- $k$ = number of successes
- $p$ = probability of success on each trial

The combinatorial term is:

$$
\binom{n}{k}
=
\frac{n!}{k!(n-k)!}
$$

---

# Important Binomial Assumptions

A standard binomial model assumes:

1. A fixed number of trials
2. Two possible outcomes per trial
3. Constant probability $p$
4. Independent trials

Those assumptions matter.

If one equipment failure changes the probability that another component fails, independence may not be reasonable.

---

# Concept 4 - Poisson Distribution

The Poisson distribution is commonly used to model the **number of events occurring during a specified interval**.

Examples may include:

- Water-main failures per month
- Pump alarms per week
- Service interruptions per year
- Sewer blockages per month
- Equipment faults per operating period

The random variable is a count:

$$
X=0,1,2,3,\ldots
$$

---

# Poisson Parameter

The Poisson distribution has one primary parameter:

$$
\lambda
$$

which represents the expected number of events during the specified interval.

If a system averages:

$$
2.1
$$

water-main failures per month, then:

$$
\lambda=2.1
$$

for a monthly model.

The time interval is part of the meaning of $\lambda$.

A rate of 2.1 failures **per month** is not the same model as 2.1 failures **per year**.

---

# Poisson Probability Mass Function

For:

$$
X \sim Poisson(\lambda)
$$

the probability of exactly $k$ events is:

$$
P(X=k)
=
\frac{
e^{-\lambda}\lambda^k
}{
k!
}
$$

---

# Worked Example - Water-Main Failures

Using the lesson dataset, calculate the observed mean monthly number of failures.

The total number of failures is:

$$
75
$$

over:

$$
36
$$

months.

Therefore:

$$
\bar{x}
=
\frac{75}{36}
$$

$$
\bar{x}
\approx
2.083
$$

As an initial Poisson model, we can estimate:

$$
\lambda
\approx
2.083
$$

failures per month.

---

# Probability of Zero Failures

For:

$$
k=0
$$

the Poisson equation becomes:

$$
P(X=0)
=
\frac{
e^{-2.083}(2.083)^0
}{
0!
}
$$

Because:

$$
(2.083)^0=1
$$

and:

$$
0!=1
$$

we obtain approximately:

$$
P(X=0)
\approx0.125
$$

So the model estimates roughly a:

$$
\boxed{12.5\%}
$$

probability of experiencing zero water-main failures during a month.

---

# Probability of Multiple Outcomes

Suppose we want:

> What is the probability of three or more failures during a month?

This is:

$$
P(X \ge 3)
$$

Rather than calculating:

$$
P(3)+P(4)+P(5)+\cdots
$$

it is easier to use the complement:

$$
P(X \ge 3)
=
1-P(X\le2)
$$

This connects directly to the CDF concepts introduced in Lesson 00.

---

# Python Implementation

SciPy provides probability distributions through:

```python
from scipy import stats
```

For the Poisson model:

```python
from scipy import stats


lambda_monthly = 75 / 36

probability_zero = stats.poisson.pmf(
    k=0,
    mu=lambda_monthly,
)
```

The probability of three or more failures can be calculated using:

```python
probability_three_or_more = stats.poisson.sf(
    k=2,
    mu=lambda_monthly,
)
```

Here:

```text
pmf
```

means **probability mass function**, while:

```text
sf
```

means **survival function**.

For a discrete random variable:

$$
P(X>k)
=
1-P(X\le k)
$$

The survival function calculates this exceedance probability directly.

---

# PMF vs. PDF

This distinction is important.

## Discrete Variables

Discrete distributions use a:

**Probability Mass Function (PMF)**

The probability at a specific value can be greater than zero.

For example:

$$
P(X=2)
$$

can represent the probability of exactly two failures.

## Continuous Variables

Continuous distributions use a:

**Probability Density Function (PDF)**

For a truly continuous random variable:

$$
P(X=x)=0
$$

Probability is associated with an **interval**, not one exact point.

This distinction was intentionally simplified in Lesson 00. We can now make it more precise.

---

# Concept 5 - Normal Distribution

The normal distribution is one of the most widely used continuous probability distributions.

It has the familiar bell-shaped form.

It is defined by:

- Mean $\mu$
- Standard deviation $\sigma$

and is written:

$$
X \sim N(\mu,\sigma^2)
$$

---

# Characteristics of the Normal Distribution

A normal distribution is:

- Continuous
- Symmetric
- Centered at the mean
- Completely defined by $\mu$ and $\sigma$

For a normal distribution:

$$
Mean = Median = Mode
$$

The standard deviation controls how widely observations are dispersed.

---

# Engineering Applications

Normal distributions may be reasonable for variables such as:

- Measurement error
- Manufacturing dimensional variation
- Some laboratory measurements
- Aggregated process variability

But the normal distribution is **not** automatically appropriate simply because it is familiar.

---

# Physical Reasonableness

Suppose average daily water demand is modeled as:

$$
X \sim N(4.0,1.5^2)
$$

A normal distribution technically permits:

$$
X<0
$$

That would imply negative water demand.

If the probability of negative values is negligible, the approximation might still be acceptable.

If substantial probability lies in physically impossible regions, the model is questionable.

This illustrates a recurring principle:

> **Statistical fit is not the only criterion for selecting a distribution. Physical plausibility matters.**

---

# Standardization and the Z-Score

For a normally distributed variable, an observation can be standardized using:

$$
z
=
\frac{x-\mu}{\sigma}
$$

The z-score represents how many standard deviations an observation lies from the mean.

Suppose:

$$
\mu=100
$$

and:

$$
\sigma=10
$$

For:

$$
x=120
$$

then:

$$
z
=
\frac{120-100}{10}
=
2
$$

The observation lies two standard deviations above the mean.

---

# Python Normal Distribution

Suppose pump discharge pressure is modeled with:

$$
\mu=52 \text{ psi}
$$

and:

$$
\sigma=3.5 \text{ psi}
$$

The probability that pressure is below 48 psi can be calculated with:

```python
probability = stats.norm.cdf(
    x=48,
    loc=52,
    scale=3.5,
)
```

The probability that pressure exceeds 60 psi can be calculated using:

```python
probability = stats.norm.sf(
    x=60,
    loc=52,
    scale=3.5,
)
```

---

# Concept 6 - Lognormal Distribution

Many engineering variables cannot be negative and exhibit **right-skewed distributions**.

Examples may include:

- Repair duration
- Some construction costs
- Some contaminant concentrations
- Certain equipment lifetimes
- Some hydraulic or environmental measurements

For these variables, the lognormal distribution may be worth considering.

A variable is lognormally distributed when its logarithm is normally distributed.

---

# Shape of the Lognormal Distribution

Unlike the normal distribution, the lognormal distribution is:

- Positive
- Right-skewed
- Bounded below by zero
- Capable of representing occasional large values

This can make it useful when the physical variable cannot be negative and extreme high values occur occasionally.

---

# Engineering Example

Consider repair durations:

```text
1.8 hr
2.1 hr
2.4 hr
2.7 hr
3.0 hr
3.3 hr
4.1 hr
6.8 hr
11.5 hr
```

The distribution is not symmetric.

Most repairs are relatively short, while a few require substantially more time.

A normal distribution may not represent this pattern well.

A lognormal distribution may be more plausible.

That conclusion should still be evaluated rather than assumed.

---

# Concept 7 - Exponential Distribution

The exponential distribution is often used to model **time between independent events occurring at a constant average rate**.

Potential applications include:

- Time between equipment failures
- Time between alarms
- Time between service interruptions
- Time between arrivals

If events follow a Poisson process, the time between those events follows an exponential distribution.

This creates an important relationship:

```text
Poisson
Number of events during an interval
             ↕

Exponential
Time between events
```

---

# Exponential Parameter

If events occur at average rate:

$$
\lambda
$$

then the exponential distribution has mean:

$$
E[T]
=
\frac{1}{\lambda}
$$

Suppose a component experiences an average of:

$$
0.25
$$

failures per year.

Then the mean time between failures under this model is:

$$
\frac{1}{0.25}
=
4 \text{ years}
$$

---

# Exponential CDF

The cumulative probability that an event occurs by time $t$ is:

$$
P(T\le t)
=
1-e^{-\lambda t}
$$

The probability that the component survives beyond time $t$ is:

$$
P(T>t)
=
e^{-\lambda t}
$$

This concept will become particularly important during the reliability engineering lessons.

---

# The Memoryless Property

The exponential distribution has an unusual property called **memorylessness**.

Under the model, the probability of surviving an additional period does not depend on how long the component has already survived.

In practical terms, the model assumes that an old component has the same instantaneous failure behavior as a new component.

For many physical assets, this is unrealistic.

Pipes corrode.

Bearings wear.

Pumps deteriorate.

Concrete degrades.

Therefore, the exponential distribution may be useful for some failure processes but inappropriate for strongly age-dependent deterioration.

Later reliability lessons will introduce distributions better suited to changing failure rates.

---

# Comparing Common Distributions

| Distribution | Type | Represents | Key Parameters |
| --- | --- | --- | --- |
| Bernoulli | Discrete | One binary outcome | $p$ |
| Binomial | Discrete | Number of successes in fixed trials | $n,p$ |
| Poisson | Discrete | Event counts over an interval | $\lambda$ |
| Normal | Continuous | Symmetric variability | $\mu,\sigma$ |
| Lognormal | Continuous | Positive right-skewed quantities | Log-space parameters |
| Exponential | Continuous | Time between constant-rate events | $\lambda$ |

The table is a starting point.

It is not a distribution-selection algorithm.

---

# Choosing a Candidate Distribution

Before selecting a probability distribution, ask questions about the physical variable.

## Question 1 - Is the Variable Discrete or Continuous?

Failure count:

```text
Discrete
```

Pressure:

```text
Continuous
```

---

## Question 2 - What Values Are Physically Possible?

Can the variable be negative?

Is it bounded?

Can it take arbitrarily large values?

---

## Question 3 - What Does the Distribution Look Like?

Is it:

- symmetric,
- right-skewed,
- left-skewed,
- multimodal,
- concentrated,
- highly dispersed?

---

## Question 4 - What Physical Process Generates the Data?

Is the variable:

- a count,
- a binary outcome,
- a waiting time,
- an accumulated measurement,
- a physical dimension,
- a failure process?

---

## Question 5 - Are the Distribution Assumptions Reasonable?

For example, a Poisson process commonly assumes a constant event rate and independent events.

Water-main failures may violate these assumptions if:

- seasonal conditions affect failure rates,
- pipe age varies,
- material varies,
- pressure varies,
- one failure affects surrounding infrastructure.

A Poisson model might still provide a useful approximation.

But its limitations should be understood.

---

# Fitting Is Not Validation

Software can fit a probability distribution to almost any numerical dataset.

For example:

```python
params = stats.norm.fit(values)
```

The existence of fitted parameters does **not** demonstrate that the normal distribution is appropriate.

A responsible workflow is closer to:

```text
Understand the variable
        ↓
Understand the physical process
        ↓
Inspect the observed distribution
        ↓
Select plausible candidate models
        ↓
Estimate parameters
        ↓
Compare model with observations
        ↓
Evaluate assumptions
        ↓
Interpret engineering usefulness
```

The `.fit()` function handles precisely one of those steps.

---

# Comparing Observed and Theoretical Distributions

Return to the water-main failure dataset.

Create the observations:

```python
import numpy as np


failures = np.array(
    [
        2, 1, 3, 2, 0, 2, 4, 1, 2, 3, 1, 2,
        2, 3, 1, 2, 4, 2, 1, 3, 2, 2, 0, 1,
        3, 2, 1, 4, 2, 3, 2, 1, 5, 2, 3, 1,
    ],
    dtype=int,
)
```

Estimate:

```python
lambda_monthly = failures.mean()
```

Then calculate theoretical Poisson probabilities:

```python
from scipy import stats


failure_counts = np.arange(
    failures.min(),
    failures.max() + 1,
)

poisson_probabilities = stats.poisson.pmf(
    failure_counts,
    mu=lambda_monthly,
)
```

Compare those probabilities with the observed relative frequencies.

The purpose is not merely to produce two sets of numbers.

Ask:

> **Does the theoretical model resemble the observed behavior sufficiently for the intended engineering use?**

---

# Mean and Variance as Diagnostic Clues

For a Poisson distribution:

$$
E[X]=\lambda
$$

and:

$$
Var(X)=\lambda
$$

Therefore, the theoretical mean and variance are equal.

This provides a useful diagnostic clue.

Calculate:

```python
sample_mean = failures.mean()

sample_variance = failures.var(ddof=1)
```

Compare the two.

If the variance is dramatically larger than the mean, the data may exhibit **overdispersion** relative to a simple Poisson model.

If the variance is substantially smaller, the data may exhibit **underdispersion**.

Neither automatically proves that the Poisson model is unusable.

It tells you that the assumptions deserve further investigation.

---

# CDF and Exceedance Probability

Theoretical distributions connect directly to Lesson 00.

Suppose:

$$
X \sim Poisson(2.083)
$$

and we want:

$$
P(X\le3)
$$

Use:

```python
stats.poisson.cdf(
    k=3,
    mu=lambda_monthly,
)
```

For:

$$
P(X>3)
$$

use:

```python
stats.poisson.sf(
    k=3,
    mu=lambda_monthly,
)
```

The same conceptual framework applies to continuous distributions.

The difference is that the probability now comes from a mathematical model rather than solely from the empirical observations.

---

# Empirical Probability vs. Model Probability

Suppose the historical dataset contains several months with three or more failures.

An empirical estimate would be based directly on:

$$
\frac{\text{Months meeting condition}}
{\text{Total observed months}}
$$

A theoretical estimate would use the fitted distribution.

These values will not necessarily be identical.

That is expected.

The empirical probability represents:

> What fraction of the observed record satisfied the condition?

The theoretical probability represents:

> What probability does the assumed model assign to the condition?

That distinction becomes increasingly important as the curriculum progresses.

---

# Visualization

Visual comparison is one useful way to evaluate a candidate distribution.

For the water-main failure counts, compare:

- observed relative frequencies,
- theoretical Poisson probabilities.

For continuous variables, useful comparisons may include:

- histogram vs. theoretical PDF,
- empirical CDF vs. theoretical CDF.

Visualization does not replace formal statistical testing.

But it often reveals obvious model problems before more sophisticated methods are attempted.

---

# Engineering Interpretation

Suppose a Poisson model appears reasonably consistent with the observed monthly failure counts.

The model could then support questions such as:

- probability of zero failures,
- probability of one failure,
- probability of three or more failures,
- expected monthly failures,
- probability of unusually high failure counts.

That does **not** establish that:

- failure rates will remain constant,
- all pipes have equal failure probability,
- failures are independent,
- seasonal effects do not exist,
- deterioration is absent.

The model is an abstraction.

The engineering question is whether the abstraction is useful enough for the decision being made.

---

# Observation vs. Interpretation

## Observation

The historical dataset contains an average of approximately 2.08 failures per month.

## Model

A Poisson distribution with:

$$
\lambda=2.083
$$

can be constructed.

## Interpretation

The model may provide a useful first approximation of monthly failure-count uncertainty.

## Assumption

The process is being treated approximately as a constant-rate event process.

## Limitation

Actual water-main failures may depend on:

- pipe age,
- material,
- diameter,
- soil conditions,
- pressure,
- temperature,
- previous failures,
- construction history,
- seasonal effects.

Keeping these categories separate prevents a mathematical model from quietly becoming a physical claim.

---

# Common Mistakes and Misinterpretations

## Mistake 1 - Choosing a Distribution by Appearance Alone

A bell-shaped histogram does not prove normality.

A right-skewed histogram does not prove lognormality.

Distribution selection should consider both data and physical process.

---

## Mistake 2 - Using Continuous Distributions for Counts Without Thought

Counts such as:

```text
0, 1, 2, 3
```

are naturally discrete.

A distribution allowing:

```text
2.6 failures
```

may not represent the process appropriately.

---

## Mistake 3 - Ignoring Impossible Values

A model that assigns substantial probability to physically impossible conditions should be questioned.

---

## Mistake 4 - Confusing PDF Height with Probability

For continuous distributions, PDF height is **density**, not probability at an exact point.

Probability comes from area over an interval.

---

## Mistake 5 - Treating a Good Fit as Proof

A distribution can resemble historical observations while having assumptions that are physically unreasonable.

---

## Mistake 6 - Ignoring the Time Interval

A Poisson rate must have context.

```text
2 failures/month
```

and:

```text
2 failures/year
```

are radically different models.

---

## Mistake 7 - Assuming Independence

Infrastructure events often share common causes.

A freeze event may produce many pipe failures.

A major storm may produce multiple alarms.

A power outage may affect several facilities.

Events occurring within the same system are not automatically independent.

---

# Python Implementation

Useful SciPy methods include:

```python
stats.poisson.pmf()
stats.poisson.cdf()
stats.poisson.sf()

stats.binom.pmf()
stats.binom.cdf()
stats.binom.sf()

stats.norm.pdf()
stats.norm.cdf()
stats.norm.sf()

stats.lognorm.pdf()
stats.lognorm.cdf()
stats.lognorm.sf()

stats.expon.pdf()
stats.expon.cdf()
stats.expon.sf()
```

The naming pattern is intentionally consistent.

### PMF

```text
Probability at a discrete value
```

### PDF

```text
Density for a continuous value
```

### CDF

```text
P(X ≤ x)
```

### SF

```text
P(X > x)
```

The survival function is particularly useful for engineering exceedance and reliability calculations.

---

# Validation

Do not rely exclusively on library output.

For at least one discrete probability calculation:

1. Calculate the probability manually.
2. Calculate it using SciPy.
3. Compare the results.

For example:

$$
P(X=0)
$$

for a Poisson model can be calculated directly using:

$$
P(X=0)
=
e^{-\lambda}
$$

and compared with:

```python
stats.poisson.pmf(
    k=0,
    mu=lambda_monthly,
)
```

The results should agree within floating-point precision.

---

# Reusable Python Components

Probability functionality may eventually belong under:

```text
src/applied_infrastructure_analytics/probability/
```

Potential functionality might include:

```text
distributions.py
```

However, avoid creating wrappers that merely rename SciPy functions.

A function such as:

```python
def poisson_probability(k: int, rate: float) -> float:
    return stats.poisson.pmf(k, rate)
```

adds little value.

Reusable project code should provide meaningful domain-independent functionality, validation, or analysis that is not already cleanly handled by the underlying library.

---

# Knowledge Check

Answer the following without using Python unless necessary.

1. What is the difference between a discrete and continuous random variable?

2. Why is monthly water-main failure count discrete?

3. What is the difference between an empirical distribution and a theoretical distribution?

4. What does $\lambda$ represent in a Poisson distribution?

5. What is the difference between a PMF and a PDF?

6. Why might the normal distribution be inappropriate for some engineering variables?

7. Why might a lognormal distribution be more reasonable for a positive, strongly right-skewed variable?

8. What is the relationship between the Poisson and exponential distributions?

9. What does the memoryless property of the exponential distribution imply?

10. Why might memorylessness be inappropriate for deteriorating infrastructure?

11. Why does fitting a distribution not prove that the distribution is appropriate?

12. Why should physical constraints be considered when selecting a probability distribution?

---

# Explain It to an Engineer

A project manager asks:

> "Why don't we just use a normal distribution for everything? We already know how to calculate the mean and standard deviation."

Explain why different engineering processes require different probability models.

Your explanation should not rely primarily on equations.

---

# Lesson Summary

After completing this lesson, you should understand the fundamental characteristics of:

- Bernoulli distributions
- Binomial distributions
- Poisson distributions
- Normal distributions
- Lognormal distributions
- Exponential distributions

More importantly, you should understand that probability distributions are **models of uncertain processes**.

They are not merely mathematical curves fitted to data.

The central lesson is:

> **Choose a probability distribution because its behavior and assumptions reasonably represent the engineering process, not simply because software can fit it.**

---

# Analytical Toolbox

This lesson adds the following tools to the analytical methods available for future exercises.

## Discrete Probability Models

- Bernoulli distribution
- Binomial distribution
- Poisson distribution

## Continuous Probability Models

- Normal distribution
- Lognormal distribution
- Exponential distribution

## Probability Calculations

- PMF
- PDF
- CDF
- Survival function
- Exceedance probability

## Model Evaluation

- Empirical vs. theoretical distributions
- Parameter estimation
- Mean-variance comparison
- Physical plausibility
- Distribution assumptions

## Analytical Reasoning

- Discrete vs. continuous variables
- Model vs. observation
- Statistical fit vs. physical reasonableness
- Assumption identification
- Model limitations

These methods remain available throughout the remainder of the curriculum.

---

# Transition to Applied Exercise

This lesson used:

- 36 controlled monthly observations,
- one primary failure-count variable,
- a known observation interval,
- guided distribution selection,
- and manually verifiable calculations.

**Exercise 02a** will remove much of that structure.

You will receive a realistic infrastructure dataset containing multiple variables representing different types of uncertainty.

You will need to determine:

- which variables are worth modeling,
- whether they are discrete or continuous,
- which candidate distributions are physically reasonable,
- how distribution parameters should be estimated,
- how theoretical models compare with empirical observations,
- and whether the resulting models are useful for engineering decisions.

The exercise will not tell you:

> "Fit a Poisson distribution to Column A and a normal distribution to Column B."

Instead, the problem will ask you to investigate uncertainty in the engineering system.

You will decide which probability models, if any, are appropriate.

That distinction is the point.
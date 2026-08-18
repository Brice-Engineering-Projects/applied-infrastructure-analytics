# Lesson XX - [Lesson Title]

## Purpose

[Explain why this analytical concept matters in infrastructure engineering.]

[Describe the types of engineering questions this method can help answer.]

Keep the purpose focused on the engineering need rather than beginning with mathematical definitions.

The student should understand:

> **Why do I need to know this?**

before learning how the method works.

---

# Engineering Motivation

[Introduce a practical infrastructure problem that creates a need for the analytical method.]

Examples may involve:

* Hydrology
* Water distribution
* Wastewater collection
* Groundwater
* Infrastructure reliability
* Asset management
* Construction costs
* Infrastructure operations

The engineering problem should naturally lead to the statistical concept.

For example:

> A municipal utility has several years of daily water-production records. Before evaluating future capacity requirements, the engineering team wants to understand typical demand, variability, and unusually high-demand conditions.

Then establish the analytical need:

> Before evaluating capacity, the engineer needs a way to summarize the central tendency, spread, and range of observed demand.

Avoid introducing the statistical method before establishing why it is useful.

---

# Learning Objectives

After completing this lesson, you should be able to:

* [Explain the primary concept in plain language.]
* [Describe why the method is useful.]
* [Understand the mathematical foundation.]
* [Perform the calculation manually when practical.]
* [Implement the method using Python.]
* [Validate the Python result.]
* [Interpret the result in an engineering context.]
* [Identify important assumptions and limitations.]
* [Recognize common mistakes or misinterpretations.]

Objectives should emphasize understanding and interpretation rather than calculation alone.

---

# Prerequisites

Before beginning this lesson, you should be familiar with:

* [Previous concept]
* [Previous concept]
* [Relevant Python skill]
* [Relevant mathematical concept]

Reference previous Applied Infrastructure Analytics lessons where appropriate.

If no previous statistical knowledge is required, state that explicitly.

---

# Engineering Scenario

## Background

[Describe the infrastructure system.]

Include enough engineering context for the student to understand:

* What system is being evaluated
* Why the analysis is being performed
* Who might reasonably request the analysis
* What decision or investigation motivates the work

Do not introduce unnecessary complexity simply to make the scenario appear realistic.

---

## Engineering Question

State the primary engineering question clearly.

> **[Insert primary engineering question.]**

Examples:

> How variable is daily water demand relative to typical system demand?

> How frequently have historical streamflows exceeded a proposed design threshold?

> Is pump runtime changing over time?

> Does the available evidence suggest that two operating periods behave differently?

The statistical method introduced in the lesson should contribute directly to answering this question.

---

# Dataset

## Dataset Description

[Describe the instructional dataset.]

Include:

* Engineering system represented
* Observation period
* Observation frequency
* Number of observations, if appropriate
* Important variables
* Units
* Whether the data are simulated or external

The instructional dataset may be intentionally small or clean when doing so improves conceptual understanding.

---

## Variables

| Variable     | Description   | Unit   |
| ------------ | ------------- | ------ |
| `[variable]` | [Description] | [Unit] |
| `[variable]` | [Description] | [Unit] |
| `[variable]` | [Description] | [Unit] |

Include only fields relevant to understanding the instructional dataset.

---

## Data Location

```text
data/[raw|external]/[domain]/[dataset]/
```

Example:

```text
data/raw/water_distribution/01_daily_demand/
```

---

# Initial Data Inspection

Before performing statistical analysis, inspect the dataset.

Begin by answering:

* What does each row represent?
* What variables are available?
* What data types are present?
* Are values missing?
* Are units clear?
* Does the observation period match expectations?
* Do any values immediately appear questionable?

Example:

```python
import pandas as pd

df = pd.read_csv("path/to/data.csv")

print(df.head())
print(df.info())
```

Add additional inspection steps only where they contribute meaningfully to understanding the data.

---

## Initial Observations

Before calculating the primary statistics, consider:

* What patterns are immediately visible?
* Are any observations unusual?
* Does the dataset appear complete?
* Are values within plausible engineering ranges?
* What questions arise from the initial inspection?

Do not begin by assuming that unusual observations are errors.

---

# Concept 1 - [Concept Name]

## Conceptual Understanding

Explain the concept without equations first.

Address:

* What does the concept represent?
* What question does it answer?
* Why is it useful?
* How should the result be interpreted?
* What does it not tell us?

The student should be able to explain the concept to another engineer without relying on mathematical notation.

---

## Engineering Interpretation

Connect the concept directly to infrastructure engineering.

For example:

> In a water-demand dataset, the mean provides one measure of typical demand. However, it does not describe how much demand varies from day to day.

Explain when the concept is useful and when it may be insufficient by itself.

---

# Mathematical Foundation

Introduce the mathematical definition after the conceptual explanation.

$$
[\text{Insert equation}]
$$

where:

* $x$ = [definition]
* $n$ = [definition]
* $\bar{x}$ = [definition]
* [additional terms]

---

## What the Equation Is Doing

Explain the equation step by step in plain language.

For example:

1. [First operation]
2. [Second operation]
3. [Third operation]
4. [Interpretation of result]

The objective is to connect the mathematics to the underlying concept.

---

## Units

Explain the units of the result.

For example:

> If the observations are measured in MGD, the mean is also expressed in MGD.

Where intermediate calculations change units, explain this explicitly.

For example:

> Variance is expressed in squared units, while standard deviation returns the measure to the original units.

---

## Assumptions

Identify important assumptions where applicable.

Examples may include:

* Independent observations
* Representative sampling
* Distributional assumptions
* Stationarity
* Constant variance
* Linear relationships

Do not introduce assumptions that do not apply to the method.

---

# Manual Worked Example

Use a small dataset when manual calculation improves understanding.

Example:

| Observation |   Value |
| ----------: | ------: |
|           1 | [value] |
|           2 | [value] |
|           3 | [value] |
|           4 | [value] |
|           5 | [value] |

---

## Step 1 - [Calculation]

Show the calculation.

$$
[\text{Calculation}]
$$

Explain what is being calculated and why.

---

## Step 2 - [Calculation]

$$
[\text{Calculation}]
$$

Explain the result.

---

## Step 3 - [Calculation]

Continue only as long as the manual process contributes to conceptual understanding.

Do not turn the lesson into an arithmetic endurance event.

---

## Manual Result

Summarize the result:

$$
[\text{Final result}]
$$

Interpret it in plain language.

> [Engineering interpretation.]

---

# Python Implementation

Now perform the same analysis using Python.

## Direct Implementation

When educationally useful, implement the mathematical definition directly.

```python
# Implement the calculation from its mathematical definition.
```

Explain how the code corresponds to the mathematical formulation.

Do not recreate complex statistical algorithms merely for the sake of avoiding a library function.

---

## Library Implementation

Perform the calculation using an established library.

```python
# Perform the calculation using Pandas, NumPy, SciPy,
# Statsmodels, or another appropriate library.
```

Explain:

* Which function is being used
* What it returns
* Important default behavior
* Any parameters that materially affect the result

---

# Validation

Compare the results obtained using different methods where practical.

| Method                       |  Result |
| ---------------------------- | ------: |
| Manual calculation           | [value] |
| Direct Python implementation | [value] |
| Library implementation       | [value] |

The results should agree within an appropriate numerical tolerance.

If they do not, investigate why.

Possible causes include:

* Different statistical definitions
* Sample vs. population calculations
* Missing-value handling
* Rounding
* Incorrect implementation
* Different library defaults

Remember:

> **Python completing a calculation without an error does not establish that the calculation is correct.**

---

# Visualization

## Analytical Question

Before creating the visualization, state what it is intended to investigate.

> **[What are we trying to learn from this plot?]**

---

## Plot

```python
import matplotlib.pyplot as plt

# Create the visualization.
```

The visualization should contribute to the analysis rather than merely decorate the lesson.

---

## Interpretation

Discuss what the visualization shows.

Consider:

* Overall pattern
* Distribution
* Variability
* Extreme observations
* Trends
* Groups
* Relationships

Connect the visualization to the numerical results where appropriate.

---

# Concept 2 - [Concept Name]

Repeat the instructional sequence where necessary:

1. Conceptual understanding
2. Engineering interpretation
3. Mathematical foundation
4. Manual example when useful
5. Python implementation
6. Validation
7. Visualization where useful
8. Interpretation

Do not force every concept through every step if a step provides little educational value.

---

# Comparing Related Concepts

When the lesson introduces related statistics or methods, compare them directly.

For example:

| Method     | What It Describes | Strength   | Limitation   |
| ---------- | ----------------- | ---------- | ------------ |
| [Method 1] | [Description]     | [Strength] | [Limitation] |
| [Method 2] | [Description]     | [Strength] | [Limitation] |

Discuss when one measure may be more informative than another.

The objective is to develop method selection rather than formula memorization.

---

# Engineering Interpretation

Return to the original engineering scenario.

Summarize the analytical results.

For example:

> [Statistic or analytical result.]

Then explain what those results mean for the system being studied.

Address:

* What does the evidence show?
* What does it suggest?
* What does it not establish?
* What additional context matters?

---

# Observation vs. Interpretation

Clearly distinguish observed evidence from possible explanations.

## Observation

> [State what the data directly show.]

## Possible Interpretation

> [State one or more plausible explanations.]

## Additional Evidence Needed

> [Identify information that could support or reject those explanations.]

This distinction becomes increasingly important as the curriculum advances.

---

# Engineering Judgment

Consider the broader engineering implications.

Questions may include:

* Is the observed condition practically significant?
* Is the available dataset representative?
* Are the results affected by unusual events?
* Could operating conditions explain the result?
* Could measurement problems explain the result?
* Is additional analysis required?
* Would another engineering model be necessary?
* What uncertainty remains?

The statistical result should inform engineering judgment rather than replace it.

---

# Limitations

Identify limitations associated with the analysis.

Potential limitations may include:

* Small sample size
* Short observation period
* Missing observations
* Measurement uncertainty
* Distribution assumptions
* Unobserved variables
* Changing operating conditions
* Temporal dependence
* Limited system metadata

Avoid generic limitations that do not materially apply to the lesson.

---

# Common Mistakes and Misinterpretations

## Mistake 1 - [Description]

Explain the mistake.

Explain why it is incorrect.

---

## Mistake 2 - [Description]

Explain the mistake and its potential effect on an engineering conclusion.

---

## Mistake 3 - [Description]

Include common Python or library behavior only when it creates a meaningful analytical risk.

Focus primarily on reasoning errors.

---

# Reusable Python Component

If the lesson produces functionality worth reusing, identify the appropriate source location.

```text
src/applied_infrastructure_analytics/[module]/
```

Example:

```text
src/applied_infrastructure_analytics/descriptive/
└── dispersion.py
```

Potential function:

```python
def [function_name](...):
    ...
```

The function should:

* Have a clear analytical purpose
* Use type hints
* Follow project Python standards
* Avoid unnecessary abstraction
* Be reusable beyond the current dataset

Do not create custom functions merely because the repository has a `src/` directory.

---

# Testing

If reusable analytical functionality was created, add appropriate tests.

```text
tests/[module]/
```

Tests should focus on behavior such as:

* Known values
* Expected calculations
* Boundary conditions
* Invalid inputs
* Missing data
* Numerical tolerances

Example:

```python
def test_[function_name]_known_values() -> None:
    ...
```

Testing should validate the analytical implementation without distracting from the lesson's statistical objective.

---

# Knowledge Check

Answer these questions without running Python unless the question specifically requires calculation.

1. [Conceptual question]

2. [Interpretation question]

3. [Comparison question]

4. [Engineering application question]

5. [Common misconception question]

Knowledge checks should test understanding rather than memory of syntax.

---

# Explain It to an Engineer

Answer the following without equations:

> **[Insert conceptual question that requires explaining the lesson to another engineer.]**

Example:

> Why can two datasets have the same mean but represent very different operating conditions?

A clear explanation without equations is evidence of conceptual understanding.

---

# Lesson Summary

After completing this lesson, you should understand:

* [Concept]
* [Concept]
* [Mathematical relationship]
* [Python implementation]
* [Interpretation]
* [Engineering implication]

The most important idea is:

> **[Insert central lesson takeaway.]**

---

# Analytical Toolbox

This lesson adds the following tools to the analytical methods available for future exercises:

* [Method]
* [Method]
* [Visualization]
* [Diagnostic technique]

These methods remain available in later lessons.

Future exercises may require their use without explicitly instructing you to apply them.

---

# Transition to Applied Exercise

The lesson used:

* [Small / controlled dataset]
* [Known variables]
* [Demonstrated methods]
* [Guided interpretation]

The corresponding applied exercise changes the problem.

You will receive:

* [Description of realistic engineering dataset]
* [Approximate scope]
* [Multiple files if applicable]
* [More realistic data characteristics]

The exercise will require you to determine how the concepts from this lesson should be applied.

The applied exercise is located at:

```text
docs/04_exercises/XXa_[topic]/exercise.md
```

The associated data are located at:

```text
data/raw/[domain]/[dataset]/
```

Unlike the lesson, the applied exercise will not necessarily identify:

* Which variables are important
* Which observations require investigation
* Every statistical method to use
* What conclusions should be reached

That investigation is the exercise.

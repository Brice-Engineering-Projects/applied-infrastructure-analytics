# Exercise XXa - [Exercise Title]

## Assignment

[Provide a concise description of the engineering assignment.]

You are supporting [utility / municipality / engineering team / asset-management group / operations staff] with an evaluation of [infrastructure system or engineering problem].

The organization has provided historical data related to the system and has requested an independent analysis.

Your responsibility is to:

* Understand the engineering problem
* Review the available data
* Evaluate data quality
* Determine an appropriate analytical approach
* Perform and validate the analysis
* Interpret the available evidence
* Develop a defensible engineering conclusion
* Recommend appropriate next steps

The objective is not simply to calculate statistics.

The objective is to determine:

> **What do the available data tell us about the engineering problem?**

---

# Engineering Background

[Describe the infrastructure system and relevant engineering context.]

Include information that an engineer would reasonably know before beginning the assignment.

Potential information may include:

* System purpose
* Facility type
* General configuration
* Service area
* Equipment configuration
* Known operational concerns
* Relevant design criteria
* Historical context
* Reason the analysis was requested

Do not include analytical findings that should be discovered from the data.

---

# Problem Statement

[Describe the specific problem that prompted the analysis.]

For example:

> Operations staff have reported that Pump Station 14 appears to be cycling more frequently than it did historically. Staff are concerned that the change may indicate increasing influent flow, changing pump performance, or another operational condition.

The problem statement may identify concerns or observations reported by others.

It should not establish that those concerns are correct.

---

# Primary Engineering Question

The primary question for this assignment is:

> **[Insert engineering question.]**

Examples:

> Has pump-station operating behavior changed meaningfully during the period represented by the available data?

> Does the historical water-demand record indicate that existing production capacity is becoming increasingly constrained?

> Do historical asset failures support the utility's current replacement priorities?

> Has observed groundwater elevation changed significantly between the two monitoring periods?

The question should focus on the engineering problem rather than prescribe a statistical technique.

---

# Supporting Questions

The following questions may help frame the investigation:

* [Supporting engineering question]
* [Supporting engineering question]
* [Supporting engineering question]
* [Supporting engineering question]

Supporting questions should guide the investigation without becoming a step-by-step solution.

Advanced exercises may contain few or no supporting questions.

---

# Information Provided

The following information has been provided for the assignment.

## Engineering Information

[Provide relevant system information.]

Examples may include:

* Design capacity
* Equipment count
* Pipe diameter
* Storage volume
* Pump configuration
* Asset class
* Service population
* Relevant elevations
* Known operating rules

Only provide information that would reasonably be available to the analyst.

---

# Data Provided

The dataset is located at:

```text
data/raw/[domain]/[dataset]/
```

Files provided may include:

```text
README.md
[primary_data].csv
[metadata].csv
[event_history].csv
[additional_data].csv
```

The exact contents will depend on the assignment.

Treat all files under `data/raw/` as original source data.

**Do not modify the raw files.**

---

# Data Source

Dataset type:

> **[Simulated Operational Data / External Data]**

If simulated:

> This dataset is synthetic and was generated to represent realistic infrastructure system behavior. It does not contain records from an actual utility.

If external:

> This dataset was obtained from [source]. Refer to the dataset documentation for provenance information.

---

# Your Role

Approach this assignment as the engineer or analyst responsible for evaluating the available evidence.

You have not been provided with:

* A predetermined conclusion
* An answer key
* A list of important observations
* A list of anomalies
* The expected numerical results

Your analysis should determine what conclusions, if any, are supported by the data.

---

# Part 1 - Understand the Assignment

Before writing analysis code, summarize the problem in your own words.

Document:

1. What engineering system is being evaluated?
2. Why has the analysis been requested?
3. What is the primary engineering question?
4. What decisions might eventually be influenced by the analysis?
5. What information would you ideally want to evaluate the problem?

Do not begin with statistical calculations.

Begin by understanding the problem.

---

# Part 2 - Data Inventory

Review the files provided.

Create a data inventory containing, at minimum:

| File   | Purpose   | Records | Key Fields | Time Period | Notes   |
| ------ | --------- | ------: | ---------- | ----------- | ------- |
| [file] | [purpose] | [count] | [fields]   | [period]    | [notes] |

Determine:

* What does each file represent?
* What does each row represent?
* What identifiers are available?
* Which files appear related?
* What time periods are represented?
* What observation frequencies are present?
* What units are used?
* Which variables appear potentially relevant?

Do not assume that every supplied variable is required for the analysis.

---

# Part 3 - Initial Data Inspection

Inspect the data programmatically.

Potential inspection methods include:

```python
df.head()
df.tail()
df.info()
df.describe()
df.isna().sum()
```

These are examples, not a required checklist.

Use the inspection methods appropriate for the dataset.

Determine:

* Dataset dimensions
* Data types
* Missing values
* Date and time coverage
* Potential duplicate records
* Value ranges
* Categories
* Unique identifiers

Document important initial observations.

---

# Part 4 - Engineering Reasonableness Review

Before performing detailed statistical analysis, evaluate whether the data appear physically and operationally plausible.

Consider questions such as:

* Are values within reasonable engineering ranges?
* Are units internally consistent?
* Do equipment states make sense?
* Are timestamps plausible?
* Are calculated or recorded quantities physically possible?
* Do related variables behave consistently?
* Are there observations requiring additional investigation?

Do not automatically remove unusual values.

An unusual value may represent:

* A legitimate extreme event
* An equipment failure
* An operational change
* A sensor problem
* A data-entry problem
* A condition important to the analysis

Investigate before deciding.

---

# Part 5 - Data Quality Assessment

Evaluate the quality of the supplied data.

Investigate as appropriate for:

* Missing observations
* Duplicate records
* Duplicate timestamps
* Irregular observation intervals
* Invalid values
* Sensor dropout
* Constant or frozen measurements
* Unexpected discontinuities
* Inconsistent units
* Identifier problems
* Incomplete periods
* Changed equipment or operating conditions

Document each material issue identified.

For significant data-quality issues, record:

| Issue   | Evidence   | Potential Impact | Treatment  |
| ------- | ---------- | ---------------- | ---------- |
| [issue] | [evidence] | [impact]         | [decision] |

Do not correct data merely because they look inconvenient.

Every material cleaning decision should have a defensible reason.

---

# Part 6 - Analytical Plan

Before performing the primary analysis, develop a brief analytical plan.

Document:

## Engineering Question

[Restate the question.]

## Relevant Data

Identify which datasets and variables appear relevant.

## Proposed Analysis

Describe the analytical methods you intend to use.

## Why These Methods?

Explain why the proposed methods are appropriate for the engineering question.

## Potential Limitations

Identify known limitations before beginning the analysis.

The analytical plan may change as additional information is discovered.

That is acceptable.

Document material changes in approach.

---

# Part 7 - Data Processing

Create analysis-ready data without modifying the original source files.

The general workflow should be:

```text
data/raw/
    ↓
Inspection
    ↓
Cleaning
    ↓
Transformation
    ↓
data/processed/
```

Processing may include:

* Parsing timestamps
* Correcting data types
* Filtering invalid observations
* Joining datasets
* Resampling
* Aggregating
* Creating calculated variables
* Standardizing categories
* Handling missing observations

Processing decisions should be reproducible through Python.

Avoid manually editing source CSV files.

---

# Part 8 - Exploratory Analysis

Explore the data before attempting to answer the primary engineering question.

Use methods appropriate for the dataset.

Potential methods may include concepts learned in previous lessons, such as:

* Descriptive statistics
* Histograms
* Empirical CDFs
* Percentiles
* Box plots
* Time-series plots
* Scatter plots
* Distribution analysis

Do not create every possible statistic or plot.

Each analysis should contribute to understanding the system.

For every major visualization, be able to answer:

> **What question am I trying to answer with this plot?**

---

# Part 9 - Primary Analysis

Perform the analysis necessary to address the engineering question.

Apply concepts from the current lesson and, where appropriate, previous lessons.

The exercise may not explicitly identify every method that should be used.

You are responsible for determining:

* Which variables should be analyzed
* Which observations should be included
* Which statistical methods are appropriate
* Which comparisons are meaningful
* Which visualizations contribute to the analysis

Document the reasoning behind important analytical choices.

---

# Part 10 - Investigate Important Findings

Identify observations or patterns that materially affect the engineering interpretation.

Examples may include:

* Extreme observations
* Changes through time
* Unexpected distributions
* Different operating regimes
* Equipment-specific behavior
* Storm-related responses
* Failure periods
* Maintenance effects
* Changes in variability
* Unexpected relationships among variables

For each important finding, distinguish among:

## Observation

What do the data directly show?

## Possible Explanation

What might explain the observation?

## Supporting Evidence

What other information supports the explanation?

## Alternative Explanation

What else could reasonably produce the same observation?

Do not treat plausible explanations as established facts without supporting evidence.

---

# Part 11 - Validation

Validate important analytical results.

Possible validation methods include:

* Independent calculations
* Alternative statistical implementations
* Known-value checks
* Unit checks
* Cross-file comparisons
* Physical reasonableness checks
* Visual confirmation
* Sensitivity analysis

Ask:

* Does the result make physical sense?
* Are the units correct?
* Is the magnitude plausible?
* Do related datasets support the finding?
* Could a data-quality problem explain the result?
* Does another reasonable analytical approach produce a similar conclusion?

Successful execution of Python code is not sufficient validation.

---

# Part 12 - Engineering Interpretation

Return to the primary engineering question.

Summarize what the evidence shows.

Separate:

```text
Observed Evidence
        ↓
Statistical Findings
        ↓
Engineering Interpretation
        ↓
Conclusion
```

Avoid extending conclusions beyond what the available data support.

Where uncertainty remains, state it explicitly.

---

# Part 13 - Limitations

Identify limitations that materially affect the analysis.

Potential limitations may include:

* Observation period
* Sample size
* Missing data
* Sensor uncertainty
* Unknown operating conditions
* Equipment changes
* Incomplete maintenance records
* External variables not provided
* Statistical assumptions
* Temporal dependence
* Simulated-data limitations

For each important limitation, consider:

> **Could this limitation materially change the engineering conclusion?**

Focus on meaningful limitations rather than producing a generic disclaimer list.

---

# Part 14 - Engineering Conclusion

Answer the primary engineering question directly.

> **[Restate primary engineering question.]**

Develop a concise conclusion based on the available evidence.

A valid conclusion may be:

* The evidence supports the reported concern.
* The evidence does not support the reported concern.
* The evidence suggests a change, but the cause cannot be established.
* The available data are insufficient to reach a defensible conclusion.

Do not force certainty where the evidence does not justify it.

---

# Part 15 - Recommendation

Recommend an appropriate engineering next step.

Potential recommendations may include:

* No immediate action
* Continue monitoring
* Increase monitoring frequency
* Inspect equipment
* Verify instrumentation
* Review operating procedures
* Collect additional data
* Perform hydraulic modeling
* Perform field testing
* Conduct additional statistical analysis
* Evaluate maintenance needs
* Perform condition assessment
* Evaluate rehabilitation
* Begin capital planning analysis

The recommendation should follow from the evidence.

Do not recommend capital improvements merely because a statistical difference exists.

---

# Part 16 - Communication

Prepare a concise summary suitable for an engineering project manager, utility manager, or operations supervisor.

The summary should communicate:

## Issue

Why was the analysis performed?

## Data

What information was evaluated?

## Findings

What were the most important analytical findings?

## Conclusion

What does the evidence support?

## Recommendation

What should happen next?

The summary should communicate engineering meaning rather than narrate Python procedures.

---

# Required Deliverables

Submit the following unless otherwise specified by the exercise.

## 1. Analysis Code

Provide reproducible Python code used for:

* Data loading
* Data inspection
* Data processing
* Statistical analysis
* Visualization

---

## 2. Processed Data

Store material analysis-ready datasets under:

```text
data/processed/[domain]/[dataset]/
```

Do not overwrite the original raw data.

---

## 3. Figures

Provide the figures necessary to support the analysis.

Every figure should:

* Have a clear purpose
* Include appropriate labels
* Include units
* Be interpretable without reading the source code

---

## 4. Analytical Results

Provide the important numerical results required to support the engineering conclusion.

Do not include statistics merely because they can be calculated.

---

## 5. Engineering Summary

Provide a concise written summary containing:

* Problem
* Data evaluated
* Methods
* Findings
* Limitations
* Conclusion
* Recommendation

---

# Suggested Project Workspace

Use the associated notebook or Python workspace:

```text
notebooks/XXa_[topic]/
└── workspace.ipynb
```

or create appropriate Python scripts if that better supports the analysis.

Reusable analytical functionality may be added to:

```text
src/applied_infrastructure_analytics/
```

when justified.

Exercise-specific exploratory code does not need to become reusable package code.

---

# Use of Previous Lessons

Methods introduced in previous lessons remain available.

You may need to use concepts including:

* Histograms
* PDF and CDF
* Descriptive statistics
* Probability distributions
* Exceedance probability
* Confidence intervals
* Hypothesis testing
* Regression
* Time-series analysis

depending on your current position in the curriculum.

The exercise will not necessarily instruct you when to use previously learned methods.

Part of the exercise is learning to recognize when they are useful.

---

# What You Are Not Given

Unless specifically stated otherwise, the exercise does not provide:

* A completed analysis
* Expected numerical results
* A list of anomalies
* A predetermined statistical model
* A list of required variables
* A predetermined engineering conclusion
* A completed notebook
* A solution script
* An answer key

The absence of these items is intentional.

---

# Getting Help

If you become stuck, use the following progression.

## Level 1 - Conceptual Review

Return to the corresponding lesson and review the relevant concept.

---

## Level 2 - Directional Hint

Ask for guidance about what type of analysis or concept may be relevant.

Example:

> I am trying to determine whether pump cycling changed between these periods. What concepts should I consider?

---

## Level 3 - Method Guidance

Ask for help understanding how a method should be applied without requesting the completed analysis.

Example:

> How should I compare variability between two operating periods?

---

## Level 4 - Debugging Assistance

Provide your code, result, and expected analytical intent.

Example:

> I am trying to calculate daily pump starts from 5-minute status data, but my result appears too high. Can you help me debug my approach?

---

## Level 5 - Focused Demonstration

If necessary, request a simplified example using different data.

This preserves the opportunity to complete the actual exercise independently.

---

# Exercise Completion Checklist

Before considering the exercise complete, verify that you can answer the following.

## Engineering Problem

* [ ] I understand why the analysis was requested.
* [ ] I can clearly state the primary engineering question.

## Data

* [ ] I inventoried the supplied data.
* [ ] I understand what the important fields represent.
* [ ] I evaluated data quality.
* [ ] I preserved the raw data.

## Analysis

* [ ] I selected analytical methods for a reason.
* [ ] I investigated important observations.
* [ ] I validated material results.
* [ ] I considered alternative explanations.

## Interpretation

* [ ] I distinguished observations from interpretations.
* [ ] I identified meaningful limitations.
* [ ] My conclusion is supported by the available evidence.

## Engineering Decision

* [ ] I answered the primary engineering question.
* [ ] My recommendation follows from the analysis.
* [ ] I did not claim more certainty than the evidence supports.

## Communication

* [ ] My figures communicate useful information.
* [ ] Units are clearly identified.
* [ ] My engineering summary can be understood without reviewing the Python code.

---

# Final Reflection

After completing the exercise, answer the following questions.

1. What was the most important finding?

2. What analytical decision had the greatest influence on your result?

3. What was the most significant data-quality issue?

4. What additional data would most improve the analysis?

5. What conclusion would you be least comfortable defending and why?

6. If you received this assignment professionally, what would you do next?

7. Which analytical concepts from previous lessons proved useful?

8. What did you initially expect to find, and did the evidence support that expectation?

The objective of the reflection is not to determine whether the analysis produced the expected answer.

It is to evaluate the quality of the analytical reasoning.

---

# Completion Standard

This exercise is complete when you can defend:

> **What you did, why you did it, what you found, how you validated it, what the evidence does and does not establish, and what you recommend doing next.**

A technically correct statistical calculation without defensible engineering interpretation is incomplete.

Likewise, a plausible engineering conclusion without supporting analytical evidence is incomplete.

The objective is to connect both:

```text
Engineering Understanding
          +
Analytical Evidence
          +
Statistical Reasoning
          +
Validation
          +
Engineering Judgment
          ↓
Defensible Engineering Decision
```

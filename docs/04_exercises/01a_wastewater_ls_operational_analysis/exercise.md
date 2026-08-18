# Exercise 01a - Wastewater Pump Station Operational Analysis

## Purpose

A municipal wastewater utility is evaluating the operation of an existing pump station after operations staff reported periods of unusually high pump activity.

The utility has provided approximately one year of operational data from the station's SCADA system, local rainfall records, alarm history, and maintenance records.

You have been asked to perform an initial analytical review of the available information.

The objective is not to calculate a predetermined list of statistics.

Your objective is to use the analytical tools developed in Lessons 00 and 01 to determine:

> **What does the available operational record tell us about normal pump-station behavior, variability, and unusual operating conditions?**

This exercise introduces a more realistic infrastructure analytics workflow.

You will need to:

- understand multiple source files,
- evaluate data quality,
- determine which variables are relevant,
- select appropriate statistical methods,
- investigate unusual observations,
- compare related operational information,
- distinguish evidence from interpretation,
- and develop an engineering recommendation.

---

# Engineering Background

The **Riverview Water Utility** operates **Wastewater Pump Station PS-17**, which serves a predominantly residential wastewater collection basin.

The station contains two submersible centrifugal pumps operating in a lead-lag configuration.

Under normal conditions, one pump operates as the lead pump.

The second pump may operate when:

- influent flow exceeds the capacity of the lead pump,
- wet-well levels continue to rise,
- operating controls call for additional pumping,
- or unusual system conditions occur.

The station operates automatically based primarily on wet-well level.

Operations staff have reported that the station appears to experience periods of increased runtime and pump cycling.

They are uncertain whether these periods represent:

- normal wastewater-flow variability,
- rainfall-related response,
- changes in pump performance,
- control behavior,
- instrumentation problems,
- or some combination of these factors.

Before commissioning a detailed engineering evaluation, the utility wants an initial analysis of the historical operating record.

---

# Your Role

You are the engineer responsible for the initial data investigation.

The utility has provided several data exports but has not provided:

- a cleaned analytical dataset,
- a list of known data-quality problems,
- predetermined outliers,
- a prescribed statistical workflow,
- expected analytical results,
- or a predetermined engineering conclusion.

You are expected to determine how the available information should be evaluated.

---

# Primary Engineering Question

The primary question is:

> **What constitutes normal operation at PS-17, and what evidence exists of operating conditions that differ materially from that normal behavior?**

This question should guide the analysis.

Do not begin by calculating every statistic available in Pandas.

Statistics should be selected because they help answer an engineering question.

---

# Supporting Engineering Questions

Your investigation should provide sufficient evidence to discuss questions such as:

- What does typical station operation look like?
- How variable is station operation?
- How do Pump 1 and Pump 2 compare?
- How frequently does the station experience relatively high wet-well levels?
- How frequently do both pumps operate?
- Are pump starts reasonably consistent or highly variable?
- Are unusually high runtime periods present?
- Do unusual conditions appear isolated or clustered?
- Does rainfall appear to correspond with changes in station operation?
- Do alarm or maintenance records provide useful context for unusual observations?
- Are there data-quality issues that materially affect the conclusions?

These are investigative questions.

They are not intended to prescribe one calculation for each question.

---

# Available Data

The exercise dataset is located under:

```text
data/raw/wastewater/01a_pump_station_operations/
```

The data package contains:

```text
data/raw/wastewater/01a_pump_station_operations/
│
├── README.md
├── station_metadata.csv
├── scada_history.csv
├── rainfall_history.csv
├── alarm_history.csv
└── maintenance_history.csv
```

Treat all files in this directory as **raw source data**.

Do not modify them.

Any cleaned or transformed datasets should be stored under:

```text
data/processed/wastewater/01a_pump_station_operations/
```

---

# Dataset Type

> **Simulated Operational Data**

The supplied data are synthetic.

They are designed to represent the types of records that may be encountered during a municipal wastewater pump-station evaluation.

The files do not represent an actual utility or facility.

The simulation should nevertheless be treated as operational data.

Do not assume that:

- every record is valid,
- every timestamp is complete,
- every sensor is accurate,
- every file uses identical temporal resolution,
- every unusual value is erroneous,
- or every apparent relationship is causal.

---

# Source File Descriptions

## `station_metadata.csv`

This file contains station and equipment information.

Potential fields include:

- station identifier,
- station name,
- pump identifiers,
- pump capacities,
- wet-well operating levels,
- high-level alarm elevation,
- wet-well dimensions,
- SCADA recording interval,
- and observation period.

Review this file before analyzing the operational data.

Engineering context should be understood before interpreting sensor measurements.

---

# `scada_history.csv`

This is the primary operational dataset.

The file represents approximately one year of SCADA observations recorded at regular intervals.

Potential fields include:

```text
timestamp
station_id
wet_well_level_ft
influent_flow_gpm
discharge_flow_gpm
pump_1_status
pump_2_status
pump_1_current_amp
pump_2_current_amp
pump_1_runtime_hr
pump_2_runtime_hr
```

The exact contents of the supplied file should be inspected rather than assumed.

The SCADA file will contain substantially more observations than the controlled dataset used in Lesson 01.

---

# `rainfall_history.csv`

This file contains precipitation observations associated with the pump-station service area.

Potential fields include:

```text
timestamp
rainfall_in
```

Rainfall data may have a different recording frequency from the SCADA data.

Determine the temporal resolution before combining datasets.

---

# `alarm_history.csv`

This file contains recorded station alarms.

Potential information includes:

```text
alarm_timestamp
alarm_code
alarm_description
alarm_state
```

Alarm records may help explain unusual operational periods.

Do not assume that every alarm indicates an equipment failure.

---

# `maintenance_history.csv`

This file contains selected station maintenance records.

Potential information includes:

```text
work_order_id
event_date
equipment_id
maintenance_type
description
```

Maintenance records may provide context for changes in station behavior.

The absence of a maintenance record does not prove that no operational event occurred.

---

# Analytical Toolbox Available

You have now completed:

## Lesson 00

- Histograms
- Probability density
- Empirical cumulative distributions
- Exceedance probability

## Lesson 01

- Mean
- Median
- Mode
- Minimum
- Maximum
- Range
- Variance
- Standard deviation
- Percentiles
- Quartiles
- Interquartile range
- Box plots
- Resistant vs. non-resistant statistics

You may use any of these tools where appropriate.

You are **not required to use every tool**.

Part of the exercise is selecting methods appropriate to the engineering question.

---

# Part 1 - Understand the System

Before analyzing the SCADA record, review the station metadata.

Document your understanding of:

- station configuration,
- number of pumps,
- pump operating arrangement,
- approximate pump capacities,
- wet-well operating range,
- alarm levels,
- observation period,
- and SCADA recording frequency.

Then describe in your own words how you expect the station to operate under normal conditions.

Identify any assumptions you are making.

---

# Part 2 - Data Inventory

Review every supplied file.

Develop a data inventory.

A useful structure may be:

| File | Records | Time Period | Frequency | Key Variables | Potential Use |
| --- | ---: | --- | --- | --- | --- |
| | | | | | |

Determine:

- what each row represents,
- which identifiers connect the files,
- which files contain time-series observations,
- which files contain event records,
- whether recording frequencies differ,
- and which variables appear relevant to the engineering questions.

Do not merge the datasets yet.

First understand them.

---

# Part 3 - Data Quality Assessment

Evaluate the supplied data before performing the primary statistical analysis.

Investigate, where relevant:

- missing values,
- missing timestamps,
- duplicate timestamps,
- duplicate records,
- unexpected time intervals,
- impossible or questionable sensor values,
- inconsistent equipment states,
- discontinuities,
- cumulative-meter resets,
- and other suspicious conditions.

Do not assume that every unusual observation should be removed.

For each material issue, document:

| Issue | Evidence | Potential Impact | Proposed Treatment |
| --- | --- | --- | --- |
| | | | |

Your treatment should be reproducible.

Do not edit the raw CSV files manually.

---

# Part 4 - Establish Normal Operation

Use appropriate descriptive statistics and visualizations to characterize typical station operation.

You decide which variables and statistics are useful.

Your analysis should develop a defensible understanding of:

- typical wet-well level,
- typical influent conditions,
- typical discharge conditions,
- typical pump activity,
- and normal variability.

Consider whether the mean or median provides the more informative measure for each variable.

Do not assume the same statistic is appropriate for every variable.

---

# Part 5 - Evaluate Variability

Determine how much station operation varies throughout the historical record.

Select appropriate measures of dispersion.

Possible tools include:

- range,
- standard deviation,
- percentiles,
- interquartile range,
- histograms,
- box plots.

Consider:

> **Does the station usually operate within a relatively narrow range, or is substantial variability normal?**

Support your conclusion with evidence.

---

# Part 6 - Compare Pump Operation

Compare Pump 1 and Pump 2.

Determine whether the available data suggest meaningful differences in their operation.

Potential considerations include:

- runtime,
- frequency of operation,
- starts,
- motor current,
- concurrent operation,
- and other available measurements.

Do not assume that two pumps in the same station should have identical statistics.

Consider the lead-lag operating strategy when interpreting differences.

---

# Part 7 - Investigate Pump Starts

Use the SCADA status information to identify pump starts.

A pump start represents a transition from:

```text
OFF → ON
```

Develop a reproducible method for identifying these transitions.

Determine how pump-start behavior varies throughout the record.

Consider:

- typical starts per day,
- variability in daily starts,
- unusually high cycling periods,
- differences between pumps.

Be careful when interpreting state transitions across missing SCADA intervals.

A missing observation can make an apparent state transition ambiguous.

---

# Part 8 - Investigate Wet-Well Levels

Evaluate the distribution of recorded wet-well levels.

Determine whether the station generally operates within the expected operating range identified in the metadata.

Investigate observations approaching or exceeding important operating thresholds.

Consider whether percentile or exceedance analysis provides useful information.

Do not interpret every high wet-well observation as a station failure.

---

# Part 9 - Identify Unusual Operating Conditions

Develop a defensible method for identifying operating periods that deserve further investigation.

You may consider:

- extreme percentiles,
- IQR-based screening,
- unusual pump runtimes,
- high pump-start counts,
- high wet-well levels,
- simultaneous pump operation,
- unusual motor current,
- or combinations of variables.

Do not treat a statistical screening rule as proof that an observation is invalid.

The objective is to identify:

> **Conditions worth investigating.**

Not:

> **Rows worth deleting.**

---

# Part 10 - Investigate the Context of Unusual Conditions

Once unusual operating periods have been identified, investigate their context.

Use other available records where appropriate.

Potential evidence includes:

- rainfall,
- alarms,
- maintenance records,
- pump operating states,
- wet-well level,
- influent flow,
- discharge flow,
- motor current.

Ask:

> **What else was happening when station behavior changed?**

Look for supporting or contradictory evidence.

---

# Part 11 - Rainfall and Station Response

Investigate whether rainfall appears to correspond with changes in station operation.

Do not begin by assuming that rainfall causes increased wastewater flow.

Instead, examine the evidence.

Consider whether rainfall corresponds with changes in:

- influent flow,
- wet-well level,
- runtime,
- pump starts,
- simultaneous pump operation,
- or alarms.

Remember:

> **Association is evidence of a relationship, not proof of causation.**

More advanced methods for quantifying relationships will be introduced later in the curriculum.

For this exercise, descriptive evidence is sufficient.

---

# Part 12 - Alarm Investigation

Review the alarm history.

Determine:

- which alarm types occur,
- how frequently they occur,
- whether alarms cluster in time,
- and whether they correspond with unusual SCADA conditions.

Consider whether an alarm record changes your interpretation of any observations previously identified as unusual.

---

# Part 13 - Maintenance Investigation

Review the maintenance history.

Determine whether maintenance events correspond with:

- changes in runtime,
- changes in current,
- altered pump usage,
- unusual alarms,
- or other operational changes.

Do not force a relationship merely because two events occur near one another.

Document what the available evidence supports.

---

# Part 14 - Distribution vs. Chronology

Lessons 00 and 01 have primarily described the **distribution** of observations.

Operational data also have chronology.

Compare what you learn from:

- descriptive statistics,
- histograms,
- box plots,
- empirical CDFs,
- and chronological plots.

Consider:

> **What information disappears when timestamps are ignored?**

For example, ten unusual observations occurring throughout a year may have a different engineering meaning from ten unusual observations occurring during one six-hour event.

You are not yet expected to perform formal time-series analysis.

Recognize the limitation.

---

# Part 15 - Develop an Operating Profile

Using your analysis, develop a concise statistical profile of PS-17.

The profile should describe what you consider to be normal operation.

Possible characteristics include:

- wet-well level,
- influent flow,
- discharge flow,
- pump runtime,
- pump starts,
- motor current,
- simultaneous pump operation.

Choose metrics that actually help characterize the station.

Do not create a table containing every possible statistic merely because Python can calculate them.

---

# Part 16 - Investigate One Operating Event

Select **one operating period** that you believe deserves closer engineering investigation.

This could involve:

- unusually high wet-well levels,
- unusually high pump runtime,
- excessive cycling,
- unusual motor current,
- concurrent pump operation,
- an alarm sequence,
- rainfall response,
- or another condition supported by the data.

Develop a focused event analysis.

Document:

## What Happened?

Describe the observed condition.

## When Did It Happen?

Identify the relevant time period.

## What Evidence Supports It?

Use multiple data sources where appropriate.

## What Might Explain It?

Identify reasonable engineering hypotheses.

## What Cannot Be Determined?

Identify information that would be required before reaching a stronger conclusion.

This section should resemble a small engineering investigation rather than a statistics exercise.

---

# Part 17 - Validation

Select several important calculations and validate them independently.

Examples may include:

- mean runtime,
- standard deviation,
- percentile values,
- exceedance probability,
- pump-start count,
- simultaneous-operation frequency.

Where possible, compare:

```text
Direct Calculation
        ↓
Library Calculation
        ↓
Engineering Plausibility
```

A result is not validated merely because Python returned a number without crashing.

Python has tremendous confidence in terrible input.

---

# Part 18 - Engineering Interpretation

Return to the primary question:

> **What constitutes normal operation at PS-17, and what evidence exists of operating conditions that differ materially from that normal behavior?**

Your interpretation should distinguish among:

### Observed

Directly supported by the supplied data.

### Inferred

A reasonable interpretation supported by multiple observations.

### Unknown

Cannot be established from the supplied information.

Avoid presenting hypotheses as established causes.

---

# Part 19 - Limitations

Identify limitations that materially affect your conclusions.

Potential limitations may include:

- observation period,
- data resolution,
- missing records,
- questionable sensor measurements,
- absence of calibration information,
- lack of hydraulic system information,
- rainfall-gauge representativeness,
- limited maintenance history,
- aggregation of operational variables,
- lack of upstream flow monitoring.

For each important limitation, consider:

> **Could this limitation materially change my interpretation?**

---

# Part 20 - Engineering Recommendation

Prepare recommendations based on your findings.

Recommendations may include:

- continued monitoring,
- sensor validation,
- pump inspection,
- control review,
- additional flow monitoring,
- rainfall-response investigation,
- maintenance review,
- hydraulic evaluation,
- additional historical analysis.

Recommendations should follow from the evidence.

Do not recommend replacing a pump because a box plot drew a dot above a whisker.

---

# Required Deliverables

## 1. Analysis Notebook

Complete the primary investigation in:

```text
notebooks/01a_pump_station_operations/
└── workspace.ipynb
```

The notebook should execute successfully from beginning to end.

---

## 2. Processed Data

Store material processed datasets under:

```text
data/processed/wastewater/01a_pump_station_operations/
```

Do not modify the raw source files.

Processing should be reproducible from code.

---

## 3. Data Quality Summary

Provide a concise summary containing:

| Issue | Evidence | Treatment | Potential Impact |
| --- | --- | --- | --- |
| | | | |

Include only meaningful issues.

---

## 4. Operating Profile

Develop a concise statistical profile of normal PS-17 operation.

Select the variables and statistics that best communicate normal operating conditions.

---

## 5. Pump Comparison

Provide an appropriate comparison of Pump 1 and Pump 2.

The comparison should address both:

- central tendency,
- and variability.

---

## 6. Figures

Provide figures sufficient to support your analysis.

At minimum, your work should communicate:

- distributions of important operational variables,
- pump comparison,
- chronology of important station behavior,
- and the selected unusual operating event.

The exact figures are your decision.

---

## 7. Event Investigation

Provide a focused investigation of one operating period deserving additional engineering attention.

Use multiple data sources where appropriate.

---

## 8. Engineering Summary

Prepare a concise engineering summary containing:

### Issue

Why was the analysis performed?

### Data

What information was evaluated?

### Data Quality

Were there material limitations or questionable records?

### Normal Operation

What does typical station operation look like?

### Unusual Conditions

What conditions deserve additional attention?

### Findings

What are the most important analytical results?

### Limitations

What cannot be determined?

### Conclusion

What does the available evidence support?

### Recommendations

What should the utility do next?

---

# Reusable Code

During the exercise, identify analytical functionality that may be useful elsewhere in the project.

Potential examples include:

```python
calculate_descriptive_statistics()
calculate_exceedance_probability()
identify_state_transitions()
calculate_daily_pump_starts()
```

Do not automatically move all notebook code into `src/`.

Reusable functionality should be:

- general,
- typed,
- tested,
- independent of the PS-17 dataset.

Dataset-specific exploratory analysis belongs naturally in the notebook.

---

# Testing

Any reusable functionality added to:

```text
src/applied_infrastructure_analytics/
```

should have corresponding tests under:

```text
tests/
```

Use small known-value datasets for validation.

For example, a pump-start function should be testable using a short known sequence such as:

```text
OFF
OFF
ON
ON
OFF
ON
```

The expected number of starts can then be determined manually.

---

# Getting Help

The purpose of the exercise is independent problem solving.

If you become stuck, use progressively stronger assistance.

## Level 1 - Review the Lessons

Return to Lessons 00 and 01.

## Level 2 - Conceptual Guidance

Ask which statistical concept may be appropriate for a particular engineering question.

## Level 3 - Method Guidance

Ask how to implement a method without requesting results from the exercise dataset.

## Level 4 - Debugging

Provide your code, expected behavior, and observed behavior.

## Level 5 - Separate Example

Request a worked demonstration using a different dataset.

Avoid requesting completed analysis of the exercise data.

There is intentionally no solution notebook or answer key.

---

# Reflection

After completing the exercise, answer the following questions.

1. Which statistic was most useful for defining typical station operation?

2. Which measure was most useful for understanding variability?

3. Did the mean and median lead to the same interpretation for every variable?

4. Which variables were most affected by extreme observations?

5. Did any statistically unusual observations appear operationally legitimate?

6. Did any apparently reasonable observations become suspicious only after comparing them with another dataset?

7. What information did chronology reveal that descriptive statistics alone did not?

8. How did rainfall, alarm, or maintenance records affect your interpretation?

9. Which data-quality decision had the greatest potential to change your results?

10. What additional information would you request from the utility?

11. Which conclusion are you most confident defending?

12. Which conclusion would you be least comfortable presenting as definitive?

---

# Completion Standard

This exercise is complete when you can explain:

> **What normal PS-17 operation looks like, how much that operation varies, which conditions differ materially from normal behavior, what evidence may explain those conditions, and what cannot be concluded from the available data.**

A successful analysis should demonstrate more than the ability to calculate descriptive statistics.

It should demonstrate the ability to decide:

> **Which statistics matter, why they matter, and what they mean for the infrastructure system being evaluated.**

---

# Looking Ahead

This exercise describes operational behavior.

It does not yet provide the statistical tools necessary to model the probability distribution underlying that behavior.

The next lesson introduces **common probability distributions** and examines how theoretical distributions can be used to represent uncertain engineering variables.

Later lessons will add tools for:

- return periods,
- statistical inference,
- regression,
- time-series analysis,
- Monte Carlo simulation,
- reliability analysis,
- Bayesian inference,
- and Markov models.

The operational datasets introduced here may be revisited as the analytical toolbox expands.
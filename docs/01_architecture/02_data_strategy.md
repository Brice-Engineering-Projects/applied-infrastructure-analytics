# Data Strategy

## Purpose

This document defines the data strategy for **Applied Infrastructure Analytics**.

Data are not treated merely as inputs required to demonstrate statistical methods.

They are a fundamental part of the learning experience.

The project is designed to develop the ability to receive, understand, investigate, process, analyze, and interpret infrastructure data in a manner that increasingly resembles professional engineering analytics work.

The data strategy therefore establishes standards for:

* Dataset realism
* Simulated engineering systems
* Dataset scale
* Raw and processed data
* External data
* Multi-file datasets
* Data quality
* Metadata and documentation
* Reproducibility
* Hidden simulation ground truth
* Progressive data complexity
* Data provenance
* Exercise design

The central principle is:

> **Data should represent the engineering system and data collection process being studied, not merely provide convenient numbers for a statistical calculation.**

---

# Data Philosophy

Applied Infrastructure Analytics uses data to teach both:

```text
Statistical Analysis
        +
Engineering Investigation
```

A student should eventually be able to receive unfamiliar infrastructure data and determine:

1. What information was provided?
2. What does each variable represent?
3. How were the data collected?
4. What time period is represented?
5. Are the data complete?
6. Are the data internally consistent?
7. Are the observations physically reasonable?
8. Which variables are relevant?
9. Which datasets need to be combined?
10. What analytical methods are appropriate?
11. What limitations exist?
12. What conclusions are supported by the evidence?

The data should therefore support investigation rather than merely calculation.

---

# Data Categories

The project recognizes three primary categories of data.

## 1. Educational Data

Educational datasets are intentionally simplified to support conceptual understanding.

They may be:

* Small
* Clean
* Single-file
* Easy to inspect
* Easy to visualize
* Manually verifiable

For example, a lesson introducing variance may use ten or twenty observations so that the calculation can be reproduced manually.

This is appropriate when simplification improves understanding.

Educational datasets should not be presented as representative of the full complexity of utility or infrastructure data.

---

## 2. Simulated Operational Data

Simulated operational data are synthetic datasets designed to represent realistic infrastructure systems and data collection processes.

These datasets should reproduce meaningful characteristics of the system being modeled.

Examples include:

* SCADA histories
* Water-demand records
* Pump-station operation
* Asset inventories
* Maintenance histories
* Failure records
* Groundwater monitoring
* Construction-cost histories
* Rainfall observations
* Sensor data

These datasets are the primary mechanism for creating realistic applied exercises when suitable real data are unavailable.

---

## 3. External Data

External datasets are obtained from public, authoritative, or otherwise documented sources.

Potential sources include:

* USGS
* NOAA
* EPA
* State environmental agencies
* Transportation agencies
* Municipal open-data portals
* Public utilities
* Other authoritative infrastructure sources

External datasets should retain sufficient provenance to identify their origin and relevant documentation.

---

# Data Directory Architecture

The project uses the following general structure:

```text
data/
├── raw/
│   ├── hydrology/
│   ├── water_distribution/
│   ├── wastewater/
│   ├── groundwater/
│   ├── reliability/
│   ├── asset_management/
│   ├── construction_costs/
│   └── operations/
│
├── processed/
│   ├── hydrology/
│   ├── water_distribution/
│   ├── wastewater/
│   ├── groundwater/
│   ├── reliability/
│   ├── asset_management/
│   ├── construction_costs/
│   └── operations/
│
└── external/
    ├── hydrology/
    ├── water_distribution/
    ├── wastewater/
    ├── groundwater/
    ├── reliability/
    ├── asset_management/
    ├── construction_costs/
    └── operations/
```

Additional engineering domains may be introduced when justified by the curriculum.

---

# Raw Data

The `data/raw/` directory represents data in the form in which it is supplied to the student.

Raw data are considered **immutable**.

The student should not:

* Manually correct raw CSV files
* Delete suspicious observations from raw files
* Replace missing values directly in raw files
* Change units in raw files
* Rename categories inside raw files
* Overwrite the original dataset with cleaned data

Instead:

```text
data/raw/
    ↓
Processing Code
    ↓
data/processed/
```

This preserves the original evidence and allows the analysis to be reproduced.

---

# Raw Data Should Feel Received

When an applied exercise represents a utility or engineering assignment, the raw dataset should resemble something the analyst might plausibly receive.

For example:

```text
data/raw/wastewater/07_pump_station_analysis/
├── station_metadata.csv
├── scada_history.csv
├── alarm_history.csv
├── maintenance_history.csv
└── rainfall_history.csv
```

The exercise should not automatically collapse these into:

```text
pump_analysis_ready.csv
```

before the student begins.

Part of the analytical assignment may involve determining:

* What each file contains
* How the files relate
* Which identifiers correspond
* Whether timestamps align
* Whether observation periods overlap
* Which information is relevant

The analytical process begins when the data are received.

---

# Processed Data

The `data/processed/` directory contains datasets created through reproducible analytical processing.

Examples include:

* Cleaned datasets
* Joined datasets
* Resampled time series
* Aggregated observations
* Calculated variables
* Standardized categories
* Analysis-ready tables

Processed data should generally be generated through Python code.

For example:

```text
scada_history.csv
rainfall_history.csv
maintenance_history.csv
        ↓
Python Processing
        ↓
pump_station_analysis.csv
```

The transformation from raw to processed data should be reproducible whenever practical.

---

# External Data

The `data/external/` directory contains datasets obtained from outside the project.

External data should remain as close as practical to the form originally obtained.

Transformations should produce processed datasets rather than modify the external source file.

For example:

```text
data/external/hydrology/usgs_streamflow.csv
                    ↓
             Processing
                    ↓
data/processed/hydrology/annual_peak_flow.csv
```

---

# Data Provenance

Every dataset should have identifiable provenance.

At minimum, it should be possible to determine:

* Whether the data are real or simulated
* Source or simulated source
* Engineering system represented
* Observation period
* General collection method
* Relevant units
* Date generated or obtained

For external data, provenance should also identify:

* Organization
* Dataset or station identifier where applicable
* Source documentation
* Date accessed

For simulated data, provenance should identify that the dataset is synthetic.

Simulated data should never be presented as actual utility records.

---

# Simulate Engineering Systems, Not Independent Columns

Simulated operational data should represent an engineering system.

Variables should have meaningful relationships where such relationships would exist physically or operationally.

For example, wastewater pump-station data might represent:

```text
Rainfall
    ↓
Rainfall-Dependent I&I
    ↓
Influent Flow
    ↓
Wet-Well Level
    ↓
Pump Control Logic
    ↓
Pump Status
    ↓
Pump Runtime
    ↓
Discharge Flow
```

Additional relationships may include:

```text
Pump Operation
    ↓
Motor Current

Discharge Conditions
    ↓
Discharge Pressure

Pump Failure
    ↓
Reduced Available Capacity
    ↓
Wet-Well Response
```

The simulation should produce a system of related observations.

It should not merely create:

```python
flow = random(...)
pressure = random(...)
level = random(...)
runtime = random(...)
```

with no meaningful relationship among them.

---

# Physical Plausibility

Simulated data should respect basic physical and operational constraints.

Examples include:

* Wet-well level should remain within plausible physical limits unless an overflow or sensor problem is intentionally represented.
* Pump runtime cannot be negative.
* Pump status should correspond reasonably with runtime accumulation.
* Pump starts should correspond with changes in operating status.
* Discharge flow should respond to operating pumps.
* Tank levels should respond to inflow and outflow.
* Pressure should remain within plausible system ranges unless an abnormal event occurs.
* Asset installation dates should precede inspection or failure dates.
* Repair events should occur after associated failures.
* Construction bid quantities and unit prices should produce internally consistent costs.

Statistical realism without engineering realism is insufficient.

---

# Operational Plausibility

Infrastructure systems are influenced by operating rules.

Simulated data should incorporate these rules when relevant.

Examples include:

* Lead/lag pump sequencing
* Wet-well start and stop elevations
* Tank level controls
* Pump rotation
* Equipment availability
* Maintenance outages
* Alarm thresholds
* Minimum runtime
* Maximum starts per hour
* Demand-driven operation
* Seasonal operating modes

These rules create relationships that the student can investigate.

---

# Temporal Plausibility

Time-dependent engineering data should exhibit realistic temporal behavior.

Depending on the system, this may include:

* Diurnal cycles
* Weekly cycles
* Seasonal patterns
* Long-term trends
* Storm events
* Lagged responses
* Operational cycles
* Maintenance periods
* Equipment deterioration
* Sudden failures

For example, municipal water demand may contain:

```text
Base Demand
    +
Morning Peak
    +
Evening Peak
    +
Seasonal Effect
    +
Weekend Effect
    +
Weather Effect
    +
Random Variability
```

Wastewater flow may contain:

```text
Base Sanitary Flow
    +
Diurnal Pattern
    +
Seasonal Variation
    +
Rainfall-Dependent I&I
    +
Lagged Groundwater Response
    +
Random Variability
```

Time-series data should not generally behave as independent random observations when the underlying engineering process would exhibit temporal dependence.

---

# Cross-Dataset Relationships

When an exercise contains multiple files, meaningful relationships should exist across those files.

For example:

```text
rainfall_history.csv
        ↓
scada_history.csv
        ↓
alarm_history.csv
```

A significant rainfall event may be followed by:

* Increased influent flow
* Increased pump runtime
* Higher wet-well levels
* High-level alarms

Similarly:

```text
maintenance_history.csv
        ↓
pump_availability
        ↓
scada_history.csv
```

A pump removed from service should influence recorded system operation.

These relationships should be discoverable through analysis.

---

# Dataset Scale

Dataset size should be determined by the engineering system and data collection process.

There is no preferred arbitrary row count.

For example, two years of 15-minute SCADA observations produce approximately:

$$
2 \times 365 \times 24 \times 4
===============================

70,080
$$

observations.

Two years of 5-minute observations produce approximately:

$$
2 \times 365 \times 24 \times 12
================================

210,240
$$

observations.

These are entirely reasonable dataset sizes for an operational exercise.

Likewise:

* A water-main inventory may contain 10,000 or more assets.
* A maintenance database may contain tens of thousands of work orders.
* A construction-cost database may contain thousands of bid items.
* A sensor network may produce millions of observations.
* A 30-year annual peak-flow record may legitimately contain only 30 observations.

The governing principle is:

> **Dataset size should reflect the frequency, duration, and nature of the engineering process being represented.**

Large datasets should not be created merely to appear realistic.

Small datasets should not be artificially enlarged when the engineering process naturally produces few observations.

---

# Observation Frequency

Time-series frequency should reflect plausible data collection practices.

Examples may include:

| Data Type              | Typical Simulated Frequency           |
| ---------------------- | ------------------------------------- |
| SCADA                  | 1, 5, 15, or 60 minutes               |
| Daily water production | Daily                                 |
| Rainfall               | 5-minute, 15-minute, hourly, or daily |
| Groundwater level      | Hourly, daily, weekly, or monthly     |
| Laboratory data        | Daily, weekly, or event-based         |
| Maintenance records    | Event-based                           |
| Asset failures         | Event-based                           |
| Condition inspections  | Annual or multi-year                  |
| Bid data               | Project/event-based                   |

The selected frequency should support the engineering scenario.

---

# Dataset Duration

Observation duration should also reflect the analytical question.

Examples include:

* Several weeks for operational troubleshooting
* One to three years for SCADA analysis
* Multiple years for water-demand analysis
* Decades for hydrologic frequency analysis
* Multiple inspection cycles for deterioration analysis
* Many years of failures for reliability analysis

Duration should not be selected solely to produce a convenient file size.

---

# Complete Operational Context

Applied datasets should increasingly contain the broader information that would reasonably be available for the engineering system.

For example, a pump-station dataset should not necessarily contain only the variable required for the lesson.

Instead of:

```text
timestamp
peak_flow_gpm
```

the supplied data might include:

```text
timestamp
station_id
wet_well_level_ft
influent_flow_gpm
discharge_flow_gpm
discharge_pressure_psi
pump_1_status
pump_1_runtime_hr
pump_1_current_amp
pump_2_status
pump_2_runtime_hr
pump_2_current_amp
pump_3_status
pump_3_runtime_hr
pump_3_current_amp
high_level_alarm
pump_failure_alarm
```

Related files may provide:

* Rainfall
* Equipment metadata
* Pump characteristics
* Maintenance history
* Alarm history

The student should determine which information is relevant to the engineering question.

---

# Relevant and Irrelevant Variables

Applied datasets should not always contain only useful variables.

Real data exports frequently contain:

* Important variables
* Contextual variables
* Redundant variables
* Administrative fields
* Variables unrelated to the immediate analysis

Including some irrelevant information is desirable because it requires the student to determine:

> **What data actually matter to this problem?**

However, irrelevant variables should remain plausible.

They should not be added merely as artificial distractions.

---

# Data Quality Strategy

Data quality problems should be introduced progressively.

Potential issues include:

* Missing observations
* Duplicate rows
* Duplicate timestamps
* Irregular intervals
* Sensor dropout
* Sensor drift
* Sensor saturation
* Implausible values
* Incorrect signs
* Inconsistent units
* Changed identifiers
* Equipment replacement
* Changed setpoints
* Maintenance outages
* Incomplete event records
* Time-zone issues
* Daylight-saving-time effects
* Inconsistent categories
* Unexplained gaps

The student should increasingly be expected to identify these conditions without being told exactly where they occur.

---

# Data Problems Must Have a Reason

Intentional imperfections should represent plausible mechanisms.

For example:

## Missing SCADA Data

Possible cause:

* Communication outage

## Repeated Constant Sensor Value

Possible cause:

* Frozen sensor signal

## Gradual Measurement Shift

Possible cause:

* Sensor drift

## Sudden Change in Pump Current

Possible cause:

* Equipment replacement
* Changed operating condition
* Instrument recalibration

## Missing Maintenance Record

Possible cause:

* Incomplete historical migration

The dataset does not necessarily need to reveal the cause directly.

But the simulation should have an internal reason for the condition.

Random corruption without an engineering or data-system rationale should be avoided.

---

# Missingness Strategy

Missing data should not always be completely random.

Infrastructure data may be missing because of:

* Communication outages
* Equipment shutdown
* Sensor failure
* Maintenance activity
* Database migration
* Power interruption

These mechanisms may themselves contain useful information.

For example:

```text
Pump Failure
     ↓
Sensor / Equipment Offline
     ↓
Missing Measurements
```

Treating all missing observations as random would remove this important characteristic.

---

# Outlier Strategy

Simulated datasets should contain both:

## Legitimate Extreme Events

Examples:

* Major storm
* Extreme demand
* High groundwater
* Equipment overload
* Unusual construction bid
* Rare failure event

and:

## Erroneous Observations

Examples:

* Sensor spike
* Negative flow caused by instrumentation error
* Incorrect decimal placement
* Duplicate record
* Data-entry mistake

The student should not automatically know which type an unusual observation represents.

The objective is to encourage:

```text
Detect
   ↓
Investigate
   ↓
Cross-Reference
   ↓
Interpret
   ↓
Decide
```

rather than:

```text
Detect
   ↓
Delete
```

---

# Engineering Events

Operational datasets should include events when appropriate.

Examples include:

* Storms
* Pump failures
* Maintenance shutdowns
* Equipment replacement
* Control changes
* Tank outages
* Major demand events
* Power interruptions
* Main breaks
* Rehabilitation
* Inspection events

Events should influence related observations realistically.

An equipment failure should not exist only as a row in `maintenance_history.csv`.

If appropriate, its effect should also be observable in operational data.

---

# Equipment Deterioration

Some advanced datasets may simulate gradual deterioration.

Examples include:

* Reduced pump efficiency
* Increased motor current
* Increased vibration
* Increasing failure frequency
* Sensor drift
* Reduced equipment capacity

Deterioration should generally occur over a plausible time scale.

The student should not automatically be told that deterioration exists.

Identifying whether a meaningful change occurred may be part of the exercise.

---

# Changing Operating Conditions

Not every change in observed behavior should represent failure.

Simulated systems may include:

* Changed control setpoints
* Lead/lag rotation
* Seasonal operating procedures
* New equipment
* System expansion
* Changed demand
* Maintenance practices
* Downstream hydraulic changes

This is important because engineering analysis requires distinguishing:

> **Changing equipment condition**

from:

> **Changing operating environment**

---

# Multi-File Dataset Strategy

Intermediate and advanced exercises should increasingly use multiple related files.

A typical dataset may contain:

```text
station_metadata.csv
scada_history.csv
maintenance_history.csv
alarm_history.csv
rainfall_history.csv
```

Other exercises may include:

```text
asset_inventory.csv
inspection_history.csv
failure_history.csv
work_orders.csv
rehabilitation_history.csv
```

or:

```text
project_metadata.csv
bid_items.csv
engineer_estimates.csv
bid_results.csv
cost_indices.csv
```

The student should determine how these sources relate.

---

# Identifiers

Related datasets should use realistic identifiers.

Examples include:

```text
station_id
asset_id
pump_id
work_order_id
inspection_id
project_id
sensor_id
```

Identifiers should support joining datasets while occasionally reflecting realistic complications such as:

* Equipment replacement
* Changed asset IDs
* Legacy naming conventions

Such complications should be introduced only when educationally appropriate.

---

# Units

Engineering datasets should use explicit and plausible units whenever they would reasonably be known.

Examples include:

```text
flow_gpm
flow_mgd
pressure_psi
level_ft
rainfall_in
runtime_hr
current_amp
cost_usd
diameter_in
length_ft
```

Unit information may appear in:

* Column names
* Metadata
* Data dictionaries
* Source documentation

Exercises may occasionally include inconsistent units when unit verification is intentionally part of the problem.

Unit ambiguity should not occur accidentally.

---

# Metadata

Operational datasets should include appropriate system metadata when relevant.

For a pump station, metadata might contain:

```text
station_id
station_name
wet_well_diameter_ft
wet_well_bottom_elevation_ft
high_level_alarm_ft
pump_start_level_ft
pump_stop_level_ft
pump_count
design_flow_gpm
commission_date
```

Equipment metadata might include:

```text
pump_id
manufacturer
model
rated_flow_gpm
rated_head_ft
motor_hp
installation_date
status
```

Metadata provide engineering context without necessarily identifying the analytical answer.

---

# Data Dictionaries

Moderate and advanced datasets should generally include a data dictionary when field meanings would not otherwise be obvious.

A data dictionary may define:

| Field                | Description                                                         | Unit    |
| -------------------- | ------------------------------------------------------------------- | ------- |
| `wet_well_level_ft`  | Recorded wet-well water-surface elevation relative to station datum | ft      |
| `discharge_flow_gpm` | Station discharge flow measurement                                  | gpm     |
| `pump_1_status`      | Recorded operating status of Pump 1                                 | Boolean |
| `pump_1_current_amp` | Pump 1 motor current                                                | A       |

The data dictionary should explain what fields represent.

It should not explain what conclusions the student should draw from them.

---

# Hidden Simulation Ground Truth

Simulated datasets require an important distinction between:

```text
Student-Facing Data
```

and:

```text
Simulation Ground Truth
```

The generation process may internally know:

* True baseline behavior
* Failure dates
* Sensor anomalies
* Deterioration rates
* Rainfall-response relationships
* Changed operating setpoints
* Missing-data mechanisms
* Distribution parameters
* Event probabilities

This information should not automatically be exposed to the student.

For example, the simulation may internally specify:

```text
Pump 2 efficiency begins declining after Month 14.
```

The student-facing exercise may state only:

> Operations staff have expressed concern regarding Pump 2 performance.

The student must determine whether the available evidence supports that concern.

---

# Ground Truth Is Not an Answer Key

Simulation ground truth exists for:

* Dataset generation
* Reproducibility
* Quality assurance
* Validation of the simulation itself

It should not become a repository of exercise solutions.

The student's statistical result may not exactly reproduce the hidden simulation parameter.

That is acceptable.

Real analysis works from observations, not omniscient knowledge of the data-generating process.

---

# Simulation Specifications

Each significant simulated dataset should have an internal generation specification.

The specification may define:

* Engineering system
* Simulation duration
* Observation frequency
* Physical assumptions
* Operational rules
* Statistical distributions
* Relationships among variables
* Environmental conditions
* Failure mechanisms
* Maintenance events
* Sensor behavior
* Data-quality mechanisms
* Random seed

The specification exists to ensure that the simulation is deliberate and reproducible.

---

# Random Seeds

Simulated datasets should use controlled random seeds when appropriate.

For example:

```python
rng = np.random.default_rng(42)
```

The specific seed value is less important than reproducibility.

Running the generator with the same configuration should reproduce the same dataset unless intentional variability is part of the design.

---

# Dataset Generation Scripts

Simulated datasets should be generated through code stored under:

```text
scripts/generate_data/
```

For example:

```text
scripts/generate_data/wastewater/
└── generate_pump_station_history.py
```

Generation scripts should produce data under the appropriate:

```text
data/raw/
```

directory.

The generator should not be required for completing the student exercise.

---

# Generation Code and Exercise Integrity

Generation scripts create a special issue for a no-solution repository.

Reading the generator may expose:

* Hidden anomalies
* Failure dates
* Distribution parameters
* Intended relationships

Therefore, the existence of generation code should not be interpreted as permission to inspect it while completing the associated exercise.

The project should treat generation scripts as **dataset infrastructure**, not instructional material.

The student-facing exercise should be completed from the supplied data.

---

# Simulation Quality Assurance

Before a simulated dataset is accepted into the curriculum, it should be checked for engineering and statistical plausibility.

Quality assurance should consider:

## Structural Validation

* Expected columns exist
* Data types are appropriate
* Identifiers behave as intended
* Files can be loaded

## Physical Validation

* Values fall within plausible ranges
* Physical relationships behave reasonably
* Impossible states occur only when intentionally modeled

## Temporal Validation

* Time frequency is correct
* Expected patterns exist
* Events occur in the intended sequence

## Cross-File Validation

* Related identifiers match
* Maintenance events correspond with equipment
* Rainfall periods align with SCADA periods
* Failure events influence relevant operational records

## Statistical Validation

* Distributions behave plausibly
* Variability is appropriate
* Correlations are not accidentally unrealistic
* Noise does not overwhelm intended system behavior

The objective is not to make the answer obvious.

The objective is to ensure that the simulated system makes sense.

---

# Avoiding Over-Engineered Simulation

Simulation realism has limits.

The project should not require development of a complete hydraulic, hydrologic, process, or electrical model merely to generate exercise data.

The simulation should be:

> **Realistic enough to preserve the relationships important to the analytical problem.**

For example, generating pump-station SCADA does not necessarily require solving full transient hydraulics.

A simplified mass-balance model may be sufficient:

$$
\frac{dV}{dt}
=============

## Q_{in}

Q_{out}
$$

combined with:

* Wet-well geometry
* Pump control logic
* Approximate pump capacity
* Rainfall-dependent flow
* Operational events

The level of simulation complexity should support the lesson rather than become a separate engineering modeling project.

---

# Avoiding Artificial Statistical Perfection

Simulated data should not be constructed merely to produce textbook-perfect statistical results.

Real systems rarely produce:

* Perfect normal distributions
* Exact linear relationships
* Constant variance
* Perfect seasonal cycles
* Clean separation between populations
* Obvious failure thresholds

Noise, competing influences, measurement error, and operational variability should prevent the data from becoming suspiciously cooperative.

A regression exercise should not necessarily produce:

$$
R^2 = 0.99
$$

unless the engineering relationship genuinely warrants it.

The goal is learning to analyze evidence, not admiring how obediently synthetic data follow a textbook.

---

# Progressive Data Complexity

Data complexity should increase throughout the curriculum.

## Stage 1 - Conceptual Data

Typical characteristics:

* 10 to 100 observations
* One or several variables
* Mostly clean
* Easy to inspect manually
* Designed for conceptual understanding

Primary purpose:

> Learn what the method does.

---

## Stage 2 - Applied Data

Typical characteristics:

* Hundreds to several thousand observations
* Multiple variables
* Minor missing data
* Natural variability
* Some irrelevant information

Primary purpose:

> Apply the method independently.

---

## Stage 3 - Operational Data

Typical characteristics:

* Thousands to hundreds of thousands of observations
* Multiple files
* Time-dependent data
* Missing observations
* Operational events
* Equipment metadata
* Environmental data
* Data-quality problems

Primary purpose:

> Perform realistic engineering analysis.

---

## Stage 4 - Integrated Engineering Data

Typical characteristics:

* Multiple data systems
* Large historical records
* Asset data
* Operational data
* Maintenance records
* Failure histories
* Environmental conditions
* Changing system behavior
* Conflicting evidence

Primary purpose:

> Design and defend an analytical approach.

---

# Relationship to Curriculum Progression

A general progression may resemble:

| Lesson | Topic                       | Typical Data Complexity                                           |
| ------ | --------------------------- | ----------------------------------------------------------------- |
| 00     | Histograms, PDF & CDF       | Small observational dataset                                       |
| 01     | Descriptive Statistics      | Small-to-moderate engineering dataset                             |
| 02     | Probability Distributions   | Historical engineering observations                               |
| 03     | Return Periods & Exceedance | Multi-year environmental record                                   |
| 04     | Confidence Intervals        | Moderate sample-based dataset                                     |
| 05     | Hypothesis Testing          | Multiple groups or operating periods                              |
| 06     | Linear Regression           | Multivariable engineering dataset                                 |
| 07     | Time Series Analysis        | Large operational time series                                     |
| 08     | Monte Carlo Simulation      | Multiple uncertain engineering inputs                             |
| 09     | Bayesian Statistics         | Historical evidence plus new observations                         |
| 10     | Markov Chains               | Asset condition and transition histories                          |
| 11     | Reliability Engineering     | Integrated runtime, failure, maintenance, and operational records |

This progression is a guideline.

The engineering problem determines the final dataset design.

---

# Lesson Data vs. Applied Exercise Data

Lessons and applied exercises have different data requirements.

## Lesson Data

Lesson datasets should optimize:

* Conceptual clarity
* Visualization
* Manual verification
* Understanding

They may therefore be intentionally simplified.

## Applied Exercise Data

Exercise datasets should optimize:

* Realism
* Investigation
* Independent reasoning
* Data handling
* Engineering interpretation

They may therefore be substantially larger and more complex.

For example:

```text
Lesson:
20 annual observations

Applied Exercise:
30 years of daily or hourly observations
```

or:

```text
Lesson:
30 pump cycles

Applied Exercise:
Two years of 5-minute SCADA data
```

The difference is intentional.

---

# Dataset Documentation Strategy

Student-facing dataset documentation should provide enough information to begin an engineering analysis.

It may include:

* Engineering system description
* File inventory
* Observation period
* General collection frequency
* Field definitions
* Units
* Source type
* Whether the dataset is simulated

It should not automatically provide:

* Important findings
* Anomaly locations
* Failure dates
* Best statistical model
* Relevant variables
* Expected correlations
* Intended engineering conclusion

Documentation should explain the data.

It should not perform the investigation.

---

# Dataset README

Significant applied datasets should generally include a short `README.md`.

For example:

```text
data/raw/wastewater/07_pump_station_analysis/
├── README.md
├── station_metadata.csv
├── scada_history.csv
├── alarm_history.csv
├── maintenance_history.csv
└── rainfall_history.csv
```

The README may identify:

* Dataset purpose
* Simulated or external status
* Files supplied
* Observation period
* General source description
* Important unit conventions

It should not contain analytical findings.

---

# File Formats

CSV should be the default tabular format unless another format better represents the source data.

Potential formats include:

* CSV
* JSON
* Parquet
* Excel
* GeoJSON
* Plain text

CSV is preferred for many instructional datasets because it is:

* Human-readable
* Portable
* Easy to inspect
* Well supported by Python

Parquet may be appropriate for very large datasets where CSV becomes unnecessarily inefficient.

The file format should reflect the exercise and source context rather than a desire to use more technology.

---

# Version Control Strategy

Small and moderate datasets may be committed directly to the repository.

Very large datasets require consideration of:

* Repository size
* Git performance
* Reproducibility
* Whether regeneration is practical

When a large simulated dataset can be reproduced easily, the project may store:

```text
Generation Script
        +
Configuration
        +
Seed
```

rather than committing an unnecessarily large generated file.

However, this should be balanced against the learning objective that the student receives a dataset rather than generating it themselves.

The preferred approach for exercises is to provide the actual student-facing data whenever repository size remains reasonable.

---

# Data Processing Reproducibility

Data transformations should be reproducible.

For example:

```text
data/raw/wastewater/scada_history.csv
                ↓
scripts/process_data/wastewater/prepare_scada.py
                ↓
data/processed/wastewater/scada_clean.csv
```

Where processing is itself part of an exercise, the student should write the transformation rather than receive a completed processing script.

---

# No Manual Raw Data Correction

Raw data should not be manually edited merely to make analysis easier.

If a value is determined to be invalid, the analysis should record that decision through code.

For example:

```python
valid = df["flow_gpm"] >= 0
clean_df = df.loc[valid].copy()
```

This preserves:

* Original evidence
* Analytical decisions
* Reproducibility

The reasoning behind exclusion or correction should be documented when material to the analysis.

---

# Data Reduction

Large datasets may need to be:

* Filtered
* Aggregated
* Resampled
* Summarized

Data reduction should be an analytical decision.

For example, converting 5-minute SCADA data to daily averages may discard information about:

* Peak conditions
* Pump cycling
* Short-duration alarms
* Operational variability

The student should understand what information is lost when data are aggregated.

---

# Avoiding Data Leakage

Later lessons may involve prediction, forecasting, or model evaluation.

The project should introduce data leakage explicitly when relevant.

Examples include:

* Using future observations to predict the past
* Calculating normalization parameters from the complete dataset
* Randomly splitting time-series data
* Using information that would not have been available at the decision time

Although machine learning is not part of the initial core curriculum, leakage can occur in statistical and time-series analysis as well.

The general principle is:

> **An analysis should use only the information that would reasonably have been available at the time represented by the decision.**

---

# Engineering Context Over Statistical Convenience

Dataset design should prioritize engineering plausibility over statistical convenience.

If the engineering system produces:

* Skewed data
* Autocorrelation
* Unequal variance
* Missing observations
* Seasonal patterns
* Confounding variables

the dataset should not automatically be modified to remove those characteristics merely because a simpler statistical method would be easier.

Instead, the lesson should help determine whether the proposed method remains appropriate.

---

# Dataset Acceptance Criteria

Before a dataset becomes part of an applied exercise, it should satisfy the following questions.

## Engineering

* Does the dataset represent a plausible infrastructure system?
* Are the variables physically meaningful?
* Are units reasonable?
* Are relationships among variables defensible?

## Statistical

* Does the dataset support the intended analytical concept?
* Is variability realistic?
* Are statistical characteristics excessively artificial?

## Operational

* Does the dataset reflect plausible operating behavior?
* Are events and equipment states internally consistent?

## Educational

* Does the dataset create useful analytical decisions?
* Is complexity appropriate for the student's current stage?
* Does the dataset require reasoning rather than merely calculation?

## Reproducibility

* Can the source or generation process be identified?
* Can simulated data be regenerated?
* Can processing steps be reproduced?

## Exercise Integrity

* Does student-facing documentation avoid revealing the intended findings?
* Can the student investigate the problem independently?

A dataset should not be accepted merely because it contains enough rows and looks complicated.

---

# Data Strategy Principle

Before creating or selecting a dataset, ask:

> **What would an engineer reasonably receive if this were a real assignment?**

Then ask:

> **What relationships, limitations, and imperfections would reasonably exist in those data?**

Then:

> **What information should the student have to begin the analysis, and what should they have to discover?**

The objective is not to create unnecessarily difficult datasets.

The objective is to create **credible engineering evidence that must be investigated**.

As the curriculum progresses, the student should increasingly move from:

> **Here are the numbers needed for the calculation.**

to:

> **Here are the files the utility provided. Determine what they tell us.**

That progression is central to Applied Infrastructure Analytics.

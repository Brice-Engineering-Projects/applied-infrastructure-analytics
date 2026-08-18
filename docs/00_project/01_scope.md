# Applied Infrastructure Analytics - Project Scope

## Purpose

This document defines the scope of the **Applied Infrastructure Analytics** project.

The project is intentionally focused on developing practical statistical, computational, and analytical skills through realistic infrastructure engineering problems.

Because infrastructure analytics overlaps with many technical disciplines, the project could easily expand into hydraulic modeling, asset management software, machine learning, GIS, optimization, financial modeling, and numerous other subjects.

Those topics may be valuable, but uncontrolled expansion would weaken the primary learning objective.

The purpose of this scope is therefore to establish:

* What the project is intended to teach
* What types of engineering problems belong in the project
* What technical methods are appropriate
* What level of data realism is expected
* How simulated engineering datasets should be constructed
* What is outside the primary scope
* How advanced topics should be introduced
* How the project should remain focused as it grows

---

# Primary Scope

Applied Infrastructure Analytics focuses on the intersection of:

```text
Infrastructure Engineering
          +
Statistics & Probability
          +
Data Analysis
          +
Python
          +
Engineering Judgment
```

The project teaches analytical methods by applying them to realistic civil and environmental engineering datasets.

The primary emphasis is not on performing calculations.

The emphasis is on understanding:

> **How can data and quantitative methods improve infrastructure engineering decisions?**

The project should increasingly resemble the complete analytical process an engineer or infrastructure analyst would follow after receiving data from a utility, municipality, consultant, or other infrastructure organization.

This includes:

1. Understanding the engineering problem
2. Receiving and inspecting the available data
3. Determining what the data represent
4. Evaluating data quality
5. Identifying relevant variables
6. Selecting appropriate analytical methods
7. Performing the analysis
8. Validating results
9. Interpreting the evidence
10. Identifying limitations
11. Determining what additional information may be required
12. Developing a defensible engineering conclusion or recommendation

---

# Core Technical Scope

The project includes the following primary analytical areas.

## Descriptive Statistics

Topics include:

* Mean
* Median
* Mode
* Range
* Variance
* Standard deviation
* Coefficient of variation
* Percentiles
* Quartiles
* Interquartile range
* Outlier identification
* Distribution shape
* Exploratory data analysis

These concepts establish the foundation for understanding engineering datasets before more advanced analysis is performed.

---

## Probability

Topics include:

* Random variables
* Probability concepts
* Histograms
* Probability Density Functions
* Cumulative Distribution Functions
* Exceedance probability
* Probability distributions
* Distribution parameters
* Distribution fitting
* Extreme events
* Return periods

Probability is used to describe uncertainty in natural, operational, and infrastructure systems.

---

## Statistical Inference

Topics include:

* Samples and populations
* Sampling variability
* Confidence intervals
* Hypothesis testing
* Statistical significance
* Practical significance
* Comparison of groups
* Uncertainty in estimated parameters

The emphasis should remain on understanding what conclusions can reasonably be drawn from limited observations.

---

## Regression

Topics include:

* Correlation
* Simple linear regression
* Regression coefficients
* Residuals
* Goodness of fit
* Model assumptions
* Prediction
* Prediction uncertainty
* Engineering interpretation

Regression should be treated as a tool for investigating relationships rather than simply generating equations.

---

## Time Series Analysis

Topics include:

* Time-indexed engineering data
* Trend
* Seasonality
* Cyclic behavior
* Rolling statistics
* Autocorrelation
* Lagged relationships
* Stationarity
* Forecasting fundamentals
* Time-dependent uncertainty

Example applications may include:

* Water demand
* Wastewater flow
* Groundwater elevation
* Pump runtime
* Pressure
* Rainfall
* Sensor measurements

---

## Monte Carlo Simulation

Topics include:

* Random sampling
* Input distributions
* Parameter uncertainty
* Simulation design
* Repeated trials
* Output distributions
* Probability of failure
* Sensitivity to assumptions
* Engineering risk

Monte Carlo simulation should emphasize the propagation of uncertainty through engineering calculations and decision models.

---

## Bayesian Statistics

Topics include:

* Prior information
* Likelihood
* Posterior probability
* Bayesian updating
* Sequential evidence
* Uncertainty
* Engineering interpretation

Applications should focus on situations where infrastructure decisions are updated as new information becomes available.

Examples may include:

* Inspection results
* Failure observations
* Condition assessments
* Sensor information
* Reliability estimates

---

## Markov Chains

Topics include:

* States
* Transition probabilities
* Transition matrices
* State evolution
* Long-term behavior
* Condition deterioration
* Intervention effects

Primary applications should focus on infrastructure condition and deterioration modeling.

---

## Reliability Engineering

Topics include:

* Probability of failure
* Probability of survival
* Reliability functions
* Failure rates
* Component reliability
* System reliability
* Series systems
* Parallel systems
* Redundancy
* Availability
* Risk and consequence

Reliability engineering serves as an opportunity to integrate concepts developed throughout earlier lessons.

---

# Engineering Application Scope

The project should use engineering scenarios that are realistic enough to require interpretation but sufficiently bounded to maintain focus on the analytical concept being taught.

Primary application areas include the following.

## Water Distribution Systems

Potential applications include:

* Daily water demand
* Peak demand
* Pressure
* Tank levels
* Pump operation
* Pump reliability
* Water production
* Flow measurements
* Main failures
* Service interruptions

---

## Wastewater Collection Systems

Potential applications include:

* Wastewater flow
* Wet-weather flow
* Inflow and infiltration
* Pump station runtime
* Pump starts
* Wet-well levels
* Force-main performance
* Pump failures
* Overflow risk

---

## Hydrology and Water Resources

Potential applications include:

* Rainfall
* Streamflow
* Annual peak flow
* Flood frequency
* Exceedance probability
* Return periods
* Groundwater elevation
* Drought conditions
* Watershed observations

Hydrologic exercises should emphasize statistical concepts rather than becoming complete hydrologic or hydraulic design exercises.

---

## Infrastructure Asset Management

Potential applications include:

* Asset age
* Asset condition
* Failure history
* Failure frequency
* Probability of failure
* Inspection data
* Deterioration
* Remaining service life
* Intervention timing
* Risk

Asset-management problems provide an important application area for Bayesian methods, Markov chains, reliability analysis, and statistical modeling.

---

## Construction and Capital Costs

Potential applications include:

* Historical bid prices
* Unit costs
* Construction cost variability
* Engineer's estimates
* Bid distributions
* Cost escalation
* Project cost uncertainty
* Contingency analysis

Cost analysis may be used where it supports the statistical learning objective.

The project should not become a general financial-modeling curriculum.

---

## Infrastructure Operations

Potential applications include:

* Runtime
* Flow
* Pressure
* Temperature
* Vibration
* Energy consumption
* Equipment starts
* Alarm frequency
* Maintenance events
* Operational performance

Operational datasets are particularly useful for time series, reliability, and anomaly-related exercises.

---

## Sensor and Monitoring Data

Potential applications include:

* Pressure sensors
* Flow meters
* Level sensors
* Vibration measurements
* Temperature measurements
* Equipment monitoring
* Environmental sensors

Sensor datasets may contain realistic data-quality issues such as:

* Missing observations
* Duplicate timestamps
* Measurement drift
* Sensor failure
* Implausible readings
* Irregular sampling

These characteristics should be introduced when they support the learning objective.

---

# Python Scope

Python is the primary computational language for the project.

The project should emphasize practical analytical programming rather than software development for its own sake.

Core technologies may include:

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Statsmodels
* Pytest

Additional libraries may be introduced when justified by a lesson.

---

# Python Skills Within Scope

Lessons and exercises may include:

* Reading CSV and similar data files
* Inspecting DataFrames
* Cleaning data
* Filtering data
* Joining related datasets
* Grouping and aggregation
* Statistical calculations
* Numerical calculations
* Data visualization
* Time-series manipulation
* Random sampling
* Simulation
* Reusable functions
* Type hints
* Input validation
* Unit testing
* Basic analytical package organization

Python should support the analytical objective rather than become the objective itself.

---

# Reusable Analytical Tools

Where appropriate, lessons should produce small reusable analytical components.

Examples include:

```python
def descriptive_statistics(...):
    ...
```

```python
def empirical_cdf(...):
    ...
```

```python
def exceedance_probability(...):
    ...
```

```python
def confidence_interval(...):
    ...
```

```python
def reliability(...):
    ...
```

These components should reinforce understanding of the underlying analytical method.

They should not simply duplicate library functionality without an educational purpose.

---

# Testing Scope

Reusable analytical functions should be tested when practical.

Testing may include:

* Known-value tests
* Boundary conditions
* Missing-data behavior
* Invalid inputs
* Empty datasets
* Numerical tolerances
* Comparison against trusted library calculations

Testing is included because analytical software should be verified rather than trusted simply because it executes successfully.

The objective is not to develop an exhaustive enterprise testing framework.

---

# Data Scope

Data are a central component of Applied Infrastructure Analytics.

The project should not treat datasets merely as convenient collections of numbers required to demonstrate statistical formulas.

Datasets should represent the type, structure, scale, relationships, and imperfections that an engineer or infrastructure analyst might reasonably encounter in practice.

The project may use:

* Small educational datasets
* Realistic simulated engineering datasets
* Public engineering datasets
* Historical public data
* Generated operational datasets
* Multiple related datasets representing a single infrastructure system

Datasets should be selected or generated based on their ability to support both the statistical learning objective and the engineering analytical process.

---

# Data Directory Structure

The primary data directory should follow the general structure:

```text
data/
├── raw/
│   ├── hydrology/
│   ├── water_distribution/
│   ├── wastewater/
│   ├── groundwater/
│   └── reliability/
│
├── processed/
│
└── external/
```

Additional domain directories may be added when justified by the curriculum.

Examples may include:

```text
construction_costs/
asset_management/
operations/
```

The directory structure should remain organized around the engineering source or purpose of the data rather than individual Python scripts.

---

# Raw Data

The `data/raw/` directory represents data as originally received for an exercise or analytical assignment.

Raw data should be treated as **immutable**.

Student analysis should not overwrite, manually correct, or otherwise modify the original raw files.

For example:

```text
data/raw/wastewater/
├── scada_history.csv
├── pump_events.csv
├── maintenance_history.csv
├── rainfall.csv
└── station_metadata.csv
```

may collectively represent the information supplied by a utility for a pump-station analysis.

Any cleaning, transformation, aggregation, feature engineering, or combination of these files should produce new data rather than altering the originals.

This reflects good analytical and data-engineering practice and preserves the ability to reproduce the analysis from the original source information.

---

# Processed Data

The `data/processed/` directory contains data created through analytical processing.

Examples include:

* Cleaned datasets
* Joined datasets
* Aggregated time series
* Calculated features
* Standardized categories
* Validated observations
* Analysis-ready tables

Processed data should be reproducible from the raw or external data through Python code whenever practical.

Manual modification of processed data should be avoided.

The preferred workflow is:

```text
Raw Data
    ↓
Inspection
    ↓
Cleaning / Validation
    ↓
Transformation
    ↓
Processed Data
    ↓
Statistical Analysis
```

---

# External Data

The `data/external/` directory contains data obtained from external public or authoritative sources.

Potential sources may include:

* USGS
* NOAA
* EPA
* State environmental agencies
* Transportation agencies
* Municipal open-data portals
* Public utilities
* Other authoritative infrastructure sources

External data should retain sufficient provenance to identify:

* Source
* Original dataset
* Date obtained
* Relevant units
* Relevant documentation
* Any transformations subsequently performed

External data should not be included merely because it is available.

It should support a defined engineering or learning objective.

---

# Simulated Operational Data

Realistic simulated data are explicitly within the primary scope of the project.

For many lessons, simulated operational datasets should be preferred over artificially simplified statistical datasets.

The objective is not merely to generate plausible individual numbers.

The objective is to simulate the behavior of an **engineering system and its associated data collection process**.

For example, simulated wastewater flow should not normally be created as an arbitrary sequence of independent random values.

A more realistic simulation may incorporate:

```text
Base Sanitary Flow
        +
Diurnal Demand Pattern
        +
Weekday / Weekend Effects
        +
Seasonal Variation
        +
Rainfall-Dependent I&I
        +
Random Operational Variability
        +
Exceptional Events
        +
Measurement Error
```

Related variables should respond consistently with the simulated system.

For a pump station:

```text
Influent Flow
      ↓
Wet-Well Level
      ↓
Pump Control Logic
      ↓
Pump Starts / Stops
      ↓
Discharge Flow
      ↓
Runtime / Electrical Measurements
```

Rainfall may influence influent flow.

Influent flow may influence wet-well level.

Wet-well level may control pump operation.

Pump availability may affect station response.

Maintenance events may change equipment availability.

Sensor problems may affect recorded measurements without changing the underlying physical system.

The result should behave like data produced by a plausible infrastructure system rather than a collection of unrelated random variables.

---

# Complete Operational Context

When an exercise represents data received from a utility or infrastructure owner, the dataset should generally include the broader information that would reasonably accompany the engineering problem.

For example, a pump analysis should not automatically provide only:

```text
Peak Flow = 4,323 gpm
Pump Capacity = 4,619 gpm
```

Instead, the student may receive:

* SCADA history
* Flow measurements
* Wet-well levels
* Pump status
* Pump runtime
* Pump starts
* Discharge pressure
* Electrical measurements
* Alarm history
* Maintenance records
* Equipment metadata
* Rainfall information
* Operating setpoints

Not every variable needs to be relevant to the statistical method being studied.

Determining which information is relevant is itself part of the analytical exercise.

---

# Multi-File Engineering Datasets

Real engineering analyses frequently require information from multiple sources.

Exercises may therefore provide multiple related files rather than one perfectly prepared analysis table.

For example:

```text
data/raw/wastewater/lesson_07/
├── station_metadata.csv
├── scada_history.csv
├── alarm_history.csv
├── maintenance_history.csv
└── rainfall_history.csv
```

The student may need to determine:

* How files relate to one another
* Which identifiers should be used
* Whether time periods overlap
* Whether units are compatible
* Which datasets are relevant
* Whether records can be reliably joined
* Whether gaps or inconsistencies exist

This is considered part of infrastructure analytics rather than unnecessary preprocessing.

---

# Dataset Scale

Dataset size should reflect the nature, frequency, duration, and scale of the engineering process being represented.

Datasets should not be artificially limited to a convenient number such as 1,000 records when a realistic engineering dataset would contain substantially more observations.

For example:

Two years of 15-minute SCADA observations contain approximately:

$$
2 \times 365 \times 24 \times 4 = 70,080
$$

records for a continuously monitored variable.

Two years of 5-minute observations contain approximately:

$$
2 \times 365 \times 24 \times 12 = 210,240
$$

records.

A water-main asset registry may contain thousands or tens of thousands of pipe segments.

A maintenance-management export may contain tens of thousands of work orders.

A historical construction-cost dataset may contain thousands of bid items.

Conversely, a 30-year annual peak-flow record legitimately contains only 30 observations.

The objective is therefore **not to create large datasets for their own sake**.

The objective is:

> **Dataset size should be appropriate for the engineering system and data collection process being represented.**

---

# Relevant and Irrelevant Variables

Real engineering datasets are rarely delivered with only the variables required for a specific statistical calculation.

Applied exercises should increasingly reflect this reality.

A dataset may contain variables that:

* Are essential to the analysis
* Provide useful context
* Become relevant only after investigation
* Are unrelated to the immediate engineering question

The student should not always be told which variables are important.

Part of the analytical process is determining:

> **What information do I actually need to answer the engineering question?**

This requirement should become increasingly important in intermediate and advanced lessons.

---

# Data Quality

Data quality is considered part of the analytical process.

Exercises may intentionally contain realistic problems such as:

* Missing observations
* Duplicate records
* Duplicate timestamps
* Incorrect data types
* Irregular timestamps
* Sensor dropouts
* Sensor drift
* Implausible measurements
* Negative values where physically impossible
* Inconsistent categories
* Changed equipment identifiers
* Changed operating setpoints
* Maintenance outages
* Equipment replacements
* Incomplete records
* Extreme events
* Unit inconsistencies
* Time-zone or daylight-saving-time issues

These issues should not be inserted merely to make exercises difficult.

Each should represent a plausible problem encountered in engineering data.

Students should not necessarily be told in advance which problems are present.

Data inspection is part of the assignment.

---

# Legitimate Extremes vs. Bad Data

Simulated datasets should distinguish between unusual observations caused by data problems and unusual observations caused by legitimate engineering events.

For example, an extreme flow observation could represent:

* A major rainfall event
* Fire flow
* Industrial demand
* Operational changes
* Equipment failure
* A sensor malfunction
* A data-entry problem

Statistical unusualness alone should not reveal which explanation is correct.

Where appropriate, related datasets should provide evidence that allows the student to investigate the event.

This reinforces the principle that:

> **Statistical identification should lead to investigation, not automatic deletion.**

---

# Progressive Data Complexity

Dataset complexity should increase as analytical capability develops.

## Foundational Lessons

Early lessons may use datasets that are:

* Relatively small
* Mostly clean
* Easy to inspect
* Easy to visualize
* Manually verifiable

The purpose is to understand foundational concepts without unnecessary complexity.

---

## Intermediate Lessons

Intermediate datasets should increasingly include:

* Hundreds or thousands of observations
* Multiple variables
* Multiple related files
* Time-dependent measurements
* Categorical information
* Natural variability
* Extreme observations
* Missing information
* Minor data-quality problems

Students should increasingly be responsible for determining which information is relevant.

---

## Advanced Lessons

Advanced exercises should increasingly resemble actual engineering analytical assignments.

Datasets may include:

* Tens or hundreds of thousands of observations
* Multiple data sources
* Operational histories
* Maintenance histories
* Failure events
* Asset metadata
* Environmental conditions
* Sensor measurements
* Changing operating conditions
* Missing records
* Conflicting evidence
* Irrelevant variables
* Significant data-quality issues

The student should increasingly receive the engineering problem and available information without being given a prescribed analytical sequence.

---

# Simulation Reproducibility

Simulated datasets should be reproducible.

Generation methods should use documented assumptions and controlled random seeds where appropriate.

The simulation process should internally define items such as:

* Physical or operational assumptions
* Statistical distributions
* Relationships between variables
* Operating rules
* Event probabilities
* Data collection frequency
* Known anomalies
* Missing-data mechanisms
* Random seed
* Units
* Physical constraints

However, information that would reveal the intended analytical findings should not automatically be included with the student-facing exercise.

For example, documentation accompanying an exercise should not reveal:

> Pump 2 begins losing efficiency on Day 317.

if identifying that change is part of the assignment.

Reproducibility should preserve the ability to regenerate the dataset without converting the simulation specification into an answer key.

---

# Dataset Documentation

Each dataset should provide enough documentation to understand what was supposedly supplied without revealing the analytical solution.

Appropriate documentation may include:

* Dataset title
* Engineering system represented
* Whether the data are simulated or external
* Observation period
* File descriptions
* Column definitions
* Units where they would reasonably be known
* Data source or simulated source
* General collection frequency

Documentation should not automatically identify:

* Which variables are analytically important
* Which observations are anomalous
* Which data-quality problems were intentionally inserted
* Which statistical model fits the data
* What engineering conclusion should be reached

Those determinations belong to the analysis.

---

# End-to-End Analytical Scope

Applied exercises should increasingly represent the complete analytical workflow rather than isolated statistical calculations.

A typical advanced exercise may begin with:

> The utility has provided the following historical data exports and requested an evaluation of system performance.

The student may then need to perform:

```text
Receive Data
     ↓
Inventory Files
     ↓
Understand Variables
     ↓
Check Units
     ↓
Inspect Data Quality
     ↓
Identify Relevant Information
     ↓
Clean / Transform
     ↓
Explore
     ↓
Select Analytical Methods
     ↓
Perform Statistical Analysis
     ↓
Validate Results
     ↓
Interpret Findings
     ↓
Evaluate Limitations
     ↓
Develop Engineering Recommendation
```

The statistical technique being studied remains important, but it should increasingly exist within this larger analytical process.

---

# Engineering Decision Scope

The project includes engineering interpretation and decision support.

Exercises may ask the student to:

* Interpret analytical results
* Identify potential concerns
* Compare alternatives
* Quantify uncertainty
* Evaluate evidence
* Identify additional data requirements
* Recommend further investigation
* Determine whether available evidence supports action

However, statistical analysis should not be presented as a substitute for complete engineering design.

---

# Engineering Calculations

Basic engineering calculations are within scope when they provide context for the statistical analysis.

Examples include:

* Capacity thresholds
* Flow balances
* Failure ratios
* Pump availability
* Asset age
* Unit cost
* Risk calculations

Complex engineering models should generally remain outside the project unless the model itself is necessary to demonstrate the analytical concept.

For example:

> Using a known pump capacity within a Monte Carlo simulation is within scope.

Developing a complete hydraulic pump-station design model as part of the statistics lesson is not.

---

# Topics Outside the Primary Scope

The following areas are generally outside the primary scope of this project.

## Complete Engineering Design

The project is not intended to teach complete design procedures for:

* Water distribution systems
* Wastewater collection systems
* Pump stations
* Treatment facilities
* Stormwater systems
* Culverts
* Pipelines

Engineering design concepts may provide context, but the analytical method remains the primary learning objective.

---

## Full Hydraulic or Hydrologic Modeling

Software and methods such as:

* EPANET
* SWMM
* HEC-RAS
* HEC-HMS

may be referenced or eventually integrated into advanced exercises.

However, teaching these modeling systems is not a primary objective of Applied Infrastructure Analytics.

---

## Geographic Information Systems

GIS may eventually provide spatial context for infrastructure datasets.

However, the project is not intended to teach:

* ArcGIS
* QGIS
* Spatial database administration
* Cartographic design
* Complete geospatial workflows

Spatial analysis may be introduced later if directly relevant to an analytical lesson.

---

## Machine Learning

Machine learning is not part of the initial core curriculum.

Concepts such as:

* Classification
* Random forests
* Gradient boosting
* Neural networks
* Clustering

may eventually be added as an extension to the project.

However, statistical foundations should be established before machine-learning methods are introduced.

Machine learning should not be used where a simpler statistical method adequately answers the engineering question.

---

## Artificial Intelligence and Large Language Models

LLMs and generative AI are not primary analytical tools within the core curriculum.

They may assist with learning, documentation, or future extensions, but they should not replace:

* Statistical reasoning
* Data inspection
* Analytical programming
* Engineering interpretation
* Independent problem solving

The project should remain useful without requiring an LLM to perform the analysis.

---

## Application Development

The project is not primarily intended to teach:

* FastAPI
* Django
* Flask
* React
* Authentication
* Cloud deployment
* Microservices
* Production database architecture

Analytical methods developed in this project may eventually be incorporated into separate applications.

Application development should remain separate from the core statistical curriculum.

---

## General Finance

Construction costs, lifecycle costs, uncertainty, and capital planning may appear when they support infrastructure analytics.

The project is not intended to become a curriculum in:

* Corporate finance
* Securities
* Portfolio theory
* Options
* Derivatives
* Quantitative trading

Those subjects belong in dedicated financial-analysis projects.

---

## Optimization

Optimization may eventually complement capital planning and infrastructure decision analysis.

Examples could include:

* Project selection under budget constraints
* Resource allocation
* Maintenance scheduling
* Risk-reduction optimization

However, optimization is not part of the initial core learning roadmap.

It should be treated as a future extension after the statistical foundation has been established.

---

# Scope Boundary Between Related Projects

Applied Infrastructure Analytics may produce methods that are useful in other engineering projects.

For example:

```text
Applied Infrastructure Analytics
            ↓
Probability of Failure
            ↓
Infrastructure Lifecycle & Capital Planning
            ↓
Risk-Based Capital Prioritization
```

The statistical method may be learned and developed here.

The larger asset-management or capital-planning system belongs in the project focused on that problem.

Similarly:

```text
Applied Infrastructure Analytics
            ↓
Monte Carlo Simulation
            ↓
Pump Capacity Uncertainty
            ↓
Hydraulic / Infrastructure Application
```

The simulation methodology belongs here.

A complete production engineering application built around that methodology may belong elsewhere.

This separation helps keep Applied Infrastructure Analytics focused on developing transferable analytical skills.

---

# Exercise Scope

Applied exercises should reinforce analytical methods, Python skills, data investigation, and engineering reasoning.

Exercises should increasingly require some combination of:

* Understanding the engineering assignment
* Inventorying available data
* Data inspection
* Data-quality assessment
* Determining relevant variables
* Cleaning and transforming data
* Joining related datasets
* Statistical analysis
* Visualization
* Python implementation
* Validation
* Interpretation
* Identification of limitations
* Engineering recommendations

As the curriculum progresses, exercises should provide progressively less instruction regarding which analytical method to use.

The objective is to transition from:

> **Perform this calculation.**

toward:

> **Evaluate this engineering problem using the available data.**

---

# No-Solution Policy

Completed exercise solutions are outside the scope of the repository.

The repository should not contain:

* Completed solution notebooks
* Answer keys
* Final analytical reports for exercises
* Hidden solution directories
* Precomputed outputs that reveal the expected answer
* Dataset documentation that exposes intentionally embedded findings

This restriction is intentional.

The project is designed for active learning.

When assistance is needed, conceptual explanations, documentation, debugging support, and incremental hints are preferable to complete solutions.

---

# Cumulative Application

Later lessons should reuse earlier analytical concepts whenever appropriate.

For example:

```text
Reliability Analysis
        ↑
Markov Chains
        ↑
Bayesian Updating
        ↑
Monte Carlo Simulation
        ↑
Time Series
        ↑
Regression
        ↑
Statistical Inference
        ↑
Probability
        ↑
Descriptive Statistics
        ↑
Exploratory Data Analysis
```

This does not imply that every advanced exercise must use every previous method.

Instead, students should increasingly determine which tools are relevant to the engineering question.

Data complexity should grow alongside analytical complexity so that later exercises require both stronger statistical methods and stronger data-analysis judgment.

---

# Future Expansion

Potential future extensions may include:

* Multivariate regression
* Generalized linear models
* Survival analysis
* Advanced reliability modeling
* Spatial statistics
* Machine learning
* Anomaly detection
* Optimization
* Decision analysis
* Risk-based capital planning
* Digital-twin analytics

Future topics should be added only when they build naturally upon the statistical and engineering foundations established by the core curriculum.

---

# Scope Control Principle

Before adding a new topic, dataset, technology, or exercise, ask:

> **Does this addition improve the student's ability to use realistic infrastructure data and quantitative methods to understand an engineering problem and make a better engineering decision?**

If the answer is yes, the addition may belong in Applied Infrastructure Analytics.

If the primary purpose is instead to teach another engineering discipline, software framework, or unrelated analytical field, it probably belongs in another project.

The objective is not to make Applied Infrastructure Analytics cover everything.

The objective is to make it **exceptionally good at connecting statistics, Python, realistic infrastructure data, and engineering judgment from initial data receipt through engineering interpretation and decision-making**.

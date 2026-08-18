# Project Structure

## Purpose

This document defines the canonical repository structure for **Applied Infrastructure Analytics**.

The repository is organized to support four related objectives:

1. Structured statistical and analytical lessons
2. Applied infrastructure engineering exercises
3. Realistic engineering datasets
4. Reusable Python analytical tools

The structure intentionally separates:

* Curriculum documentation
* Raw engineering data
* Processed analytical data
* Student analysis
* Reusable source code
* Dataset-generation and processing utilities
* Automated tests

This separation allows the project to progress from small educational examples toward realistic, end-to-end infrastructure analytics assignments without losing reproducibility or organization.

---

# Repository Structure

```text
applied_infrastructure_analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
│   ├── diagrams/
│   ├── figures/
│   └── images/
│
├── data/
│   ├── raw/
│   │   ├── hydrology/
│   │   ├── water_distribution/
│   │   ├── wastewater/
│   │   ├── groundwater/
│   │   ├── reliability/
│   │   ├── asset_management/
│   │   ├── construction_costs/
│   │   └── operations/
│   │
│   ├── processed/
│   │   ├── hydrology/
│   │   ├── water_distribution/
│   │   ├── wastewater/
│   │   ├── groundwater/
│   │   ├── reliability/
│   │   ├── asset_management/
│   │   ├── construction_costs/
│   │   └── operations/
│   │
│   └── external/
│       ├── hydrology/
│       ├── water_distribution/
│       ├── wastewater/
│       ├── groundwater/
│       ├── reliability/
│       ├── asset_management/
│       ├── construction_costs/
│       └── operations/
│
├── docs/
│   ├── 00_project/
│   │   ├── 00_overview.md
│   │   ├── 01_scope.md
│   │   └── 02_learning_philosophy.md
│   │
│   ├── 01_architecture/
│   │   ├── 00_structure.md
│   │   ├── 01_lesson_architecture.md
│   │   └── 02_data_strategy.md
│   │
│   ├── 02_standards/
│   │   ├── 00_lesson_template.md
│   │   ├── 01_exercise_template.md
│   │   └── 02_python_standards.md
│   │
│   ├── 03_lessons/
│   │   ├── 00_histograms_pdf_cdf.md
│   │   ├── 01_descriptive_statistics.md
│   │   ├── 02_probability_distributions.md
│   │   ├── 03_return_periods_exceedance.md
│   │   ├── 04_confidence_intervals.md
│   │   ├── 05_hypothesis_testing.md
│   │   ├── 06_linear_regression.md
│   │   ├── 07_time_series_analysis.md
│   │   ├── 08_monte_carlo_simulation.md
│   │   ├── 09_bayesian_statistics.md
│   │   ├── 10_markov_chains.md
│   │   └── 11_reliability_engineering.md
│   │
│   ├── 04_exercises/
│   │   ├── 00a_histograms_pdf_cdf/
│   │   │   └── exercise.md
│   │   ├── 01a_descriptive_statistics/
│   │   │   └── exercise.md
│   │   ├── 02a_probability_distributions/
│   │   │   └── exercise.md
│   │   ├── 03a_return_periods_exceedance/
│   │   │   └── exercise.md
│   │   ├── 04a_confidence_intervals/
│   │   │   └── exercise.md
│   │   ├── 05a_hypothesis_testing/
│   │   │   └── exercise.md
│   │   ├── 06a_linear_regression/
│   │   │   └── exercise.md
│   │   ├── 07a_time_series_analysis/
│   │   │   └── exercise.md
│   │   ├── 08a_monte_carlo_simulation/
│   │   │   └── exercise.md
│   │   ├── 09a_bayesian_statistics/
│   │   │   └── exercise.md
│   │   ├── 10a_markov_chains/
│   │   │   └── exercise.md
│   │   └── 11a_reliability_engineering/
│   │       └── exercise.md
│   │
│   └── 05_references/
│       ├── formulas.md
│       ├── probability_reference.md
│       ├── statistical_reference.md
│       └── bibliography.md
│
├── notebooks/
│   ├── 00_histograms_pdf_cdf/
│   │   └── workspace.ipynb
│   ├── 00a_histograms_pdf_cdf/
│   │   └── workspace.ipynb
│   ├── 01_descriptive_statistics/
│   │   └── workspace.ipynb
│   ├── 01a_descriptive_statistics/
│   │   └── workspace.ipynb
│   └── ...
│
├── scripts/
│   ├── generate_data/
│   │   ├── hydrology/
│   │   ├── water_distribution/
│   │   ├── wastewater/
│   │   ├── groundwater/
│   │   ├── reliability/
│   │   ├── asset_management/
│   │   ├── construction_costs/
│   │   └── operations/
│   │
│   └── process_data/
│       ├── hydrology/
│       ├── water_distribution/
│       ├── wastewater/
│       ├── groundwater/
│       ├── reliability/
│       ├── asset_management/
│       ├── construction_costs/
│       └── operations/
│
├── src/
│   └── applied_infrastructure_analytics/
│       ├── __init__.py
│       │
│       ├── io/
│       │   ├── __init__.py
│       │   ├── loaders.py
│       │   └── validation.py
│       │
│       ├── descriptive/
│       │   ├── __init__.py
│       │   ├── central_tendency.py
│       │   ├── dispersion.py
│       │   └── percentiles.py
│       │
│       ├── probability/
│       │   ├── __init__.py
│       │   ├── histogram.py
│       │   ├── pdf.py
│       │   ├── cdf.py
│       │   ├── distributions.py
│       │   └── return_periods.py
│       │
│       ├── inference/
│       │   ├── __init__.py
│       │   ├── confidence_intervals.py
│       │   ├── hypothesis_tests.py
│       │   └── bayesian.py
│       │
│       ├── regression/
│       │   ├── __init__.py
│       │   ├── linear.py
│       │   └── diagnostics.py
│       │
│       ├── timeseries/
│       │   ├── __init__.py
│       │   ├── autocorrelation.py
│       │   ├── decomposition.py
│       │   └── forecasting.py
│       │
│       ├── simulation/
│       │   ├── __init__.py
│       │   └── monte_carlo.py
│       │
│       ├── reliability/
│       │   ├── __init__.py
│       │   ├── markov.py
│       │   ├── reliability.py
│       │   └── risk.py
│       │
│       ├── visualization/
│       │   ├── __init__.py
│       │   ├── histogram.py
│       │   ├── boxplot.py
│       │   ├── scatter.py
│       │   ├── time_series.py
│       │   └── probability.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── constants.py
│           ├── formatting.py
│           └── helpers.py
│
├── tests/
│   ├── io/
│   ├── descriptive/
│   ├── probability/
│   ├── inference/
│   ├── regression/
│   ├── timeseries/
│   ├── simulation/
│   ├── reliability/
│   └── visualization/
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
└── LICENSE
```

---

# Directory Responsibilities

## `assets/`

Contains static visual resources used throughout the project.

```text
assets/
├── diagrams/
├── figures/
└── images/
```

Examples include:

* Conceptual engineering diagrams
* Statistical diagrams
* Architecture diagrams
* Figures used in documentation
* Supporting images

Generated analytical plots should generally be reproducible from code rather than manually stored unless they are specifically required by project documentation.

---

# `data/`

The `data/` directory contains the engineering datasets used throughout the curriculum.

Data are separated into three primary categories:

```text
data/
├── raw/
├── processed/
└── external/
```

---

## `data/raw/`

Contains simulated or otherwise supplied engineering data in the form in which the student receives it.

Raw data should be treated as immutable.

Examples include:

```text
data/raw/wastewater/
data/raw/water_distribution/
data/raw/hydrology/
```

A realistic assignment may contain several related files.

For example:

```text
data/raw/wastewater/07_pump_station_analysis/
├── station_metadata.csv
├── scada_history.csv
├── alarm_history.csv
├── maintenance_history.csv
└── rainfall_history.csv
```

The student may need to determine how the files relate and which information is relevant.

Raw data should not be modified during analysis.

---

## `data/processed/`

Contains datasets generated from raw or external data through reproducible analytical processing.

Examples include:

* Cleaned observations
* Joined datasets
* Aggregated time series
* Calculated variables
* Analysis-ready datasets

A typical workflow is:

```text
data/raw/
    ↓
Python Processing
    ↓
data/processed/
    ↓
Statistical Analysis
```

Processed files should be reproducible whenever practical.

---

## `data/external/`

Contains data obtained from external authoritative sources.

Potential sources include:

* USGS
* NOAA
* EPA
* State agencies
* Municipal open-data portals
* Public utilities
* Transportation agencies

External data should retain sufficient source and provenance information to identify its origin.

---

# Data Domains

Data are organized primarily by engineering domain.

Initial domains include:

### `hydrology/`

Rainfall, streamflow, flood records, watershed observations, and related hydrologic data.

### `water_distribution/`

Water demand, pressure, flow, tank levels, production, pump operation, and water-main information.

### `wastewater/`

Wastewater flow, pump-station operation, wet-well levels, alarms, I&I, maintenance, and related collection-system information.

### `groundwater/`

Groundwater elevations, monitoring-well measurements, aquifer observations, and related environmental information.

### `reliability/`

Equipment failures, availability, downtime, repair history, and reliability-related observations.

### `asset_management/`

Asset inventories, condition assessments, inspection records, failure histories, deterioration observations, and intervention records.

### `construction_costs/`

Historical bid prices, unit costs, project costs, estimates, escalation data, and related cost information.

### `operations/`

General infrastructure operational datasets that do not belong naturally within another domain.

Additional domains may be added when justified by the curriculum.

---

# `docs/`

The `docs/` directory defines the curriculum, architecture, standards, lessons, exercises, and supporting references.

```text
docs/
├── 00_project/
├── 01_architecture/
├── 02_standards/
├── 03_lessons/
├── 04_exercises/
└── 05_references/
```

---

## `docs/00_project/`

Defines the purpose and boundaries of Applied Infrastructure Analytics.

```text
00_project/
├── 00_overview.md
├── 01_scope.md
└── 02_learning_philosophy.md
```

### `00_overview.md`

Defines the overall project purpose, objectives, curriculum, and intended outcomes.

### `01_scope.md`

Defines what belongs within the project and establishes boundaries between Applied Infrastructure Analytics and related engineering or software-development projects.

### `02_learning_philosophy.md`

Defines how concepts should be taught and practiced, including:

* Concepts before formulas
* Engineering problems before abstract exercises
* Realistic data
* Independent problem solving
* Cumulative learning
* Progressive assistance
* Engineering judgment
* No completed solutions

---

# `docs/01_architecture/`

Defines how the project is organized.

```text
01_architecture/
├── 00_structure.md
├── 01_lesson_architecture.md
└── 02_data_strategy.md
```

### `00_structure.md`

Defines the canonical repository structure.

### `01_lesson_architecture.md`

Defines how lessons and applied exercises should progress from engineering motivation through analytical interpretation and engineering decision-making.

### `02_data_strategy.md`

Defines:

* Data realism
* Simulated operational data
* Dataset scale
* Raw-data immutability
* Processed-data generation
* External-data provenance
* Multi-file datasets
* Data-quality characteristics
* Progressive complexity
* Simulation reproducibility

---

# `docs/02_standards/`

Contains reusable development and curriculum standards.

```text
02_standards/
├── 00_lesson_template.md
├── 01_exercise_template.md
└── 02_python_standards.md
```

These documents establish consistent expectations for future project development.

---

# `docs/03_lessons/`

Contains the instructional material for each statistical topic.

Lessons focus on **learning the analytical method**.

The general progression is:

```text
Engineering Motivation
        ↓
Conceptual Understanding
        ↓
Mathematical Foundation
        ↓
Worked Example
        ↓
Python Implementation
        ↓
Interpretation
        ↓
Engineering Judgment
```

Lessons may use small or simplified datasets when this improves conceptual understanding.

---

# `docs/04_exercises/`

Contains the applied engineering assignments associated with each lesson.

Exercises focus on **using the analytical method independently**.

Each exercise set should generally progress through:

```text
Guided Practice
      ↓
Applied Practice
      ↓
Engineering Analysis
      ↓
Challenge Problem
```

Later exercises should increasingly integrate concepts from previous lessons.

Exercise directories do **not** contain completed solutions.

---

# Lesson and Exercise Numbering

Lessons use sequential numbers:

```text
00_histograms_pdf_cdf
01_descriptive_statistics
02_probability_distributions
...
```

Applied exercises use the corresponding lesson number followed by `a`:

```text
00a_histograms_pdf_cdf
01a_descriptive_statistics
02a_probability_distributions
...
```

This creates a consistent relationship:

```text
00  → Learn Histograms, PDF & CDF
00a → Apply Histograms, PDF & CDF

01  → Learn Descriptive Statistics
01a → Apply Descriptive Statistics
```

---

# `docs/05_references/`

Contains supporting reference material.

Examples include:

* Formula references
* Probability references
* Statistical terminology
* Bibliography and source material

Reference documentation should support the curriculum without becoming an answer key for applied exercises.

---

# `notebooks/`

Contains optional interactive analytical workspaces.

Notebooks are intended for:

* Exploration
* Visualization
* Experimental analysis
* Manual investigation
* Learning

They should not contain completed exercise solutions distributed with the repository.

The default notebook name is:

```text
workspace.ipynb
```

rather than:

```text
solution.ipynb
```

For substantial reusable analytical logic, implementation should eventually move into `src/`.

---

# `scripts/`

Contains executable utilities supporting data generation and processing.

```text
scripts/
├── generate_data/
└── process_data/
```

---

## `scripts/generate_data/`

Contains reproducible generators for simulated engineering datasets.

Generation scripts may model:

* Infrastructure system behavior
* Environmental variability
* Operational logic
* Equipment performance
* Failure events
* Sensor measurements
* Missing data
* Data-quality problems

Generation scripts should use controlled random seeds where appropriate.

The generated dataset belongs in `data/raw/`.

The generator itself belongs here.

Student-facing exercise documentation should not reveal intentionally embedded findings merely because they are represented in the generation logic.

---

## `scripts/process_data/`

Contains reproducible transformations used to convert raw or external information into processed datasets.

Examples include:

* Cleaning
* Standardization
* Joining
* Aggregation
* Feature calculation
* Time-series alignment

Where processing is part of the student's exercise, the student may create the appropriate script during the assignment rather than receiving a completed version.

---

# `src/`

Contains reusable analytical Python functionality developed throughout the curriculum.

```text
src/applied_infrastructure_analytics/
```

Source code should contain functionality that has value beyond one specific exercise.

Examples include:

* Descriptive-statistics utilities
* Empirical CDF functions
* Distribution analysis
* Confidence intervals
* Regression diagnostics
* Time-series utilities
* Monte Carlo tools
* Reliability calculations
* Visualization helpers

Exercise-specific exploratory code does not automatically belong in `src/`.

---

# Analytical Package Organization

The analytical package is organized primarily by statistical or computational method:

```text
descriptive/
probability/
inference/
regression/
timeseries/
simulation/
reliability/
visualization/
```

This allows analytical tools to remain reusable across engineering domains.

For example, an empirical CDF function may be used for:

* Streamflow
* Water demand
* Construction costs
* Pump runtime
* Asset failures

The function therefore belongs under:

```text
probability/
```

rather than under a specific engineering domain.

---

# `tests/`

Contains automated tests for reusable analytical code.

The test structure should generally mirror `src/`.

```text
src/.../probability/
        ↕
tests/probability/
```

Tests may include:

* Known-value calculations
* Boundary conditions
* Invalid inputs
* Missing-data behavior
* Numerical tolerance checks
* Comparisons with trusted statistical libraries

The purpose is to verify analytical code rather than assume that successful execution implies correctness.

---

# No Solutions Directory

The repository intentionally contains **no solution directory**.

The following should not be added:

```text
solutions/
answer_keys/
completed_exercises/
```

Applied exercises are intended to require independent analysis.

When assistance is necessary, conceptual guidance, hints, debugging assistance, or simplified demonstrations should be used rather than completed solutions.

---

# Separation of Responsibilities

The overall repository flow can be summarized as:

```text
docs/03_lessons/
        │
        │ teaches concepts
        ↓
docs/04_exercises/
        │
        │ defines engineering assignments
        ↓
data/raw/
        │
        │ provides received engineering data
        ↓
notebooks/ + scripts/
        │
        │ exploration and processing
        ↓
data/processed/
        │
        │ analysis-ready information
        ↓
src/
        │
        │ reusable analytical methods
        ↓
tests/
        │
        │ verification
        ↓
Engineering Interpretation
        ↓
Engineering Decision
```

Not every exercise must use every directory.

Early lessons may be considerably simpler.

The structure exists to support increasing analytical complexity without requiring artificial complexity where it provides no educational value.

---

# Structural Principle

The repository structure should reinforce the analytical workflow rather than merely organize files.

As the curriculum advances, the student should increasingly experience the project as:

> **An engineering problem accompanied by realistic data that must be understood, investigated, analyzed, validated, and interpreted.**

The structure should support that progression while preserving:

* Original data
* Reproducibility
* Separation of concerns
* Reusable analytical code
* Independent learning
* Clear engineering context

The repository is therefore organized not simply as a statistics curriculum, but as a progressively more realistic **infrastructure analytics working environment**.

# Python Standards

## Purpose

This document defines the Python development standards for **Applied Infrastructure Analytics**.

The project serves two related purposes:

1. Teaching applied statistics and infrastructure analytics
2. Developing reusable, reliable analytical Python code

The coding standards should support both objectives.

Code should be:

* Readable
* Reproducible
* Testable
* Numerically reliable
* Appropriately typed
* Easy to validate
* Understandable to another engineer

The objective is not to maximize abstraction or software complexity.

The objective is:

> **Write analytical code that another engineer or developer can understand, reproduce, validate, and trust.**

---

# Core Principle

Python is an analytical tool within this project.

The analytical reasoning remains more important than the syntax.

A sophisticated implementation of an inappropriate statistical method is still a poor analysis.

The preferred order is:

```text
Engineering Question
        ↓
Analytical Approach
        ↓
Mathematical Understanding
        ↓
Python Implementation
        ↓
Validation
        ↓
Engineering Interpretation
```

Code supports the analysis.

It does not replace analytical reasoning.

---

# Python Version

The project targets:

```text
Python 3.12+
```

The Python version should be defined using:

```text
.python-version
```

and configured appropriately in:

```text
pyproject.toml
```

New code should use modern Python syntax supported by the project's minimum Python version.

---

# Package Management

The project uses **uv** for:

* Virtual environment management
* Dependency management
* Package installation
* Lockfile management
* Running project commands

Do not maintain parallel dependency workflows using:

* `pip`
* `pipenv`
* Poetry
* Conda

unless a specific external requirement makes one necessary.

The primary project files are:

```text
pyproject.toml
uv.lock
```

---

# Environment Setup

A typical project setup should use:

```bash
uv sync
```

Commands should generally be executed through the project environment using:

```bash
uv run <command>
```

Examples:

```bash
uv run python script.py
uv run pytest
uv run ruff check .
uv run mypy src
```

This reduces differences between local development environments.

---

# Dependency Philosophy

Dependencies should be added because they solve a meaningful project requirement.

Avoid introducing libraries merely to simplify a trivial operation or demonstrate another tool.

The core analytical stack may include:

* Pandas
* NumPy
* Matplotlib
* SciPy
* Statsmodels
* Pytest
* Ruff
* mypy

Additional libraries should be introduced when required by the curriculum or engineering problem.

---

# Dependency Categories

Dependencies should be separated appropriately within `pyproject.toml`.

Runtime analytical dependencies may include:

```text
pandas
numpy
matplotlib
scipy
statsmodels
```

Development dependencies may include:

```text
pytest
ruff
mypy
```

Notebook-related dependencies may be grouped separately if appropriate.

The project should avoid accumulating unused packages.

---

# General Coding Style

Python code should follow modern Python conventions and PEP 8 principles.

Code should prioritize:

1. Correctness
2. Clarity
3. Reproducibility
4. Maintainability
5. Performance

Performance optimization should occur when the dataset or computation requires it.

Do not sacrifice clarity for insignificant performance improvements.

---

# Naming Conventions

Use descriptive names.

Preferred:

```python
daily_flow_mgd
pump_runtime_hours
annual_peak_flow_cfs
failure_probability
wet_well_level_ft
```

Avoid:

```python
x
x1
data2
temp
stuff
val
```

Short mathematical names may be appropriate when implementing a mathematical definition and their meaning is obvious from context.

For example:

```python
n = len(values)
```

is reasonable.

---

# Engineering Units in Variable Names

Where practical, include engineering units in names for physical quantities.

Examples:

```python
flow_gpm
flow_mgd
pressure_psi
head_ft
diameter_in
length_ft
rainfall_in
runtime_hr
velocity_fps
cost_usd
```

This is especially important when multiple unit systems may appear.

Prefer:

```python
flow_gpm
```

over:

```python
flow
```

when the unit is not otherwise unmistakable.

---

# DataFrame Column Naming

DataFrame columns should generally use:

```text
snake_case
```

Examples:

```text
timestamp
station_id
wet_well_level_ft
discharge_flow_gpm
pump_1_status
pump_1_current_amp
```

Avoid unnecessary spaces, punctuation, and inconsistent capitalization in processed datasets.

Raw datasets should not be manually renamed merely to conform to this convention.

Column standardization should occur through reproducible processing code.

---

# Functions

Functions should perform a clear analytical task.

Prefer:

```python
def calculate_exceedance_probability(
    values: np.ndarray,
    threshold: float,
) -> float:
    ...
```

over large functions that:

* Load data
* Clean data
* Calculate statistics
* Create plots
* Write files
* Print conclusions

all at once.

Functions should generally have one primary responsibility.

---

# Function Naming

Function names should describe actions.

Examples:

```python
calculate_mean()
calculate_exceedance_probability()
build_empirical_cdf()
validate_flow_data()
calculate_daily_pump_starts()
```

Avoid vague names such as:

```python
process()
run()
do_analysis()
handle_data()
```

unless the context makes the responsibility unmistakable.

---

# Type Hints

Reusable Python code under:

```text
src/
```

should use type hints.

Example:

```python
def calculate_range(values: np.ndarray) -> float:
    return float(np.max(values) - np.min(values))
```

Another example:

```python
def calculate_exceedance_probability(
    values: np.ndarray,
    threshold: float,
) -> float:
    exceedances = np.sum(values > threshold)

    return float(exceedances / len(values))
```

Type hints improve:

* Readability
* IDE support
* Static analysis
* Refactoring
* Interface clarity

---

# Exploratory Code and Type Hints

Not every line in a notebook requires explicit typing.

For example:

```python
df = pd.read_csv(data_path)
```

is sufficient during exploratory analysis.

The distinction is:

```text
Exploratory Analysis
        ↓
Useful Reusable Logic
        ↓
src/
        ↓
Type Hints + Tests
```

Do not burden exploratory work with unnecessary software ceremony.

Once analytical logic becomes reusable project functionality, stronger standards apply.

---

# Return Types

Reusable functions should normally declare return types.

Example:

```python
def calculate_mean(values: np.ndarray) -> float:
    return float(np.mean(values))
```

For multiple related outputs, consider:

* `dataclass`
* Typed dictionaries
* Pandas DataFrames
* Named structures

depending on the analytical purpose.

Avoid returning unexplained tuples when the values are not immediately obvious.

---

# Dataclasses

Use dataclasses when several related values represent a meaningful analytical result or engineering object.

Example:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class DescriptiveStatistics:
    observations: int
    mean: float
    median: float
    minimum: float
    maximum: float
    range: float
    variance: float
    standard_deviation: float
```

This is preferable to:

```python
return n, mean, median, minimum, maximum, range_, variance, std_dev
```

which forces the caller to remember what eight positional values supposedly mean. Humans already have enough opportunities to rearrange numbers incorrectly.

---

# Docstrings

Public reusable functions should include concise docstrings.

Example:

```python
def calculate_exceedance_probability(
    values: np.ndarray,
    threshold: float,
) -> float:
    """Calculate the empirical probability of exceeding a threshold."""
```

More complex functions should document:

* Purpose
* Parameters
* Return value
* Important assumptions
* Relevant units
* Exceptions where necessary

Do not write enormous docstrings that merely translate every line of code into English.

---

# Comments

Comments should explain:

* Why something is being done
* Important assumptions
* Non-obvious analytical decisions
* Engineering reasoning

Good:

```python
# Remove observations recorded while the flow meter was flagged
# as out of service in the maintenance history.
```

Less useful:

```python
# Filter dataframe.
```

Avoid comments that simply narrate Python syntax.

---

# Paths

Do not scatter hard-coded absolute paths throughout the project.

Avoid:

```python
df = pd.read_csv(
    "C:/Users/brice/Documents/projects/data/pump_data.csv"
)
```

Prefer project-relative paths.

For example:

```python
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
```

For notebooks, use a consistent project-root strategy appropriate to the notebook environment.

---

# Use `pathlib`

Use `pathlib.Path` for filesystem paths.

Preferred:

```python
from pathlib import Path


data_path = Path("data/raw/wastewater/scada_history.csv")

df = pd.read_csv(data_path)
```

Avoid manual string concatenation:

```python
path = "data/" + folder + "/" + filename
```

---

# Raw Data Immutability

Python code should never overwrite raw source data during normal analysis.

Avoid:

```python
df.to_csv("data/raw/wastewater/scada_history.csv")
```

Processed output should be written under:

```text
data/processed/
```

The expected workflow is:

```text
Raw Data
    ↓
Python
    ↓
Processed Data
```

not:

```text
Raw Data
    ↓
Python
    ↓
Modified Raw Data
```

---

# Data Loading

Data-loading logic should be explicit and understandable.

Example:

```python
from pathlib import Path

import pandas as pd


data_path = Path(
    "data/raw/wastewater/07_pump_station_analysis/scada_history.csv"
)

df = pd.read_csv(
    data_path,
    parse_dates=["timestamp"],
)
```

Where important, specify:

* Date columns
* Data types
* Missing-value conventions
* Units
* Encodings

Do not rely blindly on automatic type inference for critical engineering fields.

---

# Data Validation

Important assumptions about input data should be checked.

Examples include:

```python
required_columns = {
    "timestamp",
    "station_id",
    "discharge_flow_gpm",
}

missing_columns = required_columns - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Missing required columns: {sorted(missing_columns)}"
    )
```

Other validation may include:

* Expected units
* Unique identifiers
* Timestamp ordering
* Valid ranges
* Missing values
* Duplicate records

Validation should reflect meaningful analytical requirements.

---

# Missing Data

Missing values should be handled deliberately.

Do not automatically use:

```python
df.dropna()
```

without understanding what is being removed.

Before treating missing data, investigate:

* Which variables are missing?
* How frequently?
* During what periods?
* Is missingness related to system operation?
* Could missingness itself be informative?
* How will removal or imputation affect the analysis?

The treatment should follow from the analytical context.

---

# Outliers

Do not automatically remove statistical outliers.

Avoid workflows such as:

```python
df = df[
    np.abs(stats.zscore(df["flow_gpm"])) < 3
]
```

unless there is a defensible reason for that treatment.

An extreme observation may represent:

* A legitimate event
* A system failure
* An unusual operating condition
* A measurement error

Statistical unusualness does not establish invalidity.

---

# Avoid Row-Wise Loops When Vectorization Is Clear

For tabular numerical operations, prefer Pandas or NumPy vectorized operations when they remain readable.

Prefer:

```python
df["flow_difference_gpm"] = (
    df["influent_flow_gpm"] - df["discharge_flow_gpm"]
)
```

over:

```python
for index, row in df.iterrows():
    df.loc[index, "flow_difference_gpm"] = (
        row["influent_flow_gpm"] - row["discharge_flow_gpm"]
    )
```

This becomes increasingly important as operational datasets grow to hundreds of thousands of observations.

---

# Vectorization Is Not a Religion

Do not replace clear Python with unreadable vectorized expressions merely to eliminate a small loop.

Clarity remains important.

For event-based algorithms such as:

* Pump starts
* State transitions
* Failure sequences
* Markov transitions

a loop may sometimes express the logic more clearly.

Choose the implementation that is both correct and understandable.

---

# NumPy

Use NumPy primarily for:

* Numerical arrays
* Vectorized calculations
* Random number generation
* Mathematical operations
* Simulation

Prefer the modern random generator API:

```python
rng = np.random.default_rng(42)
```

rather than relying on global random state.

---

# Randomness and Reproducibility

Any lesson or script involving random simulation should use reproducible random-number generation unless randomness across executions is explicitly required.

Example:

```python
rng = np.random.default_rng(42)

samples = rng.normal(
    loc=100.0,
    scale=15.0,
    size=10_000,
)
```

The seed should be deliberate.

Simulation results should not mysteriously change every time the analysis is executed.

---

# Pandas

Use Pandas primarily for:

* Tabular engineering data
* Data cleaning
* Joining datasets
* Aggregation
* Grouping
* Time-indexed data
* Data export

Prefer readable method chains or intermediate variables over deeply nested expressions.

Good:

```python
daily_flow = (
    df.set_index("timestamp")["flow_gpm"]
    .resample("D")
    .mean()
)
```

If an expression becomes difficult to interpret, break it into meaningful intermediate steps.

---

# Method Chaining

Method chaining is encouraged when the sequence remains easy to understand.

Example:

```python
daily_summary = (
    df.dropna(subset=["flow_gpm"])
    .set_index("timestamp")
    .resample("D")["flow_gpm"]
    .agg(["mean", "max"])
)
```

Avoid chains so long that debugging requires archaeological equipment.

Intermediate variables are perfectly acceptable.

---

# Copying DataFrames

Be deliberate when creating modified subsets.

Prefer:

```python
valid_data = df.loc[df["flow_gpm"] >= 0].copy()
```

when the subset will subsequently be modified.

This helps avoid ambiguous view-versus-copy behavior.

---

# Time-Series Data

Timestamps should be parsed as datetime values rather than retained as arbitrary strings.

Example:

```python
df["timestamp"] = pd.to_datetime(df["timestamp"])
```

Time-series analyses should consider:

* Sorting
* Duplicate timestamps
* Missing intervals
* Observation frequency
* Time zones
* Daylight-saving-time behavior
* Resampling effects

Never assume timestamps are clean merely because they successfully parse.

---

# Chronological Sorting

Time-series data should normally be explicitly sorted before temporal analysis.

```python
df = df.sort_values("timestamp")
```

This is especially important before calculating:

* Differences
* Rolling statistics
* State transitions
* Lagged variables
* Runtime changes

---

# Rolling Calculations

Rolling calculations must avoid using future information when the analysis represents a historical decision process.

For example:

```python
df["rolling_mean"] = (
    df["flow_gpm"]
    .rolling(window=24)
    .mean()
)
```

The analyst should understand which observations are included in the window.

Centered windows should be used only when future observations are legitimately available for the analysis.

---

# Statistical Libraries

Use established statistical libraries for standard analytical methods.

Preferred libraries include:

```text
NumPy
Pandas
SciPy
Statsmodels
```

Do not manually recreate complex statistical algorithms for production analytical use when a mature, validated implementation already exists.

Manual implementations are appropriate when their purpose is educational.

---

# Educational vs. Analytical Implementation

A lesson may implement a statistic manually to expose its mechanics.

For example:

```python
mean = sum(values) / len(values)
```

The reusable analytical implementation may use:

```python
mean = np.mean(values)
```

These serve different purposes.

The first teaches.

The second performs reliable analysis.

---

# Sample vs. Population Statistics

Be explicit about definitions when library defaults differ.

For example, Pandas sample standard deviation uses:

```python
df["flow_gpm"].std(ddof=1)
```

while population standard deviation uses:

```python
df["flow_gpm"].std(ddof=0)
```

The choice should follow the statistical problem.

Do not change `ddof` merely to force agreement with an expected number.

---

# Floating-Point Comparisons

Do not generally compare floating-point analytical results using exact equality.

Avoid:

```python
assert result == 3.14159
```

Prefer:

```python
import pytest


assert result == pytest.approx(3.14159)
```

or appropriate NumPy comparison functions.

Tolerance should reflect the numerical problem.

---

# Numerical Precision

Retain sufficient numerical precision during calculations.

Round primarily for:

* Tables
* Reports
* Figures
* Human-readable output

Avoid repeated rounding during intermediate calculations unless the engineering method specifically requires it.

Prefer:

```python
result = calculation()
display_result = round(result, 2)
```

rather than rounding every intermediate value.

---

# Engineering Units and Calculations

Unit conversions should be explicit.

Example:

```python
GALLONS_PER_MILLION_GALLONS = 1_000_000.0

flow_gpd = flow_mgd * GALLONS_PER_MILLION_GALLONS
```

For important or repeated conversions, use clearly named constants or helper functions.

Avoid unexplained values such as:

```python
result = flow * 448.831
```

when the meaning of the conversion factor is not obvious.

---

# Constants

Meaningful constants should be named.

Example:

```python
MINUTES_PER_DAY = 1_440
GALLONS_PER_MILLION_GALLONS = 1_000_000
```

Engineering-specific constants may be stored under:

```text
src/applied_infrastructure_analytics/utils/constants.py
```

when they are used throughout the project.

Do not centralize constants that are meaningful only within one small analysis.

---

# Matplotlib

Matplotlib is the default visualization library.

Example:

```python
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

ax.hist(df["flow_gpm"])
ax.set_xlabel("Flow (gpm)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Recorded Flow")

fig.tight_layout()
plt.show()
```

Prefer the object-oriented Matplotlib interface using:

```python
fig, ax = plt.subplots()
```

for reusable or moderately complex plots.

---

# Visualization Standards

Every analytical figure should generally include:

* Descriptive title
* Labeled axes
* Units
* Appropriate scale
* Legend when necessary

Plots should answer analytical questions.

Avoid unnecessary:

* 3D effects
* Decorative styling
* Excessive annotation
* Visual clutter

Infrastructure analytics has somehow survived without turning every histogram into a corporate dashboard.

---

# Plot Titles

Titles should describe what the figure represents.

Prefer:

```text
Daily Maximum Influent Flow
```

over:

```text
Flow Graph
```

For professional analytical outputs, context may be included:

```text
Pump Station 14 - Daily Maximum Influent Flow
January 2025 through December 2026
```

---

# Axis Labels

Axis labels should include units where applicable.

Preferred:

```python
ax.set_xlabel("Discharge Flow (gpm)")
ax.set_ylabel("Wet-Well Level (ft)")
```

Avoid:

```python
ax.set_xlabel("Flow")
ax.set_ylabel("Level")
```

when units matter.

---

# Figures and Reproducibility

Important figures should be reproducible from code.

If a figure is saved:

```python
fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
)
```

The source code used to generate it should remain part of the analysis.

---

# Notebook Standards

Notebooks are primarily analytical workspaces.

They may contain:

* Markdown explanation
* Exploratory code
* Calculations
* Visualizations
* Intermediate reasoning
* Engineering interpretation

A notebook should still follow a logical analytical sequence.

Preferred structure:

```text
Problem
    ↓
Data Loading
    ↓
Data Inspection
    ↓
Data Quality
    ↓
Processing
    ↓
Analysis
    ↓
Validation
    ↓
Interpretation
```

Avoid notebooks consisting of dozens of unrelated cells executed in an unknowable order.

---

# Notebook Execution Order

A completed notebook should execute successfully from beginning to end.

Do not rely on hidden state created by running cells out of order.

Before considering a notebook complete:

1. Restart the kernel.
2. Run all cells from the beginning.
3. Verify that the analysis completes successfully.

This catches an impressive number of problems created by the ancient human tradition of "it worked five minutes ago."

---

# Notebook vs. Source Code

Exploration belongs naturally in notebooks.

Reusable logic belongs under:

```text
src/
```

For example:

```python
# Initial notebook exploration
daily_starts = ...
```

may later become:

```python
def calculate_daily_pump_starts(
    status: pd.Series,
) -> pd.Series:
    ...
```

if the logic is useful beyond the current exercise.

Do not move every three-line calculation into the package.

---

# Scripts

Use scripts when the workflow is:

* Repeated
* Non-interactive
* Reproducible
* Suitable for batch execution

Examples include:

```text
scripts/generate_data/
scripts/process_data/
```

Scripts should normally define a `main()` function.

Example:

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

This keeps execution behavior explicit.

---

# Logging

For reusable scripts, prefer logging over excessive `print()` statements when operational information matters.

Example:

```python
import logging


logger = logging.getLogger(__name__)

logger.info("Loaded %d SCADA records", len(df))
```

Simple educational examples may use `print()` when logging would add unnecessary complexity.

---

# Exceptions

Raise meaningful exceptions when reusable functionality receives invalid input.

Example:

```python
if values.size == 0:
    raise ValueError("values must contain at least one observation")
```

Avoid silently returning misleading results.

Exceptions should help identify what condition violated the function's requirements.

---

# Assertions

Use `assert` primarily for internal invariants and tests.

Do not rely on assertions for normal input validation in reusable analytical functions because assertions can be disabled.

Use explicit exceptions for user-facing validation.

---

# Testing Standards

Reusable analytical code should be tested with Pytest.

Tests belong under:

```text
tests/
```

and should generally mirror the source structure.

Example:

```text
src/applied_infrastructure_analytics/probability/cdf.py

tests/probability/test_cdf.py
```

---

# Test Naming

Test names should describe expected behavior.

Preferred:

```python
def test_empirical_cdf_returns_expected_probabilities() -> None:
    ...
```

or:

```python
def test_calculate_range_rejects_empty_input() -> None:
    ...
```

Avoid:

```python
def test_1() -> None:
    ...
```

The test name should help explain what failed.

---

# Known-Value Tests

Analytical functions should use small known datasets where results can be independently verified.

Example:

```python
def test_calculate_range_known_values() -> None:
    values = np.array([2.0, 4.0, 8.0])

    result = calculate_range(values)

    assert result == pytest.approx(6.0)
```

Known-value tests are particularly important for statistical functionality.

---

# Edge Cases

Where relevant, tests should consider:

* Empty arrays
* Single observations
* Constant values
* Missing values
* Negative values
* Invalid thresholds
* Unsorted timestamps
* Duplicate timestamps
* Extreme values

Not every function must handle every possible edge case.

Expected behavior should be intentional.

---

# Analytical Validation vs. Software Testing

Automated testing and analytical validation are related but different.

## Software Test

Asks:

> Does the function behave as implemented?

## Analytical Validation

Asks:

> Is this the correct analytical method and does the result make sense?

A passing test suite does not establish that the engineering analysis is appropriate.

Both forms of validation matter.

---

# Ruff

Ruff should be used for linting and formatting according to project configuration.

Typical commands:

```bash
uv run ruff check .
uv run ruff format --check .
```

To format code:

```bash
uv run ruff format .
```

The project configuration in `pyproject.toml` should remain the source of truth for enabled rules.

---

# Static Type Checking

Reusable source code should be checked with mypy.

Typical command:

```bash
uv run mypy src
```

Type checking should improve code reliability without forcing unnecessary complexity into exploratory notebooks.

Strictness may increase as the analytical package matures.

---

# Test Execution

Run the complete test suite using:

```bash
uv run pytest
```

For additional detail:

```bash
uv run pytest -v
```

Tests should be runnable from the project root.

---

# Quality Check

Before committing substantial reusable code, the expected local quality checks are:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy src
uv run pytest
```

Where appropriate, these checks should also run through CI.

---

# Continuous Integration

The project CI workflow should verify, at minimum:

```text
Formatting
    ↓
Linting
    ↓
Type Checking
    ↓
Tests
```

CI exists to verify that repository standards remain satisfied across changes.

It should not replace local testing.

---

# Imports

Imports should be organized consistently.

Typical order:

```python
from pathlib import Path

import numpy as np
import pandas as pd

from applied_infrastructure_analytics.probability.cdf import (
    empirical_cdf,
)
```

Groups should generally follow:

1. Python standard library
2. Third-party packages
3. Local project imports

Ruff should enforce import organization where configured.

---

# Avoid Wildcard Imports

Do not use:

```python
from numpy import *
```

or:

```python
from module import *
```

Explicit imports make analytical dependencies clearer and reduce namespace ambiguity.

---

# Module Responsibilities

Modules under `src/` should correspond to coherent analytical responsibilities.

Example:

```text
probability/
├── histogram.py
├── pdf.py
├── cdf.py
├── distributions.py
└── return_periods.py
```

Avoid large generic modules such as:

```text
statistics.py
helpers.py
everything.py
```

when functionality has a clear analytical home.

---

# Utility Modules

The `utils/` package should be used sparingly.

A function should not be placed in `helpers.py` merely because its proper location requires thought.

Prefer domain-specific placement when possible.

For example:

```python
empirical_cdf()
```

belongs in:

```text
probability/cdf.py
```

not:

```text
utils/helpers.py
```

`utils/` should contain genuinely cross-cutting functionality.

---

# Avoid Premature Abstraction

Do not create:

* Abstract base classes
* Factory patterns
* Plugin systems
* Dependency injection frameworks
* Generic statistical engines

unless the project actually develops a requirement for them.

A function is often enough.

For example:

```python
def empirical_cdf(...):
    ...
```

does not require:

```text
AbstractDistributionAnalyzerFactory
```

Humanity will survive the absence.

---

# Performance

Correctness and clarity take priority during early implementation.

Performance optimization becomes appropriate when:

* Operational datasets become large
* Simulation counts become substantial
* Runtime interferes with analysis
* Memory consumption becomes problematic

Potential approaches include:

* NumPy vectorization
* Efficient Pandas operations
* Appropriate data types
* Chunked processing
* Parquet
* Algorithmic improvements

Measure performance before optimizing it.

---

# Memory Efficiency

Large operational datasets may require attention to memory usage.

Potential techniques include:

* Loading only required columns
* Explicit data types
* Categoricals
* Chunked reads
* Parquet
* Avoiding unnecessary DataFrame copies

Do not introduce these techniques prematurely into small educational datasets.

They should appear when the scale of the problem makes them meaningful.

---

# Reproducibility

An analysis should be reproducible from:

```text
Repository
    +
Environment Definition
    +
Raw Data
    +
Processing Code
    +
Analysis Code
```

Another user should not need:

* Undocumented manual spreadsheet edits
* Files stored outside the repository
* Hidden notebook state
* Unknown random seeds
* Unrecorded processing decisions

to reproduce the result.

---

# Analytical Traceability

Material transformations should be traceable.

For example:

```text
Raw SCADA
    ↓
Remove Invalid Sensor Period
    ↓
Resample to Hourly
    ↓
Calculate Daily Statistics
    ↓
Perform Analysis
```

Important decisions should be visible in code and, where appropriate, documented in the analysis.

---

# Avoid Hidden Analytical Decisions

Do not bury important engineering assumptions inside unexplained code.

Poor:

```python
df = df[(df["flow"] > 100) & (df["flow"] < 5000)]
```

Better:

```python
MIN_VALID_FLOW_GPM = 100.0
MAX_VALID_FLOW_GPM = 5_000.0

valid_flow = df["flow_gpm"].between(
    MIN_VALID_FLOW_GPM,
    MAX_VALID_FLOW_GPM,
)

validated_df = df.loc[valid_flow].copy()
```

Better still, document why those limits are appropriate.

---

# Output Formatting

Separate analytical precision from presentation precision.

For example:

```python
mean_flow_gpm = df["flow_gpm"].mean()

print(f"Mean Flow: {mean_flow_gpm:,.1f} gpm")
```

Do not modify the underlying value merely to make output attractive.

---

# Engineering Tables

Tables intended for engineering interpretation should include:

* Descriptive labels
* Units
* Appropriate precision
* Consistent formatting

For example:

| Statistic          | Flow (gpm) |
| ------------------ | ---------: |
| Mean               |      1,842 |
| Median             |      1,796 |
| Standard Deviation |        312 |
| Maximum            |      3,107 |

Avoid displaying meaningless machine precision such as:

```text
Mean Flow = 1842.1736482917 gpm
```

unless that precision is analytically relevant.

---

# Documentation and Code

Lesson documentation should explain:

* Why a method is used
* What the code is doing
* How the result should be interpreted

Code comments should not carry the entire instructional burden.

Likewise, documentation should not contain large unexplained code blocks.

The two should reinforce one another.

---

# Security and Sensitive Data

The project should not contain:

* Credentials
* API keys
* Passwords
* Private connection strings
* Proprietary client data
* Personally identifiable information
* Confidential utility information

Secrets should never be committed to Git.

Environment variables or appropriate secret-management mechanisms should be used when future exercises require authenticated external services.

---

# Real Utility Data

If actual utility data are ever introduced, verify that the data are authorized for use before committing them to the repository.

Potentially sensitive information should be removed or anonymized as required.

The use of realistic simulated data is preferred when actual operational records cannot appropriately be distributed.

---

# Definition of Reusable Code

Code belongs under `src/` when it satisfies one or more of the following:

* It will be used in multiple lessons.
* It will be used in multiple exercises.
* It represents a general analytical method.
* It benefits from independent testing.
* It forms part of the project's analytical toolkit.

Code does not automatically belong under `src/` because it exists.

---

# Definition of Exploratory Code

Exploratory code may remain in a notebook or exercise script when it is:

* Specific to one dataset
* Investigative
* Temporary
* Primarily visual
* Used to test an analytical idea

Exploratory work is a legitimate part of analysis.

It does not need to be disguised as production software.

---

# Code Review Questions

Before considering reusable analytical code complete, ask:

## Correctness

* Does the code calculate what I think it calculates?
* Have I independently validated the result?

## Engineering

* Are units explicit?
* Are physical assumptions reasonable?
* Are engineering limits documented?

## Statistics

* Is the statistical definition correct?
* Are library defaults understood?
* Are assumptions appropriate?

## Data

* Are missing values handled intentionally?
* Are outliers investigated rather than automatically removed?
* Is raw data preserved?

## Software

* Is the code readable?
* Are names descriptive?
* Are reusable functions typed?
* Are important functions tested?
* Does the quality check pass?

## Reproducibility

* Could another person reproduce the analysis from the repository?

---

# Standard Analytical Workflow

The preferred Python workflow for an applied exercise is:

```text
1. Define Engineering Question
            ↓
2. Locate Raw Data
            ↓
3. Load Data
            ↓
4. Inspect Structure
            ↓
5. Assess Data Quality
            ↓
6. Validate Engineering Plausibility
            ↓
7. Process Data
            ↓
8. Explore Data
            ↓
9. Perform Statistical Analysis
            ↓
10. Validate Results
            ↓
11. Visualize Important Findings
            ↓
12. Interpret Engineering Meaning
            ↓
13. Document Limitations
            ↓
14. Develop Recommendation
```

Python supports every stage after the engineering question is established.

It does not decide the engineering question.

---

# Final Standard

Code produced for Applied Infrastructure Analytics should be understandable enough that another technically competent engineer can determine:

> **What was calculated?**

> **How was it calculated?**

> **What assumptions were made?**

> **What data were used?**

> **Can the result be reproduced?**

> **Can the implementation be trusted?**

The project does not seek software complexity for its own sake.

The standard is simpler:

> **Use Python to make engineering analysis more transparent, reproducible, testable, and reliable.**

When software sophistication contributes to those objectives, use it.

When it does not, prefer the simpler implementation.

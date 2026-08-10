# Understanding PDFs and CDFs for Infrastructure Analytics

## Purpose

Probability distributions allow engineers to move beyond describing what has
already happened and begin reasoning about **uncertainty, likelihood, and risk**.

For an infrastructure engineer, the important question is usually not:

> What is the equation for this probability distribution?

The more useful questions are:

> What does this distribution tell me about the behavior of the system?

and:

> What is the probability that a value important to my design will be exceeded?

This lesson develops that intuition using annual peak streamflow.

---

# 1. Start With the Observations

Suppose we have twenty years of annual maximum streamflow measurements:

| Year | Peak Flow (cfs) |
|------|-----------------|
| 1 | ... |
| 2 | ... |
| ... | ... |
| 20 | ... |

These measurements are our **observed sample**.

They tell us what happened during those twenty years.

Before fitting probability models, we should first understand the data itself.

Typical descriptive statistics include:

- Mean
- Median
- Minimum
- Maximum
- Range
- Standard deviation

These statistics summarize the dataset, but they do not completely describe
how observations are distributed.

For that, we need to look at the **shape of the data**.

---

# 2. The Histogram: What Did We Observe?

A histogram groups observations into ranges called **bins**.

For example:

| Flow Range (cfs) | Observations |
|------------------|-------------:|
| 400–500 | 2 |
| 500–600 | 6 |
| 600–700 | 7 |
| 700–800 | 4 |
| 800–900 | 1 |

A histogram might therefore look approximately like:

              ███
          ███████
      ███████████
      ███████████████
  ███████████████████
  -----------------------
  400 500 600 700 800 900
           Flow (cfs)

The histogram answers:

> **Where did the observations occur?**

If most observations are between 550 and 700 cfs, the histogram will have
more area concentrated in that region.

If only a few observations occur above 800 cfs, the histogram will show a
thin upper tail.

### Engineering interpretation

The histogram gives us an initial picture of the behavior of annual peak flow.

We might observe:

- Typical annual peaks occur around 600–700 cfs.
- Very low flows are uncommon.
- Very high flows are uncommon.
- The distribution may be skewed toward larger flows.

But the histogram has an important limitation.

Its appearance depends partly on the bins we choose.

Changing the bin width can change the apparent shape of the histogram.

We therefore often want a smoother representation of the distribution.

That brings us to the PDF.

---

# 3. PDF: Where Is Probability Concentrated?

PDF stands for:

> **Probability Density Function**

The PDF describes **where probability is concentrated across possible values
of a continuous variable**.

For our problem, the variable is annual maximum streamflow.

Instead of thinking about individual histogram bins, imagine replacing the
blocky histogram with a smooth curve.

For example:

                  PDF
                   /\
                 /    \
               /        \
             /            \
___________/                \___________

400    500    600    700    800    900
             Flow (cfs)

The PDF answers a question similar to:

> **Which ranges of annual peak flow are relatively more likely than others?**

If the PDF is high around 650 cfs, values near 650 cfs occur in a region
where probability is highly concentrated.

If the PDF is very low around 900 cfs, values around 900 cfs are relatively
uncommon.

---

# 4. A Critical Distinction: Density Is NOT Probability

This is one of the most important ideas in this lesson.

Suppose the PDF at 700 cfs has a value of:

    f(700) = 0.003

That does **not** mean:

> There is a 0.3% probability of observing exactly 700 cfs.

For a continuous variable, the probability of observing one exact value is
effectively zero.

There are infinitely many possible values:

    699.999
    700.000
    700.001
    700.002
    ...

Instead, probability comes from an **interval**.

For example:

    P(650 < Q < 700)

The probability is represented by the **area underneath the PDF** between
650 and 700 cfs.

Conceptually:

                   PDF
                    /\
                  /████\
                /███████\
______________/██████████\____________
             650        700

             shaded area
              = probability

Therefore:

> **PDF height = probability density**

while

> **Area under the PDF = probability**

This distinction becomes extremely important when working with continuous
engineering variables.

---

# 5. Why Must the Total PDF Area Equal 1?

Some annual peak flow must occur.

Therefore, if we consider every possible annual peak flow, the total
probability must equal:

    1.0

or:

    100%

Mathematically, this means:

> **The total area underneath a valid PDF equals 1.**

Conceptually:

                   /\
                 /    \
               /        \
_____________/____________\_____________

      Entire area = 1.0 = 100%

The curve itself can have many different shapes.

The total area underneath it must still equal one.

---

# 6. Histogram vs PDF

The histogram and PDF are closely related, but they are not identical.

## Histogram

The histogram describes the **observed sample**.

It asks:

> Where did our twenty observations occur?

## PDF

The PDF represents a **continuous probability model** for the variable.

It asks:

> Where is probability concentrated across possible values?

This distinction becomes important when we begin fitting theoretical
distributions.

For example, hydrologic data might be modeled using:

- Normal distribution
- Lognormal distribution
- Gumbel distribution
- Log-Pearson Type III distribution

The observations remain the observations.

The fitted distribution is a **model of the process that produced them**.

Those are not the same thing.

---

# 7. Why Overlay a PDF on a Histogram?

This is what Part 3 of the assignment is asking you to explore.

You begin with the histogram:

    observed data

Then estimate or fit a probability density:

    probability model

Then plot them together.

Conceptually:

                   PDF
                    /\
            ███   /  \
        ████████/     \
    ███████████████    \
    █████████████████   \
    -------------------------
    400 500 600 700 800 900

This lets you visually compare:

> **Does the probability model resemble the observed distribution?**

If the curve follows the overall shape of the histogram reasonably well,
the model may provide a useful approximation.

If the curve poorly represents the histogram, the assumed distribution may
not be appropriate.

This idea becomes extremely important later in:

- Flood-frequency analysis
- Reliability analysis
- Monte Carlo simulation
- Asset failure modeling
- Demand forecasting
- Risk analysis

You should never select a probability distribution merely because a Python
library makes it convenient.

The distribution needs to make sense for the physical process and the data.

---

# 8. What Does the PDF Tell Us?

Suppose your PDF looks approximately like:

                     /\
                   /    \
                 /        \
               /            \
_____________/                \________
400    500    600    700    800    900

You might conclude:

> Probability is concentrated primarily around 600–700 cfs.

You might also observe:

> Annual peaks around 850–900 cfs appear much less common.

Notice the wording.

We are **not** saying:

> 650 cfs has a probability of X%.

Instead, we are describing where probability density is concentrated.

To answer questions such as:

> What percentage of annual peaks are below 700 cfs?

we need another tool.

That tool is the CDF.

---

# 9. CDF: How Much Probability Has Accumulated?

CDF stands for:

> **Cumulative Distribution Function**

The CDF answers:

> **What is the probability that the variable is less than or equal to a
> particular value?**

For streamflow:

    F(700) = P(Q ≤ 700)

Suppose:

    F(700) = 0.75

This means:

> There is an estimated 75% probability that annual maximum streamflow is
> 700 cfs or less.

Unlike the PDF, the vertical axis of the CDF **is directly interpretable as
probability**.

The CDF always increases from approximately:

    0 → 1

or:

    0% → 100%

Conceptually:

1.0 |                         ________
    |                    ____/
0.8 |                ____/
    |             __/
0.6 |          __/
    |        _/
0.4 |     __/
    |   _/
0.2 |__/
    |
0.0 +--------------------------------
    400 500 600 700 800 900
             Flow (cfs)

As flow increases, more probability accumulates.

---

# 10. PDF and CDF Are Two Views of the Same Distribution

This is the central concept.

The PDF shows:

> **Where probability is concentrated.**

The CDF shows:

> **How much probability has accumulated up to a particular value.**

Think of the PDF as terrain and the CDF as a running total of all the terrain
you have passed.

For example, suppose we want:

    P(Q ≤ 700)

Using the PDF, we would find the area underneath the curve from the lowest
possible flow through 700 cfs.

Using the CDF, that accumulation has already been calculated.

We simply evaluate:

    F(700)

Therefore:

    P(Q ≤ 700) = F(700)

---

# 11. Exceedance Probability

Infrastructure engineers are frequently more interested in the opposite
question:

> What is the probability that something exceeds a design threshold?

Suppose our culvert capacity is:

    Q_capacity = 700 cfs

The CDF gives:

    P(Q ≤ 700)

But failure or exceedance occurs when:

    Q > 700

Because all probabilities must add to one:

    P(Q > 700) = 1 - P(Q ≤ 700)

Therefore:

    P(Q > 700) = 1 - F(700)

Suppose:

    F(700) = 0.75

Then:

    P(Q > 700) = 1 - 0.75

    P(Q > 700) = 0.25

or:

    25%

This would mean:

> Based on the probability model, there is an estimated 25% annual
> probability that peak flow exceeds 700 cfs.

That statement is much more useful to an engineer than simply saying:

> The mean annual peak flow is 625 cfs.

The mean describes the center of the data.

The exceedance probability describes **risk relative to a design threshold**.

---

# 12. The Engineering Connection

Now we can connect everything.

Suppose:

    Culvert Capacity = 700 cfs

We want to understand the relationship between environmental loading and
infrastructure capacity.

The problem becomes:

    Environmental Load
          Q
          |
          v
    Probability Distribution
          |
          v
    P(Q > Capacity)
          |
          v
    Exceedance Risk

This same framework appears throughout infrastructure engineering.

## Water Distribution

    Demand > System Capacity

## Wastewater

    Influent Flow > Treatment Capacity

## Lift Stations

    Incoming Flow > Pumping Capacity

## Stormwater

    Runoff > Conveyance Capacity

## Structural Engineering

    Load > Structural Resistance

## Asset Management

    Deterioration > Acceptable Condition

## Reliability Engineering

    Demand > Capacity

Probability allows us to quantify how often those undesirable conditions
might occur.

---

# 13. Empirical vs Theoretical Distributions

There is another important distinction that will matter in this assignment.

## Empirical Distribution

An empirical distribution comes directly from observations.

For example, if 15 of 20 annual peaks were at or below 700 cfs:

    P(Q ≤ 700) ≈ 15 / 20

    P(Q ≤ 700) ≈ 0.75

This estimate requires very few assumptions.

But it is limited by the available observations.

With only twenty years of data, extremely rare events may never have been
observed.

---

## Theoretical Distribution

A theoretical distribution assumes the data follow some mathematical
probability model.

Examples include:

- Normal
- Lognormal
- Exponential
- Gumbel

The parameters of that distribution are estimated using observed data.

The fitted model can then estimate probabilities for values that may not
have occurred directly in the historical sample.

This is powerful.

It is also dangerous if the assumed distribution is inappropriate.

The computer will happily calculate twelve decimal places of nonsense.

---

# 14. Why the Textbook Introduces Lognormal, Exponential, and Gumbel

The equations in the textbook are mathematical definitions of different
possible probability models.

They have different shapes because they represent different kinds of
processes.

### Lognormal Distribution

Useful for positive-valued quantities that may be right-skewed.

Potential applications include environmental concentrations, some flow
variables, and other quantities that cannot be negative.

### Exponential Distribution

Often used to model **waiting times between events** when events occur at an
approximately constant rate.

Examples might include time between certain failures or events.

### Gumbel Distribution

Designed for **extreme values**.

This makes it historically important in hydrology because engineers often
care about annual maxima such as:

- Maximum annual rainfall
- Maximum annual streamflow
- Extreme flood events

The important question is not:

> Which equation looks impressive?

It is:

> What physical process am I modeling, and does this distribution reasonably
> represent that process?

---

# 15. Your Part 3 Assignment

For Part 3, focus on understanding the relationship:

    DATA
      |
      v
    HISTOGRAM
      |
      | shows observed frequencies
      v
    ESTIMATED PDF
      |
      | describes probability density
      v
    CDF
      |
      | accumulates probability
      v
    EXCEEDANCE PROBABILITY
      |
      v
    ENGINEERING RISK

Do not worry yet about selecting the perfect flood-frequency distribution.

The objective is to understand what a PDF represents.

---

# 16. Questions to Ask While Looking at Your PDF

After plotting the PDF over your histogram, ask:

### Where is probability density highest?

This identifies the range where observations tend to concentrate.

### Where is probability density lowest?

This identifies relatively uncommon ranges.

### Is the distribution symmetric?

Compare the left and right sides.

### Is there a long upper tail?

This may indicate that unusually large flow events occur occasionally.

### Does the PDF visually represent the histogram reasonably well?

If not, consider why.

Possible explanations include:

- Small sample size
- Outliers
- Skewness
- Poor distribution assumption
- Poor density estimation
- Bin selection affecting the histogram

---

# 17. One Important Warning About Small Datasets

Twenty observations is a very small dataset for estimating extreme-event
probabilities.

Suppose the largest observed flow is:

    850 cfs

That does **not** mean flows above 850 cfs are impossible.

It only means:

> No event above 850 cfs occurred during this twenty-year sample.

This distinction is critical in infrastructure design.

Infrastructure often has a long service life.

A culvert might remain in service for:

    50–75 years

A pump station might operate for:

    30–50 years

A pipeline might remain in service for:

    75–100+ years

A short historical dataset may therefore represent only a fraction of the
conditions the infrastructure will experience.

This is one reason engineers use probability models rather than relying only
on observed maxima.

---

# 18. Mental Model to Remember

When you forget the terminology, remember these four questions.

## Histogram

> **What happened in my sample?**

## PDF

> **Where is probability concentrated?**

## CDF

> **What is the probability of being at or below this value?**

## 1 - CDF

> **What is the probability of exceeding this value?**

For infrastructure analytics, the last question is often where the
engineering decision begins.

---

# 19. Connecting This to the Culvert Problem

Your culvert has:

    Capacity = 700 cfs

Do not immediately calculate an answer.

Work through the reasoning:

### Step 1

Look at the histogram.

Where does 700 cfs fall relative to the observed flows?

### Step 2

Look at the PDF.

Is 700 cfs located near a high-density region or out in the tail?

### Step 3

Look at the CDF.

Estimate:

    F(700)

Interpret that number as:

    P(Q ≤ 700)

### Step 4

Calculate the complement:

    1 - F(700)

Interpret that as:

    P(Q > 700)

### Step 5

Translate the statistic into engineering language.

Do not merely report:

    P(Q > 700) = X

Explain what that probability means for the proposed culvert.

---

# 20. Final Conceptual Check

Before moving beyond Part 3, make sure you can explain this situation.

An engineer asks:

> "The PDF is highest around 625 cfs. Does that mean 625 cfs has the highest
> probability?"

A strong answer would recognize that this wording is not quite correct.

For a continuous variable, the PDF describes **density**, not the probability
of one exact value.

The high PDF around 625 cfs tells us that probability is concentrated in
the region around 625 cfs.

Probabilities come from **areas under the PDF over intervals**.

That distinction is fundamental to everything that follows.

---

# 21. Where This Is Going

The concepts introduced here form a progression:

    Observed Data
         ↓
    Descriptive Statistics
         ↓
      Histogram
         ↓
        PDF
         ↓
        CDF
         ↓
    Exceedance Probability
         ↓
    Return Period
         ↓
    Reliability / Risk
         ↓
    Monte Carlo Simulation
         ↓
    Infrastructure Decision Making

Later, instead of asking only:

> "What flows have historically occurred?"

we will be able to ask:

> "What is the probability that this infrastructure will experience loading
> beyond its capacity during its service life?"

That is the transition from **descriptive statistics** to **risk-based
infrastructure analytics**.

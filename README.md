# DDQNTSCA-PER: A Double Deep Q-Network with Prioritized Experience Replay for Decentralized Traffic Signal Control: 
# README — Table 6 Statistical Analysis (Revised Manuscript)

## Overview
This folder contains the analysis files, data, and code used to compute the
statistics presented in **Table 6** of the revised manuscript submitted to
*Cluster Computing (2025)*.

All reported values — **mean, minimum, maximum, standard deviation (SD),
median, interquartile range (IQR), and 95% confidence intervals (CI)** —
were computed directly from **raw per-episode simulation data** generated
during SUMO experiments (505 episodes total).

---

## Contents

| File Name | Description |
|------------|--------------|
| `gph.xlsx` | Raw per-episode simulation data (each column represents a method). |
| `per_episode_data.csv` | Cleaned CSV version of `gph.xlsx` with labeled columns. |
| `table6_summary_stats.csv` | Computed summary statistics for each method. |
| `table6_generated.tex` | LaTeX-formatted table for inclusion in the manuscript (Table 6). |
| `stats_table6.py` | Python script that performs all statistical computations. |
| `README_Table6_Revised.md` | This documentation file. |

---

## Analysis Environment

- **Language:** Python 3.10  
- **Libraries:**  
  - `pandas` (v2.2+)  
  - `numpy` (v1.26+)  
  - `scipy` (v1.13+)  
- **Simulator:** SUMO 1.20.0 (Simulation of Urban Mobility)

---

## Methodology

1. **Raw Data Collection:**  
   Each SUMO episode recorded per-vehicle metrics such as waiting time,
   travel time, and queue length at every signalized intersection.

2. **Aggregation:**  
   The episode-level aggregates (average waiting time per episode) were
   exported to `gph.xlsx`.

3. **Statistical Computation:**  
   The following statistics were computed for each method:

   - \( N \): number of episodes (505)  
   - \( \text{Mean}, \text{Min}, \text{Max}, \text{SD}, \text{Median}, \text{IQR} \)
   - **95% Confidence Interval (CI):**
     \[
     CI = \bar{x} \pm t_{\alpha/2,\,n-1} \times \frac{s}{\sqrt{n}}
     \]
     where \( \bar{x} \) is the mean, \( s \) is the sample standard deviation,
     and \( n \) is the number of episodes.

4. **Output Files:**  
   The computed statistics are saved in CSV and LaTeX formats for
   reproducibility and direct inclusion in the revised manuscript.

---

## How to Reproduce

### Step 1 — Install Dependencies
```bash
pip install numpy pandas scipy

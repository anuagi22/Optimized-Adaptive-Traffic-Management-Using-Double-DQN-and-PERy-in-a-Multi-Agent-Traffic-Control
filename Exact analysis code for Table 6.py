# stats_table6.py
# Compute full descriptive statistics + 95% CI from raw per-episode data.

import os
import numpy as np
import pandas as pd

try:
    from scipy import stats
    use_scipy = True
except Exception:
    use_scipy = False

# ------------------------------
# CONFIG
# ------------------------------
INPUT_XLSX = "gph.xlsx"        # path to your Excel file
OUT_PER_EPISODE = "per_episode_data.csv"
OUT_SUMMARY = "table6_summary_stats.csv"
OUT_TEX = "table6_generated.tex"

# Set your preferred column labels here (must match number of columns in gph.xlsx)
DEFAULT_LABELS = ["Vidali et al. [14]", "Bouktif et al. [17]", "Chen et al. [15]", "DDQNTSCA"]

# Confidence level
ALPHA = 0.05  # 95% CI

# ------------------------------
# LOAD DATA
# ------------------------------
df = pd.read_excel(INPUT_XLSX, header=None)

# Assign column labels
if df.shape[1] == len(DEFAULT_LABELS):
    df.columns = DEFAULT_LABELS
else:
    df.columns = [f"Method_{i+1}" for i in range(df.shape[1])]

# Optional: drop rows with all NaNs
df = df.dropna(how="all")

# ------------------------------
# STATS FUNCTIONS
# ------------------------------
def ci_95(mean, sd, n, alpha=ALPHA, use_t=True):
    '''Return (lower, upper) 95% CI. Uses t-distribution if use_t and n>1; else normal.'''
    if n <= 1 or sd == 0 or not use_t:
        z = 1.96
        se = sd / np.sqrt(max(n, 1))
        return mean - z * se, mean + z * se
    se = sd / np.sqrt(n)
    tcrit = stats.t.ppf(1 - alpha/2, df=n-1) if use_scipy else 1.96
    return mean - tcrit * se, mean + tcrit * se

def iqr(series):
    '''Interquartile range (Q3 - Q1), ignoring NaNs.'''
    q1 = np.nanpercentile(series, 25)
    q3 = np.nanpercentile(series, 75)
    return q3 - q1

# ------------------------------
# COMPUTE SUMMARY
# ------------------------------
rows = []
for col in df.columns:
    s = pd.to_numeric(df[col], errors='coerce').dropna()
    n = int(s.shape[0])
    mean = float(s.mean())
    sd = float(s.std(ddof=1)) if n > 1 else 0.0
    mn = float(s.min()) if n > 0 else np.nan
    mx = float(s.max()) if n > 0 else np.nan
    med = float(s.median()) if n > 0 else np.nan
    _iqr = float(iqr(s)) if n > 0 else np.nan

    lo, hi = ci_95(mean, sd, n, use_t=use_scipy)

    rows.append({
        'Method': col,
        'N (episodes)': n,
        'Mean': mean,
        'Std Dev': sd,
        'Min': mn,
        'Max': mx,
        'Median': med,
        'IQR': _iqr,
        '95% CI Lower': lo,
        '95% CI Upper': hi
    })

summary = pd.DataFrame(rows)

# ------------------------------
# SAVE OUTPUTS
# ------------------------------
df.to_csv(OUT_PER_EPISODE, index=False)

summary_rounded = summary.copy()
for c in ['Mean','Std Dev','Min','Max','Median','IQR','95% CI Lower','95% CI Upper']:
    summary_rounded[c] = summary_rounded[c].astype(float).round(4)
summary_rounded.to_csv(OUT_SUMMARY, index=False)

latex_rows = []
for _, r in summary_rounded.iterrows():
    latex_rows.append(
        f"{r['Method']} & {int(r['N (episodes)'])} & {r['Mean']:.4f} & {r['Std Dev']:.4f} & "
        f"{r['Min']:.4f} & {r['Max']:.4f} & {r['Median']:.4f} & {r['IQR']:.4f} & "
        f"{r['95% CI Lower']:.4f}--{r['95% CI Upper']:.4f} \\"
    )

latex_table = r"""\begin{table}[htbp]
\centering
\caption{Descriptive statistics computed from \textbf{raw per-episode SUMO simulation data} (N episodes). Results include mean, minimum, maximum, standard deviation (SD), median, interquartile range (IQR), and 95\% confidence intervals (CI).}
\label{tab:table6_stats}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccc}
\hline
\textbf{Method} & \textbf{N (episodes)} & \textbf{Mean} & \textbf{Std Dev} & \textbf{Min} & \textbf{Max} & \textbf{Median} & \textbf{IQR} & \textbf{95\% CI (Lower--Upper)} \\ \hline
""" + "\n".join(latex_rows) + r"""
\hline
\end{tabular}%
}
\end{table}
"""

with open(OUT_TEX, 'w', encoding='utf-8') as f:
    f.write(latex_table)

print('\n=== Table 6 Summary (from raw per-episode data) ===')
print(summary_rounded.to_string(index=False))
print(f'\nSaved:\n - {os.path.abspath(OUT_PER_EPISODE)}\n - {os.path.abspath(OUT_SUMMARY)}\n - {os.path.abspath(OUT_TEX)}')

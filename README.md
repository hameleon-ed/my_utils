# my_utils
#### Useful utilities across Python projects

Key features:

- Plots and charts
- Statical analysis
- Code plotting

## Install

Set up the environment:
```bash
uv sync
```

To upgrade all dependencies to their latest versions:
```bash
uv lock --upgrade
uv sync
```

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── tasks.py           <- Invoke file for task management
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         my_utils and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src
    └── my_utils       <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes my_utils a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    └── plots.py                <- Code to create visualizations
```

--------

## 🔁 How to reuse it in other projects
### Option A — Editable install (BEST for development)

Clone the my_utils repository to the root folder of a project (my_utils and a project should be in the same folder)
In your main project:

```bash
uv add --editable ../my_utils
```

Then use:

```bash
from my_utils.plotting import boxplots
```

### Option B — Git dependency (clean, versioned)

```bash
uv add git+https://github.com/hameleon-ed/my_utils.git
```

If you have pushed changes to `my_utils` on GitHub and want to pull them into your project, use the --update-package (or -P) flag:

```bash
uv lock --upgrade-package my-utils
uv sync
```
| Tip: uv lock file uses hyphens by convention, e.g., `my-utils`, even if your folder or Git repo is named `my_utils`

---

Based on the 
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>
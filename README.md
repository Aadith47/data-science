# Data-science

My practice repo for learning data science with Python. Right now it's mostly the basics: pandas, numpy, seaborn and matplotlib. I'll add machine learning stuff as I get to it.

Nothing here is polished. It's notebooks and scripts I wrote while learning, so expect some messy bits.

## What's in here

- **Pandas:** loading data, cleaning it, filtering, groupby
- **NumPy:** arrays and basic operations
- **Seaborn / Matplotlib:** plots for exploring data.
- **Palmer Penguins EDA:** my most complete project so far (details below)

## Palmer Penguins EDA

I explored the Palmer Penguins dataset (344 penguins, 3 species) to practice EDA. The main things I found:

- Flipper length and body mass are strongly correlated (0.87)
- Gentoo penguins are the heaviest of the three species
- Males are bigger than females in every species
- Bill length vs bill depth looks like a weak negative trend overall, but splits into three clear clusters once you color by species

`export_charts.py` saves the charts as separate images.

## Running it

```
pip install pandas numpy seaborn matplotlib
python export_charts.py
```

For the notebooks, install Jupyter and open them the usual way.

## Coming next

- Predicting penguin species from the measurements
- More ML basics with scikit-learn

## About

I'm Aadith, an IT graduate focused on data science and AI/ML. Feel free to open an issue or message me on LinkedIn if you spot something wrong or have a suggestion.

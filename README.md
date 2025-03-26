# Job Satisfaction Regression Analysis

## 📚 Libraries Used

This project was developed using the following Python libraries:

- **pandas** – for data manipulation and analysis  
- **numpy** – for numerical operations  
- **matplotlib** – for data visualization  
- **seaborn** – for statistical plotting  

## 💡 Motivation

While exploring public datasets, I came across the [Stack Overflow Developer Survey](https://survey.stackoverflow.co/), which, among many other things, asks developers about their **Job Satisfaction**. Having just learned how to build and interpret a regression model, I saw this as a great opportunity to:

1. Practice my data processing and modeling skills
2. Investigate what factors contribute to high job satisfaction

## 📁 Repository Contents

- `Learning_Satisfaction.ipynb`  
  A direct dive into the dataset. This notebook includes initial data processing, model building, and evaluation.

- `EDA_correlations.ipynb`  
  A deeper exploratory data analysis focused on identifying correlations between features and Job Satisfaction. This was used to investigate why the model struggled to produce meaningful predictions.

## 📉 Summary of Results

Unfortunately, the results were disappointing:

- **Many missing values** in the `Job Satisfaction` column made modeling difficult.
- **Weak or no significant correlations** were found between job satisfaction and other variables.
- Slight correlations were observed with:
  - A certain level of **influence in the organization**
  - **Work experience**
  
  However, these were not strong enough to enable a reliable prediction model. As a result, the model performed **barely better than a random number generator**.

Still, this was a valuable learning experience in real-world data handling, modeling, and the importance of meaningful feature relationships.

## 🙏 Acknowledgements

- **Dataset**: [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)

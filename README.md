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

## 📂 Repository Contents

- `stack-overflow-developer-survey-2024.zip`  
  The raw dataset used for analysis, obtained from Stack Overflow's Developer Survey.

- `preprocessing.py`  
  A Python script containing reusable functions for data cleaning and preprocessing. These functions were originally developed during exploratory data analysis and are now used to streamline the workflow in the model-building notebook.

- `EDA_correlations.ipynb`  
  An exploratory data analysis notebook focusing on correlation analysis between variables. This helped to understand the structure of the data and highlighted why modeling was challenging.

- `Learning_Satisfaction.ipynb`  
  The main notebook where data processing, model building, and evaluation take place. It leverages the functions defined in `preprocessing.py`.

## 📉 Summary of Results

Unfortunately, the results were disappointing:

- **Many missing values** in the `Job Satisfaction` column limited the usable data.
- **Weak or no significant correlations** were found between job satisfaction and other variables.
- Slight correlations were observed with:
  - A certain level of **influence in the organization**
  - **Work experience**
  - Knowledge-columns
  
These correlations, however, were not strong enough to enable a reliable prediction model. As a result, the model performed **barely better than a random number generator**.

Still, this project provided valuable insights into the challenges of real-world data, the importance of feature quality, and hands-on experience in building a full data pipeline.

## 🙏 Acknowledgements

- **Dataset**: [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)

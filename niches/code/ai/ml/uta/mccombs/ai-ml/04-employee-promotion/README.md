# Employee Promotion - Advanced ML

## Exercise definition

- [Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_master.ipynb)
- Predict promotions from employee training and work records.
- Explore the data and compare bagging and boosting models.
  - Try the original data and data with the groups balanced by adding or removing examples.
  - Tune the models and explain the final choice.
- This was the extra advanced ML assignment.

## Solution

- [Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_solution.ipynb)
- [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_solution.html)
- I prepared the data and compared bagging and boosting models.
  - Tried oversampling: add more examples from the smaller group.
  - Tried undersampling: use fewer examples from the larger group.
- I picked tuned XGBoost trained on the original data.
- Saved test scores:
  - Accuracy: 0.939.
  - Precision: 0.836.
  - Recall: 0.355.
  - F1: 0.499.
- Accuracy looked good, but the model missed many actual promotions.
- Department, region, and recruitment patterns raised questions about bias.
  - An important feature doesn't prove what caused a promotion.
- August 9, 2026 is an estimate from the saved notebook and HTML dates. No emailed deadline was found.

## Takeaways

- The notebook's business summary swaps two terms.
  - False negative: missed an employee who was promoted.
  - False positive: predicted promotion for someone who wasn't promoted.
- Check recall, precision, and F1 alongside accuracy when one outcome is rare.
- Balancing the groups didn't automatically improve the validation scores.
- Very strong training scores can mean the model has learned the training data too closely (overfitting).
- Past promotion choices can carry bias into a model. Feature importance isn't proof that someone deserves promotion.

## Applications

- I'd use these comparisons for other data where one outcome is rare, or to check how a model changes a shortlist.
- For promotion review, check for unfair patterns and keep a person in the decision.
  - Recall is too low to use this model to rule people out.

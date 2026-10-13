# Employee Promotion — Advanced ML

## Exercise definition

[Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_master.ipynb)

Identify employees likely to be promoted from their training and work records. Explore the data, compare ensemble models on original and resampled data, tune candidates, and explain the final choice. This is the additional advanced ML assignment.

## Solution

[Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_solution.ipynb) · [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/3.5%20-%20Advanced%20Machine%20Learning%20-%20Employee%20Promotion/FullCode_Additional__Project_AML_solution.html)

I prepared the data, compared bagging and boosting models, and tested oversampling and undersampling. I selected tuned XGBoost trained on the original data. Its saved test results are 0.939 accuracy, 0.836 precision, 0.355 recall, and 0.499 F1.

The high accuracy hides a substantial limit: the model misses many actual promotions. The notebook also discusses feature importance and possible bias in department, region, and recruitment patterns. I would treat those observations as questions to investigate, rather than proof that a feature causes promotion.

Completion is recorded as August 9, 2026, estimated from the saved notebook and HTML file dates; an assignment deadline was not found in email.

## Takeaways

- For the promotion class, a false negative misses an employee who was promoted; a false positive predicts promotion for someone who was not. The original notebook’s business summary reverses those descriptions.
- Compare recall, precision, and F1 alongside accuracy when the target class is uncommon.
- Resampling did not automatically improve validation performance. Very strong training scores can still signal overfitting.
- Historical promotion patterns can reproduce past decisions and bias; feature importance does not establish merit.

## Applications

I could use the comparisons to study an imbalanced classification problem or audit how a model changes a shortlist. Any use in promotion review would need fairness checks and a human decision; the saved recall is too low to treat this model as a reliable gate.

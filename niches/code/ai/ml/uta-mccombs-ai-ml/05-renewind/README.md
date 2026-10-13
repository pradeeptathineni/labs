# ReneWind - Neural Networks

## Exercise definition

- [Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_master.ipynb)
- Use wind turbine sensor readings to predict failures before equipment needs replacing.
- Compare neural networks and consider the cost of missed failures when choosing one for inspection planning.

## Solution

- [Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_solution.ipynb)
- [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_solution.html)
- I put the inputs on a similar scale and compared seven network setups.
  - Changed layers, the optimizer (how weights are updated), controls for overfitting, and weights for each class.
- I picked model 5 using the validation results, then checked the supplied test set.
- Saved test scores:
  - Accuracy: 0.9912.
  - Macro-average recall: 0.9287.
  - Macro-average F1: 0.9560.
- Scores for failures in the classification report:
  - Precision: 0.98.
  - Recall: 0.86.
  - F1: 0.92.
- Macro recall averages the scores for both classes. It isn't the share of failures found.
- The final notebook text gives failure recall as 0.87, while the saved report shows 0.86.
  - Check the saved predictions before using the exact number.

## Takeaways

- Pick the model from validation results, then check the final test set.
- Missing a failure and sending an unnecessary inspection cost different amounts.
  - Accuracy alone doesn't tell me that tradeoff.
- Compare training and validation scores when adding layers or controls for overfitting.
- Name the class and averaging method when quoting a score.
  - A good macro-average can still hide missed failures.

## Applications

- I'd try these comparisons on equipment with sensor records.
- Before a trial, check the failure predictions, data collected over time, inspection costs, and false alarms.

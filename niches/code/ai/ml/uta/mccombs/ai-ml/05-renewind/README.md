# ReneWind — Neural Networks

## Exercise definition

[Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_master.ipynb)

Use wind turbine sensor data to predict failures before they require replacement. Build and compare neural networks, account for the cost of missed failures, and recommend a model for inspection planning.

## Solution

[Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_solution.ipynb) · [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/4%20-%20Intro%20to%20Neural%20Networks%20-%20ReneWind/INN_ReneWind_Main_Project_FullCode_Notebook_solution.html)

I standardized the inputs and compared seven neural network configurations, changing their layers, optimizer, regularization, and class weighting. I selected model 5 from its validation performance and then checked the supplied test set.

The saved test table reports 0.9912 accuracy, with macro-averaged recall of 0.9287 and F1 of 0.9560. The failure class has 0.98 precision, 0.86 recall, and 0.92 F1 in the classification report. Macro recall averages both classes; it is not the share of failures detected. The final prose rounds failure recall differently at 0.87, so I would check the saved predictions before quoting an exact operational rate.

## Takeaways

- Model choice should use validation results before the final test set.
- Missing a failure and sending an unnecessary inspection have different costs. Accuracy alone does not express that tradeoff.
- Compare training and validation behavior when adding capacity or regularization.
- Name the averaging method and evaluated class. Macro recall can look strong while the failure class still has meaningful misses.

## Applications

I could adapt this comparison to predictive maintenance for equipment with sensor records. A useful next step would be to check the failure-class predictions and evaluate time-based data, inspection costs, and false alarms before a monitored trial.

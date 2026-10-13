# FoodHub — Python Foundations and Data Analysis

## Exercise definition

[Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_master.ipynb)

Analyze FoodHub’s order data with Python. Check its quality, explore customer and restaurant patterns, calculate delivery and commission measures, and recommend changes to the business.

## Solution

[Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_solution.ipynb) · [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_solution.html)

I inspected 1,898 orders with pandas and used plots and grouped comparisons to answer the assignment questions. Weekday delivery averaged about 28.34 minutes, compared with 22.47 minutes on weekends. About 10.54% of orders took more than an hour including preparation. Ratings were concentrated at 4–5, with many missing, so they gave limited evidence about poor service.

I recommended improving feedback collection, investigating weekday delays, and tailoring offers to different spending patterns. These are proposals from the observed data; the notebook does not test their effect.

## Takeaways

- Separate food preparation from delivery when looking for delays. A slow total time can have more than one cause.
- Missing and compressed ratings limit what customer satisfaction comparisons can tell me.
- Little correlation in this dataset does not prove two operations are independent or that delivery time never matters to a customer.

## Applications

I could use this approach to review a delivery service, compare performance across days, and identify where better feedback would help. Operational changes would need a follow-up comparison to see whether they worked.

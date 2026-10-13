# FoodHub - Python Foundations and Data Analysis

## Exercise definition

- [Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_master.ipynb)
- Use FoodHub's order data to check customer spending, restaurant orders, ratings, and wait times.
- Check the data, calculate delivery times and commissions, and suggest changes to the service.

## Solution

- [Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_solution.ipynb)
- [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/1%20-%20Python%20Foundations%20-%20FoodHub%20Data%20Analysis/Template_Notebook_Full_code_Version_solution.html)
- I checked 1,898 orders with pandas, plots, and grouped tables.
- Delivery took longer on weekdays.
  - Weekday average: 28.34 minutes.
  - Weekend average: 22.47 minutes.
- About 10.54% of orders took over an hour, counting preparation and delivery.
- Most ratings were 4 or 5. Many orders weren't rated, so ratings didn't tell me much about poor service.
- I suggested better feedback, a closer look at weekday delays, and offers based on customer spending.
  - I didn't test whether these changes helped.

## Takeaways

- Check preparation and delivery separately. Either can add to the wait.
- Missing ratings and mostly high scores make it hard to spot unhappy customers.
- Preparation and delivery times barely moved together in this data.
  - That doesn't prove the two are independent.
  - Little change in ratings with delivery time doesn't mean customers don't care how long they wait.

## Applications

- I'd use this to compare delivery times by day and customer spending, and find where better feedback would help.
- Try a change, then check whether it helped.

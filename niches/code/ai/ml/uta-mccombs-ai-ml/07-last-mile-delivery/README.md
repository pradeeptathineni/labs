# Last-Mile Delivery - Agents for Automation

## Exercise definition

- [Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_master.ipynb)
- Use shipment logs, customer records, locker availability, and the supplied playbook to handle delivery problems.
- Identify the problem, choose an action, write a customer message, and send required cases to a supervisor.
- Check the workflow on the ten supplied shipments.

## Solution

- [Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_solution.ipynb)
- [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_solution.html)
- I used LangGraph to route the work between deciding an action, writing a message, and reviewing both.
  - Pydantic checks the expected fields in model replies.
- Tools get the facts needed for a decision:
  - Shipment and customer details.
  - Free locker space.
  - Cases that must go to a supervisor.
  - Relevant playbook passages.
- Routine delivered and scanned events stop before any tools or models are called.
- Duplicate scans are removed. Required escalations are enforced in code.
- Saved results for the ten course cases:
  - Task completion: 10/10.
  - Escalation decisions: 8/8 cases with a problem.
  - Tool-call accuracy: 100%.
- SHP-005 has a mismatch between the playbook and expected answer.
  - The expected answer says to reroute to a locker, but the nearby locker is full.
  - Matching that answer doesn't make the reroute possible.
- October 4, 2026 is based on the day before the October 5 deadline.
  - The notebook and HTML were edited again on October 10.

## Takeaways

- Keep required escalation rules in code. Skip model calls for routine events.
- Keep routing, retry limits, and final review together so I can follow the workflow.
- Check that tools were used correctly and the chosen action is possible.
- Ten visible test cases help find mistakes. They don't show how this will perform on real deliveries.
- Checking reply fields and screening keywords helps, but it doesn't catch every model error or prompt injection (instructions hidden in the input).

## Applications

- I'd use this to help a dispatcher gather the facts, choose an action, and draft a message for review.
- Before a trial:
  - Fix the locker mismatch.
  - Add an action for holding the package at the depot.
  - Test on a separate set of messy delivery cases.

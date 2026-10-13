# Last-Mile Delivery — Agents for Automation

## Exercise definition

[Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_master.ipynb)

Build a workflow for delivery exceptions using shipment logs, customer records, locker availability, and the supplied resolution playbook. Classify the event, choose an action, draft a customer message, enforce escalation rules, and evaluate the ten supplied shipments.

## Solution

[Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_solution.ipynb) · [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/6%20-%20AI%20Agents%20for%20Automation/Project_3_Full_Code_solution.html)

I used LangGraph to coordinate resolution, communication, and critic steps, with Pydantic schemas for structured outputs. Tools fetch shipment and customer details, check locker capacity, identify escalation requirements, and retrieve playbook passages. Routine delivered and scanned events stop before tools or models are called. Duplicate scans are removed, and mandatory escalations are enforced in code.

The saved run reports 10/10 task completions, 8/8 escalation decisions on exception cases, and 100% tool-call accuracy. These results cover the ten visible course cases. SHP-005 exposes a policy conflict: the label expects a locker reroute even though the nearby locker is full. Passing the label check does not make that action feasible.

The recorded completion date is October 4, 2026, one day before the emailed October 5 deadline. The published notebook and export include later edits from October 10.

## Takeaways

- Use deterministic rules for required escalations and avoid model calls for routine events.
- Keep routing, retry limits, and final review in one place so the workflow is understandable.
- Validate tools and available capacity, not just whether an action matches a label.
- A visible ten-case test set helps debug the workflow but cannot establish production performance.
- Structured output and keyword checks help constrain a workflow; they are not complete protection against model errors or prompt injection.

## Applications

I could use this as a starting point for dispatcher assistance: gather the evidence, recommend an action, and draft the message for review. Before a trial, I would resolve the locker-policy conflict, add hold-at-depot handling, and evaluate a separate set of messy delivery cases.

# Medical Assistant — NLP and Generative AI

## Exercise definition

[Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_master.ipynb)

Build a retrieval-assisted prototype that answers a fixed set of medical questions from the supplied reference manual. Compare generation settings and retrieval choices, then assess answer grounding and relevance.

## Solution

[Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_solution.ipynb) · [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_solution.html)

I explored local quantized models, prompts, and generation settings, then split and embedded the supplied PDF for retrieval. The notebook uses biomedical embeddings and compares answers with retrieved passages. It also tries model-based checks of grounding and relevance.

Better retrieval often improved the answers, but weak passages could still produce confident, irrelevant responses. The small model’s self-evaluation was inconsistent: it sometimes ignored the requested scoring format and confused grounding with completeness. CPU evaluation could take several minutes per question. The saved notebook contains partial runs and observations, rather than evidence of clinical accuracy.

## Takeaways

- Retrieval decides which evidence the generator sees. Cleaning PDF noise and choosing useful chunks matter.
- More retrieved context can add distraction rather than improve an answer.
- Changing prompts and inference settings is parameter tuning; it does not train the model.
- A small model judging its own answer is a rough check, not independent validation.
- Cache models and embeddings, and measure runtime alongside answer quality.

## Applications

I could reuse this approach for searching technical manuals or internal reference documents. For medical material, I would keep it as a supervised reference experiment with source passages visible and qualified review of any answer.

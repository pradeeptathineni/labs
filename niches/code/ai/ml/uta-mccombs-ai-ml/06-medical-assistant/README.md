# Medical Assistant - NLP and Generative AI

## Exercise definition

- [Full-code master notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_master.ipynb)
- Build a small tool that finds useful passages in the supplied medical manual before writing an answer (RAG).
- Keep the questions fixed while comparing answer settings and retrieved passages.
- Check whether the manual supports each answer and whether the passages match the question.

## Solution

- [Full-code solution notebook](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_solution.ipynb)
- [HTML report](https://github.com/pradeeptathineni/uta-mccombs-ai-ml/blob/c4a93c06f1b7dee5d38248af36f4778aa849c870/5%20-%20NLP%20with%20Generative%20AI%20-%20Medical%20Assistant/Full_Code_NLP_RAG_Project_Notebook_solution.html)
- I tried smaller, compressed local models (quantized models), prompts, and settings for generating answers.
- I split the PDF into pieces and converted them into searchable numbers (embeddings).
  - Used biomedical embeddings to find passages for the medical questions.
  - Compared answers with the passages found.
- Better passages often gave better answers. Poor matches could still lead to confident answers that missed the question.
- Having the small model judge its own answers didn't work reliably.
  - It sometimes ignored the requested score format.
  - It treated missing detail as a problem with source support.
- Checking one question could take several minutes on the CPU.
- Some runs are partial. There was no check of accuracy in patient care.

## Takeaways

- The passages found decide what evidence the model sees.
  - Clean out PDF clutter and choose useful pieces of text.
- More text can add distractions.
- Changing prompts and answer settings doesn't train the model. Fine-tuning changes its learned weights.
- A small model checking itself gives a rough signal, not an independent review.
- Cache models and embeddings so they don't need downloading or rebuilding each time.
  - Check speed as well as answer quality.

## Applications

- I'd reuse these steps for technical manuals or company reference documents.
- For medical questions, keep the source passages visible and have a qualified person review the answer.

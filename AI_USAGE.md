# AI Usage Documentation

This document describes how AI (ChatGPT and Claude by Anthropic) was used to solve the Inflationary String Operation challenge.

## 🔄 Process of Working with AI

```
User: "can you guide me through this problem, the thing I initially thought was that using something similar to the PII detection tool where we have a file containing all the numbers in text and we can simply map it to the next number"

ChatGPT:
Yes conceptually — both involve pattern detection and transformation
— but this task is simpler and rule-based rather than entity-bas.

Claude: Analyzed the problem and identified key requirements:
- Substring matching (not just whole words)
- Case preservation needed
- Need to handle overlapping patterns

User: but isn't creating your own mapping file too tedious? it's impossible to put in all the numbers, is there another existing tool (maybe something related to PII detection tool) can help us handle this easily?

ChatGPT: Most number-parsing libraries rely on word boundaries and won’t work for embedded substrings like "ten" in "tennis".
Claude: The "tennis" → "elevennis" example reveals this is **substring matching**, not word-boundary matching. This is unusual for NLP tasks.

User:" i don't think digits are something that we need to consider here, isn't the problem only about numbers in strings"

User: We don't need a full mappings for all the numbers but only from 1 to 19 and then handle 29 -> 30, 39 -> 40 etc.? Should we create a separate file to contain all the mappings then import it?
ChatGPT: Yes, we also need to handle 20 -> 21, 30 -> 31 cases. Creating a separate file for mapping is a clean and structured approach.

User: " can you put number_map content in a separate file and then later import it for use? also I think it's not the optimal approach if we start matching from the longest string if what we have is a  short string, is there maybe a way to create number_map so record each number elements length, so that when we have a string of length n, we only need to look at elements inside the map that have length <= n, help me brainstorm a good way for easy look up."

User: "help me preapre the whole repository to submit to github, including the readme, project files, test files, and make the script handling testing easily"

```



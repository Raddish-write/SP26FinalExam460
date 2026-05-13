# Development Log – The Torchbearer

**Student Name:** Michael Milton
**Student ID:** 132765149

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – 11MAY2026: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

My initial plan is to first Analyze the problem as outlined in part 1 and begin on building structures for Djikstra's path selection as outlined in part 2. If I have time, I will begin on part 3 and determine correctness for the Djikstra's method as well, and potententially move into outlining why Greedy selection fails. 

Update: Q1 and Q2 completed, and code has been committed and pushed. Q3 and Q4 slotted for tomorrow. 

---

## Entry 2 – 12MAY2026: Search implimentation

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Completed answers 3 and 4. Finished the path selection code while the way previously written code was still fresh in my head from yesterday._
_Major bug encountered that was causing instability. Discovered it was due to setting collection1() = collection2(). Unlike in other languages_
_Rather than cloning a collection, python will simply rename the collection to match. Fixed via using collection1() = collection2().copy()_
_Also encountered issue regarding preferred answer format. Comment instruction says return tuple, howver program checks for 2 element list succeeded_
_which was much easier to impliment._

_Questions 5 and 6 partially answered based on work done so far. Tomorrow will answer questions analyzing efficiency._
---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | _1_ |
| Part 2: Precomputation Design | _1.5_ |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |

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

## Entry 3 – 14MAR2026: Final Answers

_Rexamined the code that I have already finished in order to wrap up questions 5 and 6._
_Same date as entry below._

---

## Entry 4 – 14MAR2026: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_I think that the time given for the assignment was more than adequate._
_Given more time I would likely go back through the classnotes, as I have the feeling that I_
_missed a vital step in optimization somewhere. However much of the time I spent was more due to_
_frustration with Python more than the material taught itself._

---

## Final Entry – 14MAR2026: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | _1_ |
| Part 2: Precomputation Design | _1.5_ |
| Part 3: Algorithm Correctness | _1_ |
| Part 4: Search Design | _4_ |
| Part 5: State and Search Space | _1_ |
| Part 6: Pruning | _1_ |
| Part 7: Implementation | _2_ |
| README and DEVLOG writing | _2_ |
| **Total** | _13.5_ |
-_Note that much of the time is due to trying to remember previous work. Contiguous work would have been faster likely._

# The Torchbearer

**Student Name:** Michael Milton
**Student ID:** 132765149
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _A single shortest path run is not enough for the torchbearer problem because a shortest path may possibly skip over some relic rooms and a valid route is defined here in part as one that collects every relic._

- **What decision remains after all inter-location costs are known:**
  _After the cost to travel between every room has been calculated, the order of relic and/or end rooms visited must be selected._

- **Why this requires a search over orders (one sentence):**
  _Because the graph is directed and weighted, going one direction down the path may increase cost dramatically for a future decision despite being the best choice from that node so multiple valid paths must be compared._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _Start Node_ | _The Torch Bearer is garunteed to start at the start node and so must travel some distance from here every time_ |
| _Relic Node_ | _Each relic node must be visited in order to be a valid path, and so must travel some distance from here every time_ |
| _Exit Node_ | _The exit node must be reachable from all relic nodes and must be visited, and so is highly likely to be backtracked from as well_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | _Dictionary_ |
| What the keys represent | _Each key represents the starting Node from which we are measuring distance from_ |
| What the values represent | _The values are themselves dictionaries, where each key represents a node connected to the source node and the value is the shortest distance between them_|
| Lookup time complexity | _Dictionary lookup time complexity is O(1) or constant. To lookup distance from one node to another is constant, and from a source to every other node is _ |
| Why O(1) lookup is possible | _Dictionary keys point directly to a memory location via hashing with is (generally) a constant speed operation_ |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _Once per relic room and again once for the start and end node_
- **Cost per run:** _For every time it is run, it is called once per Vertex and once per Edge_
- **Total complexity:** _O((E+V)logV)_
- **Justification (one line):** _Each edge and each Vertex must be considered for every call, so it must be at least E+V. However, the Queue (which is filled along verticies) is a minheap which scales logarithmically and so is (E+V)logV_

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._

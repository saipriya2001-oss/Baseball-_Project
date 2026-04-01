# AI PROMPTS LOG

## Student: Soma Sekhar & Sai Priya
## Project: Baseball Elimination using Max Flow

---

## 🔹 Problem 1: Understanding the Problem
- **Issue:** We did not understand how to convert baseball elimination into a graph problem.
- **Prompt Used:**
  "Explain baseball elimination problem in simple terms with example"
- **Modification:**
  We simplified explanation and mapped teams → nodes, games → edges manually.

---

## 🔹 Problem 2: Implementing Max Flow (Ford-Fulkerson / Edmonds-Karp)
- **Issue:** Difficulty implementing max flow in Python.
- **Prompt Used:**
  "Give simple Python implementation of Edmonds-Karp algorithm without complex loops"
- **Modification:**
  - Rewrote code using simple loops
  - Used dictionary instead of advanced structures
  - Made BFS easy to understand

---

## 🔹 Problem 3: Building Flow Network
- **Issue:** Confusion in creating graph structure.
- **Prompt Used:**
  "How to construct flow network for baseball elimination step by step"
- **Modification:**
  - Created:
    - Source → Game nodes
    - Game → Team nodes
    - Team → Sink
  - Simplified naming (team1_team2)

---

## 🔹 Problem 4: Incorrect Output (Wrong Subset R)
- **Issue:** Output subset was incomplete.
- **Prompt Used:**
  "Fix min-cut logic for baseball elimination Python code"
- **Modification:**
  - Added reverse edge traversal in residual graph
  - Fixed BFS for min-cut
  - Now correct subset is returned

---

## 🔹 Problem 5: Input Handling
- **Issue:** File input vs manual input confusion.
- **Prompt Used:**
  "Make Python program take input by copy-paste instead of file"
- **Modification:**
  - Removed file handling
  - Used `input()` based driver code

---

## 🔹 Final Result
- Code correctly determines:
  - Eliminated teams
  - Certificate of elimination (subset R)
- Matches expected output for all test cases
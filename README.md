
**Baseball Elimination Project**

This project implements a Baseball Elimination algorithm using Python to determine whether a team in a league has been mathematically eliminated from finishing in first place. The concept is based on analyzing team standings and remaining games to evaluate if a team still has a chance to win the league.

The program reads input data representing multiple teams, including their current performance and remaining matches. It then processes this information using two main components: a Team Manager module and an Elimination Checker module.

The TeamManager class is responsible for organizing and storing team data such as wins, losses, and remaining games.
The check_elimination function applies an algorithm (often based on network flow or max-flow techniques) to determine whether a team is eliminated.

The main script:

Reads the number of teams and their data from standard input.
Stores the data in a structured format.
Iterates through each team to check its elimination status.
Outputs whether the team is eliminated and, if so, identifies the subset of teams responsible for the elimination.

The project demonstrates key concepts from algorithm design, especially graph theory and flow networks, along with practical skills in Python programming, input handling, and modular code structure.

The goal of this project is to provide a computational solution to a real-world sports problem, showing how mathematical modeling and algorithms can be used to make strategic decisions in competitive environments.


# ⚾ Baseball Elimination (Max Flow Project)

## 👨‍💻 Team Members
- Soma (Student B)
- Priya (Student A)

---

## 📌 Project Description
This project solves the **Baseball Elimination Problem** using:

- Max Flow (Edmonds-Karp Algorithm)
- Min Cut (for certificate of elimination)

It determines:
- Whether a team is eliminated
- Which subset of teams (R) eliminates it

---

## 🧠 Approach

### 1. Trivial Elimination
If:
wins[x] + remaining[x] < wins[i]
→ Team is eliminated

---

### 2. Non-Trivial Elimination (Flow Network)

Graph Structure:
- Source → Game Nodes
- Game Nodes → Team Nodes
- Team Nodes → Sink

We compute:
- Max Flow
- If flow < total games → team eliminated

---

### 3. Certificate of Elimination
- Use Min-Cut
- Teams reachable from source form subset R

---

## ▶️ How to Run

```bash
python ddd.py

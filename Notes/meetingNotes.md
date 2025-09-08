# 📝 Meeting Notes

## **Meeting Title:** TA Meeting
### **Date:** Thursday, September 4th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara, Kevin Likcani(TA)

### 📒 Notes
- Adding more features to the game can help overall grade
- Adding more information to the documentation can compensate for not great diagrams
- Diagrams
  - try to have 3-4 diagrams
    - components interaction dataflow
    - entire process (from start to finish) 
      - circles to arrow pointing to each other (348)
    - different states of the game
    
---
## **Meeting Title:** Team Meeting
### **Date:** Wednesday, September 3rd, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara

#### 📌 Agenda / Discussion Points

1. Documentation overview
2. Update person hours and task board
3. Project status update scrum


#### ✅ Updates / Decisions Made

- Katie (dev): Completed advanced datastructure accoriding to game instructions. Implemented game logic and mine detection logic to flag or uncover. If a mine is uncovered then the game ends, if it is flagged and you try to uncover it blocks you.
- Christina (dev): Working on expandOpenCells function which recusively uncovers the open cells around the one uncovered. This has been pushed to github. Ran into some issues when testing, kept running into the base case (not covered and flagged) however no errors were raised. working on finding a workaround, may need to change isCovered or isFlagged. 
- Vi (dev): finished random mine placement function. changed board manager class so the boardcontent gets initalized with 0s instead of -1s.
So check if its the first turn (by seeing if its all 0s), let the user click the first cell, and then place the mines randomly (the -1s). If there was a specific reason why we had it initalize to all -1s (although the board doesn't have the mine calculation nums yet) but it does terminate the game when a mine is hit.
- Kundana (PM): created a overall system architecture document.
- Navya (scrum): outlined all documentation, will help PM with system architecture document
- Decision: try and implement game logic by next Thursday Meeting
- Decision: Create new branch so when we merge there are no conflicts

#### 📋 To-Do Items / Action Items

- [ ] fix expandOpenCells function — **Assigned to:** Christina and Katie (devs) | **Deadline:** Friday, September 5th
  - ESTIMATED PERSON HOURS: 2
  - ACTUAL: 
- [ ] mine calculation — **Assigned to:** Vi (dev) | **Deadline:** Friday, September 5th
  - ESTIMATED PERSON HOURS: 1
  - ACTUAL: 
- [ ] Implement baseline Tkinter — **Assigned to:** Navya (scrum) | **Deadline:** Friday, September 5th
  - ESTIMATED PERSON HOURS: 2
  - ACTUAL: 
- [X] Look at system architecture documentation and comment any additions/changes — **Assigned to:** Everyone | **Deadline:** Friday, September 5th

#### 📅 Next TA Meeting

- **Date:** Thursday, September 4th
- **Time:** 9:30 AM
- **Location / Platform:** EATON 3001

#### 📅 Next Scrum Meeting

- **Date:** Friday, September 5th
- **Time:** 5 PM
- **Location / Platform:** EATON 2

#### 📅 Next Team Meeting

- **Date:** Wednesday, September 10th
- **Time:** 1 PM
- **Location / Platform:** Teams

---

## **Meeting Title:** First TA Meeting
### **Date:** Thursday, August 28th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara, Kevin Likcani(TA)

### 📒 Project Notes

#### 📅 Deadlines
- Code freeze is **not strict**, but **any changes made after Fri, Sept. 19th will not be considered**.

#### 🗂️ Key Data Structures
- Outlined in the project website.  
- Ensure all core structures are clearly documented in the code and final submission.

#### 📊 General Meetings Outline
- Each person should:
  - Present **what they worked on**.  
  - **Show their code** and provide a **demo** of functionality.  
- Meetings should be **professional** and last **20–30 minutes**.  
- Include **Scrum-style check-in questions**:
  - What did you work on?  
  - What will you work on next?  
  - Any blockers?  

#### ⏱️ Person-Hours Estimate
- Use a **user story point system**.  
- List out **all action items** and **prioritize** them.  
- **Check off items** as they are completed.  
- Update the log **each week**.  
- Current setup is **good** — keep consistent updates.

#### 📑 Program Architecture Documentation
- TA will grade using **Professor’s rubric**.  
- Documentation should:  
  - **Fit exactly what the rubric requires**.  
  - Provide a **high-level description**.  
  - Include **system architecture diagrams** (data flow, data architecture).  
    - At least **1–3 diagrams**, enlarged for readability.  
  - Be at least **3–4 pages minimum**.  
  - **Describe the diagrams in depth** and explain how the architecture supports the system.

#### 📝 Code Documentation
- Add a **prologue at the beginning** of each file.  
- Include **comments on every major code block** so the flow is easy to follow.  
- Comment as if you are **teaching someone new** to the project.  
- The more clarity, the better — but avoid over-commenting.

#### 🤖 Use of AI & External Sources
- You **may use AI or external references** (w3schools, StackOverflow, etc.), but:  
  - **Alter the code** — do not copy-paste.  
  - Provide **attribution** and a note on **why the code was used**.  
  - If AI is used, **include the prompt** and explain its purpose.  
- Try to **minimize AI usage**, but follow the above guidelines if necessary.

#### 👥 Peer Evaluations
- Must be completed **on time**.  
- Submitted at the **end of the project**. 

---
## **Meeting Title:** First Team Meeting
### **Date:** Wednesday, August 27th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara

#### 📌 Agenda / Discussion Points

1. Ensure understanding of project details and game functionality
2. Set up all meeting and stand up times
3. Assign roles (Project Manager, Scrum Master, Developer)
4. Decide how to assign Person-Hours for each task 
5. Get started!

#### ✅ Updates / Decisions Made

- Meet for 10-15 minutes after Monday and Friday class for Stand Up
- Everyone is a developer
- Using Expert Judgment for Person-Hours judgement
  - The simplest and common method
  - An expert—someone with significant experience on similar projects—provides an estimate based on their knowledge
- Set up daily scrum via messages 
- Formal ROLES:
  - Project Manager: Kundana Dongala
  - Scrum Master: Navya Nittala
  - Developers: Christina Sorensen, Vi Lara, and Katie Nordberg

#### 📋 To-Do Items / Action Items

- [X] Organize Kanban Board — **Assigned to:** Kundana Dongala (PM) | **Deadline:** Friday, August 29th
- [X] Set up and outline all documentation requirements — **Assigned to:** Navya Nittala (Scrum) | **Deadline:** Friday, August 29th
- [ ] Explore Tkinter — **Assigned to:** Everyone | **Deadline:** Friday, August 29th
- [X] Set up 10x10 grid — **Assigned to:** Katie Nordberg (Dev) | **Deadline:** Friday, August 29th
  - ESTIMATED MAN HOURS: 3
  - ACTUAL: 1.5 
- [X] Create a mockup of the grid design and game flow — **Assigned to:** Vi Lara (Dev) | **Deadline:** Friday, August 29th
  - ESTIMATED MAN HOURS: 4
  - ACTUAL:
- [ ] Outline functions (high level overview) — **Assigned to:** Christina Sorensen (Dev) | **Deadline:** Friday, August 29th
  - ESTIMATED MAN HOURS: 2
  - ACTUAL:

#### 📅 Next TA Meeting

- **Date:** Thursday, August 28th
- **Time:** 9:30 AM
- **Location / Platform:** EATON 301

#### 📅 Next Scrum Meeting

- **Date:** Friday, August 29th
- **Time:** 5 PM
- **Location / Platform:** EATON 2

#### 📅 Next Team Meeting

- **Date:** Wednesday, September 3rd
- **Time:** 1 PM
- **Location / Platform:** Teams

#### 🗒️ Notes

- Vi has a class at 2PM on Wednesdays

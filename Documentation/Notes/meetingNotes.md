# 📝 Meeting Notes

## **Meeting Title:** TA Meeting
### **Date:** Thursday, September 18th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara, Kevin Likcani(TA)

### 📒 Notes/ToDo
- Documentation meets all requirements
- [ ] Change window title to "playing" once run is clicked
- [ ] Add columns and rows with numbers and letters
- review requirements in canvas and make sure everything is there (good on game setup, but double check)

---

## **Meeting Title:** Team Meeting
### **Date:** Wednesday, September 17th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara

#### 📌 Agenda / Discussion Points

1. Review final submission
2. Discuss testing and any changes

#### ✅ Updates / Decisions Made

- Katie (dev): did some testing. made board class diagram. 
- Christina (dev): created and pushed documentation for testing. noticed game board stays after you win or lose. will try to implement reset button. 
- Vi (dev): fixed the expandOpenCells function. created states of the game diagram. 
- Kundana (PM): Tested program and confirmed all documentation requirements
- Navya (scrum): organized repo for submission and finalized system srchitecture doc. 

#### 📋 To-Do Items / Action Items
- [ ] fix game reset — **Assigned to:** Christina (devs) | **Deadline:** Thursday, September 18th
  - ESTIMATED PERSON HOURS: 0.5
  - ACTUAL: 
- [ ] Submit GitHub Repo (Navya submits)

#### 📅 Next TA Meeting

- **Date:** Thursday, September 18th
- **Time:** 9:30 AM
- **Location / Platform:** EATON 3001
  
---
## **Meeting Title:** TA Meeting
### **Date:** Thursday, September 11th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara, Kevin Likcani(TA)

### 📒 Notes
- Arch. Documentation looks good
- Excel sheet looks good
- Project looks good
- Good standing!! On track to 100%!!
- Submission is GitHub repo
  
---

## **Meeting Title:** Team Meeting
### **Date:** Wednesday, September 10th, 2025
---

#### 👥 Attendees

- Navya Nittala, Kundana Dongala, Katie Nordberg, Christina Sorensen, Vivian Lara

#### 📌 Agenda / Discussion Points

1. Update person hours and task board
2. Project status update scrum
3. Outline diagrams
4. Finalize Tkinter
5. Discuss bug in expandOpenCells 

#### ✅ Updates / Decisions Made

- Katie (dev): spent about 30 mins testing the code, look good on windows. mine generation is working well with tkinter as well. expandOpenCells is not working with tkinter, bug deals with console version of it. when tested with Christina there were mines placed but there the mine count wasnt added until recently. it works recursively where it should uncover all the cells which have 0, but it is currently opening all the cells that are not a mine. proposed adding a base case to check if the surrounding mines are 0. 
- Christina (dev): N/A
- Vi (dev): finished the mine calculations. once expandOpenCells bug is fixed, will integrate with UI
- Kundana (PM): worked on TA requests for estimated time sheet excel. Documentation will be done tomorrow.
- Navya (scrum): pushed tkinter UI, will work on diagrams for documentation
- Decision: Diagrams
  - Different States of the Game 
    - Use Vi's UI mockup for this
  - Components Interaction Dataflow
    - boardManager class --> keeps track of rows, columns, mines
    - initializeBoard function --> propogrates and initalizes board content and stare properties as 0, creates an empty board
    - Refer to comments for the rest
  - entire process (from start to finish)
    - combine above 2 to create this one

#### 📋 To-Do Items / Action Items

- [X] fix expandOpenCells bug to open only cells with 0 — **Assigned to:** Christina (devs) | **Deadline:** Thursday, September 11th
  - ESTIMATED PERSON HOURS: 1
  - ACTUAL: 1
- [X] mine calculation UI update — **Assigned to:** Vi (dev) | **Deadline:** Friday, September 12th
  - ESTIMATED PERSON HOURS: 1
  - ACTUAL: 0.5
- [ ] Write out system architecture based on comments — **Assigned to:** Kundana (PM) and Navya (scrum)| **Deadline:** Friday, September 12th
  - ESTIMATED PERSON HOURS: 4
  - ACTUAL: 2
- [ ] Make Logic Diagram — **Assigned to:** Katie (dev) & Navya (scrum) | **Deadline:** Friday, September 12th
  - ESTIMATED PERSON HOURS: 4
  - ACTUAL: 2
- [ ] Make Different States of the Game diagram — **Assigned to:** Vi (dev) | **Deadline:** Friday, September 12th
  - ESTIMATED PERSON HOURS: 1
  - ACTUAL: 1

#### 📅 Next TA Meeting

- **Date:** Thursday, September 11th
- **Time:** 9:30 AM
- **Location / Platform:** EATON 3001

#### 📅 Next Scrum Meeting

- **Date:** Friday, September 5th
- **Time:** 5 PM
- **Location / Platform:** EATON 2

#### 📅 Next Team Meeting

- **Date:** Wednesday, September 17th
- **Time:** 9 AM
- **Location / Platform:** Teams
---

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

- [X] fix expandOpenCells function — **Assigned to:** Christina and Katie (devs) | **Deadline:** Friday, September 5th
  - ESTIMATED PERSON HOURS: 2
  - ACTUAL: 
- [X] mine calculation — **Assigned to:** Vi (dev) | **Deadline:** Friday, September 5th
  - ESTIMATED PERSON HOURS: 1
  - ACTUAL: 
- [X] Implement baseline Tkinter — **Assigned to:** Navya (scrum) | **Deadline:** Friday, September 5th
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

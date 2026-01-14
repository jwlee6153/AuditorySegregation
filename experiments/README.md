# Auditory Segregation Experiment (PsychoPy)

This document describes an auditory segregation experiment built with **PsychoPy**.

---

## 1. Experiment Goal 

The experiment tests whether listeners can detect a **figure tone** embedded
within a sequence of **background chords**.

On each trial, participants decide whether a figure tone was **present or absent**
while different combinations of figure and background stimuli are used.

---

## 2. Overall Experiment Structure

The experiment consists of **three sequential phases**:

1. Practice phase  
2. Threshold calibration phase (staircase)  
3. Main experiment  

Each phase is implemented as a separate PsychoPy routine or script.

---

## 3. Task Description

- **Task:** Figure detection
- **Responses:** Keyboard responses

Each trial presents:
- A short sound sequence
- A response window immediately after playback

---

## 4. Stimulus Structure

### 4.1 Timing

- Total duration per stimulus: **2.4 s**
- Number of chords per stimulus: **40**
- Duration per chord: **60 ms**
- No gaps between chords

---

### 4.2 Background Stimuli

Each trial presents a sequence of background chords. Each chord contains **8 pure tones**.

Two background types are used:

- **Consonant background:** repeated **C-major triad–based** chords  
- **Dissonant background:** chords built from **random tone sets** (no stable tonal center)

Background frequencies cover a wide range and are arranged to avoid tones clustering
in one narrow frequency region.

---

### 4.3 Figure Stimuli

The figure is a **single pure tone** that may be embedded in the background sequence.

Two figure sets are used:

- **In-key (no-sharp) set:** tones that belong to the C-major scale  
- **Out-of-key (sharp) set:** the corresponding sharp-note variants (outside the C-major scale)

On each trial, the figure is either **present** or **absent**.


---

## 5. Experimental Conditions

Each trial is defined by a combination of:

- Background type  
- Figure type  
- Figure presence  

All combinations are presented across the experiment.

---

## 6. Trial Control via Condition CSV

Trial conditions are controlled using an external CSV file loaded into
PsychoPy loops.

Each row corresponds to one trial and specifies which stimulus to present
and how the response should be evaluated.

### 6.1 CSV Columns

- `target` – audio file path for the figure tone  
- `tarcategory` – figure tone category label  
- `background` – background type (e.g., consonant / dissonant)  
- `figure` – figure presence flag (1 = present, 0 = absent)  
- `correct` – correct response key  
- `relation` – figure–background relation label

### 6.2 Usage in PsychoPy

The CSV file is assigned to a PsychoPy loop component.
Values from each row are read automatically on every trial and used to
control stimulus selection and response logging.

---

## 7. Practice Phase

The practice phase familiarizes participants with the task structure.

- Same trial structure as the main experiment
- Figure tone presented at a higher intensity
- Substantially fewer trials
- Feedback provided after each response

---

## 8. Threshold Calibration Phase

This phase calibrates the **intensity of the figure tone** individually for
each participant.

### 8.1 Loop Structure

- Implemented using PsychoPy’s **staircase loop type**
- Separate staircase loops are defined for condition-specific blocks
- Staircase logic is handled directly by PsychoPy’s loop settings

---

### 8.2 Staircase Procedure

- **Method:** 1-up / 2-down adaptive staircase
- The figure tone is **present on every trial**
- Participants indicate whether they heard the figure tone

Rules:
- Two correct detections → figure intensity decreases  
- One missed detection → figure intensity increases  

---

### 8.3 Staircase Parameters

- Initial level difference: **6 dB**
- Step size:
  - Starts at **2 dB**
  - Reduced to **0.5 dB** after multiple reversals
- Each staircase terminates after a fixed number of reversals
- Threshold estimated from the final reversals

The final figure intensity used in the main experiment is derived from the
lowest threshold across blocks to ensure reliable audibility.

---

### 8.4 Threshold Script Organization

The threshold calibration is implemented across **two separate Python files**
(`threshold_1.py` and `threshold_2.py`).

The full calibration consists of **four condition-specific blocks**.
For practical reasons (file size and manageability), these blocks are split
across two scripts, with **two blocks per file**.

Both scripts use identical staircase logic and parameters.

---

## 9. Main Experiment

- Uses the calibrated figure intensity
- No feedback is provided
- Same task structure as the practice phase

In the main experiment, **all condition combinations are fully intermixed**.
Background type, figure type, and figure presence are randomized across trials.

---

## 10. PsychoPy Implementation Notes

- Implemented using **PsychoPy Builder with embedded Python code**
- Stimulus playback uses pre-generated `.wav` files
- Trial logic, condition assignment, and response logging handled in Python
- Separate PsychoPy routines/scripts are used for:
  - Practice
  - Threshold calibration
  - Main experiment

---

## 11. Data Output

- PsychoPy automatically logs:
  - Condition variables
  - Responses
  - Accuracy
  - Reaction times
- Raw data files are generated per participant
- Participant data are **not included** in this repository

# Modified Early Warning Score (MEWS) Calculator

This repository contains a Python implementation of the Modified Early Warning Score (MEWS) calculator. The MEWS is a scoring system used in healthcare to identify patients who are at risk of deteriorating experiencing a medical emergency. This README provides an overview of the MEWS, explains its meaning and applications, and provides step-by-step instructions on how run and use the code.

## Table of Contents
- [Introduction](#introduction)
- [Mean and Applications](#meaning-and-applications)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction
The Modified Early Warning Score (MEWS) is a clinical tool used to assess the severity of a patient's condition based their vital signs. It assigns scores to different physiological parameters such as heart rate, respiratory rate, systolic blood pressure, body temperature, and level of consciousness. By summing up these scores, healthcare professionals can quickly evaluate a patient's overall condition and identify those who may require immediate intervention or closer monitoring.

## Meaning and Applications
TheWS is designed to provide an early warning of clinical deterioration in patients. It helps healthcare providers identify individuals who are risk of developing complications or experiencing a medical emergency. By regularly monitoring and calculating the MEWS score, medical teams can intervene promptly and provide appropriate care to prevent adverse outcomes.

 MEWS score is particularly useful in hospital settings, including emergency departments, intensive care units, and general wards. It enables healthcare professionals to prioritize patient care, allocate resources effectively, and make informed decisions about interventions, such as escalating care, initiating treatment, or transferring patients to higher levels of care.

## Getting Started
To use the MEWS calculator, follow the steps below.

### Prerequisites
- Python 3.x installed on your system

### Installation
1. Clone this repository to your local machine or download the code as a ZIP file.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
To calculate the MEWS score for a patient, you need to provide their vital signs: heart rate, respiratory rate, systolic blood pressure, body temperature, and level of consciousness. The `calculate_mews` function in the `mews` file takes these parameters as input and returns the corresponding MEWS score.

The MEWS score calculated based on the following criteria:

| Vital Sign              | Score |
|-------------------------|-------|
| Heart Rate (HR)         |       |
| &nbsp;&nbsp;≥ 130       | 3     |
| &nbsp;&nbsp;110-129     | 2     |
| &nbsp;&nbsp;100-109     | 1     |
| Respiratory Rate (RR)   |       |
| &nbsp;&nbsp;≥ 30        | 3     |
| &nbsp;&nbsp;21-29       | 2     |
| &nbsp;&nbsp;9-20        | 1     |
| Systolic Blood Pressure (SBP) | |
| &nbsp;&nbsp;≤ 70        | 2     |
| &nbsp;&nbsp;71-100      | 1     |
| Body Temperature        |       |
| &nbsp;&nbsp;≥ 39        | 2     |
| &nbsp;&nbsp;38-38.9     | 1     |
| Level of Consciousness (LOC) |   |
| &nbsp;&nbsp;< 15        | 3     |
| &nbsp;&nbsp;10-14       | 2     |
| &nbsp;&nbsp;13          | 1     |

To calculate the MEWS score, call the `calculate_mews` function and pass the patient's vital signs arguments. The function will return the MEWS score as an integer.

## Example
Here's an example usage of the MEWS calculator:

```python
from mews import calculate_mews

heart_rate = 120
respiratory_rate = 22
systolic_blood_pressure = 90
body_temperature = 37.5
level_of_consciousness = 14

m_score = calculate_mews    heart_rate, respiratory_rate, systolic_blood_pressure,
    body_temperature, level_of_consciousness
)

print("MEWS Score:", mews_score)
```

In this example, the MEWS score is calculated for a patient with the following vital signs- Heart Rate: 120 bpm
- Respiratory Rate: 22 breaths per minute
- Systolic Blood Pressure: 90 mmHg
- Body Temperature: 37.5°C
- Level of Consciousness: 14

 output will be:
``MEWS Score: 2
```

Based on the MEWS score, healthcare professionals can interpret the patient's condition and take appropriate actions.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact
For more information or questions, feel free to reach out:

LinkedIn: [Reza Eghbal](https://www.linkedin.com/in/mreghbal)

Twitter: [Reza Eghbal](https://twitter.com/mreghbal)

Thank you for your interest in this project! Don't forget to follow me on LinkedIn and Twitter for more updates and healthcare-related content.

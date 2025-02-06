"""1527. Patients With a Condition
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces.
This table contains information of the patients in the hospital.


Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes.
Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.
"""

import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains("(^DIAB1.*)|( DIAB1.*)")]

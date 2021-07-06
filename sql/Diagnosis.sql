CREATE TABLE `Diagnosis` (
  `diagnosis_id` int NOT NULL AUTO_INCREMENT,
  `doctor_id` int NOT NULL,
  `patient_id` int NOT NULL,
  `assistant_doctor_id` int NOT NULL,
  `doctor_notes` varchar(255) DEFAULT NULL,
  `doctor_diagnosis` varchar(255) NOT NULL,
  `symptoms_id` int NOT NULL,
  `syndrome_id` int NOT NULL,
  PRIMARY KEY (`diagnosis_id`)
)
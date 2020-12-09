USE tcm

CREATE TABLE `Patient` (
  `user_id` bigint NOT NULL,
  `patient_id` bigint NOT NULL,
  `doctor_id` bigint NOT NULL,
  `diagnosis_id` bigint NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `patient_id_UNIQUE` (`patient_id`)
)
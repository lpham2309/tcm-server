CREATE TABLE `Patient` (
  `user_id` varchar(255) NOT NULL,
  `patient_id` varchar(255) NOT NULL,
  `doctor_id` varchar(128) NOT NULL,
  `diagnosis_id` varchar(255) NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `patient_id_UNIQUE` (`patient_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
)
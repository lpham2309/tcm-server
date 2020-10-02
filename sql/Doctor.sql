CREATE TABLE `Doctors` (
  `user_id` int NOT NULL,
  `doctor_id` int NOT NULL,
  PRIMARY KEY (`doctor_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
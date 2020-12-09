CREATE TABLE `Symptoms` (
  `symptom_id` int NOT NULL DEFAULT '1',
  `symptom_name` varchar(250) NOT NULL,
  `symptom_subgroup_id` int NOT NULL,
  PRIMARY KEY (`symptom_id`),
  KEY `symptom_subgroup_d_idx` (`symptom_subgroup_id`),
  CONSTRAINT `symptom_subgroup_d` FOREIGN KEY (`symptom_subgroup_id`) REFERENCES `Symptom_Subgroups` (`symptom_subgroup_id`) ON DELETE CASCADE ON UPDATE CASCADE
)
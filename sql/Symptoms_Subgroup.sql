CREATE TABLE `Symptom_Subgroups` (
  `symptom_subgroup_id` int NOT NULL AUTO_INCREMENT,
  `symptom_id` int NOT NULL,
  `symptom_subgroup_name` varchar(250) NOT NULL,
  PRIMARY KEY (`symptom_subgroup_id`)
)
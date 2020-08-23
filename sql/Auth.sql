USE tcm

CREATE TABLE `Auth` (
  `auth_user_id` varchar(255) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`auth_user_id`),
  UNIQUE KEY `auth_user_id_UNIQUE` (`auth_user_id`)
)
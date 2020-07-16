CREATE TABLE `tcm`.`users` (
  `user_id` VARCHAR(255) NOT NULL,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `date_of_birth` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `phone_number` INT NOT NULL,
  `gender` VARCHAR(20) NOT NULL,
  `userscol` VARCHAR(45) NULL,
  `auth_user_id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  UNIQUE INDEX `auth_user_id_UNIQUE` (`auth_user_id` ASC) VISIBLE);

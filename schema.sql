-- -----------------------------------------------------
-- Table `FunrestDatabase`.`user`
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `funrestdatabase`;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`user` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `firstname` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `gender` VARCHAR(255) NULL,
  `birthdate` DATE NULL,
  `postcode` INT NULL,
  `city` VARCHAR(255) NULL,
  `street` VARCHAR(255) NULL,
  `phone` INT NULL,
  `regularguest` TINYINT NULL,
  PRIMARY KEY (`userid`));


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`role` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`role` (
  `roleid` INT NOT NULL AUTO_INCREMENT,
  `roleadmin` VARCHAR(45) NULL,
  `rolegast` VARCHAR(45) NULL,
  `rolemitarbeiter` VARCHAR(45) NULL,
  `rolekunde` VARCHAR(45) NULL,
  PRIMARY KEY (`roleid`)); 


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`permission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`permission` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`permission` (
  `permissionid` INT NOT NULL AUTO_INCREMENT,
  `searchrooms` VARCHAR(45) NULL,
  `bookrooms` VARCHAR(45) NULL,
  `ratesite` VARCHAR(45) NULL,
  `createbill` VARCHAR(45) NULL,
  `createentity` VARCHAR(45) NULL,
  `deleteentity` VARCHAR(45) NULL,
  `changeentity` VARCHAR(45) NULL,
  PRIMARY KEY (`permissionid`));


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`userrole`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`userrole` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`userrole` (
  `userroleid` INT NOT NULL,
  `userid_fk` INT NULL,
  `roleid_fk` INT NULL,
  PRIMARY KEY (`userroleid`),
  INDEX `userid_fk_idx` (`userid_fk` ASC),
  INDEX `roleid_fk_idx` (`roleid_fk` ASC),
  CONSTRAINT `userid_fk`
    FOREIGN KEY (`userid_fk`)
    REFERENCES `FunrestDatabase`.`user` (`userid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `roleid_fk`
    FOREIGN KEY (`roleid_fk`)
    REFERENCES `FunrestDatabase`.`role` (`roleid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`rolepermission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`rolepermission` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`rolepermission` (
  `rolepermissionid` INT NOT NULL AUTO_INCREMENT,
  `fk_roleid` INT NULL,
  `fk_permissionid` INT NULL,
  PRIMARY KEY (`rolepermissionid`),
  INDEX `fk_permissionid_idx` (`fk_permissionid` ASC),
  INDEX `fk_roleid_idx` (`fk_roleid` ASC),
  CONSTRAINT `fk_permissionid`
    FOREIGN KEY (`fk_permissionid`)
    REFERENCES `FunrestDatabase`.`permission` (`permissionid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_roleid`
    FOREIGN KEY (`fk_roleid`)
    REFERENCES `FunrestDatabase`.`role` (`roleid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`hotelroom`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`hotelroom` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`hotelroom` (
  `roomid` INT NOT NULL AUTO_INCREMENT,
  `roomname` VARCHAR(255) NULL,
  `kategorie` VARCHAR(255) NULL,
  `preis` VARCHAR(255) NULL,
  PRIMARY KEY (`roomid`));


-- -----------------------------------------------------
-- Table `FunrestDatabase`.`booking`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `FunrestDatabase`.`booking` ;

CREATE TABLE IF NOT EXISTS `FunrestDatabase`.`booking` (
  `bookingid` INT NOT NULL AUTO_INCREMENT,
  `fk_roomid` INT NULL,
  `fk_userid` INT NULL,
  `bookingdate` DATETIME NULL,
  `status` VARCHAR(255) NULL,
  PRIMARY KEY (`bookingid`),
  INDEX `fk_userid_idx` (`fk_userid` ASC),
  INDEX `fk_roomid_idx` (`fk_roomid` ASC),
  CONSTRAINT `fk_userid`
    FOREIGN KEY (`fk_userid`)
    REFERENCES `FunrestDatabase`.`user` (`userid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_roomid`
    FOREIGN KEY (`fk_roomid`)
    REFERENCES `FunrestDatabase`.`hotelroom` (`roomid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`tweet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tweet` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweetId` CHAR(36) NOT NULL,
  `tweetBody` VARCHAR(320) NOT NULL,
  `createdBy` VARCHAR(45) NOT NULL,
  `createdAt` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`hashtag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`hashtag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `text` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tweet_hashtag`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tweet_hashtag` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweetId` INT NOT NULL,
  `hashtagId` INT NOT NULL,
  INDEX `fk_tweet_has_hashtag_hashtag1_idx` (`hashtagId` ASC) VISIBLE,
  INDEX `fk_tweet_has_hashtag_tweet_idx` (`tweetId` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_tweet_has_hashtag_tweet`
    FOREIGN KEY (`tweetId`)
    REFERENCES `mydb`.`tweet` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tweet_has_hashtag_hashtag1`
    FOREIGN KEY (`hashtagId`)
    REFERENCES `mydb`.`hashtag` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE tweet ADD INDEX `user_name_index` (`createdBy`);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 1', 'sbg_user1', '2020-01-02 10:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 2', 'sbg_user2', '2020-01-03 11:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 3', 'sbg_user3', '2021-01-04 09:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 4', 'sbg_user4', '2020-01-05 09:11:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 5', 'sbg_user5', '2020-01-06 10:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 6', 'sbg_user1', '2020-01-07 11:11:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 7', 'sbg_user2', '2020-02-07 05:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 8', 'sbg_user3', '2020-03-07 07:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 9', 'sbg_user4', '2020-01-08 10:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 10', 'sbg_user5', '2022-01-01 11:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 11', 'sbg_user2', '2021-01-01 10:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 12', 'sbg_user2', '2021-01-01 11:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 13', 'sbg_user1', '2014-01-01 11:10:10');
INSERT INTO tweet(tweetId, tweetBody, createdBy, createdAt) VALUES('', 'Some random text 14', 'sbg_user1', '2015-01-01 11:10:10');
UPDATE tweet SET tweetId=(SELECT uuid());

INSERT INTO hashtag(text) VALUES('#hash1');
INSERT INTO hashtag(text) VALUES('#hash2');
INSERT INTO hashtag(text) VALUES('#hash3');
INSERT INTO hashtag(text) VALUES('#hash4');
INSERT INTO hashtag(text) VALUES('#hash5');
INSERT INTO hashtag(text) VALUES('#hash6');
INSERT INTO hashtag(text) VALUES('#hash7');
INSERT INTO hashtag(text) VALUES('#hash8');
INSERT INTO hashtag(text) VALUES('#hash9');
INSERT INTO hashtag(text) VALUES('#hash10');
INSERT INTO hashtag(text) VALUES('#hash11');
INSERT INTO hashtag(text) VALUES('#hash12');
INSERT INTO hashtag(text) VALUES('#hash13');
INSERT INTO hashtag(text) VALUES('#hash14');
INSERT INTO hashtag(text) VALUES('#hash15');
INSERT INTO hashtag(text) VALUES('#hash16');
INSERT INTO hashtag(text) VALUES('#hash17');
INSERT INTO hashtag(text) VALUES('#hash18');
INSERT INTO hashtag(text) VALUES('#hash19');
INSERT INTO hashtag(text) VALUES('#hash20');

INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(1, 1);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(1, 2);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(2, 1);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(3, 3);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(4, 4);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(4, 5);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(4, 6);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(5, 1);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(5, 2);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(6, 6);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(6, 7);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(7, 7);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(8, 8);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(9, 9);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(9, 10);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(10, 10);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(10, 11);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(11, 11);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(11, 12);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(11, 12);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(11, 13);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(12, 12);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(12, 13);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(12, 14);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(12, 15);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(12, 16);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(13, 13);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(13, 17);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(13, 18);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(14, 14);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(14, 19);
INSERT INTO tweet_hashtag(tweetId, hashtagId) VALUES(14, 20);

ALTER TABLE tweet ADD UNIQUE (tweetId);
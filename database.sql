-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: projectdatabase
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(256) DEFAULT NULL,
  `user_surname` varchar(256) DEFAULT NULL,
  `user_email` varchar(256) DEFAULT NULL,
  `username` varchar(256) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `permission` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (13,'Elvedin','Kaltak','s','asdas','gAAAAABgSzA2H_iHotwybDyEnByJ8iO-147_WuiNLz0qNaLA50cdiLSXj-xFXpH3l6aZvv4XjiqbDp2YHvuhiAK3v5Mo9q9H2A==',1,1),(16,'Faris','Huric','a','fare','gAAAAABgS_482H4kEkpjX8219Lz00JEpbqEyzMkZmQgW_xPqz_CkcoHZUQO4TfB5JgATYzmxX63sS1w6spGPkfUir6_jLGh64g==',1,1),(21,'Sandra ','Hill','sadrah1@gmail.com','sandrahh','gAAAAABgTmcjuq3tsdqbJL3Y32Y23OugSE-Aa4T5qsGKyQsmbjcSTg9YTItIjhLUTP430H24AI5g2T2sy33y4ah-yVIm_Iu8wA==',1,0),(22,'Samuel','Jackson','sam.jackson@mail.com','samjack','gAAAAABgTmdrmNvlPh3MTtCHt5xXEhmKniTRkVv1S3ZrAP9FkeBRAHi7yQt7vybCtYfVErazmYQPd9c4kbXpXiDuPrWEavMzWA==',1,1),(23,'Paul ','Crawford','paulcrawford@mail.com','paul1','gAAAAABgTmeWuLbb9BQUi7Otsyrj-9mthnA0U6CGf1nb7W5-ltS9QxEH4t46ctBfh7ekmywr5W75MmO3sWoreSxlFAe7kuO3yg==',1,0),(24,'Karen','Cruz','cruz1karen@hotmail.com','ckaren77','gAAAAABgTme4QoxWWSiaGOVhySoT-y3HlIvlUDX0-9gkc58uu__Fnw9FthcgO8Jb9IUfc-yrpenwhDfTfyhoOVywKEs5O1DtCg==',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-19 14:19:04

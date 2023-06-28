-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognition_system
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Dept` varchar(20) NOT NULL,
  `Course` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Semester` varchar(45) NOT NULL,
  `ID` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Section` varchar(45) NOT NULL,
  `Roll_no` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `DOB` varchar(45) NOT NULL,
  `EmailID` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Teacher` varchar(45) NOT NULL,
  `Photo` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('CSE','B.Tech.','1','2','1','Aditi','A','1','Female','15/06/2001','aditi@gmail.com','9875022570','Delhi','Reena','Yes'),('CSE','M.Tech.','2','4','2','Aman','B','5','Male','10/10/1999','aman123@gmail.com','9870052598','Dehradun','David','Yes'),('BioTech.','B.Tech.','3','6','3','Ritika','C','30','Female','25/02/2002','ritika@gmail.com','8970150965','Dehradun','John','Yes'),('IT','M.Tech.','2','4','4','Rohan','D','10','Male','20/10/1998','rohan121@gmail.com','9632254015','Mumbai','Reena','Yes'),('CSE','B.Tech.','4','8','5','Kritika','A','25','Female','12/12/2001','kritika@gmail.com','7598052089','Lucknow','Reena','Yes'),('Civil','B.Tech.','3','6','6','Priya','D','17','Female','20/01/2002','priya@gmail.com','8521477895','Kolkata','Meena','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-11 19:06:30

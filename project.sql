-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chat_message`
--

DROP TABLE IF EXISTS `chat_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat_message` (
  `uid` int(11) DEFAULT NULL,
  `content` longtext,
  `read_status` enum('已读','未读') DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `send_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_message`
--

LOCK TABLES `chat_message` WRITE;
/*!40000 ALTER TABLE `chat_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friend_list`
--

DROP TABLE IF EXISTS `friend_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friend_list` (
  `uid1` int(11) NOT NULL,
  `uid2` int(11) NOT NULL,
  `user_group` char(10) DEFAULT '默认分组',
  `friend_group` char(10) DEFAULT '默认分组'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friend_list`
--

LOCK TABLES `friend_list` WRITE;
/*!40000 ALTER TABLE `friend_list` DISABLE KEYS */;
INSERT INTO `friend_list` VALUES (1,2,'好友','好友'),(1,3,'好友','同学'),(1,4,'同学','同学'),(1,5,'好友','好友'),(1,6,'好友','好友'),(1,7,'基友','同学'),(2,3,'好友','好友'),(2,4,'同学','同学'),(2,5,'好友','好友'),(2,6,'同学','好友'),(2,7,'好友','闺蜜'),(3,4,'同学','好友'),(3,5,'好友','同学'),(3,6,'同学','同学'),(3,7,'好友','好友'),(4,5,'闺蜜','闺蜜'),(4,6,'好友','好友'),(4,7,'同学','同学'),(5,6,'同学','同学'),(5,7,'好友','同学'),(6,7,'好友','好友');
/*!40000 ALTER TABLE `friend_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game` (
  `uid` int(11) DEFAULT NULL,
  `uname` varchar(20) DEFAULT NULL,
  `score` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'哈哈',120),(2,'哼哼',140),(3,'哈卡',210),(4,'丽丽',176),(5,'何飞',580),(6,'刘芳',620),(7,'宁武',236);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(20) DEFAULT NULL,
  `passwd` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'123','123',NULL,NULL),(2,'987','369',NULL,NULL),(3,'987','456',NULL,NULL),(4,'mxb','123','123456','123456'),(5,'lqq','1020','18502947852','1055978054@qq.com');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(30) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `email` text,
  `birthday` date DEFAULT NULL,
  `signature` longtext,
  `constellation` enum('白羊座','金牛座','双子座','摩羯座','双鱼座','巨蟹座','狮子座','处女座','天秤座','天蝎座','水瓶座','射手座') DEFAULT NULL,
  `city` text,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'哈哈','123456','女',25,'105784521','1990-10-20','不能正常','处女座','西安'),(2,'哼哼','789456','男',29,'19875235641','1986-12-10','说说什么','金牛座','北京'),(3,'哈卡','188975','女',18,'14525578882','1994-03-25','已经同意','摩羯座','上海'),(5,'何飞','427256','男',32,'12451052787','1996-12-01','和工行和','天秤座','咸阳'),(6,'刘芳','254257','女',14,'12428785422','1986-10-10','部分功能','双鱼座','北京'),(7,'宁武','422526','男',44,'19175855281','1996-06-08','更好体验','金牛座','广州'),(8,'彩虹小队','1123456','男',15,'1533sina.com',NULL,NULL,NULL,NULL),(9,'彩虹小队','1123456','男',15,'1533sina.com',NULL,NULL,NULL,NULL),(10,'彩虹小队','1123456','男',15,'1533sina.com',NULL,NULL,NULL,NULL),(11,'彩虹小队','1123456','男',15,'1533sina.com',NULL,NULL,NULL,NULL),(12,'lqq','123456','女',25,'1059978054@qq.com',NULL,NULL,NULL,NULL),(13,'lqq','123456','女',25,'1059978054@qq.com',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-25 20:17:31

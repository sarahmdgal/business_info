-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 09, 2018 at 02:34 PM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `business_info`
--
CREATE DATABASE IF NOT EXISTS `business_info` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `business_info`;

-- --------------------------------------------------------

--
-- Table structure for table `clientinfo`
--

DROP TABLE IF EXISTS `clientinfo`;
CREATE TABLE IF NOT EXISTS `clientinfo` (
  `PersonID` int(11) NOT NULL AUTO_INCREMENT,
  `salut` varchar(5) DEFAULT NULL,
  `firstname` varchar(25) DEFAULT NULL,
  `mid_init` varchar(5) DEFAULT NULL,
  `lastname` varchar(25) DEFAULT NULL,
  `suffix` varchar(5) DEFAULT NULL,
  `title` varchar(40) DEFAULT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `department` varchar(60) DEFAULT NULL,
  `address1` varchar(50) DEFAULT NULL,
  `address2` varchar(40) DEFAULT NULL,
  `suite_no` varchar(10) DEFAULT NULL,
  `city` varchar(25) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `zip_code` varchar(15) DEFAULT NULL,
  `mobile_phone` varchar(15) DEFAULT NULL,
  `office_phone` varchar(15) DEFAULT NULL,
  `home_phone` varchar(15) DEFAULT NULL,
  `fax_phone` varchar(15) DEFAULT NULL,
  `office_email` varchar(40) DEFAULT NULL,
  `home_email` varchar(40) DEFAULT NULL,
  'company_website' varchar(60) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` varchar(5) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PersonID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clientinfo`
--

INSERT INTO `clientinfo` (`PersonID`, `salut`, `firstname`, `mid_init`, `lastname`, `suffix`, `title`, `company_name`, `department`, `address1`, `address2`, `suite_no`, `city`, `state`, `postal_code`, `zip_code`, `mobile_phone`, `office_phone`, `home_phone`, `fax_phone`, `office_email`, `home_email`, `company_website`,`gender`, `age`, `notes`) VALUES
(1, 'Mr.', 'John', 'A.', 'Doe', 'Jr.', 'President', 'Doe Services', '', '123 Anywhere Ln', '', 'Suite 1', 'Anytown ', 'MD', '', '12345', '1234567890', '1234567890', '', '1234567890', 'john@doeservices.com', ,'', '', 'Male', '55', 'Test Record'),
(2, 'Ms.', 'Jenny', 'J.', 'Jones', '', '', '', '', '3 America Pl', 'Apt 1', '', 'Anytown', 'MD', '', '12345', '2345678901', '', '2344568901', '2344568901', '', 'jenny@fake.com', '',  'Female', '30', 'Test Mouse Record 2'),
(3, 'Mr.', 'Mickey', 'M.', 'Mouse', 'III', 'President', 'Mousey Services', 'Cheese Department', '1 Mouse Way', '', 'Suite 100', 'Mouseville', 'MD', '', '99999', '9999999999', '99999999999', '', '9999999999', 'mickey.m.mouse@mouseyservices.com', '', '', 'Male', '50', 'Test Record 3'),
(4, 'Ms.', 'Jane', 'A.', 'Doe', '', 'Executive Assistant', 'Mousey Services', '', '1 Mouse Way', '', 'Suite 100', 'Mouseville', 'MD', '', '99999', '9999999999', '9999999999', '1111111111', '9999999999', 'jane@mouseyservices.com', '', 'jane@fake.com', 'Female', '25', 'Test Record 4'),
(5, 'Mr.', 'James', 'B.', 'Doe', 'Jr.', 'Construction Worker', 'ABC Construction, Inc.', '', '1 Builders Way', '', 'Suite 200', 'Anywhere', 'MD', '', '12345', '999999999', '9999999999', '9999999999', '9999999999', '', '', '', 'Male', '45', 'Great employee!');
COMMIT;

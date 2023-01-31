-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2023 at 05:27 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stud_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `marks_master`
--

CREATE TABLE `marks_master` (
  `markid` int(5) NOT NULL,
  `RegNo` varchar(50) NOT NULL,
  `Semester` varchar(10) NOT NULL,
  `Subcode` varchar(50) NOT NULL,
  `SubName` varchar(100) NOT NULL,
  `Credit` varchar(10) NOT NULL,
  `Grade` varchar(10) NOT NULL,
  `GradePoint` varchar(10) NOT NULL,
  `Result` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marks_master`
--

INSERT INTO `marks_master` (`markid`, `RegNo`, `Semester`, `Subcode`, `SubName`, `Credit`, `Grade`, `GradePoint`, `Result`) VALUES
(1, '18RK001', '1', 'UCB1181', 'Induction Program', '1', 'EX', '10', 'Pass'),
(2, '18RK001', '1', 'UHS1161', 'BusinessCommunication and Value Science I', '3', 'EX', '10', 'Pass'),
(3, '18RK001', '1', 'UPH1152', 'Physics For Computing Science', '4', 'B', '8', 'Pass'),
(4, '18RK001', '1', 'UGE1162', 'Computer Programming', '4', 'C', '7', 'Pass'),
(5, '18RK001', '1', 'UBE1162', 'Principles of Electrical Engineering', '4', 'D', '6', 'Pass'),
(6, '18RK001', '1', 'UMA1153', 'Probability and Statistics', '4', 'A', '9', 'Pass'),
(7, '18RK001', '1', 'UMA1152', 'Discreete Mathematics', '4', 'D', '6', 'Pass'),
(8, '18RK001', '2', 'UCB1281', 'Environmental Science and Engineering', '0', 'EX', '10', 'Pass'),
(9, '18RK001', '2', 'UMA1253', 'Statistical Modeling', '4', 'A', '9', 'Pass'),
(10, '18RK001', '2', 'UBE1262', 'Principles of Electronics Engineering', '4', 'B', '8', 'Pass'),
(11, '18RK001', '2', 'UGE1262', 'Data Structures', '4', 'C', '7', 'Pass'),
(12, '18RK001', '2', 'UCB1201', 'Fundamentals of Economics', '4', 'C', '7', 'Pass'),
(13, '18RK001', '2', 'UHS1253', 'Business Communication and Value Science  II', '3', 'RA', '0', 'Fail'),
(14, '18RK001', '2', 'UMA1252', 'Linear Algebra', '4', 'A', '9', 'Pass'),
(15, '18RK0012374893274', '2', 'UCB1201', 'Fundamentals of Economics', '4', 'C', '7', 'Pass'),
(16, '', '2', 'UCB1201', 'Fundamentals of Economics', '4', 'C', '7', 'Pass'),
(17, '18RK001', '3', 'UCB1381', 'Online Certification Course', '0', 'A', '9', 'Pass'),
(18, '18RK001', '3', 'UMA1355', 'Computational Statistics', '4', 'B', '8', 'Pass'),
(19, '19KK001', '1', 'UCB1181', 'Induction Program', '1', 'EX', '10', 'Pass');

-- --------------------------------------------------------

--
-- Table structure for table `student_master`
--

CREATE TABLE `student_master` (
  `StudId` int(11) NOT NULL,
  `RegNo` varchar(20) NOT NULL,
  `StudentName` varchar(100) NOT NULL,
  `Course` varchar(75) NOT NULL,
  `FatherName` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `EmailId` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_master`
--

INSERT INTO `student_master` (`StudId`, `RegNo`, `StudentName`, `Course`, `FatherName`, `City`, `Phone`, `EmailId`) VALUES
(1, '18RK001', 'Das', 'Computer Science', 'Hari', 'Madurai', '9012891290', 'das@gmail.com'),
(2, '18CSRK005', 'Pankaj', 'Computer Science', 'Gupta', 'Trichy', '8989128912', 'pankaj@gmail.com'),
(3, '17CS005', 'Vidhya', 'Computer Science', 'Ramar', 'Madurai', '8912901289', 'vidhya@gmail.com'),
(4, '18RKME005', 'Narayanan', 'Mechanical', 'Shankar', 'Trichy', '9012901290', 'nara@gmail.com'),
(5, '18RKCV001', 'Prasanth', 'Civil', 'Balker', 'Cuddalore', '8890129812', 'prasanth@gmail.com'),
(6, '19CSRK010', 'Rama', 'Computer Science', 'Krishnan', 'Dharmapuri', '7812891289', 'rama@gmail.com'),
(7, '20CSRK0075', 'Farooq', 'Information Technology ', 'Ahmed', 'Coimbatore', '9089908912', 'farooq@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `subject_master`
--

CREATE TABLE `subject_master` (
  `subid` int(10) NOT NULL,
  `subcode` varchar(50) NOT NULL,
  `subname` varchar(100) NOT NULL,
  `credits` varchar(10) NOT NULL,
  `semester` varchar(5) NOT NULL,
  `semcode` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject_master`
--

INSERT INTO `subject_master` (`subid`, `subcode`, `subname`, `credits`, `semester`, `semcode`) VALUES
(1, 'UCB1181', 'Induction Program', '1', '1', 'SEM1'),
(2, 'UHS1161', 'BusinessCommunication and Value Science I', '3', '1', 'SEM1'),
(3, 'UPH1152', 'Physics For Computing Science', '4', '1', 'SEM1'),
(4, 'UGE1162', 'Computer Programming', '4', '1', 'SEM1'),
(5, 'UBE1162', 'Principles of Electrical Engineering', '4', '1', 'SEM1'),
(6, 'UMA1153', 'Probability and Statistics', '4', '1', 'SEM1'),
(7, 'UMA1152', 'Discreete Mathematics', '4', '1', 'SEM1'),
(8, 'UCB1281', 'Environmental Science and Engineering', '0', '2', 'SEM2'),
(9, 'UMA1253', 'Statistical Modeling', '4', '2', 'SEM2'),
(10, 'UBE1262', 'Principles of Electronics Engineering', '4', '2', 'SEM2'),
(11, 'UGE1262', 'Data Structures', '4', '2', 'SEM2'),
(12, 'UCB1201', 'Fundamentals of Economics', '4', '2', 'SEM2'),
(13, 'UHS1253', 'Business Communication and Value Science  II', '3', '2', 'SEM2'),
(14, 'UMA1252', 'Linear Algebra', '4', '2', 'SEM2'),
(15, 'UCB1381', 'Online Certification Course', '0', '3', 'SEM3'),
(16, 'UMA1355', 'Computational Statistics', '4', '3', 'SEM3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `marks_master`
--
ALTER TABLE `marks_master`
  ADD PRIMARY KEY (`markid`);

--
-- Indexes for table `student_master`
--
ALTER TABLE `student_master`
  ADD PRIMARY KEY (`StudId`);

--
-- Indexes for table `subject_master`
--
ALTER TABLE `subject_master`
  ADD PRIMARY KEY (`subid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `marks_master`
--
ALTER TABLE `marks_master`
  MODIFY `markid` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `student_master`
--
ALTER TABLE `student_master`
  MODIFY `StudId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `subject_master`
--
ALTER TABLE `subject_master`
  MODIFY `subid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

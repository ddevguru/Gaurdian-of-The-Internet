-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2024 at 02:53 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kuchbhi`
--

-- --------------------------------------------------------

--
-- Table structure for table `ad_transactions`
--

CREATE TABLE `ad_transactions` (
  `id` int(11) NOT NULL,
  `ad_platform` varchar(50) DEFAULT NULL,
  `clicks` int(11) DEFAULT NULL,
  `impressions` int(11) DEFAULT NULL,
  `ip_address` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `browser` varchar(50) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `charity_fund_transactions`
--

CREATE TABLE `charity_fund_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `charity_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `donation_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `credit_card_transactions`
--

CREATE TABLE `credit_card_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `merchant_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `credit_card_transactions`
--

INSERT INTO `credit_card_transactions` (`id`, `amount`, `user_id`, `merchant_id`, `location`, `result`, `submission_time`) VALUES
(1, 1250.00, 1002, '2002', 'Chicago', 'Fraudulent', '2024-07-21 05:42:07');

-- --------------------------------------------------------

--
-- Table structure for table `email_submissions`
--

CREATE TABLE `email_submissions` (
  `id` int(11) NOT NULL,
  `emailcontent` varchar(255) DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `email_submissions`
--

INSERT INTO `email_submissions` (`id`, `emailcontent`, `result`, `submission_time`) VALUES
(1, '\"Hello, we wanted to thank you for your recent purchase...\"', 'Genuine email', '2024-07-20 17:40:34');

-- --------------------------------------------------------

--
-- Table structure for table `gift_card_transactions`
--

CREATE TABLE `gift_card_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `merchant_id` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `gift_card_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `insurance_claims`
--

CREATE TABLE `insurance_claims` (
  `id` int(11) NOT NULL,
  `claimant_name` varchar(100) DEFAULT NULL,
  `claim_amount` decimal(10,2) DEFAULT NULL,
  `claim_description` text DEFAULT NULL,
  `claim_date` date DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `insurance_claims`
--

INSERT INTO `insurance_claims` (`id`, `claimant_name`, `claim_amount`, `claim_description`, `claim_date`, `result`, `submission_time`) VALUES
(1, 'Jane Smith', 20000.00, 'Fire damage to property', '2024-07-15', 'Fraudulent claim detected', '2024-07-20 18:58:08');

-- --------------------------------------------------------

--
-- Table structure for table `otp_transactions`
--

CREATE TABLE `otp_transactions` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `otp_type` varchar(100) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `referral_promo_transactions`
--

CREATE TABLE `referral_promo_transactions` (
  `id` int(11) NOT NULL,
  `referral_code` varchar(50) DEFAULT NULL,
  `promo_code` varchar(50) DEFAULT NULL,
  `num_referrals` int(11) DEFAULT NULL,
  `total_spent` decimal(10,2) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sms_submissions`
--

CREATE TABLE `sms_submissions` (
  `id` int(11) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `sms_message` text NOT NULL,
  `result` varchar(50) NOT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sms_submissions`
--

INSERT INTO `sms_submissions` (`id`, `phone_number`, `sms_message`, `result`, `submission_time`) VALUES
(1, '7028196172', '\"Hello, we wanted to thank you for your recent purchase.\"', '<function result at 0x000001DF27D8B380>', '2024-07-20 18:13:11'),
(2, '7028196172', '\"Hello, we wanted to thank you for your recent purchase.\"', '<function result at 0x000001DF27D8B380>', '2024-07-20 18:31:03'),
(3, '7028196172', '\"Hello, we wanted to thank you for your recent purchase.\"', '<function result at 0x000001CEC168B380>', '2024-07-20 18:32:25'),
(4, '8329023187', '\"Hello, we wanted to thank you for your recent purchase.\"', '<function result at 0x0000022A4E78B380>', '2024-07-20 18:38:33'),
(5, '702819172', '\"Hello, we wanted to thank you for your recent purchase.\"', 'Genuine SMS', '2024-07-20 18:41:01');

-- --------------------------------------------------------

--
-- Table structure for table `url_transactions`
--

CREATE TABLE `url_transactions` (
  `id` int(11) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phonenumber` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `email`, `phonenumber`, `password`) VALUES
(1, 'Deepak Mishra', 'deepak', '121deepak2104@sjcem.edu.in', '2147483647', 'deepak');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_submissions`
--

CREATE TABLE `user_submissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `data` text DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `submission_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ad_transactions`
--
ALTER TABLE `ad_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `charity_fund_transactions`
--
ALTER TABLE `charity_fund_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `credit_card_transactions`
--
ALTER TABLE `credit_card_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `email_submissions`
--
ALTER TABLE `email_submissions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gift_card_transactions`
--
ALTER TABLE `gift_card_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `insurance_claims`
--
ALTER TABLE `insurance_claims`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `otp_transactions`
--
ALTER TABLE `otp_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `referral_promo_transactions`
--
ALTER TABLE `referral_promo_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sms_submissions`
--
ALTER TABLE `sms_submissions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `url_transactions`
--
ALTER TABLE `url_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_submissions`
--
ALTER TABLE `user_submissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ad_transactions`
--
ALTER TABLE `ad_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `charity_fund_transactions`
--
ALTER TABLE `charity_fund_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `credit_card_transactions`
--
ALTER TABLE `credit_card_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `email_submissions`
--
ALTER TABLE `email_submissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `gift_card_transactions`
--
ALTER TABLE `gift_card_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `insurance_claims`
--
ALTER TABLE `insurance_claims`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `otp_transactions`
--
ALTER TABLE `otp_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `referral_promo_transactions`
--
ALTER TABLE `referral_promo_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sms_submissions`
--
ALTER TABLE `sms_submissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `url_transactions`
--
ALTER TABLE `url_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_submissions`
--
ALTER TABLE `user_submissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user_submissions`
--
ALTER TABLE `user_submissions`
  ADD CONSTRAINT `user_submissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-11-2024 a las 17:13:57
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `teachers`
--

CREATE TABLE `teachers` (
  `id` int(7) NOT NULL,
  `worker_id` int(10) NOT NULL,
  `specially` varchar(40) COLLATE utf8mb4_spanish_ci NOT NULL,
  `worker_name` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `register_date` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `update_date` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `teachers`
--

INSERT INTO `teachers` (`id`, `worker_id`, `specially`, `worker_name`, `register_date`, `update_date`) VALUES
(2, 22784, 'Mecanica', 'Leandro', '2024/11/23 12:13:03', '2024/11/23 16:30:33'),
(3, 33654, 'Redes', 'Irving', '26/10/2024 19:23:19', '26/10/2024 19:32:19'),
(4, 22125, 'Entornos Virtuales', 'Jair', '26/10/2024 19:23:46', '26/10/2024 19:33:19'),
(7, 22123, 'Redes', 'Diego', '27/10/2024 19:26:09', '27/10/2024 19:26:09'),
(8, 22123, 'Redes', 'Angel', '27/10/2024 19:28:38', '27/10/2024 19:28:38'),
(9, 22100, 'Redes', 'Enrique', '27/10/2024 19:30:54', '27/10/2024 19:30:54');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

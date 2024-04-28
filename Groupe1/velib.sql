-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 28 avr. 2024 à 19:03
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `velib`
--

-- --------------------------------------------------------

--
-- Structure de la table `favoris`
--

CREATE TABLE `favoris` (
  `id_favoris` int(10) NOT NULL,
  `id_user` int(10) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `data_json` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `favoris`
--

INSERT INTO `favoris` (`id_favoris`, `id_user`, `nom`, `data_json`) VALUES
(1, 1, 'Lotus', '{\"name\": \"Mairie de Rosny-sous-Bois\", \"numbikesavailable\": \"11\", \"numdocksavailable\": \"17\", \"ebike\": \"7\", \"mechanical\": \"4\"}'),
(2, 1, 'Lotus', '{\"name\": \"R\\u00e9union - Avron\", \"numbikesavailable\": \"0\", \"numdocksavailable\": \"24\", \"ebike\": \"0\", \"mechanical\": \"0\"}'),
(3, 0, 'Fleurs', '{\"name\": \"Mairie de Montreuil\", \"numbikesavailable\": \"1\", \"numdocksavailable\": \"50\", \"ebike\": \"0\", \"mechanical\": \"1\"}'),
(4, 1, 'Fleurs', '{\"name\": \"Saint-Mande - Picpus\", \"numbikesavailable\": \"4\", \"numdocksavailable\": \"31\", \"ebike\": \"4\", \"mechanical\": \"0\"}'),
(5, 1, 'Fleurs', '{\"name\": \"Boulets - Voltaire\", \"numbikesavailable\": \"5\", \"numdocksavailable\": \"18\", \"ebike\": \"2\", \"mechanical\": \"3\"}'),
(6, 1, 'Kiwi', '{\"name\": \"Roquette - Thi\\u00e9r\\u00e9\", \"numbikesavailable\": \"17\", \"numdocksavailable\": \"2\", \"ebike\": \"2\", \"mechanical\": \"15\"}'),
(7, 1, 'Chien', '{\"name\": \"Reynaldo Hahn - Lagny\", \"numbikesavailable\": \"2\", \"numdocksavailable\": \"17\", \"ebike\": \"1\", \"mechanical\": \"1\"}');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id_user` int(10) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`) VALUES
(1, 'Loic', '');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `favoris`
--
ALTER TABLE `favoris`
  ADD PRIMARY KEY (`id_favoris`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `favoris`
--
ALTER TABLE `favoris`
  MODIFY `id_favoris` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- Initialize Database Schema for Dataset2 (Concrete Data)
-- Database: beton
-- Description: Concrete compressive strength dataset with ingredient compositions and age

USE beton;

-- Create table for concrete data
CREATE TABLE IF NOT EXISTS concrete_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cement DECIMAL(10, 4) NOT NULL COMMENT 'Cement content in kg/m³',
    blast DECIMAL(10, 4) NOT NULL COMMENT 'Blast furnace slag content in kg/m³',
    fly_ash DECIMAL(10, 4) NOT NULL COMMENT 'Fly ash content in kg/m³',
    water DECIMAL(10, 4) NOT NULL COMMENT 'Water content in kg/m³',
    superplasticizer DECIMAL(10, 4) NOT NULL COMMENT 'Superplasticizer content in kg/m³',
    coarse_aggregate DECIMAL(10, 4) NOT NULL COMMENT 'Coarse aggregate content in kg/m³',
    fine_aggregate DECIMAL(10, 4) NOT NULL COMMENT 'Fine aggregate content in kg/m³',
    age INT NOT NULL COMMENT 'Age of concrete in days',
    strength DECIMAL(10, 4) NOT NULL COMMENT 'Compressive strength in MPa',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_age (age),
    INDEX idx_strength (strength)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create view for data analysis
CREATE VIEW concrete_summary AS
SELECT 
    COUNT(*) as total_records,
    ROUND(AVG(strength), 2) as avg_strength,
    ROUND(MIN(strength), 2) as min_strength,
    ROUND(MAX(strength), 2) as max_strength,
    ROUND(AVG(cement), 2) as avg_cement,
    ROUND(AVG(water), 2) as avg_water,
    ROUND(AVG(age), 0) as avg_age
FROM concrete_data;

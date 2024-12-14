# 🚗 Vehicle Specifications and Pricing Analysis

## 📑 Project Overview
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white) 

This project involves the analysis of a dataset containing vehicle specifications and pricing information. 
The primary focus is to explore the relationship between the wheelbase and price across various vehicle categories.
The insights derived from this analysis aim to enhance the understanding of market dynamics and provide valuable information about vehicle pricing trends.

## Dataset Description
The dataset comprises the following columns:

- **normalized-losses**: Normalised average loss of a vehicle’s value.
- **make**: Manufacturer or brand of the vehicle (e.g., alfa-romero, Audi).
- **fuel-type**: Type of fuel used by the vehicle (e.g., gas, diesel).
- **aspiration**: Engine aspiration type (e.g., standard, turbo).
- **num-of-doors**: Number of doors on the vehicle.
- **body-style**: Vehicle’s body style (e.g., convertible, sedan).
- **wheelbase**: Distance between the front and rear axles (in inches).
- **number-of-cylinders**: Number of cylinders in the engine.
- **engine-size**: Size of the engine (in liters).
- **compression-ratio**: Ratio of the cylinder volume at different piston positions.
- **horsepower**: Engine power output (in horsepower).
- **peak-rpm**: Engine speed at which peak horsepower is achieved (in RPM).
- **city-mpg**: Fuel efficiency in city driving (in MPG).
- **highway-mpg**: Fuel efficiency in highway driving (in MPG).
- **price**: Vehicle price (in USD).

### Removed Columns
The following columns were removed from the dataset as they were not relevant for the analysis:
- `drive-wheels`
- `symboling`
- `engine-location`
- `fuel-system`
- `stroke`
- `bore`
- `length`
- `width`
- `height`
- `curb-weight`

## 🧼 Data Cleaning Process
1. **Viewing Initial Data**: The `head()` method was used to inspect the first few rows of the dataset.
2. **Data Type Conversion**:
   - The following columns were converted to `numpy.int64`:
     - `normalised-losses`
     - `price`
     - `peak-rpm`
     - `horsepower`
3. **Handling Missing Data**:
   - Missing values were represented by `?` in the dataset.
   - These were replaced with `numpy.nan`.
   - Missing numeric values were replaced with the mean of their respective columns.

### Summary of Missing Values
| Column              | Missing Values |
|---------------------|----------------|
| normalised-losses   | 42             |
| num-of-doors        | 2              |
| horsepower          | 2              |
| peak-rpm            | 2              |
| price               | 4              |

## Categories of Vehicles 🚙
The dataset includes the following categories of vehicles:
- Convertible
- Wagon
- Sedan
- Hatchback
- Hardtop

## 🥅 Analysis Goals
- Identify trends and insights into the relationship between wheelbase and price.
- Understand pricing dynamics across different vehicle categories.

## ⚒️ Tools and Technologies
- **Programming Language**: Python
- **Libraries Used**:
  - `numpy`: For handling numerical operations.
  - `pandas`: For data manipulation and analysis.

## 📈 Results
Key findings and visualizations are saved in the `results/` folder. These include:
- Trends in pricing based on wheelbase.
- Comparative analysis across vehicle categories.

# 📷 Screenshots
## 💰Price Distribution
![image](https://github.com/user-attachments/assets/f26aa9e2-73a2-400f-b92a-6f7e48b99566)

## Scatterplot of Price vs Wheelbase and Body Style
![image](https://github.com/user-attachments/assets/d0ee612e-7711-4d73-a4cb-193b32dc811d)

## Boxplot of Normalized Losses and Vehicle Type
![image](https://github.com/user-attachments/assets/d7f8715b-63e4-416f-a18e-0dcbcf4c4590)

## Acknowledgments
Special thanks to the HyperionDev community and mentors for their continuous support.

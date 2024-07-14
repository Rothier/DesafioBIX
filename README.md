# Data Science Applied to Maintenance Planning Optimization

A new data science consulting company was hired to solve and improve the maintenance planning of an outsourced transport company. The company maintains an average number of trucks in its fleet to deliver across the country. However, over the past three years, they have noticed a significant increase in expenses related to the maintenance of the air systems in their vehicles, despite keeping the size of their fleet relatively constant. The maintenance cost of this specific system is shown below in dollars:

## Objective

Your objective as a consultant is to decrease the maintenance costs of this particular system. Maintenance costs for the air system may vary depending on the actual condition of the truck.

- **If a truck is sent for maintenance, but no defect in this system is found:** 
  - Charge: $10 for the time spent during the inspection by the specialized team.
- **If a truck is sent for maintenance and it is defective in this system:**
  - Charge: $25 to perform the preventive repair service.
- **If a truck with defects in the air system is not sent directly for maintenance:**
  - Charge: $500 to carry out corrective maintenance, considering labor, replacement of parts, and other possible inconveniences (e.g., truck broke down in the middle of the track).

## Project Information

During the alignment meeting with those responsible for the project and the company's IT team, the following information was provided:

- The technical team will make all information regarding the air system of the trucks available to you. However, for bureaucratic reasons related to company contracts, all columns had to be encoded.
- Due to the company's recent digitization, some information may be missing from the database provided to you.

### Classification Information

The source of information comes from the company's maintenance sector. They have created a column in the database called `class`:
- `pos`: Trucks that had defects in the air system.
- `neg`: Trucks that had a defect in any system other than the air system.

## Requirements and Expectations

The project stakeholders are very excited about this initiative. They have outlined the following main requirements for a technical proof of concept:
1. **Can we reduce our expenses with this type of maintenance using AI techniques?**
2. **Can you present the main factors that indicate a possible failure in this system?**

These points are crucial to convince the executive board to embrace the initiative and apply it to other maintenance systems during the year 2022.

## Database Information

- **File:** `air_system_present_year.csv`
- **Description:** Contains all information from the maintenance sector for this year. Any missing value in the database is denoted by `na`.

---

Feel free to adjust any sections as needed to better fit the project's requirements.

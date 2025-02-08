# DVB-T Service Disruption Pattern Analysis

This Python script analyzes patterns in DVB-T transmission equipment events, focusing on identifying sequences of events that precede major service disruptions. The tool is designed to detect recurring event patterns that might be predictive of future technical issues.

## Features

- Analysis of DVB-T transmission data from CSV files
- Identification of event patterns preceding service disruptions
- Graphical visualization of results using matplotlib
- Support for multiple equipment types 
- Specific focus on MUX-R10 service

## Requirements

- Python 3.x
- pandas
- matplotlib
- 
## Input CSV Structure

The CSV file must contain the following columns:
- Dataevento (Event Date, format: DD/MM/YYYY HH:MM)
- Sito (Site)
- Classe (Class)
- Servizio (Service)
- Apparato (Equipment)
- Disservizio (Disruption)
- Descrizione (Description)
- Gravita (Severity)

## How It Works

The script performs the following operations:
1. Loads data from the specified CSV
2. Converts dates to the correct format
3. Filters data for specific equipment and services
4. For each "TSV Disservizio" (Service Disruption) event:
   - Analyzes the previous 5 rows
   - Counts occurrences of different event types
   - Accumulates these patterns in a DataFrame
5. Displays results in a bar chart

## Output

- Console output of found service disruption events
- Count of events preceding disruptions
- Bar chart showing the frequency of preceding events

- 

{{ config(materialized='table') }}

WITH filtered_data AS (
    SELECT *
    FROM {{ source('public', 'telegram_medical_data') }}
)

SELECT
    filtered_data."Date",
    filtered_data."Channel Title", 
    filtered_data."Channel Username", 
    filtered_data."ID", 
    filtered_data."Message", 
    filtered_data."Media Path",
    CASE 
        -- Check if the "@" character is present in the Message
        WHEN POSITION('@' IN filtered_data."Message") > 0 
        THEN SPLIT_PART(filtered_data."Message", '@', 2)  -- Extract everything after "@"
        ELSE NULL  -- Return NULL if no "@" is present
    END AS Location  -- Extracted location name after the "@"
FROM filtered_data

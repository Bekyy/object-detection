
{{ config(materialized='table') }}

SELECT * 
FROM public.telegram_medical_data


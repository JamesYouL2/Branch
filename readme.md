# Take Home Test for Branch

## Suggested Improvements

We need to try to make sure we're not overwriting data.
So, to make this product a little more robust, I would add a column in the data to show some kind of timestamp or date to show when I pulled this data.  
I would also use that to name the csvs so we could keep a historical record.  
We also need some kind of scheduler/orchestrator to handle that part of it (airflow/prefect/dagster etc).
I would add more tables depending on business use case.
The script should be inside a function instead of just standing alone.
From an injestion standpoint, it should have error cases for when the API call throws up an error (400, 529, etc). 
It should have error cases if the json isn't formatted as expected (making sure column names are consistent, everything is under results, etc).
Lastly, I'd have a direct downstream table of this where I clean up dates and put them in a datetime column, do phone number and email syntax verification, and make sure the thumnail urls are valid.
# Individual API calls are the building block. A production script is a structure: configuration,
#  fetch functions, processing functions, and output, all wired together cleanly. 
# This lesson shows you how to organize API code so it is readable, reusable, and easy to extend.

#👉 The Four-Part Structure
# A well-organized API script has four parts. Configuration holds all settings (URL, keys, parameters) in one place.
# Fetch makes the HTTP request and handles errors.
# Process transforms raw data into what you need. 
# Output prints, saves, or sends the results.

# Think of a milk collection centre at a dairy cooperative.
# Configuration: which farms are registered, what is the minimum daily target.
#Fetch: collect the morning readings from each farm. Process: calculate each farm's totals, flag those below target,compute the day's average. 
# Output: print the daily report, update the payment ledger. Each stage has one job. 
# The person doing the collection does not also handle payments on the same trip.

# Keeping these four stages separate makes the script easier to debug.
#  When something breaks, you know immediately which stage to look at.
# Maps and Location Data — Notes

## Summary
Covers latitude and longitude (with degree-minute-second examples for four cities), nautical miles, the haversine formula for great-circle distance, geocoding and reverse geocoding with the Google API, and a Plotly annotated map.

## Changes in this pass
- Corrected "New South Whales" to "New South Wales."
- Replaced a broken fragment ("Note some do not") with a sentence about decimal degrees.
- Used proper prime and double-prime marks for the minutes and seconds.
- Fixed the sin² typeset in the haversine definition.
- Changed the pip install line to a shell block, and fixed two print statements with stray f-string or punctuation issues.
- Replaced backticks with \texttt for code names.

## Strengths
- The DMS values match the decimal coordinates (for example, London 51°30′26″ N ≈ 51.507).
- The haversine formula and the atan2 form are correct.
- The nautical mile conversion (1.852 km ≈ 1.15078 statute miles) is correct.

## Open items
- The API examples need a real Google API key, which the book cannot provide. The text says so.
- The Plotly example has not been run here.

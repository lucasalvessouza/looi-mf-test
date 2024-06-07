Background
We have a list of purchase orders, each with their Purchase Order ID, and their cost.

The Purchase Order ID contains: the vendor we purchased from, an order counter (integer), and the type of order.

Our vendors are:

Alabama Architectures (aka: AA)
Brooklyn Batteries (aka BB)
Colorado Chips (aka: CC)
Delaware Diodes (aka: DD)
The order counter is the unique sequential identifier of this order.

The types of orders are Parts (P) and Circuit Boards (C).

For example -- If an ID was structured as "CC-12-P", that would mean we purchased from the vendor named CC, it's our 12th order from them, and that we ordered a Part.

Requirements
We need you to fetch a file containing the Purchase Orders from https://mf-public-demo-files.s3.amazonaws.com/pos.json

Print an integer indicating the total number of Purchase Orders that we placed

After that's complete, continue to part 2


New Requirements
Print a list of all the Purchase Order Ids and their respective costs.

The list should be grouped by Vendor, and sorted by cost in decreasing order, such that we see the most expensive to least expensive Purchase Orders for each Vendor.
Please Output the Vendors in the following order: AA, BB, CC, DD
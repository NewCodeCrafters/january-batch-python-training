# Create 2 Tables => Parent and Children

## Create a Database called `Family`

## Parent Table fields:
- id
- first_name,
- last_name,
- age,
- role ("mother", "father") 
- occupation

## Children Table fields:
- id
- first_name,
- other_name,
- age,
- gender,
- parent_id (referencing the `id` field in the Parents table)

### Tasks
- Create 5 parents
- 15 Children 
- Make sure They are linked together
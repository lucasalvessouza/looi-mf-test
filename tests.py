from index import grouped_orders

def test_grouping_data():
  mock_data = [
    {
      "id": "DD-2-P",
      "cost": 41.46
    },
    {
      "id": "DD-8-P",
      "cost": 18.59
    },
    {
      "id": "AA-4-C",
      "cost": 25.86
    },
  ]

  expected_result = {
    'AA': [
      {
        "id": "AA-4-C",
        "cost": 25.86
      }
    ],
    'DD': [
       {
        "id": "DD-2-P",
        "cost": 41.46
      },
      {
        "id": "DD-8-P",
        "cost": 18.59
      },
    ]
  }

  assert grouped_orders(mock_data) == expected_result

def test_passing_empty_data():
  mock_data = []
  expected_result = {}
  assert grouped_orders(mock_data) == expected_result
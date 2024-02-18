import json

json_data = '''
{
  "interface-status": [
    {
      "DN": "topology/pod-1/node-201/sys/phys-[eth1/33]",
      "Description": "inherit",
      "Speed": "9150",
      "MTU": "9150"
    },
    {
      "DN": "topology/pod-1/node-201/sys/phys-[eth1/34]",
      "Description": "inherit",
      "Speed": "9150",
      "MTU": "9150"
    },
    {
      "DN": "topology/pod-1/node-201/sys/phys-[eth1/35]",
      "Description": "inherit",
      "Speed": "9150",
      "MTU": "9150"
    }
  ]
}
'''


data = json.loads(json_data)


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data["interface-status"]:
    print("{:<50} {:<20} {:<10} {:<6}".format(
        interface["DN"],
        interface["Description"],
        interface["Speed"],
        interface["MTU"]
    ))

from azure.servicebus import ServiceBusService, Message, Queue

bus_service = ServiceBusService(
	service_namespace="",
	shared_access_key_name="",
	shared_access_key_value="")


#instantiates new queues/eventhubs/cloud services for a new team
def createTeam():

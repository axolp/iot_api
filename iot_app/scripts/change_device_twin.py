from azure.iot.hub import IoTHubRegistryManager

def upadteTwin(desiredState):
    flag= False
    # Connection string do IoT Hub
    CONNECTION_STRING = "HostName=roletyHUB.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=JLESadk1V7PJrjzg0H9umYopJq9X1uUX1AIoTDqnRHE="
    DEVICE_ID = "pi5"

    # Tworzymy klienta do zarządzania IoT Hub
    registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

    # Zmieniamy Desired Properties
    alowed_states= ["true", "false"]
    if desiredState in alowed_states:
        desired_properties = {
            "desired": {
                "rollers_down": desiredState,  # Zmień parametr
            }
        }
        # Aktualizujemy Twin urządzenia
        twin = registry_manager.get_twin(DEVICE_ID)
        twin_patch = {"properties": desired_properties}
        updated_twin = registry_manager.update_twin(DEVICE_ID, twin_patch, twin.etag)
        flag= True
        print("Device Twin updated successfully.")
    else:
        print("wrong arguemnt")

    return flag


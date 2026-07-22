test_settings = {'theme':'light'}
def add_setting(settings,new_settings):
    key,value = new_settings
    key = key.lower()
    value = str(value).lower()

    if key in settings:
        return "Setting 'theme' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings,new_setting):
    key,value = new_setting
    key = key.lower()
    value = str(value).lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings,key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
        
    return output

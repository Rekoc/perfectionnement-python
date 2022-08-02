subscriptions = {}
trigger = {}

def event(event: str):
    global subscriptions
    global trigger
    # Return method to call when event "ev" is passed
    trigger = lambda ev: [method(ev) for method in subscriptions[ev]]
    def decorator(method):
        # Add method callback for this event
        # setdefault() makes sure the dict has been created and init
        subscriptions.setdefault(event, []).append(method)
        return method
    return decorator

@event('evenement1')
@event('evenement2')
def react_to_event(event):
    print(f"Oh ! evenement '{event}' a eu lieu.")

@event('evenement1')
def react_to_event_2(event):
    print(f"Cool, moi aussi j'ai reagit a l'evenement '{event}'.")


def start_to_trigger():
    trigger('evenement1')
    trigger('evenement2')
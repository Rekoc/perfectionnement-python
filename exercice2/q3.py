def event(event_str: str):
    # Make sure the event list has been set
    # event.subscriptions is a method attribute, since event is global, subscriptions is it as well
    event.subscriptions = getattr(event, 'subscriptions', {})
    # Return method to call when event "ev" is passed
    event.trigger = lambda ev: [method(ev) for method in event.subscriptions[ev]]
    def decorator(method):
        # Add method callback for this event
        # setdefault() makes sure the dict has been created and init
        event.subscriptions.setdefault(event_str, []).append(method)
        return method
    return decorator

@event('evenement1')
@event('evenement2')
def react_to_event(event):
    print(f"Evenement '{event}' a eu lieu.")

@event('evenement1')
def react_to_event_2(event):
    print(f"Cool, moi aussi j'ai réagit a l'evenement '{event}'.")


event.trigger('evenement1')
event.trigger('evenement2')
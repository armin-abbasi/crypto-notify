import notify2


def pop(title="", description="", icon=""):

    notify2.init("Crypto price notifier")

    # create Notification object
    n = notify2.Notification(None)

    # set urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)

    # set timeout for a notification
    n.set_timeout(10000)

    # update notification data for Notification object
    n.update(title, description)

    # show notification on screen
    n.show()

#To test with the backid in dev -> 687107cf93259d2193e951fd

from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()

# Define a dummy receiver
def my_receiver(sender, **kwargs):
    print("Signal received.")

# Connect the signal
my_signal.connect(my_receiver)

# 🚫 This line violates the rule: using the 'weak' argument
my_signal.disconnect(my_receiver, weak=False)

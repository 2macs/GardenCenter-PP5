from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# post here means after, thus the signal gets sent to entire system after /
# order is saved or deleted
# sender is lineitems, instance is isstance being worked on, created figures
# if instance is new or need to be updated, kwargs is key word args


# receiving post save signals from orderlineitem model
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()

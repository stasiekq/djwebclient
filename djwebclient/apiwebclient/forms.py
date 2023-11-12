from django import forms

class HotelBookingForm(forms.Form):
    id = forms.IntegerField(required=False)
    roomNumber = forms.IntegerField(label='Room Number', required=False)
    guestName = forms.CharField(label='Guest Name', max_length=100, required=False)

class GetDeleteForm(forms.Form):
    id = forms.IntegerField(label='Guest ID', required=False)
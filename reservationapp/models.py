   ?                                          ?                      ?  ?  p  ????         
 ?G     nh????Zb K   (             <                  ????@ t z r e s . d l l , - 3 8 2                                                       @ t z r e s . d l l , - 3 8 1                                                   ????    @??C??????     ????       N o t i f i c a t i o n U x   C : \ P r o g r a m D a t a \ U S O S h a r e d \ L o g s \ U s e r \ N o t i f i c a t i o n U x to="media/resources/")
    availability = models.BooleanField()

    def __str__(self):
        return f"{self.resource_name}"

    def get_absolute_url(self):
        return reverse("resource_detail", kwargs={"pk": self.pk})

    # Helper function for checking if the resource has an image or not
    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None


    class Meta:
        ordering = ["category", "resource_name"]
        db_table = 'resource'

class Booking(models.Model):
    STATUS_CHOICES = [("applying", "applying"),
                        ("approved", "approved"),
                        ("declined", "declined"),
                        ]

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    # booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='booked_by', on_delete=models.CASCADE)
    # approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='approved_by',  on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(verbose_name = 'Start Date/Time')
    return_date = models.DateTimeField(verbose_name = 'Return Date/Time')
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="applying")

    def __str__(self):
        return f"{self.resource}--{self.id}-{self.reservation_date}"

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})

    @property
    def booking_rep(self):
        return f"{self.resource}"

    class Meta:
        ordering = ["reservation_date", "resource_id"]
        db_table = 'booking'
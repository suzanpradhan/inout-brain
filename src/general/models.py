from django.db import models


class General(models.Model):
    name = models.CharField(max_length=255, blank=255)

    def get_upload_path_for_logo(instance, filename):
        """
        Custom Upload Path for User Avatar
        """
        return f"logos/{filename}"

    avatar = models.ImageField(
        upload_to=get_upload_path_for_logo, null=True, blank=True
    )
    is_data_updated = models.BooleanField(default=False)

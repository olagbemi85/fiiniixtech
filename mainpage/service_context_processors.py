from .models import ServiceCategory


def serviceCategories(request):
	return {
        'serviceCategories': ServiceCategory.objects.all()
    }

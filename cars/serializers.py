from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


# Models are converted to JSON and back
class CommentSerializer(serializers.ModelSerializer):
    car = serializers.SlugRelatedField(slug_field='name', queryset=Car.objects.all())

    # Add car information
    car_name = serializers.CharField(source='car.name', read_only=True)
    car_manufacturer = serializers.CharField(source='car.manufacturer.name', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def validate_email(self, value):
        if not value or '@' not in value:
            raise serializers.ValidationError("Введите корректный email адрес")
        return value

    def validate_comment(self, value):
        if not value or len(value.strip()) < 5:
            raise serializers.ValidationError("Комментарий должен содержать минимум 5 символов")
        return value.strip()

    def validate(self, data):
        # We check that the car exists
        car = data.get('car')
        if not car:
            raise serializers.ValidationError("Автомобиль не существует")

        # Check that the email is not empty
        email = data.get('email')
        if not email:
            raise serializers.ValidationError("Введите email")

        return data


class CountrySerializer(serializers.ModelSerializer):
    # Manufacturers that link to the page
    manufacturers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Country
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field='name', queryset=Country.objects.all())

    # Country of issue
    country_name = serializers.CharField(source='country.name', read_only=True)

    # Add cars of the manufacturer
    cars = serializers.StringRelatedField(many=True, read_only=True)

    # Add the number of comments to cars of this manufacturer
    count_comments = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = '__all__'

    # Number of comments for all cars of the manufacturer
    def count_comments(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()


class CarSerializer(serializers.ModelSerializer):
    manufacturer = serializers.SlugRelatedField(slug_field='name', queryset=Manufacturer.objects.all())

    # Add manufacturer
    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)
    manufacturer_country = serializers.CharField(source='manufacturer.country.name', read_only=True)

    # Add comments on the car
    comments = CommentSerializer(many=True, read_only=True)

    # Add comments count
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_comments_count(self, obj):
        return obj.comment_set.count()

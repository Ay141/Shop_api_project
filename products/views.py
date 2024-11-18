from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Category, Product, Review
from products.serializers import CategorySerializers, ProductSerializers, ReviewSerializers
from rest_framework import status


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    categories_json = CategorySerializers(categories, many=True).data
    return Response(data=categories_json)


@api_view(['GET'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response(data={'message': 'Category not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    category_json = CategorySerializers(category, many=False).data
    return Response(data=category_json)


@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    product_json = ProductSerializers(products, many=True).data
    return Response(data=product_json)


@api_view(['GET'])
def products_detail_list_api_view(request, products_id):
    try:
        product = Product.objects.all()
    except Product.DoesNotExist:
        return Response(data={'message': 'Product not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    products_json = ProductSerializers(product, many=False).data
    return Response(data=products_json)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    reviews_json = ReviewSerializers(reviews, many=True)
    return Response(data=reviews_json)


@api_view(['GET'])
def review_detail_api_view(request, reviews_id):
    try:
        review = Review.objects.all()
    except Review.DoesNotExist:
        return Response(data={'message': 'Review not Found!'},
                        status=status.HTTP_404_NOT_FOUND)
    review_json = ReviewSerializers(review, many=False).data
    return Response(data=review_json)


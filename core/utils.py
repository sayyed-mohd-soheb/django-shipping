from .models import Box

# def find_best_box(product):
#     suitable_boxes = []

#     for box in Box.objects.all():
#         # Check dimensions
#         if (
#             product.length <= box.length and
#             product.width <= box.width and
#             product.height <= box.height
#         ):
#             # Check weight
#             if product.weight <= box.max_weight:
#                 suitable_boxes.append(box)

#     # If no box found
#     if not suitable_boxes:
#         return None

#     # Return cheapest box
#     best_box = min(suitable_boxes, key=lambda box: box.cost)
#     return best_box

def find_best_box(product):
    boxes = Box.objects.all()
    suitable_boxes = []

    for box in boxes:
        if (
            box.length >= product.length and
            box.width >= product.width and
            box.height >= product.height and
            box.max_weight >= product.weight
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    # cheapest box
    return sorted(suitable_boxes, key=lambda x: x.cost)[0]
"""
REST API for categories
"""
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from main.models import Category, Prize
from main.serializers import CategorySerializer, PrizeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of Prize categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('active_flag', 'top_flag')

    @list_route()
    def tree(self, request):
        categories = Category.get_tree()

        result = dict()

        cid = request.GET.get('cid') #Get's the category ID from the incoming GET request.
        cat = Category.objects.filter(pk=cid) #Filter the DB and return records matching cid
        if cat.count() == 1:
            cat = cat[0]
            path = [c.id for c in cat.get_ancestors()]
            result['path'] = path

        category_tree = self.makeTree(categories)

        serializer = self.get_serializer(category_tree, many=True)

        result['tree'] = serializer.data
                
        return Response(result)

    
    @detail_route()
    def childproducts(self, request, pk=None):
        if pk and pk != "0":
            
            #Get the path from the incoming cid.
            basePath = Category.objects.get(id=pk).path
            #Get all categories that match this path.
            matchedCategories = Category.objects.all().filter(path__istartswith=basePath)
            
            #Iterate over all these categories.
            idlist = []
            for index in range(len(matchedCategories)):
                idlist.insert(index, matchedCategories[index].id)
                
            products = Prize.objects.filter(category_id__in = idlist)

        else:
            products = Prize.objects.all()
        serializer = PrizeSerializer(products, many=True)
        return Response(serializer.data)
    
    
    @detail_route()
    def products(self, request, pk=None):
        if pk and pk != "0":
            products = Prize.objects.filter(category__id=pk)
        else:
            products = Prize.objects.all()
        serializer = PrizeSerializer(products, many=True)
        return Response(serializer.data)
        
    def makeTree(self, elements=[]):
        """
        Making nested lists tree for showing on frontend
        """
        elementsTree = []
        index = 0
        while index < len(elements):
            # If the next level is greater than current...
            if index + 1 < len(elements) and \
                            elements[index].depth < elements[index + 1].depth:
                # Finds the first and the last index of the direct descendants of
                # the current level.
                level = elements[index].depth
                frm = index + 1

                while index + 1 < len(elements) and \
                                elements[index + 1].depth != level:
                    index += 1

                to = index + 1

                # Create a new list with the descendants elements, resolve it, and
                # append as child.
                elements[frm - 1].children = self.makeTree(elements[frm: to])
                
                #There might be instances where the parent has children, but none of the
                #children have any children (prizes) associated. Hence, there's no point
                #showing this grandparent. The next 'if' checks for this scenario.
                if elements[frm-1].children:
                    elementsTree.append(elements[frm - 1])
    
            else:
                #Check whether the category has any prizes associated. If not, do not add to tree
                _productsInElement = Prize.objects.filter(category__id = elements[index].id)
                
                #If the prizes associated with the element is non-zero, then add to the tree.
                if len(_productsInElement) != 0:
                     elementsTree.append(elements[index])
            index += 1

        return elementsTree

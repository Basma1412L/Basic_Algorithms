# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler=None,nohandler=None):
        self.root=RouteTrieNode(handler,nohandler)
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, route, handler):
        current_node = self.root
        for part in route:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]
            current_node.no_route_handler=self.root.no_route_handler
        current_node.handler = handler
        current_node.no_route_handler=handler
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, route):
        current_node = self.root
        for c in route:
            if c not in current_node.children:
                return "not found handler"
            current_node = current_node.children[c]
        if (current_node.no_route_handler==self.root.no_route_handler and not(current_node==self.root)):
            return current_node.no_route_handler
        else:
            return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None,ntfoundhandler=None):
        self.children={}
        self.handler=handler
        self.no_route_handler=ntfoundhandler

    def insert(self, part, handler=None):
        self.children[part]=RouteTrieNode(handler)



# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler="",ntFound=""):
        self.root=RouteTrie(handler,ntFound)
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, route,handler):
        route=self.split_path(route)
        self.root.insert(route,handler)

    def lookup(self, path):
        route=self.split_path(path)
        res=self.root.find(route)
        return res

    def split_path(self, path):
        route =filter(None,path.split('/'))
        return route



router = Router("root handler","not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
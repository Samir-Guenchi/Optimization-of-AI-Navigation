from queue import Queue

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent  # node
        self.action = action  # action performed to get to this node
        self.cost = cost  # (incremented with each newly expanded node)
        if parent is None:  # root node
            self.depth = 0  # level in the graph 0 for the root node
        else:
            self.depth = parent.depth + 1  # parent level + 1

    def __hash__(self):
        self.hash = hash(self)

    def __eq__(self, other):
        return self.state == other.state

class Transition:
    def __init__(self, number, cost):
        self.numberWilaya = number
        self.cost = cost

class Wilaya:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.needs = 0
        self.Distance = [0] * 58
        self.Transition = []
        self.SupposedToGet = [0] * 5
        self.Production = [0] * 5  # -(0 wheat,1 potatoes,2 dates,3 tomatoes,
        # and 4 citrus)

class Truck:
    def __init__(self, model, size):
        self.model = model
        self.OGsize = size
        self.location = 0
        self.Product = [0] * 5
        self.sizeLeft = size
        self.goal = 0

class Map:
    def __init__(self):
        self.Wilayas = []
        self.Trucks = []
        self.TotalProd = [0] * 5

    def heuristic(self, truck):
        transitions = self.possible_actions(truck)
        goal = truck.goal
        h = []
        for i in range(len(transitions)):
            wilayanum = transitions[i].numberWilaya
            h.append(self.Wilayas[goal-1].Distance[wilayanum-1])
        return h

    def CreateWilayas(self, WilayaFile):
        with open(WilayaFile, "r") as file:
            for line in file:
                parts = line.split()
                wilaya = Wilaya(parts[0], parts[1])
                i = 2
                while i < len(parts) - 1:
                    transition = Transition(parts[i], parts[i + 1])
                    wilaya.Transition.append(transition)
                    i = i + 2
                self.Wilayas.append(wilaya)

    def HeuristicWilayas(self, HeuristicFile):
        i = 0
        with open(HeuristicFile, "r") as file:
            for line in file:
                parts = line.split()
                for k in range(58):
                    self.Wilayas[i].Distance[k] = int(float(parts[k]) * 100)
                i = i + 1

    def ProductionWilayas(self, ProductionFile):
        with open(ProductionFile, "r") as file:
            j = 0
            for line in file:
                i = 0
                parts = line.split()
                while i < 5:
                    production = parts[i]
                    self.Wilayas[j].Production[i] = production
                    self.TotalProd[i] += int(production)
                    i += 1
                j = j + 1

    def CreateTrucks(self, TrucksFile):
        with open(TrucksFile, "r") as file:
            for line in file:
                parts = line.split()
                truck = Truck(parts[0], parts[1])
                self.Trucks.append(truck)

    def AddToTruck(self, productSize, productNum, truck):
        wilayanum = truck.location
        if float(truck.sizeLeft) > 0:
            if float(truck.sizeLeft) > float(productSize):
                productnum = productNum
                truck.Product[productnum] += float(productSize)
                truck.sizeLeft = float(truck.sizeLeft) - float(productSize)
                float1 = float(self.Wilayas[wilayanum - 1].Production[productNum])
                float2 = float(productSize)
                float1 -= float2
                self.Wilayas[wilayanum - 1].Production[productNum] = float1
                return float2
            else:

                truck.Product[productNum] += float(truck.sizeLeft)
                float1 = float(self.Wilayas[wilayanum - 1].Production[productNum])
                float2 = float(truck.sizeLeft)
                float1 -= float2
                self.Wilayas[wilayanum - 1].Production[productNum] = float1
                truck.sizeLeft = 0
                return float2
        else:
            print("Size is not sufficient")

    def makeEmpty(self, truck):
        for i in range(5):
            float1 = float(self.Wilayas[truck.location - 1].Production[i])
            float2 = float(self.Wilayas[truck.location - 1].SupposedToGet[i])
            float3 = float(truck.Product[i])
            float1 += float3
            float2 -= float3
            self.Wilayas[truck.location - 1].Production[i] = float1
            self.Wilayas[truck.location - 1].SupposedToGet[i] = float2
        for i in range(5):
            truck.Product[i] = 0
        truck.sizeLeft = truck.OGsize
        truck.location = 0
        truck.goal = 0

    def WilayaNeeds(self, NeedsFile):
        with open(NeedsFile, "r") as file:
            i = 0
            for line in file:
                self.Wilayas[i].needs = line
                i += 1

    def WilayasHaveExtra(self, Productnum):
        WilayasWithExtra = [0] * 58
        for i in range(58):
            if float(self.Wilayas[i].Production[Productnum]) > float(self.TotalProd[Productnum]) * float(
                    self.Wilayas[i].needs):
                WilayasWithExtra[i] = float(self.Wilayas[i].Production[Productnum]) - (
                            float(self.TotalProd[Productnum]) * float(self.Wilayas[i].needs))
        return WilayasWithExtra

    def WilayasWithNeed(self, Productnum):
        WilayasWithNeed = [0] * 58
        for i in range(58):
            if float(self.Wilayas[i].Production[Productnum]) < float(self.TotalProd[Productnum]) * float(
                    self.Wilayas[i].needs):
                WilayasWithNeed[i] = (float(self.TotalProd[Productnum]) * float(self.Wilayas[i].needs)) - float(
                    self.Wilayas[i].Production[Productnum])
        return WilayasWithNeed

    def TruckLocation(self, truck, Productnum):
        if truck.location == 0:
            need = self.WilayasWithNeed(Productnum)
            for i in range(58):
                if need[i] - self.Wilayas[i].SupposedToGet[Productnum] > 0:
                    extra = self.WilayasHaveExtra(Productnum)
                    added = 0
                    want = need[i] - self.Wilayas[i].SupposedToGet[Productnum]
                    for j in range(58):
                        if float(truck.sizeLeft) > 0 and extra[j] != 0:
                            truck.location = j + 1
                            if extra[j] > want:
                                added = self.AddToTruck(want, Productnum, truck)
                            else:
                                added = self.AddToTruck(extra[j], Productnum, truck)
                            break
                    truck.goal = i + 1
                    self.Wilayas[i].SupposedToGet[Productnum] += added
                    return True
            return False
        else:
            return False

    def AllTrucksLocation(self):
        i = 0
        for j in range(5):
            for i in range(len(self.Trucks)):
                self.TruckLocation(self.Trucks[i], j)

class GeneralGraphSearch:
    def __init__(self):
        self.Algeria = Map()
        self.Algeria.CreateWilayas("WilayaFile.csv")
        self.Algeria.HeuristicWilayas("HeuristicFile.csv")
        self.Algeria.ProductionWilayas("ProductionFileWinter.csv")
        self.Algeria.WilayaNeeds("NeedsFile.csv")
        self.Algeria.CreateTrucks("TrucksFile.csv")
        self.Algeria.AllTrucksLocation()

    def expandNode(self, node):
        queue = Queue()
        state = int(node.state)
        possible_transitions = self.Algeria.Wilayas[state - 1].Transition
        for i in range(len(possible_transitions)):
            childNode = Node(possible_transitions[i].numberWilaya, node, "Go to " + str(possible_transitions[i].numberWilaya),
                             float(possible_transitions[i].cost))
            queue.put(childNode)
        return queue

    def BFS(self, truck):
        VisitedNodes = [False] * 58
        Solution = []
        Path = []
        Cost = 0
        initialstate = truck.location
        root = Node(initialstate)
        queue = Queue()
        queue.put(root)
        goal_state = None

        while not queue.empty():
            currentNode = queue.get()
            state = int(currentNode.state)
            if not VisitedNodes[state - 1]:
                VisitedNodes[state - 1] = True
                if state == truck.goal:
                    goal_state = currentNode
                    break
                else:
                    Solution.append(currentNode)
                    expanded = self.expandNode(currentNode)
                    while not expanded.empty():
                        childNode = expanded.get()
                        queue.put(childNode)

        if goal_state:
            while goal_state != root:
                Path.append(goal_state.state)
                Cost += float(goal_state.cost)
                goal_state = goal_state.parent
            Path.append(root.state)
            Path.reverse()

        print("Path:", Path)
        print("Cost:", Cost)

        truck.location = truck.goal
    #     self.Algeria.makeEmpty(truck)
    # def HillClimbing(self, truck, heuristic_file):
    #  state = truck.location
    #  goal = truck.goal
    #  current_cost = 0
    #  path = [state]

    #  with open(heuristic_file, "r") as file:
    #     heuristic_values = [int(float(value)) for value in file.read().split()]

    #  while state != goal:
    #     transitions = self.Algeria.Wilayas[state - 1].Transition
    #     best_state = None
    #     best_cost = float('inf')
    #     for transition in transitions:
    #         heuristic_value = heuristic_values[int(transition.numberWilaya) - 1]
    #         if float(transition.cost) + heuristic_value < best_cost and int(transition.numberWilaya) not in path:
    #             best_cost = float(transition.cost) + heuristic_value
    #             best_state = int(transition.numberWilaya)
    #     if best_state is None:
    #         break
    #     path.append(best_state)
    #     current_cost += float(transitions[best_state - 1].cost)
    #     state = best_state
    #  if state == goal:
    #     print("Path:", path)
    #     print("Cost:", current_cost)
    #  else:
    #     print("Hill climbing failed to find a path.")
    def HillClimbing(self, truck, heuristic_file):
     state = truck.location
     goal = truck.goal
     current_cost = 0
     path = [state]
 
     # Load heuristic values from the file
     with open(heuristic_file, "r") as file:
      heuristic_values = [[float(value) for value in line.split()] for line in file.readlines()]

 
     while state != goal:
         transitions = heuristic_values[state - 1]
         best_state = None
         best_cost = float('inf')
         for i, cost in enumerate(transitions):
             if cost < best_cost and i + 1 not in path:
                 best_cost = cost
                 best_state = i + 1
         if best_state is None:
             break
         path.append(best_state)
         current_cost += best_cost
         state = best_state
     if state == goal:
         print("Path:", path)
         print("Cost:", current_cost)
     else:
         print("Hill climbing failed to find a path.")
     
search = GeneralGraphSearch()
wilayaneeds0 = search.Algeria.WilayasWithNeed(0)
print(wilayaneeds0[2])
search.BFS(search.Algeria.Trucks[0])
search.BFS(search.Algeria.Trucks[1])
search.BFS(search.Algeria.Trucks[2])
search.BFS(search.Algeria.Trucks[3])
search.BFS(search.Algeria.Trucks[4])
wilayaneeds0 = search.Algeria.WilayasWithNeed(0)
print(wilayaneeds0[2])
for truck in search.Algeria.Trucks:
    search.HillClimbing(truck, "HeuristicFile.csv")

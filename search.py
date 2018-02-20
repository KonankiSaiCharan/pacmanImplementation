# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (suc,
        action, stepCost), where 'suc' is a suc to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that suc.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
# create the required stacks and path variables
    nodesPast = {}
    nodePath = util.Stack()
#Push the start state into the stack
    nodePath.push(problem.getStartState())
    record = set()
#iterate until the list is empty
    while not nodePath.isEmpty():
#Popping out the top element for further computations
        topState = nodePath.pop()
#Check if the top state is the goal state
        if problem.isGoalState(topState):
            return nodesPast[topState]
#Adding the state to the list of visited nodes i.e., the record
        record.add(topState)
        for i in problem.getSuccessors(topState):
            child, actions, Cost = i
            possiblePath=list()
            if not topState is  problem.getStartState():
#Checked whether topstate is start state
                possiblePath.extend(nodesPast[topState])
#All the required actions are appended to get a solution
            possiblePath.append(actions)
            nodesPast[child] = possiblePath
#If the child is not already visited then add it to the record
            if not child in record :
                nodePath.push(child)




def breadthFirstSearch(problem):
# create the required Queues and path variables
    nodePath = list()
    nodesPathQueue = util.Queue()
    nodePath.append(problem.getStartState())
# Push the state obtained into the queue
    nodesPathQueue.push((problem.getStartState(), list()))
    while not nodesPathQueue.isEmpty():
        topState = nodesPathQueue.pop()
#Pop out the top positioned state from the queue
        pathObtained = topState[1]
        position = topState[0]
# Check if the goal state and position are the same
        if problem.isGoalState(position) :
            return pathObtained
        for k in problem.getSuccessors(position):
#Iterate through the successors of the present node to identify if it is already visited
            child, actions, Cost = k
            if child not in nodePath:
                nodesPathQueue.push((child,pathObtained + [actions]))
#If the child is not already visited then we add this to the queue
                nodePath.append(child)
    #util.raiseNotDefined()



def uniformCostSearch(problem):
# Creating the necessary queue variables
    nodePath = []
    nodesPathPriorityQueue = util.PriorityQueue()
    nodePath.append(problem.getStartState())
#In the above statement we append the start state to the nodepath
    nodesPathPriorityQueue.push((problem.getStartState(), list()), 0)
#Here, we push the start state to gthe queue
#Iterate as long as the queue is not empty
    while not nodesPathPriorityQueue.isEmpty():
#Pop out the top state from the queue and store it
        topState = nodesPathPriorityQueue.pop()
        obtainedPath = topState[1]
        position=topState[0]
#Check if the goal state is same as the current state, if yes then return
        if problem.isGoalState(position) == True:
            return obtainedPath
#Iterate through the successors of the current node if all the above conditions are met
        for id in problem.getSuccessors(position):
            child, actions, Cost = id
            if not child in nodePath:
                Cost = problem.getCostOfActions(obtainedPath + [actions])
#Adding the cost variable along with the child 
                nodesPathPriorityQueue.push((child, obtainedPath + [actions]), Cost)
                if not problem.isGoalState(child):
                    nodePath.append(child)


def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
#Creating the necessary queue elements
    nodesPathPriorityQueue = util.PriorityQueue()
    state = problem.getStartState()
    nodePath = []
    nodePath.append(state)
#Pushing the start state into the queue
    nodesPathPriorityQueue.push((problem.getStartState(), list()), 0)
    while not nodesPathPriorityQueue.isEmpty():
#Iteration will be done as long as the queue is not empty
        topState = nodesPathPriorityQueue.pop()
        obtainedPath = topState[1]
        position = topState[0]
#Check if the current position state is the goal state
        if problem.isGoalState(position) == True:
            return obtainedPath
#If the goal state is found then return the path obtained till now
#Obtain the successors and iterate through them
        for id in problem.getSuccessors(position):
            child, actions, Cost = id
#Check whether the child nodes have already been visited
            if not child in nodePath:
                Cost = problem.getCostOfActions(obtainedPath + [actions])
                CompleteCost = Cost + heuristic(child, problem)
#Push into the queue along with the complete cost obtained
                nodesPathPriorityQueue.push((child, obtainedPath + [actions]), CompleteCost)
#If the child node is not the goal state then append it to the nodepath
                if not problem.isGoalState(child):
                    nodePath.append(child)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
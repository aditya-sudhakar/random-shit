import time
import matplotlib.pyplot as plt


#### VARIABLES ####
def redefine_variables():
    max_val = 999999999 #placeholder super big number to represent infinity
    visit_dist = [[0, 0]] #[[visited?, distance to], [visited?, distance to], ...]
    return max_val, visit_dist


#### DEFINE GRAPHS #####
def make_graph():
    # define connections between verticies
    connections = [[0 , 1 , 0 , 1],
                   [1 , 1 , 1 , 0],
                   [0 , 1 , 1 , 1],
                   [1 , 0 , 1 , 0]]

    #define weight of each edge generated
    edge_weight =  [[0 , 10 , 0 , 1],
                    [10 , 10 , 1 , 0],
                    [0 , 1 , 10 , 5],
                    [1 , 0 , 5 , 0]]

    total_vertices = len(connections[0])

    return connections, edge_weight, total_vertices

def visit_next():
    #Identify which vertex to visit next to achieve shortest path
    visited = -1

    # Choosing the vertex with the minimum distance
    for vertex in range(total_vertices):
        if visit_dist[vertex][0] == 0 and (visited < 0 or visit_dist[vertex][1] <= visit_dist[visited][1]):
            visited = vertex

    return visited

def run_dijkstra(connections, edge_weight, total_vertices):
    start = time.time()
    #default min length to inf
    # visit_dist = []
    for vertex in range(total_vertices-1):
        visit_dist.append([0, max_val])

    for vertex in range(total_vertices):
    # Finding the next vertex to be visited.
        to_visit = visit_next()
        for adj_vertex in range(total_vertices):
            # Calculate distance to unvisited adjacent vertices
            if connections[to_visit][adj_vertex] == 1 and visit_dist[adj_vertex][0] == 0:
                updated_dist = visit_dist[to_visit][1] + edge_weight[to_visit][adj_vertex]
            # Updating the distance of the adjacent vertex
                if visit_dist[adj_vertex][1] > updated_dist:
                    visit_dist[adj_vertex][1] = updated_dist
        # mark as visited
        visit_dist[to_visit][0] = 1
    loc = 0 

    # Printing out the shortest distance from the source to each vertex 
    for distance in visit_dist:
        # FOR DEBUG ONLY. COMMENT OUT 'PRINT' LINE FOR GETTING TIME DATA
        # print("The shortest path to vertex [",(ord('a') + loc),"] from vertex [a] is:",distance[1])
        loc = loc + 1
    end = time.time()
    
    duration = end - start
    return duration


#ADD BELLMAN FORD STUFF


def plot_times_hist(dij_times, bell_times):
    plt.hist([dij_times, bell_times], label=['Dijkstra', 'Bellman-Ford'])
    plt.legend(loc='upper right')
    plt.title('Distribution of computation time: Dijkstra vs Bellman-Ford')
    plt.xlabel('Time to Run [s]')
    plt.ylabel('Occurrence [dimless]')
    plt.show()


if __name__ == "__main__":

    dij_times, bell_times = [], []
    max_val, visit_dist = redefine_variables()
    connections, edge_weight, total_vertices = make_graph()
    for j in range(1000):
        max_val, visit_dist = redefine_variables()
        duration = run_dijkstra(connections, edge_weight, total_vertices)
        dij_times.append(duration)

    for j in range (1000):
        #FILL WITH ur function
        pass
    
    #### DELETE THIS!!!!!! ####
    bell_times = dij_times

    plot_times_hist(dij_times, bell_times)

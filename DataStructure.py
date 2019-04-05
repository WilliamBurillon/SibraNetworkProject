# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:45:00 2019

@author: burillow
"""
import data2py as data
import time

###========= Definition of the data structure ================###

##=== Class Node ========##

class Node:

    def __init__(self, name, line, timetableGo, timetableBack): #, go = None, back=None):
        self.name = name
        self.l_line = []
        self.l_line.append(line)

        self.timetableGo = {self.l_line[0]: timetableGo}
        self.timetableBack = {self.l_line[0]: timetableBack}
        # self.go = go
        # self.back = back

    def __str__(self):
        return self.name

    def addLine(self,line):
        self.l_line.append(line)

    def addTimetableGo(self,timetableGo):
        self.timetableGo[self.l_line[1]]=timetableGo

    def addTimetableBack(self,timetableBack):
        self.timetableBack[self.l_line[1]]=timetableBack

##====== class Arcs =========##

class Connexion:

    def __init__(self, start, finish, time):
        self.start = start
        self.finish = finish
        self.time = time

    def __str__(self):
        res = ""
        if self.start == None:

            res = " Le départ est : " + self.finish.name
        elif self.finish==None:
            res = " le termius est : " + self.start.name
        else:
            res = self.start.name + " -- > " + self.finish.name
        return res

    # def setTimeGo(self,start,finish,isGo):
    #     #     res=[]
    #     #     if isGo == True:
    #     #         for i  in range (0,len(start.timetableGo)):
    #     #             try:
    #     #                 timeFinish=start.go.timetableGo[i]
    #     #                 timeStart=start.timetableGo[i]
    #     #                 res.append(data.time2Stop(timeStart,timeFinish))
    #     #             except ValueError :
    #     #                 res.append(None)

    #

##====== class Line =========##

class Line:

    def __init__(self, l_node, l_Arcs):
        #
        self.l_node = l_node
        self.l_Arcs = l_Arcs


# Definition shortest


# def dijkstra(graph, start, finish,visitedNode,n):
#
#     graphBis = Line(graph.l_node,graph.l_Arcs)
#     print('le start est ',start)
#     print('le finish est', finish)
#     print(start == finish)
#     print(len(graph.l_node))
#
#
#
#     # for node in graph.l_node:
#     #     print('les noeuds du graph sont ', node)
#     if start == finish or n>10 :
#         return visitedNode
#     # if start.finish == None:
#     #     return None
#
#
#     elif start != finish and ( start!=None or start in graph.l_node):
#
#
#         for arc in graphBis.l_Arcs:
#
#             if start == arc.start :
#
#                 visitedNode.append(start)
#                 graphBis.l_Arcs.remove(arc)
#                 graphBis.l_node.remove(start)
#                 dijkstra(graphBis,arc.finish,finish,visitedNode,n+1)
#
#             else:
#                 break




# def shortest(graph, start, finish,path):
#     print("le start ",start)
#     currentGraph = Line(graph.l_node[:],graph.l_Arcs[:])
#     arcRes=[]
#     pathTempo=path
#     # if start == None :
#     #     return pathTempo
#     if start == finish:
#         pathTempo.append(start)
#         return pathTempo
#     # if start == None:
#     #     pathTempo=pathTempo
#
#     elif start in currentGraph.l_node:
#
#         currentGraph.l_node.remove(start)
#
#
#         for arc in currentGraph.l_Arcs:
#
#             if start == arc.start  :
#                 print(arc.finish)
#
#
#                 arcRes.append(arc)
#             if start == arc.finish:
#
#
#                 currentGraph.l_Arcs.remove(arc)
#         # print(len(arcRes))
#         for arc1 in arcRes:
#             # print(arc1.start)
#             if start not in pathTempo:
#                 pathTempo.append(start)
#             currentGraph.l_Arcs.remove(arc1)
#             return shortest(currentGraph, arc1.finish, finish, pathTempo)
#     #
#     # else:
#     #     return pathTempo
#
#

# def shortest(graph, start, finish, path={},compteur ):
#
#     # currentGraph=Line(graph.l_node,graph.l_Arcs)
#     # currentPath=path[:]
#     # arcRes=[]
#
#
#
#
#     if start == finish :
#         for path in currentPath:
#
#
#
#
#     elif start in currentGraph.l_node and start !=None :
#
#         currentGraph.l_node.remove(start)
#         if len(currentPath)==0:
#
#             for arc in currentGraph.l_Arcs:
#
#                 if start == arc.start:
#                     arcRes.append(arc)
#                 if start == arc.finish:
#                     currentGraph.l_Arcs.remove(arc)
#
#             for arc1 in arcRes:
#
#                 currentPath.append({"nb":1,"path":[arc1.finish]})
#                 currentGraph.l_Arcs.remove(arc1)
#                 return shortest(currentGraph,arc1.finish,finish,currentPath)
#
#         for path in currentPath:
#

# def shortest(graph, start, finish, path=[],compteur = 0):
#
#     nodeList=graph.l_node
#     arcList=graph.l_Arcs
#     resARc=[]
#     arcSupp=[]
#     print(start)
#     print(path)
#     # print("type path",type(path))
#
#     if start == finish:
#         lePath=path[:]
#
#         return lePath
#
#
#
#     elif start in nodeList:
#         nodeList.remove(start)
#
#         # recuperation des arc partant de start et suppression des arcs arrivant a start
#
#
        # for arc in arcList:
        #     if start == arc.start:
        #         # print("fedfs")
        #         resARc.append(arc)

#
#         # recupere arc a suppr
#         for arc in arcList:
#
#             if start == arc.finish:
#
#                 # print("fsfs")
#
#                 arcSupp.append(arc)
#         # supprime les arcs
#         for arcaSupp in arcSupp:
#
#             arcList.remove(arcaSupp)
#
#
#         # si je ne suis pas sur une correspondance , une seule direction possible
#         if len(resARc)==1 and resARc[0].finish != None:
#
#             for dict in path:
#                 print(dict.keys())
#                 if start.name in dict.keys():
#                     print("oker")
#                     dict[resARc[0].finish.name]=compteur +1
#                     arcList.remove(resARc[0])
#                     shortest(Line(nodeList, arcList), arc.finish, finish,path, compteur + 1)
#             # path[arc.finish.name]=compteur +1
#
#
#         # plusieur direction possible (au départ) ou correspondance
#
#         elif len(resARc)!=0:
#             # au depart
#             if len(path)==0:
#                 # print("la2")
#                 for arc in resARc:
#
#                     # print("laaaaaaaaaaaa")
#                     if arc.finish != None:
#                         v={}
#                         v[arc.finish.name] = compteur + 1
#                         path.append(v)
#                         print("path1ere",path)
#                         arcList.remove(arc)
#                         shortest(Line(nodeList, arcList), arc.finish, finish,path, compteur + 1)
#             # si connexion il y a
#             else :
#                 # print("la3")
#                 for arc in resARc:
#                     # ajouter au bon dictionnaire
#                     for i  in range (0,len(path)) :
#
#                         if start in path[i]:
#
#                             path[i][arc.finish.name]=compteur +1
#                             arcList.remove(arc)

# def shortest(graph, start, finish, path={},compteur = 0):
#
#     nodeList=graph.l_node
#     arcList=graph.l_Arcs
#     resARc=[]
#     arcSupp=[]
#     print(path)
#     print(start)
#     # print("type path",type(path))
#
#     if start == finish:
#         print("la")
#
#         return path
#
#
#
#     elif start in nodeList:
#
#         nodeList.remove(start)
#
#         # recuperation des arc partant de start et suppression des arcs arrivant a start
#
#         for arc in arcList:
#
#             if start == arc.start:
#                 # print("fedfs")
#                 resARc.append(arc)
#
#
#         # recupere arc a suppr
#         for arc in arcList:
#
#             if start == arc.finish:
#
#                 # print("fsfs")
#
#                 arcSupp.append(arc)
#         # supprime les arcs
#         for arcaSupp in arcSupp:
#
#             arcList.remove(arcaSupp)
#
#         # si je suis au début de l'ago
#         if len(path)==0:
#             for arc in resARc:
#
#                 arcList.remove(arc)
#                 path[arc.finish.name]=compteur + 1
#                 shortest(Line(nodeList,arcList),arc.finish,finish,path,compteur+1)


        # si je ne suis pas sur une correspondance , une seule direction possible


        # if len(resARc)==1:
        #     print("sss")
        #     print("path2",path)
        #     for dict in path:
        #         print(dict)
        #         if start in dict.keys():
        #             dict[resARc[0].finish.name]=compteur +1
        #             arcList.remove(resARc[0])
        #             return shortest(Line(nodeList, arcList), arc.finish, finish,path, compteur + 1)
        #     # path[arc.finish.name]=compteur +1
        #
        #
        # # plusieur direction possible (au départ) ou correspondance
        #
        # elif len(resARc)!=0:
        #     # au depart
        #     if len(path)==0:
        #         print("la2")
        #         for arc in resARc:
        #             print("laaaaaaaaaaaa")
        #             v={}
        #             v[arc.finish.name] = compteur + 1
        #             path.append(v)
        #             print("path1ere",path)
        #             arcList.remove(arc)
        #             return shortest(Line(nodeList, arcList), arc.finish, finish,path, compteur + 1)
        #     # si connexion il y a
        #     else :
        #         print("la3")
        #         for arc in resARc:
        #             # ajouter au bon dictionnaire
        #             for i  in range (0,len(path)) :
        #
        #                 if start in path[i]:
        #
        #                     path[i][arc.finish.name]=compteur +1
        #                     arcList.remove(arc)
        #                     return shortest(Line(nodeList,arcList),arc.finish,finish,path,compteur+1)

#  return shrotest pour les autres cas + conditon arret


# def shortest(graph,start,finish,path={},compteur=0):
#     # print("rfs")
#     leStart=start
#     print("le start", start)
#
#     for key in path:
#         print(key)
#     resArc=[]
#     if leStart == finish :
#         return path
#     if leStart == None:
#
#     if len(path)==0:
#         for arc in graph.l_Arcs:
#             if start == arc.start:
#                 # print("fedfs")
#                 resArc.append(arc)
#
#         for arc in resArc:
#             # print("kfls")
#             path[arc.finish]=compteur + 1
#             return shortest(graph,arc.finish,finish,path,compteur+1)
#
#
#     elif start in path.keys() and start != finish and start!=None:
#         #on prend tous les arcs partant de start
#         print("le start 2 :===", start)
#         for arc in graph.l_Arcs:
#             if start == arc.start:
#                 # print("fedfs")
#                 resArc.append(arc)
#
#         for arc in resArc:
#             # print("kfls")
#             path[arc.finish]=compteur + 1
#             return shortest(graph,arc.finish,finish,path,compteur+1)





















# ---------------- Creation des noeud ----------

# ------- Creation de tous les noeuds sans connexion avec les autres ------------
# ====== Creation des Nodes =======
nodeList1 = []

# creation des noeuds de la ligne 1 par rapport au dico regular date go 1 ---------------------

for key in data.regular_date_go1.keys():

    nodeList1.append(Node(str(key), 1, data.regular_date_go1[key], data.regular_date_back1[key]))#data.getNextGo(data.regular_path, str(key)), data.getNextBack(data.regular_path, str(key))))


nodeList2 = []

# creation des noeuds de la ligne 2
# s il apparait dans la ligne 1, on modifie juste le noeuds de la ligne 1 en rajoutant les horaire de la ligne 2 au noeuds en question
# sinon on le crée simplement

for key in data.regular_date_go2.keys():
    dedans = False
    for i in range(0,len(nodeList1)):
        if str(key)==nodeList1[i].name:
            nodeList1[i].addLine(2)
            nodeList1[i].addTimetableGo(data.regular_date_go2[key])
            nodeList1[i].addTimetableBack(data.regular_date_back2[key])
            nodeList2.append(nodeList1[i])

            dedans=True

        else:

            pass

    if dedans == False:
        nodeList2.append(Node(str(key), 2, data.regular_date_go2[key], data.regular_date_back2[key]))

# talbeau de tout les noeuds sans redondance

nodeListFinale=nodeList1[:]

for node in nodeList2:
    if node not in nodeListFinale :
        nodeListFinale.append(node)




# ---------------------- Affichage des noeuds -----------------------------
# Test pour voir si les noeuds des différentes listes sont bien les mêmes
# for i in range(0, len(nodeList1)):
#     for j in range (0,len(nodeList2)):
#
#         if nodeList1[i]==nodeList2 [j]:
#
#             print("tout est noirreerererer")
#             print(nodeList1[i])
#             print(nodeList2[j])
#
#
# for i in range (0, len(nodeList1)):
#     print('le noeud ', i, " :\n")
#     print(nodeList1[i].name,"\n")
#     print(nodeList1[i].l_line, "\n")
#
# for i in range (0, len(nodeList2)):
#     print('le noeud ', i, " :\n")
#     print(nodeList2[i].name,"\n")
#     print(nodeList2[i].l_line, "\n")

# ----------------- creation des connexion -----------------------
# pour la ligne 1

connexionListAller1=[]

for i in range(0,len(nodeList1)):

    strNext = data.getNextGo(data.regular_path1,nodeList1[i].name)
    for j in range(0,len(nodeList1)):
        if len(strNext)==0:
            leNext=None
            break
        elif strNext[0] == nodeList1[j].name:

            leNext = nodeList1[j]

            break

    connexionListAller1.append(Connexion(nodeList1[i],leNext,1))


# print("Connexion aller \n", len(connexionListAller1), " arcs")
# for i in range(0,len(connexionListAller1)):
#     print("l arc  ", i, " \n")
#     print(" depart",connexionListAller1[i].start)                     # Cette partie donne une liste de 12 arcs dont le dernier a finish = non
#     print(" arriver",connexionListAller1[i].finish)
# print("\n")
#



connexionListRetour1=[]
nodeList1bis=nodeList1[:]
nodeList1bis.reverse()
# print(len(nodeList1bis))
# for node in nodeList1bis:
#      print(node)

#cette partie donne liste dont les deux dernier arcs ont un finish = none
for i in range(0,len(nodeList1bis)):
    # print(i)
    # print(nodeList1bis[i].name)
    strNext1 = data.getNextBack(data.regular_path1,nodeList1bis[i].name)
    # print(strNext1)
    if len(strNext1)==0 :
        leNext1=None
    elif len(strNext1)==1:
        # print("taille strNext = 1 ")
        for j in range(0,len(nodeList1bis)):
            # print(j)
            if strNext1[0] == nodeList1bis[j].name:

                leNext1 = nodeList1bis[j]

                break
    elif len(strNext1)==2:
        # print("taille strNext = 2 ")
        strNext1.reverse()
        # print("la")
        for k in range (0, len(nodeList1bis)):

            if strNext1[1]==nodeList1bis[k].name  :
                # print("la")
                # print("StrNext1 0 : ",strNext1[0] )
                # print("StrNext1 1 : ", strNext1[1])
                # print("node list k",nodeList2[k].name)
                # print("node liste k-1 ", nodeList2[k-1].name)

                leNext1=nodeList1bis[k]
                connexionListRetour1.append(Connexion(nodeList1bis[i], nodeList1bis[k-1], 1))
                break

    connexionListRetour1.append(Connexion(nodeList1bis[i],leNext1,1))   # cet


# affichage connexionListRetour1

# print("\n")
# #
# print("connexion retour1\n" , len(connexionListRetour1), "arcs")
# for i in range(0,len(connexionListRetour1)):
#     print("l arc  ", i, " \n")
#     print(" depart",connexionListRetour1[i].start)
#     print(" arriver",connexionListRetour1[i].finish)

# pour la ligne 2 -------------------------------------------------------------------------------------------

# cette partie permet de générer une liste avec le dernier arc tq finish = none
connexionListAller2=[]
for i in range(0,len(nodeList2)):

    strNext = data.getNextGo(data.regular_path2,nodeList2[i].name)
    for j in range(0,len(nodeList2)):

        if len(strNext)==0:
            leNext=None

        elif strNext[0] == nodeList2[j].name:

            leNext = nodeList2[j]

            break

    connexionListAller2.append(Connexion(nodeList2[i],leNext,1))

# print("Connexion aller 2\n", len(connexionListAller2), " arcs")
# for i in range(0,len(connexionListAller2)):
#     print("l arc  ", i, " \n")
#     print(" depart",connexionListAller2[i].start)
#     print(" arriver",connexionListAller2[i].finish)
# print("\n")


connexionListRetour2=[]
nodeList2bis=nodeList2[:]
nodeList2bis.reverse()


# liste connexion avec derniere connexion tq finsish = none
for i in range(0,len(nodeList2bis)):

    strNext1 = data.getNextBack(data.regular_path2,nodeList2bis[i].name)

    for j in range(0,len(nodeList2bis)):
            if len(strNext1)==0:
                leNext1= None
            elif strNext1[0] == nodeList2bis[j].name:

                leNext1 = nodeList2bis[j]

                break


    connexionListRetour2.append(Connexion(nodeList2bis[i],leNext1,1))

# affichage listRetour2

# print("\n")
# print("connexion retour2\n" , len(connexionListRetour2), "arcs")
# for i in range(0,len(connexionListRetour2)):
#     print("l arc  ", i, " \n")
#     print(" depart",connexionListRetour2[i].start)
#     print(" arriver",connexionListRetour2[i].finish)

# concatenation ListConnexion
listConnexion = []
listConnexion = connexionListAller1 + connexionListAller2 + connexionListRetour1 + connexionListRetour2

# -------------------- Test ---------------------

graph = Line(nodeListFinale,listConnexion)


for node in graph.l_node:

    print(node)
for arc in graph.l_Arcs:

    print(arc)


strStart = "Vernod"
strFinish = "Bonlieu"



# for node in graph.l_node:
#     print(node.)

# for node in graph.l_node:
#     if strStart == node.name:
#         start = node
#
#     if strFinish == node.name:
#         finish = node
# res = shortest(graph,start,finish)
# print(res)
# for key in res:
#     print( key)






























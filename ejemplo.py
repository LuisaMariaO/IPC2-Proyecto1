from os import system,startfile
def generarGraphviz():
    graphviz='''
    digraph L{
    node[shape=box fillcolor="#FFEDBB" style =filled]
    
    subgraph cluster_p{
        label= "Matriz Dispersa"
        bgcolor = "#398D9C"
        raiz[label = "0,0"]
        edge[dir = "both"]
        
        
        Fila1[label="1",group=1];   
        Fila2[label="2",group=1];   
        Fila3[label="3",group=1];   
        Fila4[label="4",group=1];   
        Fila5[label="5",group=1];   
       
        Fila1->Fila2;
        Fila2->Fila3;
        Fila3->Fila4;
        Fila4->Fila5; 
       
        Columna1[label = "1",group=2,fillcolor=yellow];
        Columna2[label = "2",group=3,fillcolor=yellow];
        Columna3[label = "3",group=4,fillcolor=yellow];
        Columna4[label = "4",group=5,fillcolor=yellow];
        Columna5[label = "5",group=6,fillcolor=yellow];
        
        Columna1->Columna2;
        Columna2->Columna3;
        Columna3->Columna4;
        Columna4->Columna5;
        
        raiz->Fila1;
        raiz->Columna1;
        
        {rank=same;raiz;Columna1;Columna2;Columna3;Columna4;Columna5}
        nodo1_1[label="1,1",fillcolor=green,group=2]
        nodo4_4[label="4,4",fillcolor=green,group=5]
        nodo5_3[label="5,3",fillcolor=green,group=4]
        nodo2_2[label="2,2",fillcolor=green,group=3]
        nodo2_4[label="2,4",fillcolor=green,group=5]
        nodo3_4[label="3,4",fillcolor=green,group=5]
        nodo5_5[label="5,5",fillcolor=green,group=6]

        
        Fila1->nodo1_1;
        {rank=same;Fila1;nodo1_1}
        Fila2->nodo2_2;
        nodo2_2->nodo2_4;
        {rank=same;Fila2;nodo2_2;nodo2_4}
        Fila3->nodo3_4;
        {rank=same;Fila3;nodo3_4}
        Fila4->nodo4_4;
        {rank=same;Fila4;nodo4_4}
        Fila5->nodo5_3;
        nodo5_3->nodo5_5;
        {rank=same;Fila5;nodo5_3,nodo5_5}
      
        Columna1->nodo1_1;
        Columna2->nodo2_2;
        Columna3->nodo5_3;
        Columna4->nodo2_4;
        Columna5->nodo5_5;
        nodo2_4->nodo3_4;
        nodo3_4->nodo4_4;
    
    }

}
    
    '''
    miArchivo= open('graphviz.dot','w')
    miArchivo.write(graphviz)
    miArchivo.close()
    
    system('dot -Tpng graphviz.dot -o graphviz.png')
    system('graphviz.png')
    #startfile('graphviz.png')
    
    


generarGraphviz()
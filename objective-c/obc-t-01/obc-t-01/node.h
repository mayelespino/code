//
//  node.h
//  obc-t-01
//
//  Created by mayel espino on 3/11/17.
//  Copyright © 2017 mayel espino. All rights reserved.
//

#ifndef node_h
#define node_h

//@interface node : NSObject
//@property char value;
//@property(retain) node *next;
//@property(retain) node *prev;
//@end

typedef struct node node;
struct node {
    char value;
    node *next;
    node *prev;
};
#endif /* node_h */

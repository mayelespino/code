//
//  LinkedList.m
//  obc-t-01
//
//  Created by mayel espino on 3/11/17.
//  Copyright © 2017 mayel espino. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "linkedList.h"
#import "node.h"

@implementation linkedList : NSObject
- (id) init{
    _current = malloc(sizeof(node));
    _start = _current;
    return self;
}

- (void) addValue: (char) inValue {
    _current->value = inValue;
    _current->prev = (node *)_current;
    _current->next = malloc(sizeof(node));
    _current = _current->next;
    _current->next = nil;
    
}

- (void) printList{
    node *iterator = _start;
    while (iterator->next != nil){
        NSLog(@"%c", iterator->value);
        iterator = iterator->next;
    }
}
@end

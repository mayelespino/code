//
//  linkedList.h
//  obc-t-01
//
//  Created by mayel espino on 3/11/17.
//  Copyright © 2017 mayel espino. All rights reserved.
//

#ifndef linkedList_h
#define linkedList_h
#import "node.h"

@interface linkedList : NSObject
@property node *start;
@property node *current;
- (id) init;
- (void) addValue: (char) inValue;
- (void) printList;
@end

#endif /* linkedList_h */

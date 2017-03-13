//
//  main.m
//  obc-t-01
//
//  Created by mayel espino on 3/11/17.
//  Copyright © 2017 mayel espino. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "linkedList.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"Start!");
        linkedList *LnkLst = [[linkedList alloc] init];
        [LnkLst addValue: 'a'];
        [LnkLst addValue: 'A'];
        [LnkLst addValue: 'B'];
        [LnkLst addValue: 'C'];
        [LnkLst addValue: 'D'];
        [LnkLst addValue: 'd'];
        [LnkLst printList];
        NSLog(@"Stop!");
    }
    return 0;
}

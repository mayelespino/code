 //
//  main.m
//  ObjectiveCTutorialProduct
//
//  Created by mayel espino on 8/28/15.
//  Copyright (c) 2015 mayelespino. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSString *str = @"stack";
        
        NSMutableArray *charArray = [NSMutableArray arrayWithCapacity:str.length];

        
        for (int i=0; i<str.length; ++i) {
            NSString *charStr = [str substringWithRange:NSMakeRange(i, 1)];
            [charArray addObject:charStr];
        }

//        const char *tmpArray = [str UTF8String];
//        NSMutableArray *charArray = [NSMutableArray arrayWithCapacity:str.length];
//        [charArray addObject:tmpArray];
//        
        
        NSLog(@"%@",charArray);
        [charArray sortUsingComparator:^(NSString *a, NSString *b){
            return [a compare:b];
        }];
        NSLog(@"%@",charArray);
    } //autoreleasepool
}

//NOTES:
//http://w3facility.org/question/sort-characters-in-nsstring-into-alphabetical-order/
//http://stackoverflow.com/questions/3581532/convert-nsstring-into-char-array
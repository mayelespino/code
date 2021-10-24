//
//  ViewController.swift
//  webTest
//
//  Created by mayel espino on 9/3/17.
//  Copyright © 2017 mayel espino. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var webView: UIWebView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        webView.loadRequest(URLRequest(url: URL(string: "http://localhost")!))
    }
    
    @IBAction func forward(_ sender: Any) {
        if webView.canGoForward
        {
            webView.goForward()
        }
    }
    
    @IBAction func cancel(_ sender: Any) {
        webView.stopLoading()
    }
    
    @IBAction func reLoad(_ sender: Any) {
        webView.reload()
    }
    

    @IBAction func back(_ sender: Any) {
        if webView.canGoBack
        {
            webView.goBack()
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


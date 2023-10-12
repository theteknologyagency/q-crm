/** @odoo-module **/
import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { registry } from "@web/core/registry";
import { browser } from "@web/core/browser/browser";
const userMenuRegistry = registry.category("user_menuitems");
var rpc = require('web.rpc');

var doc_url = ''
var support_url = ''
var online_url = ''
var show_support_url = false
var show_account_url = false
var show_doc_url = false


rpc.query({
    fields: ['doc_url','support_url','online_url','show_support_url','show_account_url','show_doc_url'],
    model: 'sh.debranding.config',
    method: 'search_read',
    limit: 1,
}).then(function (output) {
    doc_url = output && output[0] && output[0].doc_url
    support_url = output && output[0] && output[0].support_url
    online_url = output && output[0] && output[0].online_url
    if(output && output[0] && output[0].show_doc_url == true){
    	show_doc_url = true
    }
    if(output && output[0] && output[0].show_account_url == true){
    	show_account_url = true
    }
    if(output && output[0] && output[0].show_support_url == true){
    	show_support_url = true
    }
    
    delete userMenuRegistry.content['documentation']
    delete userMenuRegistry.content['support']
    delete userMenuRegistry.content['odoo_account']
    
    if(show_doc_url){
    	 userMenuRegistry.add("documentation", shDocumentationItem);
    }
   if(show_support_url){
	   userMenuRegistry.add("support", shSupportItem);
   }
   if(show_account_url){
	   userMenuRegistry.add("odoo_account", shAccountItem);
   }
   
   
   
  
});



function shDocumentationItem(env) {

    

    return {
        type: "item",
        id: "documentation",
        description: env._t("Documentation"),
        href: doc_url,
        callback: () => {
            browser.open(doc_url, "_blank");
        },
        sequence: 10,
    };
}

function shSupportItem(env) {

   

    return {
        type: "item",
        id: "support",
        description: env._t("Support"),
        href: support_url,
        callback: () => {
            browser.open(support_url, "_blank");
        },
        sequence: 20,
    };
}

function shAccountItem(env) {

 

    return {
        type: "item",
        id: "account",
        description: env._t("Account"),
        href: online_url,
        callback: () => {
            browser.open(online_url, "_blank");
        },
        sequence: 60,
    };
}




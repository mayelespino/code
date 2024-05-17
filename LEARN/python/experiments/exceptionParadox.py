Print
Exit
Customer10:14:28 AM PST maespino says, Initial Question/Comment: How to install jboss on my stage or hyper machine?
System10:14:34 AM PST System says, Maneesh has joined this session!
System10:14:34 AM PST System says, Connected with Maneesh
Agent10:15:04 AM PST Maneesh says, hi
Customer10:15:07 AM PST maespino says, Hi
Customer10:15:19 AM PST maespino says, I need JBOSS installed on my machine.
Agent10:15:26 AM PST Maneesh says, k
Customer10:15:30 AM PST maespino says, either on my stage or a hyper machine.
Agent10:15:47 AM PST Maneesh says, give me minute
Customer10:15:55 AM PST maespino says, which manifest should I deploy?
Customer10:17:16 AM PST maespino says, Still there?
Agent10:17:34 AM PST Maneesh says, yes i am trying to find the link
Customer10:17:39 AM PST maespino says, thanks
Customer10:21:21 AM PST maespino says, is JBOSS not part of the default manifest(s) or part of apachectl ?
Agent10:21:44 AM PST Maneesh says, https://ice.paypal.com/ICEPanel/PackageInfo.action
Agent10:21:54 AM PST Maneesh says, you can get that infos here
Agent10:22:24 AM PST Maneesh says, https://ice.paypal.com/ICEPanel/ManifestInfo.action
Agent10:22:39 AM PST Maneesh says, this talks about the manifest and the info
Customer10:23:02 AM PST maespino says, I do not see jboss in that list.
Customer10:24:02 AM PST maespino says, is there a link in ICE where I can give the name of the package and it will tell me the name of the manifest(s) that include it ?
Agent10:24:29 AM PST Maneesh says, yes
Agent10:24:34 AM PST Maneesh says, give me aminute
Customer10:24:57 AM PST maespino says, k
Customer10:28:39 AM PST maespino says, still there?
Agent10:28:54 AM PST Maneesh says, yes
Agent10:29:19 AM PST Maneesh says, https://ice.paypal.com/ICEPanel/PackageInfo.action
Agent10:29:30 AM PST Maneesh says, this is the link for package related manifest
Agent10:30:19 AM PST Maneesh says, why do you want to deploy jboss on the stage by default it should be already there
Customer10:31:00 AM PST maespino says, I do not see JBOSS or jboss anywhere.
Agent10:31:09 AM PST Maneesh says, https://confluence.paypal.com/cnfl/display/~jvint/Install+JBoss+with+Puppet
Customer10:33:10 AM PST maespino says, thanks for that link, so jboss is NOT part of the default installation on stage2 machines?
Agent10:33:25 AM PST Maneesh says, yes
Agent10:33:39 AM PST Maneesh says, it is pushed through puppet
Customer10:34:51 AM PST maespino says, so my question is, I can assume that any stage2 will already have JBOSS installed?
Agent10:35:25 AM PST Maneesh says, ideally yes
Customer10:35:48 AM PST maespino says, how can I check on the stage2 to see if and where it is installed?
Agent10:37:30 AM PST Maneesh says, https://confluence.paypal.com/cnfl/display/Mast/_jboss_start
Customer10:38:58 AM PST maespino says, hmm I do not have that directory in my stage:
Customer10:38:59 AM PST maespino says, cd /opt/jboss/bml/bin/
Customer10:39:07 AM PST maespino says, STAGE2P7346
Agent10:40:20 AM PST Maneesh says, k
Agent10:40:35 AM PST Maneesh says, that means jboss is nt on your stage
Customer10:41:55 AM PST maespino says, correct, and I do not have root permissions on my stage, who can I ask to deploy jboss on my stage?
Agent10:42:15 AM PST Maneesh says, lt me do it for you
Customer10:42:30 AM PST maespino says, yes please.
Customer10:42:38 AM PST maespino says, on two stages:
Customer10:42:47 AM PST maespino says, STAGE2P7346
Customer10:42:48 AM PST maespino says, and
Customer10:43:26 AM PST maespino says, stage2dev309
Agent10:43:34 AM PST Maneesh says, k
Customer10:45:17 AM PST maespino says, thanks
Customer10:48:12 AM PST maespino says, how are we doing?
Agent10:51:15 AM PST Maneesh says, still in progess
Customer10:51:53 AM PST maespino says, coot thanks, and a question: Once installed, I will be able to start/stop jboss on my own (my user id)?
Customer10:52:12 AM PST maespino says, or is it automatically started/stopped by apachectl?
 The following Agent is typing: Maneesh.

Send

Session ID: 953705  
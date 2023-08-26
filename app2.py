import streamlit as st
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(data):
  data = data.lower()
  data = data.replace('\n', " ")
  data = re.sub('[^a-zA-Z ]+', '', data)
  return data

def retrieve_documents(query, documents):
    preprocessed_query = preprocess(query)
    preprocessed_documents = [preprocess(doc) for doc in documents]
    all_texts = [preprocessed_query] + preprocessed_documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    sorted_documents = [document for _, document in sorted(zip(similarity_scores[0], documents), reverse=True)]
    return sorted_documents[:1]

def main():
    st.title("Enter the query you want to resolve:")
    query = st.text_input("", "")
    df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/SocGen/res-1.csv", index_col=False,usecols=['Issue ','Resolution'])
    retreived = retrieve_documents(query,list(df['Issue ']))
    print(retreived)
    incident_response = {'File from Upstream Application is not reaching the downstream application folder.': 'FTR configuration (EDI) was not updated in the downstream application post informatica migration. The config was updated to resolve this issue.',
 'Hyperion Essbase script was creating the file in source folder but failed to push it to the target folder.': '2 jobs were creating 2 files at the same time which is creating deadlock while pushing the file in FTR. Jobs were rescheduled to fix this issue.',
 'Files transferred between systems are arriving corrupted or incomplete': 'Check for data integrity during transfer. Validate checksums or hashes before and after transfer. Ensure that the file transfer method (FTP, SFTP, HTTP) supports binary transfers for non-text files. If the issue persists, consider compressing the file before transfer to mitigate data corruption',
 'Upstream to downstream FTR  failed due to Keys.': 'SSH keys mismatch, dev team sent the public SSH keys which FTR team updated at their end',
 'Files were created in upstream but 0 kb files were sent to downstream.': ' Autosys team corrected the connection at autosys server end  to Fix it.',
 "Transferred files are reaching the destination but don't have the correct permissions, causing access issues": 'Ensure that the user or application performing the transfer has the necessary permissions to write files in the destination folder. Adjust folder permissions and ownership as needed. Regularly audit and review permissions to avoid security vulnerabilities.',
 'Files transferred between systems are being accessed by unauthorized users.': 'Review and enhance security measures. Implement secure file transfer protocols like SFTP or HTTPS. Use encryption for sensitive data. Ensure proper authentication and access controls are in place. Regularly update passwords and access credentials.',
 'File transfers fail when the system experiences high load or traffic': 'Optimize system performance and resource allocation to handle peak loads. Implement queueing mechanisms to manage file transfers during high-demand periods. Monitor system performance and scale resources as necessary.',
 ' Files transferred between systems are not compatible due to differences in file formats.': 'Standardize file formats or provide conversion tools where needed. Include format compatibility checks in the transfer process. Establish clear guidelines for file formats to prevent future compatibility issues.',
 'Unable to access services behind the router from the internet.': 'Configure port forwarding rules on the router.Double-check port numbers and IP addresses.\nVerify that the internal server or service is operational.Test connectivity using external tools.',
 'Wi-Fi coverage is limited to a certain area.': 'Reposition the router for better coverage.Use Wi-Fi extenders or mesh networks.\nAdjust router antennas.Update router firmware.Consider upgrading to a router with better range.',
 'Devices on the network have duplicate IP addresses.': 'Use DHCP to automatically assign IP addresses.Manually assign unique IP addresses.\nRelease and renew IP addresses.Verify no static IP conflicts.',
 'Devices can connect to the network but cannot access the internet.': 'Restart the router/modem and devices.Verify correct IP and subnet settings.\nRelease and renew IP addresses.Reset network settings on devices.Check for MAC address filtering or access control.',
 ' Internet connection is unusually slow': 'Perform a speed test to determine actual speeds.Close bandwidth-intensive applications.Optimize router placement for better coverage.',
 'DNS Resolution Failures: DNS servers fail to resolve domain names to IP addresses.': 'AI system verifies DNS server health, switches to backup servers, and logs the incident.',
 'Firewall Blocking: Incorrect firewall rules prevent users from accessing specific resources.': 'AI system reviews firewall rules, corrects misconfigurations, and ensures proper access.',
 'Router Malfunctions: Network routers malfunction, causing intermittent connectivity issues.': 'AI system monitors router health, triggers diagnostics, and alerts administrators.',
 'Bandwidth Saturation: Excessive network traffic saturates available bandwidth.': 'AI system identifies traffic spikes, prioritizes critical traffic, and recommends bandwidth upgrades.',
 'VPN Connectivity Problems: Users encounter problems connecting to the corporate VPN.': 'AI system monitors VPN connections, troubleshoots failures, and guides users through reconnection.',
 'The software crashes immediately after being launched.': 'Update the software to the latest version.Verify system requirements and compatibility.Check for corrupted installation files.Disable conflicting third-party software.Reinstall the software if necessary.',
 'The software becomes unresponsive and stops responding to user input.': 'Close other resource-intensive applications.Check for software updates or patches.Restart the computer.Disable unnecessary features or extensions.',
 ' The software crashes and data that was being worked on is lost.': 'Enable auto-save features within the software.Use recovery options provided by the software.Utilize temporary file recovery tools.Regularly backup your work to prevent data loss.',
 'The software displays graphical anomalies, artifacts, or distorted visuals.': 'Update graphics drivers to the latest version.Adjust graphics settings within the software.Check for known compatibility issues with your graphics card.If the issue persists, contact software support or the developer.',
 'Users encounter error messages or dialog boxes during software usage.': "Read and understand the error message for clues.Search for the error message online for solutions.Check the software's official documentation or knowledge base.Report the error to the software developer's support team.",
 'Specific features or functions of the software are not working as intended.': "Review the software's user manual or documentation.Verify that you're using the correct input methods.Check for software updates or patches that address the issue.Look for community forums or discussions about similar problems.",
 'Installation or Update Failures': 'Run the installation/update process as an administrator.Disable antivirus or security software temporarily.Check for system compatibility and requirements.\nClear temporary files and cache before installing/updating.Download the installer/update from the official source.',
 'Web applications or websites behave differently or crash across different web browsers.': 'Test and debug using web development tools.Validate the web application against web standards.Use feature detection instead of browser-specific checks.\nResearch and apply browser-specific fixes or workarounds.',
 'Software crashes due to conflicts with third-party plugins or extensions.': 'Temporarily disable plugins/extensions to isolate the issue.Update plugins/extensions to their latest versions.Check for compatibility between plugins/extensions and the software.Report the issue to the plugin/extension developer for support.',
 'Application GUI was down': 'restart the App pool for the application to fix it.',
 'The application crashes immediately upon opening': 'Update the application to the latest version.Check for compatibility with your operating system.Disable conflicting third-party software or extensions.\nReinstall the application if necessary.Run the application in compatibility mode.',
 'Random Application Crashes': "Update the application to the latest version.Check for known issues and patches from the developer.Verify that your system meets the application's requirements.\nTemporarily disable antivirus or security software.Clear application cache and temporary files",
 'Application Crashes When Performing Specific Actions': 'Check if the issue is related to a specific file or data.Test the application with different user accounts.Disable plugins or add-ons that could be causing conflicts.Review user forums or communities for similar issues and solutions.',
 ' Application Crashes When Opening Specific Files': "Ensure the file format is supported by the application.Update or reinstall software components related to the file type.Test the file on another system to confirm if it's corrupted.Repair or reinstall the application if file associations are broken.",
 'The application started crashing after a recent software update.': "Roll back the recent update to check if the issue is resolved.\nCheck for patches or hotfixes related to the recent update.\nContact the software developer's support for assistance.\nMonitor user forums for information about known issues and workarounds.",
 'The application crashes consistently on specific hardware configurations.': "Verify that your hardware meets the application's system requirements.\nUpdate device drivers for components like graphics cards.\nCheck for overheating issues and ensure proper ventilation.",
 'Application Crashes Due to Memory Issues': 'Close other memory-intensive applications while using the software.\nIncrease virtual memory or page file size in your operating system.\nUpdate or repair system memory (RAM) if faulty.',
 'The application crashes only on certain operating systems.': "Verify compatibility with the operating system version.\nCheck for updates or patches provided by the software developer.\nContact the developer's support for assistance with compatibility issues.\nConsider using virtualization or compatibility modes for the application.",
 'Accidental Deletion of Data': 'Check backup systems for a recent copy of the lost data.\nUse data recovery software to retrieve deleted files.\nRestore data from a previous backup.\nImplement better data management practices to prevent future accidents.',
 'Hard Drive or Storage Device Failure': 'Consult with data recovery specialists for hardware repair and recovery.\nRestore data from a recent backup.\nRegularly back up important data to prevent complete loss.',
 'Data files become corrupt, making them unusable.': 'Use file repair tools if available.\nRestore a clean copy of the data from backups.\nInvestigate the cause of corruption to prevent recurrence.',
 'Data is mistakenly overwritten with new content.': 'Restore a backup version with the correct data.\nUse data recovery software to attempt retrieval.\nImplement strict version control to avoid accidental overwrites.',
 'Data Loss Due to Software Bugs': 'Report the bug to the software developer to prevent future occurrences.\nRestore data from backups.\nUse data recovery tools if applicable.',
 'Sensitive data is accessed by unauthorized individuals.': 'Identify the breach source and close security vulnerabilities.\nNotify affected parties as required by data protection laws.\nImplement stronger access controls, encryption, and user authentication.\nConduct security audits to identify and address weak points.',
 'Malicious software encrypts or steals data.': 'Isolate infected systems and remove malware using security tools.\nRestore data from clean backups.Consider involving cybersecurity experts for incident response.',
 'Data is exposed or misused by employees or contractors.': 'Implement strict access controls to limit data exposure.\nMonitor user activity for unusual behavior.Provide comprehensive employee training on data protection.Conduct periodic security reviews and audits.',
 'Altering dimension hierarchies causes unexpected issues.': 'Test hierarchy changes in a development environment first.\nDocument changes and potential impacts.\nReview related calculations and scripts.\nConsider involving experienced Essbase developers.',
 'Cube Build Failures': 'Check data source connections and permissions.\nReview cube build scripts and syntax.\nMonitor disk space availability.\nVerify data integrity and structure.\nAddress any issues with data staging or ETL processes.',
 'OPMN Services are down in Hyperion Essbase server': 'Essbase is not accessible. Windows team restarted the services to fix it',
 'Essbase server switched from Primary to backup node which is not configured.': 'Essbase is not accessible, Windows team needs to switch the instance back to resolve the issue.',
 'Essbase config file was corrupted': 'Essbase server was unreachable. Restore the config file from the backup to fix the issue',
 'Servers are not accessible due to Diskspace issue': 'Clean the unwanted large files/logs manually to increase the freespace to fix the issue.',
 'Treatments are getting failed as no space in Temp DB': 'Freed Tempdb space to fix the incident.',
 'Treatments are getting failed in Database as Tablespace is full.': 'Added more spaceinto the filesystem by DBA team to resolve the issue',
 'Informatica is down due to DB issue': 'Db password was expired and reactivation the issue was resolved.',
 'Application stopped working after DB release': 'While performing the Changes Dba misunderstood the requirement and decomissioned one active service by mistake. Service was restored by DBA and listeners were restarted to fix this.',
 'Application is not accessible due to disk crash': 'Restore the database with backup to fix this issue',
 'Batch failed in production environment due to DB connectivity issue': 'DBA parameter threshhold was updated to fix this issue.',
 'Queries take longer than expected to retrieve data from the database': 'Optimize query execution plans.\nCreate appropriate indexes on frequently queried columns.\nMonitor and optimize database statistics.\nImplement caching mechanisms.\nPartition tables for improved performance.',
 'Multiple transactions are waiting for each other to release locks, causing a standstill.': 'Use appropriate isolation levels.\nOptimize transactions to minimize lock duration.\nImplement retry mechanisms for transactions.\nUse row-level locking when possible.\nMonitor and identify deadlock patterns.',
 ' Data Corruption': 'Regularly back up and verify data integrity.\nUse RAID for hardware fault tolerance.\nImplement checksums and validation checks.\nRestore data from a clean backup.\nInvolve database recovery experts if needed.',
 'Applications cannot connect to the database.': 'Check network connectivity between the application and database server.\nVerify database service status and port availability.\nCheck firewall and security settings.\nReview connection strings and credentials.\nRestart the database service if necessary.',
 'Data is permanently deleted or lost due to human error or system failure.': 'Regularly back up data and test restoration processes.\nImplement point-in-time recovery options.\nImplement proper access controls to prevent accidental deletions.\nEducate users about data management best practices.',
 'Modifications to the database schema or data model cause issues.': 'Perform schema changes during maintenance windows.\nCreate backup copies of the database before making changes.\nTest schema changes in a development environment first.\nPlan and communicate changes to relevant stakeholders.',
 'The database server lacks sufficient resources (CPU, memory, disk) for optimal performance.': 'Monitor and analyze resource usage.\nUpgrade hardware components if necessary.\nOptimize database settings and configurations.\nImplement resource management and allocation strategies.',
 'Data backup or recovery processes fail to complete successfully.': 'Regularly test backup and recovery procedures.\nCheck storage availability for backups.\nMonitor and review backup logs for errors.\nUse consistent backup methods and tools.\nVerify backup integrity through restoration tests.',
 'Index Fragmentation: Database indexes become fragmented, leading to slow query execution.': 'AI system schedules regular index maintenance to defragment indexes.',
 'Data Volume Increase: Growing data volume results in longer query times and performance issues.': 'AI system optimizes queries, implements query caching, or proposes database partitioning.',
 'Resource Contention: Other processes compete for database resources, slowing queries.': 'AI system adjusts resource allocation, prioritizing critical queries.',
 'Query Plan Changes: Database query optimizer generates suboptimal query plans.': 'AI system analyzes query plans, identifies bottlenecks, and suggests optimizations.',
 'Server Misconfiguration: Incorrect database configuration impacts performance.': 'AI system detects and reverts misconfigurations, restores optimal settings.',
 'Hardware Failure: Critical server components fail, leading to server unavailability.': 'AI system detects hardware failures through monitoring and alerts admins for replacement.',
 'Power Supply Issues: Power disruptions cause servers to shut down unexpectedly.': 'AI system installs backup power supply and automatically restarts affected servers.',
 'Network Connectivity Problems: Network connection failures isolate servers from the network.': 'AI system detects network issues, restarts network services, and logs incidents for review.',
 'Software Crashes: Critical software running on servers crashes, rendering them unusable.': 'AI system attempts to restart software, roll back to stable version, or initiate a failover.',
 'Resource Exhaustion: Server resources such as CPU, memory, or disk space are fully utilized.': 'AI system allocates additional resources, optimizes processes, or migrates services.',
 ' Cloud services become unavailable due to infrastructure failures or maintenance.': 'Monitor service status through provider dashboards.\nImplement multi-region redundancy for critical services.\nPlan for failover and disaster recovery.\nLeverage backup providers for temporary coverage.',
 'Cloud services experience slower response times or increased latency.': 'Optimize application architecture for cloud environments.\nMonitor cloud resource utilization.\nImplement autoscaling to handle traffic spikes.\nChoose higher-performance service tiers.',
 'Data stored in the cloud becomes lost or corrupted due to hardware or software issues.': 'Regularly back up data to different geographic regions.\nUse versioning for object storage to restore previous versions.\nImplement data encryption at rest and in transit.\nTest data recovery processes.',
 'Unauthorized access or data breaches occur in the cloud environment.': 'Implement strong access controls and user authentication.\nUse encryption for sensitive data.\nRegularly audit and monitor access logs.\nEducate users about security best practices.',
 ' Cloud services fail to comply with industry regulations or internal policies.': 'Choose cloud providers that offer compliance certifications.\nImplement access controls and encryption to meet security requirements.\nRegularly audit cloud configurations for compliance.',
 'Challenges arise when migrating from one cloud provider to another or back to on-premises.': 'Design applications for portability and avoid vendor-specific features.\nUse open standards and APIs for interoperability.\nRegularly back up data in a format that allows easy migration.',
 'Unexpectedly high cloud service costs or difficulties in managing expenses.': 'Set up cost tracking and monitoring tools.\nImplement resource tagging for better cost allocation.\nRightsize cloud resources based on actual usage.\nLeverage cost optimization tools provided by cloud vendors.',
 'Challenges in integrating cloud services with existing systems or other services.': 'Ensure API compatibility and version control.\nImplement error handling and retries for API requests.\nMonitor API performance and response times.\nUse API gateways for centralized management.',
 'Concerns about the reliability and trustworthiness of the cloud service provider.': "Choose established and reputable cloud providers.\nReview service level agreements (SLAs) for uptime guarantees.\nPerform due diligence on the provider's security practices.\nSeek references and customer reviews."}
    st.write("Possible resolutions:")
    for i,document in enumerate(retreived, start=1):
        # st.write(document)
        st.write(incident_response[document])
    
    
if __name__ == "__main__":
    main()
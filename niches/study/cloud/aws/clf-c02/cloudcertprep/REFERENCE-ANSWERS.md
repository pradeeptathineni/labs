# Upstream Reference Answers

> [!IMPORTANT]
> These answers and explanations come from CloudCertPrep. They are not my answers or evidence of practice.

## clf-c02/domain1/q004

Answer: B, E

Automatically provisioning new resources to meet demand and the ability to recover quickly from failures are both core reliability principles, ensuring the system continues operating correctly under varying conditions and after failure events.
Applying the principle of least privilege is a security practice related to access control, not a reliability principle. All AWS services being considered global services is false, as many services are regional, and global reach is a separate concept from reliability. Providing compensation to customers if issues occur describes an SLA remediation mechanism and is not a design principle that contributes to system reliability.

## clf-c02/domain1/q010

Answer: D

Deploying EC2 instances in a US Region places compute resources physically closer to US users, directly reducing network latency at minimal additional cost.
Applying a Route 53 latency-based routing policy directs users to the Region with the lowest latency, but this only optimizes routing and does not itself reduce latency if all compute resources remain in Tokyo. Registering a new US domain name changes how users reach the application by name but does not move any compute resources closer to US users or reduce network latency. Building a new data center in the US and implementing a hybrid model introduces significant capital expenditure and operational complexity, contradicting the requirement to minimize costs.

## clf-c02/domain1/q013

Answer: C

Elasticity is the cloud best practice of dynamically adjusting compute capacity up or down in response to demand, avoiding over-provisioning during low-traffic periods and under-provisioning during peaks, which directly reduces cost.
Build security in every layer is the Defense in Depth principle from the Security pillar of the Well-Architected Framework, which addresses threat protection rather than capacity management. Parallelizing tasks is a performance design principle that distributes workloads across multiple smaller components to increase throughput, not a mechanism for dynamically adjusting capacity to control costs. Adopting monolithic architecture consolidates all application components into a single tightly coupled unit, which is the opposite of a cloud best practice and does not support dynamic scaling.

## clf-c02/domain1/q014

Answer: A, E

AWS increases speed and agility by allowing customers to provision resources in minutes rather than weeks, and handles physical security along with most data and network security so customers can focus on building applications rather than managing infrastructure.
Unlimited free storage is not an AWS benefit, as storage services such as Amazon S3 and EBS are billed based on the amount of data stored and retrieved. Complete control over physical infrastructure is not available to AWS customers, as AWS owns and manages all physical hardware, data centers, and networking equipment on the customer's behalf. Operating applications on behalf of customers is not an AWS benefit, as customers remain responsible for building, deploying, and managing their own applications under the shared responsibility model.

## clf-c02/domain1/q015

Answer: B

Decoupling means designing components to operate independently so that a failure in one part does not cascade into failures across the rest of the application, improving overall resilience.
Treating an application as a single cohesive unit describes a monolithic architecture, which is the opposite of decoupling and creates tightly coupled dependencies between components. Allowing quick updates to a monolithic application describes an advantage of a well-structured monolith, not of decoupling, and updating a monolith typically requires deploying the entire application as a unit. Tracking API calls made to AWS services describes the function of AWS CloudTrail, which is an auditing and logging service unrelated to application architecture design.

## clf-c02/domain1/q019

Answer: D

Elasticity in AWS means the platform automatically provisions and de-provisions resources in response to real-time changes in demand, so workloads consume only what they need and scale back when demand drops.
Automatically scaling on-premises resources is not what elasticity describes in the AWS context; elasticity is a cloud characteristic that removes the need to invest in on-premises hardware at all, as the cloud provider dynamically adjusts compute capacity. An Elastic Load Balancer distributes incoming traffic across existing instances to prevent any single instance from being overwhelmed, but it does not add or remove instances in response to demand; that capacity adjustment is performed by Auto Scaling. Reducing interdependencies between application components describes the design principle of loose coupling, which improves resilience and maintainability, but is a separate architectural concept from elasticity.

## clf-c02/domain1/q023

Answer: D

The three recognized AWS cloud computing service models are IaaS, PaaS, and SaaS. Networking as a Service is not one of them and does not exist as a defined cloud computing model in the AWS framework.
Platform as a Service is one of the three recognized cloud computing models, providing customers with a managed platform for developing and deploying applications without managing the underlying infrastructure. Infrastructure as a Service is one of the three recognized cloud computing models, giving customers virtualized compute, storage, and networking resources they manage themselves. Software as a Service is one of the three recognized cloud computing models, delivering fully managed applications to end users over the internet without any infrastructure or platform management required.

## clf-c02/domain1/q065

Answer: B

Using loosely coupled components means each part of an application can scale, fail, and be updated independently without cascading failures to other components, which is the foundational AWS best practice for building resilient and scalable architectures.
Using tightly coupled components creates direct dependencies between parts of an application so that a failure or change in one component directly affects others, increasing the risk of cascading failures and making the system harder to scale and maintain independently. A monolithic design combines all components into a single unit that is difficult to scale or update independently, which is the opposite of the modular approach AWS recommends. Stateful components store session data locally on a specific instance, which prevents requests from being distributed freely across instances and undermines horizontal scaling and resilience.

## clf-c02/domain1/q077

Answer: C

AWS allows resources to be provisioned programmatically through APIs, CloudFormation templates, and SDKs, drastically reducing the time to deploy infrastructure compared to traditional procurement and physical setup.
AWS does not operate an IT ticketing platform for resource requests. Resources are provisioned on demand through self-service APIs and consoles without requiring formal request and approval workflows. AWS does not shorten provisioning time through code validation services, which are a software quality tool unrelated to how quickly infrastructure can be deployed. AWS does not automate requests from a company's existing IT vendor list, as it replaces traditional vendor procurement entirely by providing infrastructure directly through its own platform.

## clf-c02/domain1/q084

Answer: C

When applications in the AWS Cloud communicate with a legacy application in a corporate data center, this is a hybrid architecture that combines on-premises and cloud resources in a single solution.
Cloud-native describes applications designed and built entirely to run in the cloud, with no dependency on on-premises infrastructure or legacy systems. Partner network refers to the AWS Partner Network, which is a program for technology and consulting companies that build solutions on AWS, and is not a deployment model. Infrastructure as a Service is a cloud service model that provides virtualized compute, storage, and networking resources, and does not describe the combination of cloud and on-premises components in a single architecture.

## clf-c02/domain1/q099

Answer: C

Distributing workloads across multiple Availability Zones ensures the application can continue operating if one AZ fails, embodying the design for failure principle, where the architecture anticipates and accommodates component failures.
Implement automation refers to reducing manual intervention through scripts and managed services, not to fault tolerance across zones. Design for agility refers to the ability to rapidly experiment and deploy, not to handling infrastructure failures. Implement elasticity refers to automatically scaling resources in response to demand, not to distributing workloads for fault tolerance.

## clf-c02/domain1/q128

Answer: B

Deploying across multiple Availability Zones keeps an application running when one AZ experiences an outage, as traffic fails over to instances in the remaining AZs, directly increasing availability.
Multiple AZs within a single Region do not protect against a natural disaster affecting the entire Region, as all AZs in a Region share the same geographic area and would be exposed to the same regional disruption. Availability Zones within a Region are intentionally close together with low-latency links between them, so they do not provide wider geographic coverage or serve users in distant locations. Deploying across multiple AZs redistributes existing resources rather than reducing the distance between the application and its users, so it does not decrease latency.

## clf-c02/domain1/q130

Answer: B

Loose coupling is a core AWS cloud architecture principle where components interact through well-defined interfaces, allowing each to scale, update, or fail independently without cascading effects on other parts of the system.
Implementing single points of failure is an anti-pattern that directly contradicts cloud architecture best practices, as the goal is to eliminate dependencies that could bring down an entire system. Monolithic design tightly couples all application components into a single unit, making it harder to scale, update, or recover individual parts independently. Vertical scaling increases the capacity of a single instance rather than distributing workloads, which limits scalability and creates potential single points of failure.

## clf-c02/domain1/q132

Answer: C

On-premises infrastructure requires large upfront capital expenditures for hardware and facilities, while AWS converts that spending to variable operational expense where you pay only for what you consume with no hardware purchases required.
Moving from variable operational expense (opex) to upfront capital expense (capex) this reverses the actual direction of the shift, and on-premises environments are characterized by capex, not opex, as the starting point. Moving from upfront capital expense (capex) to variable capital expense (capex) AWS usage is billed as operational expense, not capital expense, so the destination category in this option is incorrect. Elimination of upfront capital expense (capex) and elimination of variable operational expense (opex) moving to AWS eliminates capex but introduces opex rather than eliminating it, as ongoing usage costs are paid as operational expense.

## clf-c02/domain1/q141

Answer: C

By offloading infrastructure management to AWS, companies can redirect their IT staff and resources toward developing and improving their core products and services rather than maintaining data centers.
AWS does not eliminate IT bills, as customers continue to pay for the services they consume under the pay-as-you-go model. Placing a server in each customer's data center describes an on-premises or edge deployment model, which is the opposite of migrating infrastructure to the cloud. Moving to AWS does not allow servers to go unpatched, as the Shared Responsibility Model still requires customers to patch the operating systems and applications running on their own instances.

## clf-c02/domain1/q143

Answer: C

A natural disaster affecting an entire geographic area could take down a whole AWS Region, so deploying across multiple Regions in different geographies ensures the application remains operational even if one Region becomes completely unavailable.
Deploying across multiple Availability Zones within a single Region protects against isolated data center failures but does not provide protection if the entire Region and its surrounding geographic area is affected by a natural disaster. Using a hybrid cloud deployment model within the same geographic area keeps infrastructure in the affected zone, meaning a regional natural disaster would still disrupt both the on-premises and cloud components simultaneously. AWS Artifact is a portal for accessing AWS compliance reports and security documentation, not a storage or replication service, making this option factually incorrect as a disaster recovery strategy.

## clf-c02/domain1/q146

Answer: A, C

Proximity to end users reduces network latency for a better application experience, and data sovereignty compliance requirements mandate that data remains within certain geographic boundaries, making both primary factors in Region selection.
Presenting an application in the local language is an application-layer localisation decision handled through software configuration, not a factor that influences which AWS Region infrastructure is deployed in. Cooling costs in hotter climates are an operational expense absorbed entirely by AWS as part of managing its own data centers, and are not a cost or consideration that customers factor into Region selection. Proximity to the customer's office for on-site visits is not a valid technical or regulatory criterion for Region selection, as AWS data centers are not customer-accessible facilities.

## clf-c02/domain1/q148

Answer: D

Multi-site active-active runs fully redundant live copies of your application across multiple sites simultaneously, so if one site fails the other immediately serves all traffic with essentially zero downtime.
Backup and restore has the highest recovery time of all DR strategies. Data is restored from backups after a failure, meaning significant downtime is expected. Pilot light keeps a minimal version of the environment running and scales up during a disaster, resulting in a short but non-zero recovery time. Warm standby runs a scaled-down but fully functional version of the environment, which requires scaling up before handling full traffic load.

## clf-c02/domain1/q153

Answer: B, D

AWS Professional Services provides expert consulting engagements to help evaluate and plan migrations, and AWS Partner Network partners offer specialized migration expertise through certified consulting and technology firms.
AWS Trusted Advisor scans existing AWS environments for best practice recommendations across cost, performance, security, and fault tolerance, but does not evaluate whether an application is suitable for migration to the cloud. AWS Systems Manager is an operational management service for configuring, patching, and managing AWS resources at scale, and is not a migration advisory or evaluation service. AWS Secrets Manager is a service for storing and rotating application secrets such as database credentials and API keys, and has no role in evaluating applications for cloud migration.

## clf-c02/domain1/q156

Answer: B

No long-term contract is required because AWS uses a pay-as-you-go model, allowing customers to use services on demand and stop at any time without upfront commitments or termination penalties.
AWS is responsible for security in the cloud is a partial truth that misrepresents the Shared Responsibility Model. Security is shared, with AWS responsible for the infrastructure and customers responsible for their data and configurations. Provision new servers in days is inaccurate. One of AWS's key advantages is provisioning resources in minutes, not days, which is the reality that distinguishes cloud from traditional procurement. AWS manages user applications in the AWS Cloud is false. Application management remains the customer's responsibility under the Shared Responsibility Model.

## clf-c02/domain1/q161

Answer: C, D

AWS makes it easy to architect for high availability using multi-AZ deployments, load balancers, and managed services, and the cloud's elasticity allows applications to scale up or down to match demand changes quickly.
AWS does not automatically distribute all data globally by default, as data residency and replication are configuration choices the customer makes depending on the services and settings they select. AWS does not take care of operating the application, as customers remain responsible for deploying, managing, and maintaining their own application code and runtime environments. AWS does not take care of application security patching, as patching the application layer is the customer's responsibility under the Shared Responsibility Model.

## clf-c02/domain1/q173

Answer: B

Elasticity is the ability to scale resources up or down automatically to handle increases in users, traffic, or data size without any degradation in performance, making it the principle that directly addresses growth support.
Think parallel refers to the principle of designing systems to handle tasks simultaneously across multiple resources to improve throughput and speed, not specifically to handle growth in users or data size without performance loss. Decouple your components refers to reducing dependencies between application components so failures do not cascade, which improves resilience rather than addressing performance under growth. Design for failure refers to building systems that anticipate and recover from component failures automatically, which addresses resilience and availability rather than scaling to support growth.

## clf-c02/domain1/q174

Answer: C

Cloud elasticity allows resources to scale up or down on demand, eliminating the need to predict and provision for peak future capacity in advance.
Easy and fast deployment of applications in multiple Regions is a benefit of AWS's global infrastructure, enabling speed and reach, but does not remove the need to estimate future infrastructure usage. Security of the AWS Cloud refers to the protections AWS provides for its infrastructure under the shared responsibility model, which is unrelated to capacity planning or infrastructure estimation. Lower variable costs due to massive economies of scale means AWS can offer reduced pricing as its customer base grows, but lower costs do not eliminate the underlying need to estimate how much infrastructure will be required.

## clf-c02/domain1/q187

Answer: A

With AWS, developers and engineers can self-provision infrastructure in minutes through the console or APIs, eliminating the waiting time associated with traditional hardware procurement and setup.
The AWS Cloud infrastructure is much faster than an on-premises data center infrastructure is misleading. The productivity gain comes from removing provisioning delays, not from raw infrastructure speed. AWS takes over application configuration management on behalf of users is false. Application configuration remains the customer's responsibility under the Shared Responsibility Model. Users do not need to address security and compliance issues is false. Customers remain responsible for security in the cloud, including their applications, data, and access controls.

## clf-c02/domain1/q189

Answer: D

Agility in the AWS Cloud is best illustrated by the dramatically reduced time to acquire and provision new compute resources, from weeks on-premises to minutes in the cloud, enabling teams to experiment and iterate faster.
Access to multiple instance types is a flexibility benefit that allows customers to match compute to workload requirements, but does not directly describe the speed of acquiring new resources. Access to managed services reduces operational overhead by offloading infrastructure management to AWS, but is an example of reduced complexity rather than agility. Consolidated Billing is a cost management feature that combines charges from multiple accounts into a single bill, which is a billing convenience and unrelated to the speed of resource acquisition.

## clf-c02/domain1/q203

Answer: C

AWS best practice is to automate infrastructure and deployment wherever possible, which makes architectural experimentation faster and reduces human error.
Investing heavily in upfront architectural design contradicts the cloud principle that infrastructure should be treated as flexible and changeable, with automation enabling rapid iteration rather than requiring heavy planning before deployment. Using AWS reservations to reduce costs when testing production environments misapplies Reserved Instances, which are a billing commitment for predictable steady-state workloads rather than a cost reduction tool for testing environments. Provisioning large compute capacity to handle any spikes in load describes over-provisioning, which is an on-premises anti-pattern that cloud best practices replace with elastic scaling that dynamically matches capacity to actual demand.

## clf-c02/domain1/q206

Answer: B, C

Deploying across multiple Availability Zones provides physical redundancy so that if one zone experiences a failure, instances in the remaining zones continue serving traffic without interruption. Elastic Load Balancing automatically detects unhealthy targets and routes traffic only to healthy ones, preventing a single failed instance from bringing down the entire application. Both directly implement the design-for-failure principle.
Multi-factor authentication adds a second layer of security to account and user sign-in, and is an access security control with no bearing on fault tolerance or application resilience. Penetration testing simulates attacks against an application to identify security vulnerabilities, and is a security assessment practice rather than an architectural design approach for surviving component failures. Vertical scaling increases the capacity of a single instance by adding more CPU or memory, which creates a larger single point of failure rather than distributing risk, and is the opposite of the redundancy that design-for-failure requires.

## clf-c02/domain1/q215

Answer: C

Migrating from on-premises to AWS converts large upfront capital expenditures such as purchasing and maintaining physical hardware into smaller variable operational expenses, directly reducing CapEx and improving financial flexibility.
AWS does not provide free support to all enterprise customers, as support is available through paid tiers ranging from Developer to Enterprise, with costs varying by plan. AWS does not automatically protect data on behalf of customers, as data protection responsibilities such as encryption and backup configuration remain with the customer under the Shared Responsibility Model. AWS does not manage customer applications, as application-layer responsibilities including code, configuration, and runtime management remain with the customer regardless of which infrastructure services they use.

## clf-c02/domain1/q216

Answer: D, E

Automating wherever possible reduces manual errors and speeds recovery, and removing single points of failure through redundancy ensures continued operation if one component fails, both being core AWS design principles.
Always using Global Services rather than Regional Services is not a recognized design principle, as the choice between global and regional services depends on the specific workload requirements and is not a blanket architectural rule. Always choosing to pay as you go is a billing model characteristic rather than a system design principle, and pricing decisions are made based on cost optimization goals rather than architectural patterns. Treating servers as fixed resources contradicts the cloud design principle of elasticity, which calls for treating infrastructure as disposable and dynamically scalable rather than permanent and static.

## clf-c02/domain1/q225

Answer: B, C

Cloud computing eliminates single points of failure through redundancy across multiple data centers, and its geographically distributed infrastructure means no single physical failure can take down the entire system, both of which are structural advantages over traditional data centers.
Reserved compute capacity requires upfront commitment to fixed resources and exists in both cloud and traditional environments, so it is not a differentiating advantage of cloud. Virtualized compute resources are used in traditional data centers as well as in the cloud, making virtualization itself a shared characteristic rather than a cloud advantage. Dedicated hosting allocates physical hardware exclusively to one customer and is available in both cloud and traditional environments, so it does not represent an advantage of cloud computing over traditional infrastructure.

## clf-c02/domain1/q227

Answer: C

The Operational Excellence pillar of the AWS Well-Architected Framework focuses on running and monitoring workloads effectively, continuously improving processes, and automating operations to deliver business value.
The ability of a system to recover gracefully from failure describes the Reliability pillar, which focuses on workload availability and the ability to recover from disruptions. The efficient use of computing resources to meet requirements describes the Performance Efficiency pillar, which focuses on using the right resource types and sizes to match workload demands. Managing datacenter operations more efficiently does not correspond to any Well-Architected pillar, as AWS manages all physical datacenter infrastructure on behalf of customers and this is not a customer concern in the cloud.

## clf-c02/domain1/q242

Answer: B

A fault-tolerant system is designed to continue operating correctly even when some of its components fail, which is exactly what the scenario describes: three of six instances crashed but no customers were affected.
An elastic system automatically scales capacity up or down in response to changes in demand, but elasticity does not address continued operation during component failure. An encrypted system protects data from unauthorised access through cryptographic controls, which is a security property unrelated to maintaining availability when instances crash. A scalable system is designed to handle growth in workload or users by adding resources, but scalability does not ensure the application keeps running when existing instances fail.

## clf-c02/domain1/q253

Answer: B

Amazon EC2 is IaaS because AWS provides the virtualized compute infrastructure while the customer manages the operating system, middleware, and applications above it.
IaaS and SaaS combined is not a recognized classification for any single service, as each service falls under one model rather than spanning two. SaaS delivers fully managed software applications to end users with no infrastructure or platform management required, whereas EC2 requires customers to manage everything above the hypervisor. PaaS provides a managed platform where customers deploy application code without managing the underlying infrastructure, whereas EC2 gives customers direct control over the operating system and runtime environment.

## clf-c02/domain1/q254

Answer: D

Decoupling application components so they communicate through well-defined interfaces such as APIs or queues rather than direct dependencies means each component can scale, fail, and be updated independently without causing cascading failures throughout the application.
Applying the principle of least privilege is a security best practice for controlling access permissions, and while important, it relates to identity and access management rather than application architecture design. Ensuring that applications run on hardware from trusted vendors is not a customer concern on AWS, as AWS manages all underlying physical infrastructure and hardware selection on behalf of the customer. IAM policies are used to define access permissions for users and roles, and are an identity and access management tool rather than a mechanism for maintaining application performance.

## clf-c02/domain1/q261

Answer: B

AWS global reach, through its worldwide network of Regions and edge locations, enables applications to be deployed closer to international users, reducing the network distance that data must travel and lowering latency for a global audience.
Elasticity is the ability to automatically scale resources up or down in response to changing demand, and addresses capacity flexibility rather than the geographic proximity that causes latency for international users. Data durability refers to the long-term integrity and redundancy of stored data to prevent loss, and is a storage protection characteristic with no bearing on network latency or geographic reach. High availability refers to the ability of a system to remain operational and accessible with minimal downtime, and addresses uptime and fault tolerance rather than reducing latency for geographically distributed users.

## clf-c02/domain1/q263

Answer: D

Deploying AWS resources to a second AWS Region and running an Active-Active disaster recovery strategy means both Regions serve live production traffic simultaneously, so if a natural disaster eliminates one Region entirely, the other continues serving users without any downtime.
Amazon CloudFront distributes and caches content at edge locations to reduce latency for end users, but it is a content delivery service and does not replicate workloads or perform automatic failover of application infrastructure in the event of a regional disaster. Deploying resources across multiple Availability Zones within a single Region improves resilience against isolated failures, but a large-scale natural disaster can affect an entire Region simultaneously, making Multi-AZ alone insufficient when zero downtime is required. Creating point-in-time backups in another subnet stores recovery data within the same Region and requires manual restoration time, which directly conflicts with the requirement to accept no downtime. Subnets are also intra-Region constructs that offer no geographic separation.

## clf-c02/domain1/q271

Answer: D

Physical hardware costs, including servers, networking, and storage, must be purchased and maintained on-premises but are replaced by AWS managed infrastructure in the cloud, making them the key differentiator in a TCO comparison.
Application development costs remain relatively constant regardless of where an application is hosted, so they do not meaningfully affect an on-premises versus cloud comparison. Market research is not a component of TCO analysis. Business analysis costs also remain consistent regardless of hosting environment and are not a factor in infrastructure cost comparisons.

## clf-c02/domain1/q276

Answer: C

AWS Cloud agility refers to the ability to provision infrastructure resources in minutes through the console, CLI, or API, dramatically faster than the weeks or months required for on-premises hardware procurement.
Hosting applications in multiple Regions describes global reach, which is a separate cloud benefit from agility. AWS providing customizable hardware at the lowest possible cost misrepresents how AWS works, as customers do not configure or own the underlying hardware. Paying upfront to reduce costs describes Reserved Instance pricing, which is the opposite of the pay-as-you-go model that defines cloud economics.

## clf-c02/domain1/q291

Answer: D

Deploying an application across multiple Availability Zones ensures it continues running from the remaining AZs if one experiences an outage, directly increasing availability by eliminating single points of failure within a Region.
AWS service limits are account and resource quotas set by AWS that can be increased through a support request, and are entirely unrelated to how many Availability Zones an application is deployed across. Reducing application response time for global users requires deploying across multiple Regions or using a content delivery network such as CloudFront, as AZs within a single Region are geographically close together and do not reduce latency for distant users. Increasing available compute capacity requires provisioning additional instances or enabling Auto Scaling, as spreading existing resources across multiple AZs redistributes capacity rather than adding to it.

## clf-c02/domain1/q303

Answer: B, C

AWS managed services handle infrastructure provisioning, patching, and maintenance, which lowers operational complexity for customers and lets them deliver new solutions faster by focusing on application logic instead of infrastructure management.
Providing complete control over the virtual infrastructure is a characteristic of IaaS services such as EC2, not managed services, which deliberately abstract away infrastructure management in exchange for reduced operational burden. Using a managed service does not eliminate the need to encrypt data, as data protection responsibilities including encryption at rest and in transit remain with the customer under the Shared Responsibility Model. Managed services remove patching responsibilities from the customer rather than giving developers control over them, as AWS handles all underlying patching and maintenance on the customer's behalf.

## clf-c02/domain1/q307

Answer: D

AWS APIs enable programmatic management of AWS resources, allowing developers to automate provisioning, configuration, and monitoring through code rather than manual console interactions.
Using an API to access AWS services does not inherently improve the performance of the underlying resources, as API access is a management interface rather than a performance enhancement mechanism. While automation through APIs can speed up workflows, the primary benefit is programmatic control rather than a reduction in provisioning time specifically. APIs enable developers to interact with AWS services through code, but they do not reduce the number of developers needed to manage an environment and may in fact require additional development skills.

## clf-c02/domain1/q320

Answer: A, D

Multi-region architectures serve global customers with lower latency, and serverless architectures automatically scale to match demand without capacity planning, both being key design principles of the Performance Efficiency pillar.
Applying security at all layers is a design principle of the Security pillar of the AWS Well-Architected Framework, not the Performance Efficiency pillar. Implementing strong identity and access controls is also a Security pillar principle focused on protecting resources through least privilege and access management, and is unrelated to performance efficiency. Enabling audit logging is a Security and Operational Excellence pillar practice used for compliance and incident investigation, and is not a Performance Efficiency design principle.

## clf-c02/domain1/q322

Answer: C, E

AWS provides elastic resources that scale up and down with demand, eliminating the need to over-provision capacity, and offers cost savings through pay-as-you-go pricing that avoids large upfront capital investments required by on-premises data centers.
AWS does not provide free commercial software licenses, as third-party software costs are separate from AWS infrastructure pricing and must be purchased independently or through AWS Marketplace. AWS does not provide free technical support, as support is available through paid tiers and basic support only covers account and billing queries without technical assistance. AWS does not offer on-site visits for auditing, as customers requiring compliance evidence use AWS audit reports, certifications, and the AWS Artifact portal rather than physical site access.

## clf-c02/domain1/q327

Answer: C

The AWS Cloud Adoption Framework is a guidance framework created by AWS Professional Services that helps organizations plan and execute their cloud adoption journey across six perspectives: Business, People, Governance, Platform, Security, and Operations.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a security service for credential management with no connection to cloud adoption planning or road map development. AWS WAF is a web application firewall that filters malicious HTTP requests based on defined rules to protect web applications from common exploits, and is a security service with no connection to cloud adoption frameworks or strategic road maps. Amazon EFS is a managed shared network file system that provides concurrent file access from multiple compute instances, and is a storage service with no connection to cloud adoption planning or strategic frameworks.

## clf-c02/domain1/aif-q329

Answer: C

Clustering customer segments is an example of unsupervised learning because the algorithm groups data points based on similarity without being given any labeled examples or predefined categories to learn from. The model discovers the structure in the data on its own.
Predicting house prices uses labeled training data where each example has a known price, making it a supervised regression task. Spam detection trains a model on emails already labeled as spam or not spam, making it a supervised classification task. Image classification trains a model on images with known labels, such as cat or dog, also making it a supervised classification task.

## clf-c02/domain1/q330

Answer: C, E

Startups prefer AWS because they can replace large upfront capital expenditure with low variable pay-as-you-go costs, and reduce time-to-market by focusing on product development rather than building and managing data centers.
AWS allows them to pay later when their business succeeds is false. AWS requires payment for resources as they are used, not deferred until a business becomes profitable. AWS can build complete data centers faster than any other cloud provider is false and not a stated AWS value proposition. AWS removes the need to invest in operational expenditure is false. Operational expenditure still exists on AWS; the key shift is from upfront capital expenditure to ongoing variable costs.

## clf-c02/domain1/q333

Answer: A, C

As part of the AWS Migration Acceleration Program, AWS provides access to AWS Partners including consulting and technology partners with migration expertise, and AWS Professional Services which works directly with customers on cloud adoption and migration projects. Both are core components of the MAP program.
AWS Artifact is a self-service portal for accessing AWS compliance reports and security agreements, and is a compliance documentation resource rather than a component of the Migration Acceleration Program. Amazon Athena is a serverless query service that analyzes data stored in Amazon S3 using SQL, and is an analytics service with no role in enterprise cloud adoption acceleration or migration support. Amazon Pinpoint is a customer engagement service for sending targeted messages via email, SMS, and push notifications, and is a marketing communications tool with no connection to enterprise cloud migration acceleration.

## clf-c02/domain1/q343

Answer: C

Fault tolerance is the ability of a system to continue operating without interruption when one or more components fail, achieved through redundancy across Availability Zones and automatic failover, directly minimizing the risk of costly outages.
Least privilege is a security principle that restricts user and service permissions to the minimum required to perform their function, and has no bearing on system availability or outage prevention. Pilot light is a disaster recovery strategy that keeps a minimal version of the environment running in a secondary Region, which addresses recovery after an outage rather than preventing one through redundancy. Multi-threading is a software programming technique that allows concurrent execution of multiple tasks within a single application, and is unrelated to cloud architecture design for availability.

## clf-c02/domain1/q371

Answer: A

Deploying an application across at least two Availability Zones ensures that if one AZ experiences an outage, the application continues running in the other, providing high availability.
Deploying across multiple AWS Regions provides geographic redundancy for disaster recovery but introduces significant complexity and cost, and is not the standard best practice for achieving high availability within a single application deployment. Deploying on multiple servers within the same Availability Zone improves redundancy at the server level but does not protect against an AZ-wide outage, leaving the application vulnerable to a single point of failure. Rewriting application code to handle all incoming requests on a single deployment does not address infrastructure failure and cannot provide high availability if the underlying infrastructure becomes unavailable.

## clf-c02/domain1/q372

Answer: A, B

A TCO analysis compares on-premises costs including labor, IT staff, cooling, and power consumption against AWS costs, where these physical infrastructure expenses are eliminated.
Amazon EBS computing power is an AWS service cost rather than an on-premises infrastructure expense, so it does not belong in a TCO comparison of what customers stop paying for when they migrate. Software architecture refers to how an application is designed and structured, which is a technical consideration rather than an infrastructure cost factored into a TCO analysis. Software compatibility refers to whether applications can run in a new environment, which is a migration planning concern rather than a cost category included in a TCO comparison.

## clf-c02/domain1/q388

Answer: B

Loose coupling is the design practice of minimizing dependencies between application components so that a failure in one component does not cascade to others, improving overall system resilience.
Elastic coupling is not a recognized cloud design principle or architectural term, and may cause confusion with Amazon EC2 Auto Scaling or Elastic Load Balancing, which are services rather than coupling patterns. Scalable coupling is not a recognized architectural concept, and scalability is a separate design goal achieved through practices such as horizontal scaling rather than a type of component coupling. Tight coupling is the opposite of the correct answer, describing an architecture where components are highly dependent on each other, meaning a failure in one component is more likely to cascade and impact others.

## clf-c02/domain1/q397

Answer: D, E

AWS eliminates the need to guess infrastructure capacity through on-demand scaling, and enables customers to trade large upfront capital expenses for smaller variable operational expenses based on actual usage.
Customers remain responsible for monitoring their own servers and applications, as AWS provides the tools but does not perform monitoring on the customer's behalf. Compliance and auditing responsibilities are shared, with customers accountable for their own data, access controls, and application-level compliance regardless of using AWS. AWS does not provide custom hardware to individual customer specifications, as customers select from standardized instance types and managed services within the shared infrastructure.

## clf-c02/domain1/q406

Answer: C

A hybrid deployment model connects cloud-based resources with existing infrastructure not located in the cloud, such as on-premises data centers, allowing organizations to extend their environment into AWS while keeping some workloads running locally.
On-premises is a deployment model where all infrastructure is hosted and managed within an organization's own facilities with no cloud integration, which is the opposite of connecting cloud and non-cloud resources. Mixed is not a recognized cloud computing deployment model and does not appear in the AWS framework alongside on-premises, hybrid, and cloud. Cloud is a deployment model where all infrastructure and applications run entirely within the cloud provider's environment with no dependency on locally hosted resources, meaning there are no existing non-cloud resources to connect to.

## clf-c02/domain1/q420

Answer: C

Economies of scale means that as AWS grows and aggregates more customer usage, it achieves lower per-unit costs and continuously passes those savings on to customers through regular price reductions.
Saving more when you consume more describes volume-based discounts such as Reserved Instances or tiered pricing, which is a separate pricing concept rather than the definition of economies of scale. Paying more over time as usage increases describes the opposite of what economies of scale delivers, as AWS prices have consistently decreased over time rather than increased. The ability to pay as you go describes the pay-as-you-go billing model, which is a separate cloud adoption benefit unrelated to the cost reductions driven by aggregated purchasing power.

## clf-c02/domain1/q439

Answer: B

Serverless architectures are more economical because compute resources are only allocated during actual code execution, meaning there are no charges for idle capacity, unlike server-based architectures where instances run continuously and incur costs even when no requests are being processed.
Serverless architectures do not eliminate networking costs; data transfer and API call costs still apply and are billed separately based on usage. Reserved capacity discounts do not apply to serverless compute in the same way they apply to EC2 instances; serverless pricing is based entirely on the number of requests and duration of execution rather than reserved capacity commitments. The ability to scale automatically is also available on server-based architectures using Auto Scaling groups, so this is not a characteristic unique to serverless; the key economic advantage is the elimination of costs during idle periods.

## clf-c02/domain1/q459

Answer: C

AWS allows customers to launch and terminate EC2 instances based on real-time demand, so during low-traffic periods they stop paying for unused capacity, unlike traditional data centers where hardware sits idle regardless of utilization.
Launching powerful instances to handle spikes in load describes vertical scaling, which still results in over-provisioned and idle capacity during low-traffic periods and does not address the core economic inefficiency of traditional data centers. Paying upfront to get bigger discounts describes Reserved Instance pricing, which is a commitment-based model that reduces per-unit cost but does not eliminate the problem of paying for capacity during periods of low demand. Choosing cheaper instance types reduces the unit cost of compute but does not eliminate idle capacity costs, as the instances would still run and incur charges regardless of whether they are actively being used.

## clf-c02/domain1/q467

Answer: B, D

Loose coupling minimizes dependencies between components so that failures do not cascade, and treating resources as disposable means designing for failure by replacing instances rather than fixing them, enabling rapid recovery.
Reserved capacity instead of on demand is the opposite of a cloud design principle, as cloud encourages provisioning resources dynamically based on actual need. Servers instead of managed services contradicts the cloud principle of offloading operational burden to AWS wherever possible. Multi-AZ versus multi-region is not a recognized AWS design principle and presents a false trade-off, as both are valid availability strategies depending on the use case.

## clf-c02/domain1/q470

Answer: D

Deploying across multiple Availability Zones in multiple AWS Regions provides the highest level of redundancy and fault tolerance, protecting against both AZ-level failures and Region-wide outages simultaneously.
AWS is not redundant by default for customer workloads. Customers must architect their own applications for redundancy using the available infrastructure components. Deploying in a single Availability Zone provides no redundancy, as an AZ failure would take the entire application offline. Deploying across multiple Availability Zones in a single Region protects against AZ-level failures but leaves the application vulnerable to a Region-wide outage.

## clf-c02/domain1/q514

Answer: B

Deploying across multiple Availability Zones ensures that if one AZ experiences a failure, the application continues running in another, providing fault tolerance through physical redundancy within a Region.
Deploying across multiple EC2 instances improves capacity and availability within a single location but does not protect against an AZ-level failure if all instances are in the same zone. Hosting on one powerful EC2 instance consolidates the application onto a single point of failure, which reduces fault tolerance rather than increasing it. Deploying across multiple subnets improves network segmentation but does not provide fault tolerance unless those subnets span multiple Availability Zones.

## clf-c02/domain1/q517

Answer: D

Loose coupling allows individual components to be modified, updated, or replaced independently without affecting other parts of the system, enabling faster development cycles and more resilient architectures.
Eliminating the need for change management is incorrect because change management remains necessary in any architecture. Loose coupling makes changes safer and less disruptive, but does not remove the need to manage them. Cross-Region Replication is a data redundancy and disaster recovery strategy that is unrelated to the architectural principle of reducing dependencies between components. Reducing Privileged Access to AWS resources is a security practice related to the principle of least privilege, not a benefit of loose coupling.

## clf-c02/domain1/q519

Answer: D

The cloud deployment model eliminates the need to run and maintain physical data centers entirely, as all infrastructure is hosted and managed by the cloud provider in their facilities.
On-premises is a deployment model where all infrastructure is owned and operated within an organization's own facilities, which is the opposite of eliminating physical data center management. IaaS is a cloud service model that provides virtualized compute, storage, and networking resources, and is not a deployment model that addresses where or how infrastructure is physically managed. PaaS is a cloud service model that provides a managed platform for application development and deployment, and is similarly not a deployment model that determines physical data center responsibility.

## clf-c02/domain1/q530

Answer: A

AWS Regions are geographically separate locations around the world, meaning infrastructure deployed across multiple Regions remains operational even if an entire Region is affected by an outage.
Transportation devices are physical data transfer hardware such as AWS Snow Family devices and have no role in disaster recovery architecture. Support plans are subscription tiers that provide access to AWS technical assistance and do not affect infrastructure availability or redundancy. Edge locations are points of presence used for content delivery and caching, not designed for deploying full infrastructure for disaster recovery purposes.

## clf-c02/domain1/q533

Answer: C

The Performance Efficiency pillar of the Well-Architected Framework focuses on selecting the right resource types and sizes based on workload requirements to use computing resources efficiently.
Operational Excellence focuses on running and monitoring systems to deliver business value and continually improving processes and procedures, and does not specifically address compute resource selection based on workload requirements. Security focuses on protecting information and systems through risk assessment, access management, and controls, and is not concerned with matching compute resources to workload performance needs. Reliability focuses on ensuring a workload can recover from failures and dynamically acquire resources to meet demand, but its emphasis is on resilience and recovery rather than on selecting the right compute resource types for efficiency.

## clf-c02/domain1/q541

Answer: C

Designing an application to accommodate the failure of any single component, through redundancy, health checks, and automatic failover, is the core principle of designing for failure and is the recommended pattern for achieving high availability on AWS.
Ensuring low-latency network connectivity is a performance optimization consideration that improves user experience, but low latency alone does not protect an application from component failures or maintain availability during an outage. Running enough EC2 instances to handle peak load addresses capacity planning but does not build in redundancy or fault tolerance, meaning a single component failure could still bring down the application. A monolithic application that handles all operations consolidates functionality into a single unit, which creates a single point of failure and is the opposite of a highly available architecture that can survive individual component failures.

## clf-c02/domain1/q542

Answer: C, D

Elasticity lets you automatically scale resources up or down with demand, and pay-as-you-go pricing ensures you only pay for what you actually use, making both ideal for workloads with unpredictable, dynamic demand.
High availability ensures that applications remain accessible despite failures by using redundancy across multiple Availability Zones, and while it contributes to reliability it does not directly reduce costs for workloads with dynamic demand. The shared security model defines the division of security responsibilities between AWS and the customer, and is a governance principle rather than a characteristic that makes AWS cost effective for variable workloads. Reliability refers to the ability of a workload to perform its intended function correctly and consistently, and while important for system design it is not itself a pricing or cost efficiency characteristic that reduces costs for dynamic demand.

## clf-c02/domain1/q557

Answer: D

Elasticity is a key cloud design principle that means automatically scaling compute resources up or down based on actual demand, avoiding over-provisioning and reducing costs compared to traditional fixed-capacity infrastructure.
Using the largest instance possible is the opposite of good cloud design, as it leads to over-provisioning and unnecessary cost rather than matching capacity to actual demand. Provisioning capacity for peak load is a traditional on-premises approach that results in idle resources during normal periods, which cloud elasticity is specifically designed to replace. Using the Scrum development process is a software delivery methodology unrelated to cloud architecture design principles.

## clf-c02/domain1/q561

Answer: B

AWS offloads infrastructure management to its own teams, freeing customers from data center operations so they can redirect time and resources toward product development, customer engagement, and other revenue-generating activities.
Permissive security is not an AWS benefit and directly contradicts AWS's security model, which is built on the principle of least privilege and layered access controls. Control over cloud network hardware is not available to customers, as AWS manages all physical networking infrastructure on their behalf. Choice of specific cloud hardware vendors is not offered to customers, as AWS selects and manages its own hardware independently of customer preferences.

## clf-c02/domain1/q572

Answer: B

Deploying across multiple Availability Zones ensures an application remains available if one zone fails, as each AZ is a physically separate location within a Region with independent power, networking, and connectivity.
AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, which improves connectivity but does not provide application redundancy or fault tolerance. Data centers are the physical facilities that make up Availability Zones and are managed entirely by AWS, so customers cannot directly leverage individual data centers as an architectural feature. Amazon VPC provides an isolated virtual network within AWS for resource deployment and access control, but does not itself provide redundancy or ensure an application stays available during a failure.

## clf-c02/domain1/q574

Answer: B

Loosely coupling components means designing them to interact through well-defined interfaces such as queues or APIs, so that changes or failures in one component do not directly impact others.
Scaling up not out describes vertical scaling, which is an on-premises approach that cloud best practices discourage in favor of horizontal scaling through adding more instances. Building monolithic systems consolidates all application components into a single tightly coupled unit, which is the opposite of the cloud design principle of breaking applications into loosely coupled, independently deployable components. Using commercial database software is a technology procurement decision rather than an architectural design principle, and cloud best practices favor managed and purpose-built database services over proprietary commercial software where appropriate.

## clf-c02/domain1/q577

Answer: A, C

AWS reduces Total Cost of Ownership by eliminating data center capital expenses, and reduces operational expenditure through pay-as-you-go pricing and managed services that lower staffing and maintenance costs.
Increased capital expenditure describes the opposite of an AWS financial benefit. Moving to AWS replaces large upfront hardware investments with variable operational costs, reducing rather than increasing capital expenditure. Deferred payment plans for startups is not a standard AWS financial benefit. AWS charges are billed monthly based on actual usage, and there are no deferred payment arrangements offered as a general benefit to startup customers. Business credit lines for startups are not provided by AWS as a standard financial benefit. AWS does have programs such as AWS Activate that provide credits to startups, but these are promotional credits rather than credit lines or financing arrangements.

## clf-c02/domain1/q583

Answer: C

On-premises TCO includes physical data center security costs such as guards, access controls, and surveillance. These are eliminated when moving to AWS, where physical security is entirely AWS's responsibility.
Project management costs apply equally to both on-premises and cloud environments and are not a differentiating factor in a TCO comparison. Antivirus software licensing is an application-layer cost that remains the customer's responsibility regardless of whether they run on-premises or on AWS. Software development costs are also consistent across environments and do not change based on infrastructure hosting decisions.

## clf-c02/domain1/q590

Answer: A

Using multiple Availability Zones ensures high availability by distributing your application across physically isolated data centers, so that a failure in any single zone does not take the entire application offline.
Using tightly coupled components is an anti-pattern in cloud architecture, as tight dependencies between components mean a failure in one can cascade and bring down others. Using open source software is a development and licensing choice that has no bearing on cloud architectural design principles for availability or resilience. Provisioning extra capacity contradicts the cloud principle of elasticity, which favors scaling dynamically based on actual demand rather than guessing and over-provisioning upfront.

## clf-c02/domain1/q600

Answer: C

Elastic computing lets customers match resource capacity to actual demand, scaling up during peaks and down during lulls, eliminating payment for idle infrastructure and directly reducing total cost of ownership.
The Shared Responsibility Model defines the division of security duties between AWS and the customer, but does not itself reduce infrastructure costs or TCO. Single tenancy dedicates hardware to a single customer, which typically increases cost compared to the shared multi-tenant model that underpins AWS's economies of scale. Encryption is a security control that protects data at rest and in transit, and has no direct impact on infrastructure costs or TCO.

## clf-c02/domain1/q604

Answer: B

AWS's global reach, with Regions and edge locations spread worldwide, allows companies to deploy resources close to their international customers, directly reducing network latency.
Fault tolerance refers to a system's ability to continue operating despite component failures, not to reducing geographic latency. Pay-as-you-go pricing is a billing model and has no effect on network latency or geographic reach. High availability ensures systems remain operational with minimal downtime, but does not address the physical proximity needed to reduce latency for international customers.

## clf-c02/domain1/q614

Answer: C, E

Loose coupling reduces inter-component dependencies so that a failure in one part of the application does not cascade to others, and designing for scalability ensures each component can independently handle varying loads, both being essential principles when breaking apart a monolithic architecture.
Manual monitoring relies on human observation rather than automated alerting and is an anti-pattern in cloud architecture. Fixed servers contradict the cloud principle of elasticity and scalability, locking capacity to a predetermined amount regardless of demand. Relying on individual components is the defining characteristic of a monolithic architecture and is the problem being solved, not a recommended design principle.

## clf-c02/domain1/q621

Answer: A

AWS passes its operational efficiencies and massive purchasing power to customers through periodic price reductions, lowering the cost of cloud services as AWS's scale grows.
New EC2 instance types providing the latest hardware is a product development activity, not a direct financial benefit passed to customers from economies of scale. The ability to scale up and down when needed describes elasticity, which is a separate cloud benefit unrelated to economies of scale. Increased reliability in the underlying hardware describes AWS infrastructure quality, not a cost or efficiency benefit derived from operating at massive scale.

## clf-c02/domain1/q634

Answer: B, C

Elasticity allows resources to automatically scale up and down based on demand, and agility enables rapid provisioning and experimentation without long procurement cycles. Both are core advantages of the AWS Cloud over traditional infrastructure.
Unlimited uptime is not a guaranteed or marketed AWS benefit, as AWS services are subject to availability SLAs but not unconditional uptime. Colocation refers to housing your own physical servers in a third-party data center, which is a traditional infrastructure model rather than a cloud benefit. Capital expenses are a cost of traditional on-premises infrastructure that AWS replaces with variable operational expenditure, making them a disadvantage of the old model, not a benefit of the cloud.

## clf-c02/domain1/q640

Answer: C, D

Storage hardware and physical servers are on-premises capital expenses that must be purchased, maintained, and eventually replaced, making them key differentiators in a TCO comparison since they are eliminated when moving to AWS.
Software development costs remain consistent regardless of whether infrastructure is on-premises or in the cloud and are not a differentiating factor in a TCO analysis. Project management costs also apply equally across both environments and do not change based on infrastructure hosting decisions. Antivirus software licensing remains the customer's responsibility in both on-premises and cloud environments and is not eliminated by moving to AWS.

## clf-c02/domain1/q642

Answer: A, B

Scaling EC2 instances horizontally based on traffic and resizing RDS instances vertically as business needs change both demonstrate elasticity, which is the ability to adapt resource capacity dynamically to match demand.
Automatically directing traffic to less-utilized EC2 instances describes load balancing, which optimizes resource utilization but does not change the amount of resources provisioned. Using AWS compliance documents to accelerate the compliance process describes the concept of inherited compliance, not elasticity. Having the ability to create and govern environments using code describes infrastructure as code, which is a separate cloud principle unrelated to dynamic resource scaling.

## clf-c02/domain1/q644

Answer: B, C

Power consumption and labor costs for server replacement are significant on-premises expenses that disappear when migrating to AWS, making them the relevant factors in a TCO comparison.
Amazon EC2 instance availability is an AWS-side consideration, not an on-premises cost factor included in a TCO analysis. Application developer time remains consistent regardless of hosting environment and is not a differentiating infrastructure cost. Database engine capacity is a performance and sizing consideration, not an on-premises cost component that changes when moving to AWS.

## clf-c02/domain1/q651

Answer: C

The cloud deployment model fully replaces upfront capital expenditure on hardware and facilities with variable operational expenses based on actual usage, eliminating the need to own or maintain physical infrastructure.
An on-premises deployment requires the organization to purchase, own, and maintain all physical hardware and facilities, which preserves rather than eliminates capital expenditure and offers no conversion to operational expenses. A hybrid deployment combines on-premises infrastructure with cloud resources, meaning capital expenditure on owned hardware is retained alongside operational cloud costs rather than being fully traded for operational expenses. Platform as a service is a cloud service delivery model in which a provider manages a platform for building and running applications, and is not a deployment model describing where infrastructure is hosted.

## clf-c02/domain1/q662

Answer: B

Deploying RDS in Multi-AZ mode applies the design for failure principle by maintaining a synchronous standby replica in another Availability Zone, automatically failing over if the primary instance becomes unavailable.
Loose coupling refers to reducing interdependencies between application components so failures do not cascade, not to database redundancy across zones. Automate everything that can be automated refers to replacing manual operational tasks with scripted or managed processes to improve consistency. Use services, not servers refers to leveraging managed AWS services instead of provisioning and maintaining your own infrastructure.

## clf-c02/domain1/q666

Answer: C

Decoupling components means isolating them so each can function independently, communicating through asynchronous interfaces rather than direct calls, so a failure in one component does not bring down the entire application.
Implementing elasticity addresses scaling resources up and down in response to demand, but does not resolve the tight dependency problem that causes cascading failures. Enabling EC2 instances to run in parallel improves performance and throughput but does not isolate components from each other's failures. Doubling EC2 computing resources adds capacity but does not change the tightly coupled architecture, meaning a component failure would still take down the whole application.

## clf-c02/domain1/q671

Answer: B

The ability to recover from failure is a core design principle of the Reliability pillar, which focuses on ensuring workloads perform their intended function correctly and consistently, including through automatic recovery mechanisms.
Deployment to a single Availability Zone is actually an anti-pattern for reliability, as it creates a single point of failure rather than providing fault tolerance. Design for cost optimization describes the goal of the Cost Optimization pillar, not the Reliability pillar. Perform operations as code is a design principle of the Operational Excellence pillar, focused on automating operational tasks rather than on failure recovery.

## clf-c02/domain1/q672

Answer: A

AWS eliminates the need to guess future capacity needs by providing on-demand scaling, allowing organizations to provision exactly what they need and adjust in minutes rather than committing to fixed hardware infrastructure months or years in advance.
Utilizing existing hardware contracts for purchases is a characteristic of traditional on-premises procurement rather than an advantage of AWS; on the cloud, customers avoid hardware contracts entirely by paying only for what they consume. Fixing costs regardless of traffic is not an advantage of AWS; cloud costs scale with usage, and AWS offers variable pricing that adjusts to actual demand rather than fixed costs, which is one of its financial advantages over traditional fixed-capacity infrastructure. Avoiding audits using AWS reports is not a valid advantage; while AWS Artifact provides compliance reports that support customer audits, customers remain subject to their own regulatory audit requirements and cannot avoid audits by virtue of using AWS.

## clf-c02/domain1/q681

Answer: B

AWS offers a pay-as-you-go pricing model with no long-term contracts required for most services, allowing companies to avoid large upfront capital expenditure and pay only for the resources they actually consume.
AWS does not provide users with full control over the underlying physical resources; AWS manages the hardware, hypervisor, and physical infrastructure, while customers manage their workloads and data. AWS does not have edge locations in every country; AWS has edge locations in many countries for services like CloudFront, but coverage is not universal across every nation, and this is not a core reason to choose AWS over a traditional data center. While AWS has very high service limits, there are limits on the number of resources that can be created per account per Region; customers can request limit increases, but resources are not truly unlimited, making this statement inaccurate.

## clf-c02/domain1/q686

Answer: A

AWS provides on-demand resources that can be provisioned instantly for peak usage and released when not needed, so a growing startup only pays for the compute capacity it actually uses rather than purchasing hardware sized for maximum anticipated load.
Automating the provisioning of individual developer environments is a benefit of infrastructure as code tools such as AWS CloudFormation, but is a developer productivity feature rather than the primary mechanism by which AWS reduces computing costs for a growing startup. Automating customer relationship management describes CRM software functionality and is entirely unrelated to how AWS reduces computing infrastructure costs for companies. Implementing a fixed monthly computing budget is a financial governance practice that sets spending limits, but a fixed budget does not itself reduce computing costs and constrains flexibility rather than enabling cost-efficient scaling with demand.

## clf-c02/domain1/q687

Answer: D

Agility in the AWS Cloud means the ability to quickly provision resources, iterate on application requirements, and deploy changes rapidly, enabling startups to go to market fast and adapt as needs change.
Elasticity refers to dynamically scaling resources up or down in response to demand, which addresses capacity management rather than the speed of building and iterating on new applications. Reliability refers to a workload's ability to perform its intended function correctly and recover automatically from failures, which is an architectural quality rather than a characteristic that accelerates time to market. Performance refers to using computing resources efficiently to meet workload requirements, which is unrelated to the speed of provisioning and iterating on new application requirements.

## clf-c02/domain1/q691

Answer: A

Data center security costs such as physical access controls, surveillance, and guards are part of on-premises TCO that are eliminated when migrating to AWS, where physical security is included in the service.
Business analysis is a professional function that evaluates organizational needs and solutions, and is not a physical infrastructure cost included in an on-premises TCO comparison. Project management is a professional service cost associated with planning and executing initiatives, and is not a data center infrastructure expense factored into TCO. Operating system administration is a labour cost that customers retain responsibility for under the Shared Responsibility Model regardless of whether they are on-premises or on AWS, so it is not eliminated by migration and does not differentiate the two TCO models.

## clf-c02/domain1/q698

Answer: C

AWS eliminates the need to guess capacity needs by providing on-demand scaling, so organizations can provision exactly what they need and adjust in minutes rather than purchasing hardware based on peak capacity forecasts.
AWS does not audit user data; AWS has strict policies and controls against accessing customer data without authorisation, and the customer remains responsible for the privacy and governance of data stored in their AWS environment. Data stored in AWS is not automatically secure; customers must actively configure encryption, access controls, and security settings for their own data, as the shared responsibility model requires customers to protect the data they put in the cloud. AWS does not manage the compliance needs of individual customers; while AWS provides compliance certifications for its infrastructure and tools through Artifact to support customer compliance efforts, each customer is responsible for applying those frameworks to their own workloads and meeting their specific regulatory requirements.

## clf-c02/domain1/q701

Answer: A, B

Designing for automated failure recovery ensures systems self-heal without manual intervention, and deploying across multiple Availability Zones protects against AZ-level failures, both being core reliability principles.
Managing changes via documented processes is an Operational Excellence principle focused on controlled change management, not a reliability architecture principle. Testing for moderate demand does not reflect a recognized reliability principle, as the Well-Architected Framework recommends testing recovery procedures and scaling under peak and failure conditions rather than moderate load. Backing up recovery to an on-premises environment introduces a dependency on local infrastructure, which contradicts the cloud reliability principle of eliminating single points of failure and keeping recovery within the AWS environment.

## clf-c02/domain1/q703

Answer: B

High availability means an application remains accessible even when individual resources fail, achieved through redundancy across Availability Zones, auto-scaling, and automatic failover mechanisms.
Consulting AWS technical support at any time describes the 24/7 availability of support plans, which is a service offering rather than an architectural characteristic of the cloud. Making any AWS service available by paying on demand describes the pay-as-you-go pricing model, which is a billing concept unrelated to fault tolerance or uptime. Deploying in any part of the world using AWS Regions describes global reach, which is a separate cloud benefit and does not by itself ensure an application remains accessible if a resource fails.

## clf-c02/domain1/q721

Answer: C

Elasticity is the ability to automatically scale resources up or down to match changing workload demands, ensuring you have the right amount of capacity without over-provisioning or under-provisioning.
Security refers to protecting data, systems, and assets through controls and risk mitigation strategies, and is unrelated to matching resource supply with demand. Reliability refers to a workload's ability to perform its intended function correctly and recover automatically from failures, which is an architectural quality rather than a capacity management concept. High availability refers to keeping an application operational during failures through redundancy, which addresses uptime rather than the dynamic adjustment of resources to match workload demand.

## clf-c02/domain1/q723

Answer: A, C

AWS requires no upfront hardware commitments, allowing organizations to pay only for what they consume, and resources can be provisioned on demand in minutes allowing businesses to scale quickly without waiting for hardware procurement and installation.
AWS does not manage all security in the cloud; under the shared responsibility model, AWS secures the underlying infrastructure while customers are responsible for securing their applications, data, and configurations that run on top of that infrastructure. Users do not have access to free and unlimited storage on AWS; storage services such as S3 and EBS are priced based on usage, and while there are free tier limits for new accounts, storage is not free or unlimited in general. Users do not have control over the physical infrastructure; one of the trade-offs of moving to the cloud is that customers give up physical access to and control of the underlying hardware, trusting AWS to manage it securely and reliably.

## clf-c02/domain1/q728

Answer: A, C

Deploying across multiple AWS Regions places resources physically closer to international users, and CloudFront's global edge locations cache content near end users worldwide, both directly reducing latency for global customers.
Amazon Translate is a machine translation service for converting text between languages and does not automatically translate website interfaces without custom integration. Amazon Comprehend is a natural language processing service for analyzing and extracting meaning from text, not a tool for enabling multilingual application responses. Elastic Load Balancing distributes traffic across targets within a single Region and cannot route traffic between Regions to reduce geographic latency.

## clf-c02/domain1/q731

Answer: B

Provisioning web servers across multiple AWS Regions increases availability by ensuring that if one entire Region experiences an outage, users can be served from servers in another Region.
Coupling refers to the degree of dependency between application components, and is not affected by how many Regions servers are deployed in. Security is not increased simply by deploying across multiple Regions, as security depends on configuration and controls applied consistently regardless of geographic distribution. Durability refers to the long-term persistence of stored data without corruption or loss, which is a storage characteristic unrelated to where web servers are provisioned.

## clf-c02/domain1/q736

Answer: B, C

The AWS Well-Architected Framework has six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. Performance Efficiency and Security are both official pillars.
Multiple Availability Zones is an infrastructure concept and a deployment strategy, not a Well-Architected pillar. Encryption usage is a security practice that falls under the Security pillar, not a pillar in its own right. High availability is a design goal associated with the Reliability pillar, not a standalone pillar.

## clf-c02/domain1/q741

Answer: D

Infrastructure as code allows users to define and automate the provisioning of AWS resources using templates, enabling repeatable, version-controlled deployments without manual configuration.
Automating migration of on-premises hardware to AWS data centers is not possible through infrastructure as code, as physical hardware migration is a separate process managed outside of code-based provisioning. Letting a third party automate an audit of AWS infrastructure describes a compliance or security activity unrelated to infrastructure provisioning. Turning over application code to AWS to run on its infrastructure misrepresents how AWS works, as customers are always responsible for their own application code and deployment.

## clf-c02/domain1/q750

Answer: B, D

Moving to AWS immediately replaces large upfront capital expenses with variable pay-as-you-go expenses, and increases agility by enabling rapid provisioning of resources in minutes instead of weeks.
Moving to AWS typically reduces the need for undifferentiated infrastructure management work rather than increasing IT staff headcount. User control of infrastructure decreases when moving to AWS, as physical hardware management is handled entirely by AWS under the Shared Responsibility Model. AWS holds responsibility for security of the cloud, covering physical infrastructure and managed services, but security in the cloud remains the customer's responsibility, making this option factually incorrect.

## clf-c02/domain1/q752

Answer: C

Deploying to multiple AWS Regions places an application in geographically isolated locations around the world, each with independent infrastructure for maximum geographic separation.
Installing the application using multiple internet gateways is incorrect. Internet gateways connect a VPC to the internet and have no bearing on geographic isolation. Deploying the application to an Amazon VPC is incorrect. A VPC is a private network within a single Region and does not provide geographic isolation across locations. Configuring the application using multiple NAT gateways is incorrect. NAT gateways enable outbound internet access for private subnets and are unrelated to geographic distribution.

## clf-c02/domain1/q753

Answer: B

A system designed to withstand component failures is an example of high availability, which ensures an application remains accessible through redundancy and automatic failover mechanisms.
Elasticity refers to dynamically scaling resources up or down in response to demand, which addresses capacity management rather than fault tolerance. Scalability refers to the ability to handle increased load by adding resources, which is about growth capacity rather than continued operation during failures. Agility refers to the speed at which resources can be provisioned and iterated on, which is unrelated to a system's ability to withstand component failures.

## clf-c02/domain1/q761

Answer: C

Moving workloads to AWS eliminates the capital expenditure required to purchase, install, rack, and cable physical servers and networking equipment for new applications, replacing it with pay-as-you-go consumption pricing.
The cost of writing custom application code in languages such as Java or Node.js remains unchanged when moving to the cloud, as software development is a people and process cost that is independent of whether the infrastructure is on-premises or hosted on AWS. Penetration testing costs for security remain with the application team whether on-premises or in the cloud, as the need to test application and infrastructure security exists regardless of where the workload runs, and AWS provides guidance for testing its own components separately. Writing test cases for third-party applications is a development and quality assurance task that remains consistent regardless of infrastructure location, as it is determined by the third-party software requirements rather than by the hosting environment.

## clf-c02/domain1/q763

Answer: D

A hybrid cloud architecture means some resources run on-premises in existing data centers while other resources run in the AWS Cloud, connected through services such as AWS VPN or AWS Direct Connect.
Running all resources using on-premises infrastructure describes a fully on-premises deployment with no cloud involvement, which is the opposite of a cloud architecture. Running some resources on-premises and some in a colocation center describes a split between owned and rented physical data center space, but does not involve any cloud provider and therefore does not constitute a hybrid cloud architecture. Running all resources in the AWS Cloud describes a fully cloud-native deployment, which is a public cloud architecture rather than a hybrid one.

## clf-c02/domain1/q764

Answer: B, C

AWS eliminates the need to guess capacity requirements by providing on-demand scaling, and increases speed to market by enabling rapid provisioning of resources in minutes rather than weeks.
Fixed rate monthly cost is the opposite of how AWS pricing works. AWS uses a variable pay-as-you-go model, not fixed monthly billing. Increased upfront capital expenditure is also the opposite of an AWS advantage. One of the core benefits of cloud is replacing upfront capital expenditure with variable operational costs. Physical access to cloud data centers is not available to customers and is not an AWS advantage.

## clf-c02/domain1/q765

Answer: B, C

The cost of purchasing and installing physical server hardware on-premises, and the ongoing administrative cost of managing infrastructure including OS installations, patching, backups, and failure recovery, are both direct costs of maintaining on-premises infrastructure that disappear when migrating to AWS and should be included in a TCO comparison.
Credit card processing fees for application transactions are a business operational cost that exists regardless of whether the infrastructure is on-premises or in the cloud, as they are determined by the payment processor rather than the hosting environment and are therefore not relevant to a cloud versus on-premises TCO comparison. Third-party penetration testing costs may apply in both on-premises and cloud environments depending on the organization's security requirements, and are not a distinguishing cost factor that differentiates on-premises TCO from cloud architecture costs. Advertising costs for enterprise-wide campaigns are a marketing expense entirely unrelated to the infrastructure hosting model, and have no connection to the cost comparison between on-premises data center infrastructure and cloud architecture.

## clf-c02/domain1/q772

Answer: C

High availability is an AWS Cloud design best practice that ensures applications remain accessible through redundancy, multi-AZ deployments, and automatic failover mechanisms.
Tight coupling of components is an anti-pattern in cloud design, as it creates dependencies between services that cause cascading failures and contradicts the best practice of loose coupling. Single point of failure is an architectural weakness that cloud design best practices are specifically aimed at eliminating through redundancy and distributed deployments. Overprovisioning of resources is an on-premises habit that cloud adoption is intended to eliminate through pay-as-you-go pricing and elastic scaling rather than a best practice to follow.

## clf-c02/domain1/q773

Answer: C

EC2 instances can be launched on demand when needed and terminated when no longer required, so you only pay for compute during actual usage rather than maintaining hardware sized for peak capacity at all times.
Amazon EC2 costs are not billed on a monthly basis. Linux-based EC2 instances are billed per second with a one-minute minimum, meaning you pay only for the exact compute time consumed rather than a fixed monthly charge. Customers retaining full administrative access to their EC2 instances is a capability that gives customers control over their environment, but administrative access is not itself a reason why AWS is more economical than traditional data centers. Permanently running enough instances to handle peak workloads describes the traditional data center approach of over-provisioning for maximum anticipated load, which is exactly the model that makes traditional infrastructure less economical than the elastic, on-demand AWS model.

## clf-c02/domain1/q783

Answer: B

Moving to AWS replaces large upfront capital investments in hardware and facilities with lower, variable pay-as-you-go costs based on actual resource consumption.
Replacing large variable costs with lower capital investments describes the opposite of the AWS model. Traditional data centers often have both large upfront capital costs and ongoing variable operational costs, while AWS eliminates the capital component and replaces it with variable usage-based charges. Allowing the provisioning of compute and storage at a fixed level to meet peak demand describes the traditional on-premises approach of purchasing maximum anticipated capacity upfront, which is a model AWS specifically moves customers away from. Replacing the repeated scaling of virtual servers with a simpler fixed-scale model describes a static capacity model that is the opposite of the AWS approach, which enables dynamic scaling rather than replacing it with a fixed scale.

## clf-c02/domain1/q785

Answer: D

Distributing compute load across multiple resources follows the horizontal scaling best practice, improving fault tolerance and performance by avoiding single points of failure.
Creating fixed dependencies among application components violates the loose coupling principle, which aims to reduce interdependencies so failures do not cascade across the system. Aggregating services on a single instance creates a single point of failure and contradicts the best practice of distributing workloads across multiple resources. Deploying in a single Availability Zone exposes the application to an outage if that AZ fails, which contradicts the best practice of designing for high availability.

## clf-c02/domain1/q789

Answer: A

An application spanning multiple Availability Zones remains operational if one AZ experiences an outage, which is the definition of high availability.
Global reach describes deploying across multiple Regions or using a content delivery network to serve users worldwide, which goes beyond AZ-level redundancy within a single Region. Economy of scale refers to the cost benefits AWS passes to customers through aggregated purchasing power, which is a pricing concept unrelated to application architecture. Elasticity refers to dynamically scaling resources up or down in response to demand, which is independent of how many Availability Zones an application spans.

## clf-c02/domain1/q790

Answer: B

Availability Zones are isolated data center locations within a single AWS Region connected by low-latency links. Deploying EC2 instances across at least two AZs in the same Region provides high availability and meets the geographic restriction requirement.
AWS Regions are separate geographic areas, each containing multiple AZs. Deploying across multiple Regions would violate the requirement that all instances remain in a single geographic area, making this option non-compliant. Subnets are subdivisions of a VPC and can exist within a single AZ; spreading instances across subnets within the same AZ does not provide protection against an AZ-level failure. Placement groups control how instances are physically placed within an AZ for low latency or spread placement, but they do not provide cross-AZ fault isolation and are not a high-availability mechanism for surviving AZ outages.

## clf-c02/domain1/q802

Answer: A, C

AWS manages the maintenance of cloud infrastructure including hardware, networking, and facilities, and manages capacity planning for physical servers, freeing customers from these operational burdens and allowing them to focus on their applications and business objectives.
AWS does not manage the security of applications built on AWS, as application-level security including code vulnerabilities, access controls, and data protection remain the customer's responsibility under the Shared Responsibility Model. AWS does not manage the development of applications on AWS, as customers are solely responsible for designing, building, and maintaining their own applications regardless of which AWS services they run on. AWS does not manage cost planning for virtual servers, as customers are responsible for selecting the right instance types, monitoring usage, and optimizing their own spending through tools like Cost Explorer and AWS Budgets.

## clf-c02/domain1/q803

Answer: B

Deploying across multiple Availability Zones ensures the database can withstand an AZ failure and recover automatically, which directly maps to the Reliability pillar's focus on workload recovery and availability.
Performance Efficiency focuses on using compute resources efficiently to meet performance requirements, not on redundancy across failure domains. Cost Optimization focuses on eliminating unnecessary spend and choosing the right resource types, not on fault tolerance. Security focuses on protecting data and systems through access controls and detective mechanisms, not on availability architecture.

## clf-c02/domain1/q816

Answer: C

Agility in the AWS Cloud enables companies to quickly provision resources, iterate on features, and deploy changes rapidly, minimizing time to market for new functionality.
Elasticity refers to dynamically scaling resources up or down in response to demand, which addresses capacity management rather than the speed of delivering new features. High availability refers to keeping an application operational during failures through redundancy, which is an uptime characteristic unrelated to development and deployment speed. Reliability refers to a workload's ability to perform its intended function correctly and recover from failures, which is an architectural quality rather than a feature that accelerates time to market.

## clf-c02/domain1/q827

Answer: A, C

Using AWS Config to generate an inventory of AWS resources provides visibility into what resources exist and how they are configured, supporting reliability by enabling change tracking, and using AWS CloudTrail to record AWS API calls creates an auditable log of all changes made, enabling root cause analysis when failures occur. Both are change management steps that support reliability in the AWS Cloud.
Using service limits to prevent users from creating or making changes to AWS resources would block necessary scaling and operational changes, contradicting the reliability goal of being able to adapt to changing demand and recover from failures quickly. Using AWS Certificate Manager to whitelist approved resources and services is not an accurate description of what Certificate Manager does; it provisions SSL/TLS certificates and does not provide a resource whitelisting capability for change management. Using Amazon GuardDuty to validate configuration changes is not what GuardDuty does; it detects threats and malicious activity rather than validating whether resource configurations comply with desired states, which is the function of AWS Config.

## clf-c02/domain1/q829

Answer: C

Designing loosely coupled components means systems are built so that individual components can fail or be replaced without causing cascading failures, which is a core AWS Well-Architected design principle for building resilient, maintainable cloud architectures.
Thinking of servers as non-disposable resources is the opposite of an AWS design principle; the cloud encourages treating infrastructure as disposable and automating replacements, allowing failed instances to be terminated and new ones launched automatically rather than being manually repaired. Using synchronous integration of services increases tight coupling and means a failure in one service blocks others waiting for a response; AWS design principles favor asynchronous and event-driven patterns where components can operate independently without waiting for each other. Implementing the least permissive rules for security groups is a security best practice for network access control but is not a cloud architecture design principle; it relates to security hardening rather than the broader system architecture pattern described by the Well-Architected Framework.

## clf-c02/domain1/q831

Answer: C

Distributing the workload across multiple EC2 instances and running in parallel applies horizontal scaling, which handles consistently growing demand by adding more machines rather than relying on a single larger instance that will eventually hit capacity limits.
Running the application on a bigger EC2 instance applies vertical scaling, which has an upper size limit and creates a single point of failure, making it unsuitable for consistently doubling workloads over time. Switching to a different EC2 instance family optimizes for workload characteristics such as compute or memory intensity, but does not address the problem of consistently growing processing volume. Running on a bare metal EC2 instance provides direct access to physical hardware without a hypervisor layer, which can improve performance for certain workloads but does not scale to handle doubling data volumes.

## clf-c02/domain1/q833

Answer: B

Horizontally scaling EC2 instances based on demand is elasticity, the ability to automatically add or remove compute resources to match workload requirements in real time.
Economy of scale refers to the cost reductions AWS passes to customers through aggregated purchasing power across millions of users, which is a pricing benefit rather than a capacity management concept. High availability refers to keeping an application operational during failures through redundancy across multiple locations, which is unrelated to dynamically adjusting the number of instances. Agility refers to the speed at which customers can provision resources and iterate on new functionality, which addresses time to market rather than dynamic capacity adjustment.

## clf-c02/domain1/q840

Answer: B

Loose coupling reduces interdependencies between components so that a change or failure in one does not cascade to others, improving system resilience through independent, isolated components.
Scalability refers to the ability to handle increases in load by adding resources, not to reducing component interdependencies. Automation refers to reducing manual intervention through scripted or managed processes, not to architectural independence between components. Automatic scaling refers to dynamically adjusting resource capacity in response to demand, not to isolating components from each other.

## clf-c02/domain1/q844

Answer: D

Elasticity automatically adjusts compute capacity in response to changing demand, scaling out during traffic peaks and scaling in during quiet periods to maintain consistent performance without manual intervention.
Spreading web traffic across multiple Regions describes global load balancing or DNS routing, which is a separate capability unrelated to dynamically adjusting compute capacity. Automatically archiving log data to minimize storage costs describes a data lifecycle management function, not a characteristic of elasticity. Automatically selecting the most cost-effective services is not a feature AWS provides on behalf of customers, as service selection remains the customer's responsibility.

## clf-c02/domain1/q845

Answer: C

As AWS grows and serves more customers, it achieves lower per-unit costs through economies of scale and passes those savings on to customers through regular price reductions.
Pay-as-you-go pricing is a billing model that charges for actual usage rather than upfront commitments, but it does not cause prices to decrease over time. The AWS global infrastructure describes the physical footprint of Regions, AZs, and edge locations, which supports service delivery but is not the mechanism behind continual price reductions. Reserved storage pricing is a commitment-based discount option for specific services, not a driver of overall AWS pricing reductions across the platform.

## clf-c02/domain1/q853

Answer: B

Dynamically and predictively scaling to meet usage demands leverages both elasticity through automatic scaling and agility through rapid adaptation, which are core cloud computing advantages.
Provisioning capacity based on past usage and theoretical peaks is an on-premises approach that leads to over-provisioning and idle resources, which cloud adoption is specifically designed to eliminate. Building applications in a data center that grants physical access describes an on-premises or colocation model and contradicts the cloud principle of abstracting away physical infrastructure management. Breaking apart an application into loosely coupled components is a good architectural practice that improves resilience and maintainability, but it describes the loose coupling design principle rather than the use of elasticity and agility.

## clf-c02/domain1/q854

Answer: A

The pay-as-you-go model optimizes costs by ensuring you only pay for the resources you actually consume, eliminating waste from over-provisioning or purchasing hardware in advance of actual need.
Purchasing hardware before it is needed describes the traditional capital expenditure model of procuring infrastructure ahead of demand, which leads to over-provisioning and wasted spend rather than optimizing costs. Manually provisioning cloud resources introduces human effort and potential delays in responding to demand changes, and does not optimize costs compared to automated scaling that matches capacity precisely to actual usage. Purchasing for the maximum possible load means over-provisioning infrastructure to handle the worst-case demand scenario, which maximizes costs by paying for capacity that sits idle during normal usage periods rather than scaling with actual demand.

## clf-c02/domain1/q861

Answer: B

Assuming that all components can fail is a core principle of high availability design, as it drives architects to build redundancy, health checks, and automatic failover into every layer of an application rather than relying on any single component remaining available.
Designing using a serverless architecture is a valid approach for some workloads but is not a universal principle for high availability, as server-based architectures can also achieve high availability through redundancy and failover. Designing Auto Scaling into every application is a good practice for scalability but is not a universal requirement for high availability, as some applications achieve availability through redundancy rather than scaling. Using open-source code is a software development choice that has no bearing on whether an application is designed to remain available when components fail.

## clf-c02/domain1/q867

Answer: B

AWS Regions are geographically separate areas around the world, making them the correct choice for replicating data across different physical locations to satisfy disaster recovery requirements.
AWS Accounts are a logical boundary for managing resources and billing, not a geographic infrastructure component. Availability Zones are isolated data center clusters within a single Region, so replicating between AZs does not achieve geographic separation across different areas of the world. Edge locations are points of presence used for content delivery and caching, not designed for data replication or disaster recovery purposes.

## clf-c02/domain1/q875

Answer: D

Deploying across multiple Availability Zones in two AWS Regions provides protection against both AZ-level and Region-level failures, achieving the highest level of redundancy and fault tolerance available.
Deploying in a single Availability Zone in one Region creates a single point of failure at both the AZ and Region level, providing no redundancy against outages. Using multiple Elastic Network Interfaces in different subnets improves network configuration flexibility within an instance but does not provide redundancy against compute or infrastructure failures. Deploying across multiple AZs in a single Region protects against AZ-level failures but leaves the application vulnerable to a full Regional outage, which does not meet the requirement for the highest redundancy.

## clf-c02/domain1/q886

Answer: A

An Availability Zone consists of one or more physical data centers, each with independent power, cooling, and networking, designed so that a failure in one AZ does not affect others in the same Region.
A completely isolated geographic location describes an AWS Region, not an Availability Zone; Regions are the large geographic areas, and AZs are the isolated facilities within a Region. Edge locations are Points of Presence used by services such as CloudFront to cache content close to users; they are not Availability Zones and have no hosting relationship with EC2 instances or core AWS services. A description of a single source of power and networking is the opposite of what an AZ provides; AZs are specifically designed with redundant power and networking to protect against single points of failure.

## clf-c02/domain1/q897

Answer: C

A hybrid cloud architecture distributes workloads between on-premises servers and the AWS Cloud, combining existing data center infrastructure with cloud resources connected via VPN or Direct Connect.
A virtual private network is a connectivity technology that creates encrypted tunnels between networks, and is not itself an architecture type describing how workloads are distributed between cloud and on-premises environments. A virtual private cloud is a logically isolated network environment within AWS, and describes a networking construct rather than a deployment model that spans both cloud and on-premises infrastructure. A private cloud is a deployment model where all infrastructure is dedicated to a single organization and hosted either on-premises or by a third party, with no shared public cloud component.

## clf-c02/domain1/q913

Answer: D

Fault tolerance refers to the built-in redundancy of an application's components, ensuring the system continues operating correctly even when individual components fail.
The ability to accommodate growth without changing design describes scalability, which is a separate cloud concept focused on handling increased demand. How well and how quickly lost data can be restored describes recoverability, which relates to backup and disaster recovery rather than continued operation during failures. How secure an application is describes the security posture of a system, which is an entirely separate concern from redundancy and fault tolerance.

## clf-c02/domain1/q927

Answer: D

Loose coupling is the principle that systems should reduce interdependencies between components, so that changes or failures in one do not cascade to others.
Scalability refers to the ability to handle increases in load by adding resources, not to reducing interdependencies. Services, not servers is the principle of using managed AWS services instead of running your own infrastructure. Removing single points of failure is a reliability principle focused on redundancy, not on reducing component interdependencies.

## clf-c02/domain1/q935

Answer: A

Elasticity refers to the ability to automatically scale resources both up and down to match variable demand, ensuring capacity adjusts in both directions without manual intervention.
Agility refers to the speed at which customers can provision resources and iterate on new functionality, which addresses time to market rather than dynamic capacity adjustment. Security refers to protecting data, systems, and assets through controls and risk mitigation strategies, and is unrelated to scaling resources in response to demand. Scalability refers to a system's ability to handle increased load by growing capacity, but unlike elasticity it does not inherently include automatic scaling back down when demand decreases.

## clf-c02/domain1/q937

Answer: B

Running across two AZs in one Region provides high availability within the Region, and using a separate Region as the disaster recovery site protects against a full regional service interruption through geographic redundancy.
Using additional AZs within the same Region as the disaster recovery site does not protect against a regional interruption, as all AZs in a Region would be affected by the same regional outage. A local AWS Region refers to a limited-scope Region designed for data residency requirements and typically does not offer the full service availability needed to serve as a complete disaster recovery site. Running across two Regions with a third as the disaster recovery site introduces unnecessary complexity and cost, as two Regions already provide the geographic separation needed for high availability and regional failover.

## clf-c02/domain1/q947

Answer: B

Performing operations as code is an explicit design principle of the Operational Excellence pillar, which focuses on running and improving operations by automating processes and responding to events programmatically.
Performance Efficiency focuses on using compute resources efficiently to meet system requirements, not on automating operational processes. Reliability focuses on ensuring a workload performs its intended function correctly and consistently, with design principles around recovery and redundancy. Security focuses on protecting data, systems, and assets through controls and detective mechanisms.

## clf-c02/domain1/q948

Answer: C

Testing recovery procedures is a core design principle of the Reliability pillar, ensuring workloads can recover from failures by regularly validating disaster recovery and backup processes.
Vertical scaling is a performance and capacity concept associated with the Performance Efficiency pillar, not a design principle of the Reliability pillar. Manual failure recovery contradicts the Reliability pillar's principle of automating failure recovery, as manual processes introduce delays and human error during outages. Changing infrastructure manually contradicts the Reliability pillar's principle of managing change through automation to reduce the risk of introducing failures.

## clf-c02/domain1/q955

Answer: B

Elasticity allows you to scale resources up or down based on actual demand, directly addressing underutilization by ensuring you only pay for what you use instead of maintaining idle capacity.
High availability ensures an application remains operational during failures through redundancy, but does not address the problem of over-provisioned or underutilized resources. Security refers to protecting data, systems, and assets through controls and risk mitigation, which is unrelated to resource utilization. Loose coupling is an architectural principle that reduces dependencies between components to limit the blast radius of failures, and does not address idle or underutilized capacity.

## clf-c02/domain1/q981

Answer: A, D

Deploying across multiple Availability Zones eliminates single points of failure by ensuring the application continues running if one AZ goes down, directly increasing overall availability.
Reducing operational costs is not a direct benefit of multi-AZ deployment and can in fact increase costs slightly due to running resources across more locations. Serving cross-region users with low latency requires deploying across multiple Regions or using a content delivery network, not spreading instances across AZs within a single Region. Increasing the load of the application describes adding more demand, which is not a benefit of any architectural pattern.

## clf-c02/domain1/q995

Answer: C, E

Testing recovery procedures validates that disaster recovery plans work correctly, and automatically recovering from failure using health checks and auto-scaling ensures systems self-heal without manual intervention, both being core Reliability pillar design principles.
Monolithic architecture tightly couples all application components together, meaning a failure in one part can bring down the entire system, which reduces rather than increases reliability. Measuring overall efficiency is a design principle associated with the Performance Efficiency pillar, not the Reliability pillar. Adopting a consumption model is a cost management principle associated with the Cost Optimization pillar, focused on paying only for what is used rather than on system resilience.

## clf-c02/domain1/q1007

Answer: D

Economies of scale allow AWS to lower variable costs for customers by aggregating demand across millions of users, giving AWS far greater purchasing power than any individual organization could achieve on its own.
Pay-as-you-go pricing is a billing model that charges customers only for what they consume, which is a separate cloud benefit unrelated to purchase volume driving down costs. High availability refers to designing systems to remain operational during failures, which is an architectural benefit rather than a cost benefit derived from purchasing power. Global reach refers to the ability to deploy infrastructure in multiple geographic locations worldwide, which is an infrastructure benefit rather than an economic one.

## clf-c02/domain1/q1034

Answer: B

The Reliability pillar focuses on the ability of a workload to perform its intended function correctly and consistently, including the ability to recover from failures and meet availability requirements over time.
Security focuses on protecting data, systems, and assets through access controls, encryption, and detective mechanisms. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes. Operational Excellence focuses on running and monitoring systems to deliver business value and continuously improving processes and procedures.

## clf-c02/domain1/q1035

Answer: A

The Operational Excellence pillar covers the ability to run workloads effectively, gain insight into operations through monitoring and observation, and continuously improve supporting processes and procedures.
Reliability focuses on ensuring a workload performs its intended function correctly and recovers automatically from failures, not on operational processes and continuous improvement. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes over time. Cost Optimization focuses on eliminating unnecessary expenditure and selecting the right resource types to reduce overall spending.

## clf-c02/domain1/q1036

Answer: C

The Performance Efficiency pillar focuses on using computing resources efficiently to meet workload requirements, including selecting the right resource types and sizes and maintaining efficiency as demand changes over time.
Reliability focuses on ensuring a workload performs its intended function correctly and recovers from failures, not on resource selection. Cost Optimization focuses on eliminating unnecessary spend and reducing overall costs, which overlaps with right-sizing but is not the pillar that specifically defines it as a design principle. Sustainability focuses on reducing the environmental impact of cloud workloads by minimizing energy consumption and maximizing resource utilization.

## clf-c02/domain1/q1037

Answer: D

The Sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads, including understanding usage impacts, maximizing utilization, and adopting managed services to reduce the resources required.
Cost Optimization focuses on eliminating unnecessary spending and achieving financial efficiency, not on reducing environmental impact. Operational Excellence focuses on running workloads effectively, monitoring operations, and continuously improving processes and procedures. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes, which addresses technical resource use rather than environmental outcomes.

## clf-c02/domain1/q1038

Answer: C

The Security pillar focuses on protecting data, systems, and assets through risk assessments, mitigation strategies, and controls covering confidentiality, integrity, and identity management.
Operational Excellence focuses on running workloads effectively, monitoring operations, and continuously improving processes and procedures. Reliability focuses on ensuring a workload performs its intended function correctly and recovers automatically from failures. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes over time.

## clf-c02/domain1/q1039

Answer: A

The Cost Optimization pillar focuses on avoiding unnecessary costs, selecting the most appropriate resource types, and scaling without overspending.
Sustainability focuses on reducing environmental impact of cloud workloads, such as minimizing energy consumption. Operational Excellence focuses on running and monitoring systems to deliver business value and improving processes. Performance Efficiency focuses on using compute resources efficiently to meet performance requirements.

## clf-c02/domain1/q1060

Answer: A, C

The AWS CAF organizes guidance into six perspectives: Business, People, Governance, Platform, Security, and Operations. Governance focuses on orchestrating cloud initiatives while maximizing organizational benefits and minimizing transformation-related risks, and People focuses on developing an organization-wide change management strategy and building cloud skills across the workforce.
Financial is not one of the six AWS CAF perspectives; financial and cost-related guidance falls within the Business perspective, which addresses how cloud adoption drives business value and return on investment rather than existing as its own separate financial perspective. Infrastructure is not one of the six AWS CAF perspectives; guidance on building and provisioning the technology foundation for cloud workloads falls under the Platform perspective rather than a perspective named Infrastructure. Agility is a benefit and characteristic of cloud computing but is not one of the six CAF perspectives; it does not appear in the CAF framework structure alongside Business, People, Governance, Platform, Security, and Operations.

## clf-c02/domain1/q1061

Answer: A, C

The AWS CAF identifies four key benefits of cloud adoption: reduced business risk through improved reliability, increased performance, and enhanced security posture; improved ESG performance through reduced carbon footprint and greater energy efficiency enabled by cloud infrastructure; increased revenue through the ability to develop and deliver new products faster; and increased operational efficiency through optimized cost structures and workforce productivity.
Elimination of all operational expenditure is not an AWS CAF benefit; moving to the cloud converts large upfront capital expenditure to variable operational expenditure rather than eliminating ongoing costs, as customers continue to pay for cloud services based on actual consumption and operational costs such as staffing and tooling remain. Immediate compliance with all regulatory requirements is not a benefit the CAF promises; while AWS provides compliance certifications and tools to support customers' compliance programs, each customer is still responsible for applying the appropriate controls to their own workloads and meeting their specific regulatory obligations. Guaranteed elimination of all security vulnerabilities is not a CAF-defined benefit; while cloud adoption can improve the security posture of an organization through shared responsibility and access to advanced security services, the CAF does not promise that cloud migration eliminates all security risk.

## clf-c02/domain1/q1062

Answer: C

Warm standby is a disaster recovery strategy where a scaled-down but fully operational version of the application environment runs continuously in a secondary Region, allowing the company to fail over quickly by scaling the standby environment up to full production capacity when a disaster occurs, providing a balance between recovery speed and ongoing cost.
Backup and restore involves storing regular data backups and restoring them to a newly provisioned environment after a disaster, resulting in the longest recovery time of all DR strategies as infrastructure must be built from scratch during recovery rather than already being available. Pilot light keeps only the minimal core components of the environment running in the secondary Region, such as a replicated database, with other infrastructure shut down and requiring provisioning during failover, resulting in faster recovery than backup and restore but slower than warm standby since more infrastructure must be brought online. Multi-site active-active runs full production copies of the environment across multiple sites simultaneously, providing the fastest possible failover with essentially zero downtime, but at the highest ongoing cost since all sites must maintain full production capacity at all times.

## clf-c02/domain1/q1063

Answer: D

Backup and restore has the longest recovery time objective of all disaster recovery strategies because after a failure the entire infrastructure must be provisioned from scratch and data must be restored from backups before the application can resume serving traffic, but it has the lowest ongoing cost because no secondary infrastructure is running during normal operations.
Multi-site active-active runs full production capacity at multiple sites simultaneously, providing the fastest failover with essentially zero downtime, but requires the highest ongoing investment as full infrastructure costs are incurred at every site continuously. Warm standby maintains a scaled-down but functional version of the environment running continuously, resulting in faster recovery than backup and restore but at a higher ongoing cost since resources are always running in the secondary location. Pilot light keeps only critical core components such as a replicated database running continuously with other infrastructure shut down, resulting in faster recovery than backup and restore but slower than warm standby, at an ongoing cost between the two.

## clf-c02/domain1/q1064

Answer: C

Rehosting, commonly referred to as lift-and-shift, involves moving an application to the cloud without making any changes to the application code or architecture, making it the fastest migration approach that allows organizations to realize cloud benefits quickly with minimal upfront migration effort.
Replatforming involves making targeted optimizations during migration, such as moving from a self-managed database to a managed service, to gain cloud benefits while leaving the core application architecture unchanged; this requires some changes and therefore more effort than a pure rehost. Refactoring involves re-architecting the application to fully leverage cloud-native capabilities such as microservices and serverless computing, providing the greatest long-term benefits but requiring the most time and development investment of any migration strategy. Repurchasing involves replacing the existing application entirely with a different product, typically a SaaS solution, which requires learning a new platform and migrating data rather than simply moving the existing application to new infrastructure.

## clf-c02/domain1/q1065

Answer: C

Replatforming, also known as lift-tinker-and-shift, involves making targeted optimizations during migration to take advantage of cloud-managed capabilities, such as moving from a self-managed database to Amazon RDS to gain automated backups, patching, and scaling, without re-architecting the core application or changing its code.
Rehosting moves an application to the cloud with no changes to architecture or code, making it a pure lift-and-shift; switching from a self-managed database to Amazon RDS represents a change to managed infrastructure and therefore goes beyond a simple rehost. Repurchasing replaces an existing application with a fundamentally different product, such as moving to a third-party SaaS database; moving to Amazon RDS uses the same MySQL engine in managed form rather than replacing the application with a different product from a different vendor. Refactoring involves re-architecting the application to use cloud-native services and patterns such as serverless functions or microservices, which represents a far more significant change to the application design than simply migrating the database to a managed service.

## clf-c02/domain1/q1066

Answer: C

Retiring involves decommissioning applications that are no longer needed or that provide no business value, which reduces the scope and cost of migration by eliminating unnecessary workloads rather than spending effort and money moving them to the cloud where they would continue to consume resources.
Retaining involves keeping certain applications running in their current on-premises environment, typically because they are not yet ready to migrate due to technical or compliance constraints, but this strategy still incurs ongoing maintenance costs rather than eliminating the burden of applications with no business purpose. Rehosting moves applications to the cloud with no changes, which would still consume cloud resources and generate ongoing costs for applications that have no business value; decommissioning is the correct choice when there is no reason to preserve the application at all. Replatforming involves optimizing applications during migration by moving to managed services, which requires migration effort and ongoing cloud resource costs that would be wasted entirely on applications that serve no business purpose.

## clf-c02/domain1/q1092

Answer: B

The AWS Cloud Adoption Framework organizes guidance into six perspectives, Business, People, Governance, Platform, Security, and Operations, to help organizations identify skill gaps, process improvements, and technical requirements for successful cloud transformation.
The AWS Well-Architected Framework provides best practices for designing and operating workloads in the cloud across six pillars, but it is focused on workload architecture rather than organizational cloud adoption planning. The AWS Migration Acceleration Program is a consulting and technology engagement program that helps customers accelerate their migration to AWS, but it is not a framework of perspectives for cloud transformation planning. The AWS Shared Responsibility Model defines the division of security responsibilities between AWS and the customer, and is a security governance concept rather than a cloud adoption planning framework.

## clf-c02/domain1/q1093

Answer: B

The People perspective of the AWS CAF focuses on evaluating organizational structures, roles, and skills to ensure the workforce is ready for cloud adoption, including training, change management, and career development.
The Business perspective focuses on ensuring that cloud investments are aligned with business outcomes and that stakeholders can articulate the business case for cloud adoption, rather than workforce readiness. The Operations perspective focuses on defining how day-to-day cloud operations will be managed, monitored, and improved, rather than workforce skills assessment. The Platform perspective focuses on building a scalable cloud platform architecture including networking, compute, and storage design, rather than people and organizational readiness.

## clf-c02/domain1/q1094

Answer: B, D

The AWS CAF groups its six perspectives into two categories: business capabilities (Business, People, Governance) and technical capabilities (Platform, Security, Operations). Platform and Operations both fall under technical capabilities.
Business is a business capability perspective focused on aligning cloud investments with business outcomes, not a technical capability. People is a business capability perspective focused on organizational readiness, culture, and workforce skills. Governance is a business capability perspective focused on orchestrating cloud initiatives, maximizing benefits, and minimizing transformation risks.

## clf-c02/domain1/q1095

Answer: C

The Governance perspective of the AWS CAF focuses on orchestrating cloud initiatives while maximizing organizational benefits and minimizing transformation-related risks, including aligning cloud strategy with regulatory and compliance requirements.
The Security perspective focuses on achieving the confidentiality, integrity, and availability of data and cloud workloads through security controls, rather than broader transformation risk management and regulatory alignment. The Business perspective focuses on ensuring cloud investments deliver measurable business outcomes, rather than risk management and regulatory compliance. The Operations perspective focuses on ensuring cloud services are delivered at a level that meets the needs of the business on a day-to-day basis, rather than strategic risk and compliance alignment.

## clf-c02/domain1/q1096

Answer: D

The Security perspective of the AWS CAF focuses on achieving the confidentiality, integrity, and availability of data and cloud workloads, including identity management, threat detection, infrastructure protection, and incident response.
The Governance perspective focuses on orchestrating cloud initiatives, aligning cloud strategy with business goals, and managing transformation risks, rather than the technical security posture of workloads. The Operations perspective focuses on delivering cloud services to meet business needs through monitoring, incident management, and continuous improvement of operational processes. The Platform perspective focuses on designing and building a scalable, enterprise-grade cloud environment including infrastructure, networking, and provisioning, rather than data protection and security controls.

## clf-c02/domain1/q1117

Answer: B

The Business perspective of the AWS CAF helps stakeholders understand how cloud adoption can accelerate business outcomes, articulate a compelling business case, and ensure that cloud investments are tied to measurable business value.
The People perspective focuses on organizational readiness, skills development, and change management rather than building a financial or strategic business case for migration. The Platform perspective focuses on designing the cloud infrastructure architecture including compute, networking, and storage, which is a technical concern rather than a business justification activity. The Governance perspective focuses on managing risks and aligning cloud initiatives with compliance requirements, which supports the business case but is not the perspective directly responsible for articulating it.

## clf-c02/domain1/q1118

Answer: C

The Platform perspective focuses on building an enterprise-grade, scalable cloud platform by designing the target architecture for networking, compute, storage, and database services, and establishing patterns for provisioning and managing cloud resources.
The Operations perspective focuses on delivering and managing cloud services to meet day-to-day business needs through monitoring, incident management, and process improvement, not on designing the underlying platform architecture. The Security perspective focuses on protecting data and workloads through identity management, threat detection, and security controls, rather than designing the cloud infrastructure platform. The People perspective focuses on workforce readiness, organizational change, and skills development, which is unrelated to technical platform architecture.

## clf-c02/domain1/q1119

Answer: C

The Operations perspective of the AWS CAF focuses on ensuring that cloud services are delivered and managed to meet ongoing business needs, covering areas such as monitoring, incident management, event management, and continuous improvement of operational processes.
The Platform perspective focuses on designing and building the cloud environment architecture, which is a one-time design activity rather than ongoing day-to-day management. The Governance perspective focuses on strategic alignment, risk management, and compliance, which are higher-level concerns than daily operational monitoring and incident management. The Business perspective focuses on aligning cloud investments with business outcomes and measuring return on investment, rather than operational management of workloads.

## clf-c02/domain1/q1120

Answer: C

The AWS CAF defines six perspectives: Business, People, and Governance (business capabilities), and Platform, Security, and Operations (technical capabilities), providing comprehensive guidance for cloud transformation.
Four perspectives would be incomplete, as the CAF explicitly defines six distinct areas of focus to cover both business and technical dimensions of cloud adoption. Five perspectives would be missing one of the six defined areas, and does not match the actual CAF structure. Seven perspectives exceeds the actual number defined by the framework, which groups its guidance into exactly six perspectives.

## clf-c02/domain1/q1121

Answer: A, E

The AWS CAF categorizes Business, People, and Governance as business capability perspectives, which focus on strategic alignment, organizational readiness, workforce skills, risk governance, and ensuring cloud investments deliver business value; of the options listed, Business and Governance are the two business capability perspectives.
Platform is a technical capability perspective that focuses on designing and building the cloud environment architecture, not on business alignment or organizational readiness. Operations is a technical capability perspective that focuses on running, monitoring, and optimizing cloud workloads day to day, not on business-level planning or governance. Security is a technical capability perspective that focuses on protecting data confidentiality, integrity, and availability through technical security controls, not on business value or governance.

## clf-c02/domain1/q1122

Answer: B

The People perspective of the AWS CAF recommends investing in training, upskilling, and organizational change management to close skill gaps and prepare the workforce for cloud adoption, ensuring sustainable internal capability rather than dependency on external resources.
Delaying migration indefinitely until all staff are fully trained is impractical and unnecessary, as the CAF recommends iterative learning alongside migration rather than waiting for complete readiness. Outsourcing all operations permanently does not build internal capability and creates long-term dependency, which contradicts the People perspective's goal of developing organizational cloud skills. Proceeding without training risks operational failures, security incidents, and inefficient resource usage, and ignores the People perspective's emphasis on workforce readiness.

## clf-c02/domain1/q1123

Answer: B

The Governance perspective focuses on orchestrating cloud initiatives to maximize organizational benefits while minimizing transformation risks, including budget management, portfolio management, compliance alignment, and risk mitigation strategies.
Designing the target cloud architecture is a focus of the Platform perspective, which handles infrastructure, networking, and compute design decisions. Monitoring application performance after deployment is a focus of the Operations perspective, which manages day-to-day service delivery, observability, and incident management. Configuring identity and access management controls is a focus of the Security perspective, which handles identity management, permissions, and threat detection.

## clf-c02/domain1/q1124

Answer: A

The AWS CAF identifies four transformation domains: Technology, Process, Organization, and Product. The Technology domain covers migration and modernisation of infrastructure, applications, and data platforms to leverage cloud capabilities.
Networking is a component within the Platform perspective and Technology transformation domain, but it is not itself one of the four transformation domains defined by the CAF. Database is a specific service category within cloud technology, not one of the four transformation domains that the CAF uses to structure cloud adoption activities. Compute is a specific resource type within cloud infrastructure, not one of the four high-level transformation domains defined by the CAF.

## clf-c02/domain1/q1125

Answer: A, C

The AWS CAF defines four transformation domains: Technology, Process, Organization, and Product. Process focuses on digitising, automating, and optimizing business operations, while Product focuses on reimagining the business model using new capabilities enabled by cloud.
Security is one of the six CAF perspectives, not one of the four transformation domains, and it provides guidance on protecting data and workloads rather than defining a transformation pathway. Infrastructure is a component within the Technology transformation domain and the Platform perspective, but it is not itself one of the four transformation domains. Compliance is an area addressed by the Governance perspective, but it is not one of the four transformation domains defined by the CAF.

## clf-c02/domain1/q1126

Answer: B

The Align phase of the AWS CAF focuses on identifying capability gaps, evaluating cross-organizational dependencies, and assessing application readiness to create a detailed action plan for cloud adoption, making it the phase where migration readiness is determined.
The Envision phase focuses on identifying how cloud can accelerate business outcomes and creating a shared vision for transformation, which happens before readiness assessment. The Launch phase focuses on delivering pilot initiatives and demonstrating incremental business value through initial cloud deployments, which occurs after readiness has been assessed. The Scale phase focuses on expanding cloud adoption across the organization and optimizing operating models for long-term scale, which comes after initial launches have been proven successful.

## clf-c02/domain1/q1127

Answer: B

The AWS CAF defines the cloud transformation journey in four phases: Envision (identify how cloud accelerates business outcomes), Align (identify capability gaps and create an action plan), Launch (deliver pilot initiatives), and Scale (expand adoption across the organization).
Starting with Align before Envision skips the critical first step of establishing a shared vision for why the organization is adopting cloud, which is needed to guide the alignment activities. Starting with Launch before Align means deploying to the cloud without first assessing readiness or creating an action plan, which risks uncoordinated and unsuccessful migrations. Placing Align after Launch means assessing readiness after already deploying workloads, which reverses the logical order of planning before execution.

## clf-c02/domain1/q1128

Answer: C

The Launch phase of the AWS CAF involves delivering pilot initiatives, building a Cloud Center of Excellence to provide guidance and best practices, and demonstrating incremental business value through initial cloud deployments that establish the foundation for broader adoption.
The Envision phase focuses on creating a shared transformation vision and identifying how cloud can drive business outcomes, which occurs before establishing operational structures like a CCoE. The Align phase focuses on assessing readiness, identifying gaps, and creating an action plan, which is planning work that precedes the hands-on launch activities. The Scale phase focuses on expanding adoption across the entire organization after the CCoE and initial patterns have already been established during the Launch phase.

## clf-c02/domain1/q1097

Answer: C

Rehosting, also known as lift and shift, involves moving an application to the cloud without making any changes to the application code or architecture, making it the fastest migration strategy for getting workloads into AWS.
Replatforming involves making targeted optimizations during migration, such as moving a database to a managed service like Amazon RDS, which requires some changes beyond a simple lift and shift. Refactoring involves redesigning the application to take advantage of cloud-native features such as serverless computing or microservices, which requires significant development effort and is not a minimal-change approach. Repurchasing involves replacing the existing application with a different product, typically a SaaS solution, which is not a strategy for moving existing code to AWS.

## clf-c02/domain1/q1098

Answer: B

Retiring means decommissioning applications that are no longer needed, which reduces the overall migration scope and eliminates the cost and effort of maintaining unused software.
Retaining means keeping applications in their current on-premises environment because they are not ready to migrate, which is appropriate for applications still in active use rather than those that are no longer needed. Rehosting means moving an application to AWS without changes, which would waste resources on an application that provides no business value. Relocating means moving infrastructure to AWS with minimal changes, such as using VMware Cloud on AWS, which is also not appropriate for applications that should be decommissioned.

## clf-c02/domain1/q1099

Answer: B

Repurchasing involves moving to a different product, typically replacing an existing application with a cloud-based SaaS alternative, which is exactly what switching from an on-premises email system to Amazon WorkMail represents.
Replatforming involves making targeted optimizations to an existing application during migration, such as moving a self-managed database to Amazon RDS, rather than replacing the entire application with a different product. Refactoring involves redesigning the existing application architecture to leverage cloud-native features, not replacing the application with a completely different product. Rehosting involves moving the existing application as-is to the cloud, which would mean running the same on-premises email system on EC2 rather than switching to a SaaS replacement.

## clf-c02/domain1/q1100

Answer: B

Replatforming, also known as lift, tinker, and shift, involves making targeted optimizations during migration without changing the core application architecture, such as moving a self-managed database to a managed service like Amazon RDS to benefit from automated patching and backups.
Rehosting would mean moving the MySQL database to an EC2 instance and continuing to manage it manually, which does not take advantage of managed database features. Refactoring would involve redesigning the application to use a fundamentally different database approach, such as migrating from a relational database to a NoSQL service like DynamoDB, which goes beyond targeted optimization. Retaining means keeping the workload in its current on-premises environment, which does not involve any migration to AWS.

## clf-c02/domain1/q1101

Answer: D

Refactoring, also known as re-architecting, involves fundamentally redesigning an application to leverage cloud-native capabilities such as AWS Lambda for serverless computing, Amazon SQS for decoupled messaging, and containerised microservices, typically delivering the greatest long-term cloud benefits at the highest initial effort.
Rehosting moves an application to the cloud without any architectural changes, preserving the existing design rather than adopting cloud-native patterns. Replatforming makes targeted optimizations during migration, such as switching to managed services, but does not involve a full architectural redesign. Repurchasing replaces the existing application with a different product, typically a SaaS solution, rather than redesigning the existing application architecture.

## clf-c02/domain1/q1102

Answer: B

Retaining means keeping applications in their current on-premises environment, which is the appropriate strategy for workloads that are not yet ready to migrate due to compliance constraints, technical dependencies, or other unresolved requirements.
Retiring means decommissioning applications that are no longer needed, which is not appropriate for applications that are still in active use and have unresolved dependencies. Relocating means moving infrastructure to AWS with minimal changes, such as using VMware Cloud on AWS, which does not address the underlying compliance dependencies preventing migration. Repurchasing means replacing the application with a SaaS alternative, which also does not resolve the compliance constraints that are blocking the migration.

## clf-c02/domain1/q1103

Answer: A, C

Rehost and Repurchase are two of the seven migration strategies (7 Rs) defined in the AWS Cloud Adoption Framework: Rehost, Replatform, Refactor, Repurchase, Retire, Retain, and Relocate.
Revalidate is not a recognized migration strategy in the AWS CAF or any standard AWS migration framework. Redistribute is not a recognized migration strategy in the AWS CAF and does not correspond to any defined cloud migration approach. Reconfigure is not a recognized migration strategy in the AWS CAF; the closest strategy involving changes is Replatform, which makes targeted optimizations during migration.

## clf-c02/domain1/q1129

Answer: C

Relocating involves moving infrastructure to AWS without purchasing new hardware, rewriting applications, or modifying existing operations, such as migrating VMware-based workloads to VMware Cloud on AWS where the existing VMware environment continues to function with minimal changes.
Rehosting involves moving individual applications to AWS infrastructure such as EC2 instances, which requires converting virtual machines rather than preserving the existing VMware management layer. Replatforming involves making targeted optimizations during migration such as switching to managed services, which goes beyond simply moving the existing VMware environment as-is. Refactoring involves redesigning the application architecture to use cloud-native services, which is the opposite of preserving the existing VMware-based infrastructure.

## clf-c02/domain1/q1130

Answer: C

The AWS CAF defines seven migration strategies known as the 7 Rs: Rehost, Replatform, Refactor (Re-architect), Repurchase, Retire, Retain, and Relocate, each representing a different approach to handling workloads during a cloud migration.
Five Rs was an earlier version of the migration strategies that did not include Relocate and Retain, and does not reflect the current AWS CAF guidance. Six Rs is another historical version that predates the addition of the Relocate strategy, and is no longer the complete set defined by the current AWS CAF. Eight Rs exceeds the number of strategies defined by the AWS CAF, which recognizes exactly seven distinct migration approaches.

## clf-c02/domain1/q1131

Answer: C

Migrating from a relational Oracle database to a NoSQL service like Amazon DynamoDB requires fundamentally redesigning the data model and application logic, which is a refactoring or re-architecting strategy that leverages cloud-native capabilities for improved scalability and cost.
Replatforming would involve moving Oracle to Amazon RDS for Oracle or a compatible managed relational database, making targeted optimizations without changing the fundamental database paradigm. Rehosting would mean running Oracle on an EC2 instance exactly as it ran on-premises, with no changes to the database engine or architecture. Repurchasing would mean replacing the application with a completely different commercial product or SaaS solution, not redesigning the database layer to use a different AWS-native service.

## clf-c02/domain1/q1132

Answer: B

AWS Application Migration Service (AWS MGN) automates the lift-and-shift rehosting process by continuously replicating source servers to AWS, performing automated machine conversion, and launching fully provisioned instances on AWS with minimal downtime.
AWS Database Migration Service migrates databases to AWS, supporting both homogeneous and heterogeneous migrations, but it handles database workloads specifically rather than full server migrations. AWS Migration Hub provides a central location to track the progress of migrations across multiple AWS tools, but it is a tracking and visibility service rather than a tool that performs the actual server migration. AWS Snow Family provides physical devices for transferring large volumes of data to AWS offline, but does not automate the conversion and launching of servers in the cloud.

## clf-c02/domain1/q1133

Answer: C

AWS Migration Hub provides a single dashboard to discover existing servers, plan migrations, and track the status of application migrations across AWS migration tools such as Application Migration Service, Database Migration Service, and partner solutions.
AWS Application Migration Service performs the actual server replication and migration to AWS, but it handles the migration execution rather than providing a centralized tracking dashboard across multiple tools. AWS CloudTrail records API calls and management events for auditing purposes, and is an activity logging service rather than a migration progress tracking tool. AWS Config records and evaluates resource configurations for compliance, and monitors the state of AWS resources rather than tracking migration progress.

## clf-c02/domain1/q1134

Answer: C

AWS Snowball Edge is a physical data transfer device that can hold up to 80 TB per device, allowing large-scale data transfers to AWS by shipping the device rather than transferring over the network, making it ideal when network bandwidth is limited and transfer times over the internet would be impractical.
AWS DataSync automates data transfers between on-premises storage and AWS over the network, but with limited bandwidth a 100 TB transfer would take an unacceptably long time. AWS Direct Connect establishes a dedicated private network connection to AWS which improves bandwidth and consistency, but provisioning a Direct Connect link takes weeks and still may not provide sufficient bandwidth for a timely 100 TB transfer. Amazon S3 Transfer Acceleration speeds up uploads to S3 using CloudFront edge locations, but it still relies on the internet and would be constrained by the company's limited network bandwidth.

## clf-c02/domain1/q1135

Answer: C

Refactoring or re-architecting an application to use cloud-native services such as serverless computing, managed databases, and event-driven architectures delivers the greatest long-term benefits in scalability, performance, and cost efficiency, but requires the most significant investment in development time and effort.
Rehosting provides the fastest migration path with minimal effort but does not take advantage of cloud-native features, meaning long-term benefits are limited to infrastructure-level improvements only. Replatforming provides moderate cloud benefits with moderate effort by making targeted optimizations, but does not achieve the full potential of cloud-native architecture. Relocating preserves the existing infrastructure environment and provides the least cloud-native benefit, as workloads continue to run in their original configuration.

## clf-c02/domain1/q1136

Answer: B

AWS Application Discovery Service collects detailed information about on-premises servers including configuration, utilization, and network dependencies, helping companies plan their migration by understanding what they have and how applications are interconnected.
AWS Migration Hub provides a central dashboard for tracking migration progress across multiple tools, but it relies on discovery tools like Application Discovery Service to gather the underlying infrastructure data. AWS Application Migration Service performs the actual server migration by replicating and launching instances on AWS, but it does not discover or assess on-premises infrastructure. AWS Trusted Advisor provides best-practice recommendations for existing AWS environments across security, cost, and performance, but it does not discover or assess on-premises infrastructure.

## clf-c02/domain1/q1137

Answer: C

AWS Database Migration Service supports continuous data replication from on-premises databases to AWS with minimal downtime, handling both homogeneous migrations where the source and target engines are the same and heterogeneous migrations where the engines differ.
AWS Application Migration Service migrates entire servers including the operating system and applications to AWS, but it is not designed for database-specific migrations that require data replication and schema handling. AWS Schema Conversion Tool converts database schemas and stored procedures from one engine to another to support heterogeneous migrations, but it handles schema conversion rather than the actual data migration itself. AWS DataSync automates data transfers between on-premises storage systems and AWS storage services such as S3 and EFS, but it is a file-based data movement service not designed for database migration.

## clf-c02/domain1/q1138

Answer: D

Breaking a monolithic application into microservices using cloud-native services like AWS Lambda and Amazon API Gateway is a refactoring or re-architecting strategy that fundamentally changes the application design to leverage cloud capabilities.
Rehosting would move the monolithic application to EC2 as-is without changing its architecture, preserving the monolith rather than decomposing it into microservices. Replatforming would make targeted improvements such as moving the database to a managed service, but would not involve a fundamental architectural change like decomposing a monolith into microservices. Repurchasing would replace the application with a different commercial or SaaS product, not redesign the existing application into a microservices architecture.

## clf-c02/domain1/q1139

Answer: A, C

Rehost applies to the 200 servers being moved as-is through lift-and-shift migration, and Retire applies to the 150 servers that are no longer needed and should be decommissioned, reducing the overall migration scope and cost.
Replatform is incorrect for the 100 database servers because changing the database engine entirely, such as from Oracle to PostgreSQL, constitutes refactoring rather than replatforming, which would be moving Oracle to RDS for Oracle. Retain means keeping workloads on-premises, which does not describe the 50 applications being replaced with SaaS solutions, that would be Repurchase. Relocate means moving VMware-based infrastructure to VMware Cloud on AWS, which is a specific strategy for preserving VMware environments and does not describe a general lift-and-shift migration.

## clf-c02/domain1/q1140

Answer: B

Rehosting, or lift and shift, moves the application to AWS without any changes to the code or architecture, while replatforming, or lift, tinker, and shift, makes targeted optimizations during migration such as switching to a managed database or changing the caching layer, without fundamentally redesigning the application.
Rehosting does not change any application code, and replatforming makes only targeted changes, so the first option reverses the relationship between the two strategies. Rehosting moves the existing application to the cloud rather than replacing it with SaaS, which would be the repurchase strategy. Rehosting is generally faster than replatforming because it requires fewer changes and less testing, not slower, since the application is moved without modification.

## clf-c02/domain2/q003

Answer: B

AWS CloudTrail records all API calls and account activity across an AWS environment, capturing who performed each action, from which IP address, and at what time, making it the definitive source for identifying who terminated EC2 instances.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not record who performed API actions or management events. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than an audit log of account activity. EC2 Instance Usage Report provides billing and usage data about EC2 instances and does not contain API call logs or identity information about who terminated instances.

## clf-c02/domain2/q005

Answer: A

Under the Shared Responsibility Model, who is responsible for what shifts depending on the service type, with AWS taking on more responsibility for managed services while customers handle more of the stack for IaaS services.
Security of IaaS services is not solely AWS's responsibility, as customers using IaaS must manage the guest operating system, application stack, and data, while AWS is only responsible for the underlying infrastructure. Patching the guest OS is not always AWS's responsibility, as for IaaS services such as EC2 the customer is fully responsible for patching the operating system they run on their instances. Security of managed services is not solely the customer's responsibility, as AWS takes on significantly more of the security burden for managed services such as RDS and Lambda, covering the underlying platform and infrastructure layers.

## clf-c02/domain2/q011

Answer: C

IAM user groups let you organize multiple users together and assign shared permissions at the group level via IAM policies, making it easy to manage access for entire teams without configuring each user individually.
IAM roles provide temporary security credentials that can be assumed by users, services, or applications, and are not designed to organize teams or assign shared permissions to a fixed set of users in the way groups are. IAM users are individual identities each with their own credentials and permissions, and managing large numbers of users individually by attaching policies to each one is impractical compared to using groups. AWS Organizations manages multiple AWS accounts under a single structure for consolidated billing and policy enforcement, and is not the service used to organize individual IAM users into teams within a single account.

## clf-c02/domain2/q022

Answer: A

The Principle of Least Privilege means granting users only the exact permissions they need to perform their job and nothing beyond that, minimizing the risk of accidental or malicious misuse of AWS resources.
Granting IAM users at least the necessary permissions to access core AWS services describes a minimum baseline, which is the opposite of least privilege; least privilege means restricting permissions to only what is needed for a specific task rather than ensuring access to common services. Granting all trusted users access to any AWS service in the account contradicts least privilege by providing broad unrestricted access rather than targeted permissions. Granting no permissions to any IAM user is not a practical interpretation of least privilege, which is about granting the minimum required permissions rather than granting none at all.

## clf-c02/domain2/q026

Answer: A, D

AWS Shield provides managed DDoS protection at the network and transport layers, and AWS WAF lets you create rules that filter malicious web traffic at the application layer. Together they defend against the full spectrum of DDoS attacks.
AWS Config continuously monitors and records AWS resource configurations to evaluate compliance, and is a configuration management and auditing service with no capability to block or mitigate DDoS traffic. Amazon Cognito is a user identity and authentication service for web and mobile applications, providing sign-up and sign-in functionality and federated identity, and has no DDoS mitigation capabilities. AWS KMS is a key management service for creating and controlling encryption keys used to protect data, and is not involved in network traffic filtering or DDoS defense.

## clf-c02/domain2/q031

Answer: A

AWS Artifact is a self-service portal where customers can access and manage AWS compliance reports and agreements, including NDA and Business Associate Addendum (BAA) documents that govern the relationship between customers and AWS.
AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services, and is a certificate management service rather than an agreement management portal. AWS Systems Manager provides operational tools for managing AWS resources at scale including patching, parameter storage, and session management, and is not used to manage contractual agreements with AWS. AWS Organizations manages multiple AWS accounts under a master account structure for consolidated billing and service control policies, and is not a portal for managing compliance reports or agreements.

## clf-c02/domain2/q032

Answer: B, C

Amazon DynamoDB and Amazon EMR are fully managed services where AWS handles provisioning, patching, scaling, and maintenance automatically, freeing customers from managing the underlying infrastructure.
Amazon VPC is a networking construct that customers configure and manage themselves, including subnets, route tables, internet gateways, and security groups, making it a customer-configured resource rather than a fully managed service. AWS IAM is a service customers use to manage their own users, roles, and permissions, and while AWS maintains the IAM infrastructure, customers are responsible for all identity and access configuration. Amazon Elastic Compute Cloud provides virtual servers where customers are responsible for the operating system, installed software, patches, and configuration, making it an infrastructure service where the customer manages the virtual machine layer rather than a fully managed one.

## clf-c02/domain2/q036

Answer: A

IAM access keys, consisting of an access key ID and secret access key, are the credentials used to authenticate API requests programmatically through the AWS CLI, allowing IAM users to interact with AWS services from the command line without the Management Console.
A secret token is not a standard IAM credential type for CLI access; temporary security credentials issued to IAM roles include a session token in addition to an access key ID and secret, but a standalone secret token alone is not used for CLI authentication. A UserID is an internal AWS identifier assigned to IAM users but is not a credential that can be supplied to authenticate CLI requests. A user name and password are the credentials used to log in to the AWS Management Console interactively, not to authenticate programmatic CLI requests which require access keys.

## clf-c02/domain2/q037

Answer: B

The AWS Abuse Team handles reports of AWS infrastructure being used for malicious activity such as hacking, spam, or unauthorised use, and this channel is available to all customers regardless of their support tier.
The AWS Customer Service team handles general account and billing enquiries, and is not the designated contact for reporting malicious use of AWS infrastructure. The AWS Concierge team is a dedicated support resource available exclusively to Enterprise support plan customers for billing and account assistance, and does not handle abuse or malicious activity reports. The AWS Security team manages AWS's own internal security posture and vulnerability disclosure program, and is not the correct channel for customers to report malicious use of AWS resources within their own accounts.

## clf-c02/domain2/q038

Answer: A, D

Patch Management and Configuration Management are both shared controls where AWS and the customer each manage their own layer independently, with AWS responsible for the infrastructure and customers responsible for their own operating systems and applications.
IAM Management is a customer responsibility, as customers exclusively control their own users, roles, and permissions within their AWS account. VPC Management is a customer responsibility, as customers define and configure their own virtual network settings including subnets, route tables, and security groups. Data Center operations are exclusively AWS's responsibility, covering all physical infrastructure management.

## clf-c02/domain2/q043

Answer: B

Configuring infrastructure devices such as networking hardware and physical servers is entirely AWS's responsibility, as customers have no access to or control over the underlying physical infrastructure.
Client-side encryption is the customer's responsibility, as customers choose whether and how to encrypt data before sending it to AWS. Server-side encryption is also the customer's responsibility, as customers decide whether to enable encryption at rest for their data stored in AWS services. Filtering traffic with Security Groups is the customer's responsibility, as customers define and manage their own Security Group rules within their AWS environment.

## clf-c02/domain2/q046

Answer: D

AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across five categories including security, cost optimization, performance, fault tolerance, and service limits, helping you follow AWS best practices.
AWS Shield is a managed DDoS protection service that defends against distributed denial of service attacks, and does not provide broad infrastructure security recommendations. AWS Management Console is the web-based interface for accessing and managing AWS services, and does not analyze or make recommendations about your environment. AWS Secrets Manager is a service for storing, rotating, and managing access to secrets such as database credentials and API keys, and does not provide infrastructure optimization recommendations.

## clf-c02/domain2/q048

Answer: D, E

Setting password complexity rules and configuring network access rules such as security groups and NACLs are both customer responsibilities, as customers control their own identity policies and network configuration within their AWS environment.
Disk disposal is AWS's responsibility, as AWS manages the secure decommissioning and destruction of physical storage hardware. Controlling physical access to compute resources is AWS's responsibility, as customers have no access to the underlying physical infrastructure. Patching the network infrastructure is AWS's responsibility, covering the managed networking layer beneath the customer's virtual network.

## clf-c02/domain2/q056

Answer: C

Customers are responsible for patching the operating system and software on EC2 instances they launch, as the guest OS and everything running on it falls within the customer's side of the Shared Responsibility Model.
Patching underlying infrastructure is AWS's responsibility, covering the hypervisor and physical hardware beneath the customer's instances. Physical security is AWS's responsibility exclusively, as customers have no access to or control over AWS data centers. Patching network infrastructure is AWS's responsibility, covering the managed networking layer that underpins all customer virtual networks.

## clf-c02/domain2/q057

Answer: C

Configuration management is a shared control where AWS manages the configuration of its infrastructure, while the customer is responsible for configuring the operating systems, databases, and applications they deploy.
Configuration management is not solely the customer's responsibility, as AWS independently manages the configuration of all underlying infrastructure components including hardware, networking, and managed services. Configuration management is not solely AWS's responsibility, as customers retain full accountability for configuring the resources and workloads they deploy on top of the AWS infrastructure. Configuration management is explicitly recognized as a shared control in the AWS Shared Responsibility Model and is therefore fully accounted for within it.

## clf-c02/domain2/q058

Answer: B

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data such as personally identifiable information and intellectual property stored in Amazon S3, making it the correct service for automatically recognizing and classifying sensitive data.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and focuses on detecting security threats rather than classifying data. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not classify or discover sensitive data stored in S3. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to recognize or classify sensitive data.

## clf-c02/domain2/q060

Answer: A, C

Customers are responsible for encrypting their application data at rest and for training their users on proper security practices when using AWS services, both sitting on the customer side of the model.
Ensuring that AWS NTP servers are set to the correct time is entirely AWS's responsibility, as customers have no access to or control over the underlying infrastructure components that provide time synchronisation. Ensuring that access to data centers is restricted is entirely AWS's responsibility, covering physical access controls, surveillance, and protection of the facilities that house AWS infrastructure. Ensuring that hardware is disposed of properly is entirely AWS's responsibility, as customers never take possession of physical hardware and AWS manages all end-of-life processes for its own equipment.

## clf-c02/domain2/q064

Answer: B

AWS Config continuously tracks and records configuration changes to AWS resources over time, allowing you to review historical configurations and identify what changed and when.
Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances for security findings, not a service for tracking configuration changes over time. AWS Service Catalog allows organizations to create and manage approved portfolios of IT services for deployment, unrelated to tracking resource changes. AWS IAM manages user identities, roles, and access permissions within an AWS account and does not record or track configuration changes to resources.

## clf-c02/domain2/q075

Answer: B

IAM access keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic calls to AWS APIs via the CLI, SDKs, or direct HTTP requests, allowing applications and scripts to interact with AWS services without using the console.
Logging in to the AWS Management Console requires a user name and password combination, not access keys, which are reserved for programmatic and CLI access rather than browser-based console authentication. Logging in to Amazon EC2 instances uses SSH key pairs on Linux instances or a password retrieved via the console for Windows instances, and is separate from the IAM access keys used for API authentication. Authenticating to AWS CodeCommit repositories uses Git credentials or SSH keys configured separately from IAM access keys, though access keys can be used with the AWS CLI to interact with CodeCommit programmatically.

## clf-c02/domain2/q078

Answer: C, E

AWS CloudTrail logs all API calls and account activity across an AWS account, providing a complete audit trail of who did what and when. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources, providing operational visibility into account activity and performance.
Amazon CloudFront is a content delivery network that caches and distributes content to users at edge locations worldwide, and does not gather information about account activity. AWS Cloud9 is a cloud-based integrated development environment for writing, running, and debugging code, and has no account monitoring or activity logging capability. AWS CloudHSM is a hardware security module service that manages and stores cryptographic keys in dedicated hardware, and is not a tool for monitoring or gathering information about account activity.

## clf-c02/domain2/q090

Answer: B

IAM access keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic requests to AWS services through the AWS CLI and SDKs.
API keys is an informal term not specific to AWS IAM; AWS programmatic access uses access keys consisting of an access key ID and secret access key, and this informal label does not accurately describe the credential type. User names and passwords are used to log in to the AWS Management Console interactively, and are not the credentials used for CLI or SDK programmatic access, which requires access keys. SSH keys are used to connect securely to EC2 instances via Secure Shell and are not the credentials that authenticate developers' CLI requests to AWS services.

## clf-c02/domain2/q091

Answer: D

Customers are fully responsible for implementing application-level controls such as routing traffic within their own systems, as these decisions sit entirely within the customer's layer of the Shared Responsibility Model.
Patching the infrastructure components is AWS's responsibility, covering the physical servers, networking equipment, and hypervisor layer beneath the customer's workloads. Maintaining the underlying infrastructure components is AWS's responsibility, as customers have no access to or control over the physical hardware running their workloads. Maintaining physical and environmental controls is AWS's responsibility exclusively, covering data center facilities, power, cooling, and physical security.

## clf-c02/domain2/q103

Answer: C, E

MFA adds a second authentication factor beyond a password to protect console logins, and password policies enforce complexity and rotation requirements. Both directly enhance the security of access to the AWS Management Console.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service rather than a mechanism for enhancing the authentication security of the AWS Management Console itself. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and has no role in controlling or securing console login access. Security groups act as virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and operate at the network layer rather than the console authentication layer.

## clf-c02/domain2/q105

Answer: B

Under the shared responsibility model, AWS has sole responsibility for physical security of its data centers, including controls such as perimeter security, surveillance, and hardware disposal, as customers never have access to AWS physical facilities.
AWS IAM policies define permissions for users, groups, and roles within an AWS account, and creating, managing, and auditing these policies is entirely the customer's responsibility as they reflect each customer's own access control decisions. Amazon S3 bucket policies control access to objects stored within S3 buckets, and configuring and auditing these policies is the customer's responsibility as they govern how the customer's own data is accessed and shared. AWS CloudTrail logs record API calls and account activity across an AWS environment, and while CloudTrail is an AWS-managed service, enabling it, configuring log retention, and auditing the logs it produces are all customer responsibilities.

## clf-c02/domain2/q107

Answer: A, C

Patching database software and backing up databases are maintenance tasks that AWS handles automatically for managed services such as RDS, freeing up customers' IT resources from these time-consuming operational responsibilities.
Testing application releases is the customer's responsibility as it requires knowledge of the specific application logic, acceptance criteria, and business requirements that only the customer possesses, making it a task AWS cannot cover on the customer's behalf. Creating database schema requires understanding of the customer's data model and application requirements, and is a design and development activity that the customer must perform rather than a managed service task AWS provides. Running penetration tests is a security activity that customers perform on their own applications and infrastructure, and is not an operational burden AWS covers as part of its managed service offerings.

## clf-c02/domain2/q114

Answer: A

AWS Config continuously records resource configurations and changes over time, providing a detailed audit trail of what changed, when it changed, and who made the change, making it the purpose-built service for auditing change management of AWS resources.
AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, but does not record or audit configuration changes to individual resources over time. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and does not track resource configuration history or change management. Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change auditing service.

## clf-c02/domain2/q117

Answer: B

IAM users are the entities that have access keys consisting of an access key ID and secret access key associated with them for programmatic CLI access to AWS services.
An IAM group is a collection of IAM users used to manage shared permissions collectively, and is not an identity that can authenticate or be issued access keys of any kind. An IAM role uses temporary security credentials that are automatically issued and rotated when the role is assumed, and does not have permanent access keys associated with it. An IAM policy is a JSON document that defines permissions by specifying allowed or denied actions on resources, and is a permissions construct rather than an identity that can hold or be associated with access keys.

## clf-c02/domain2/q118

Answer: C

Data encryption at rest is a customer responsibility. AWS provides the tools and services to enable encryption, but customers decide whether and how to encrypt their data.
Ensuring disk drives are wiped after use is AWS's responsibility. AWS handles the secure decommissioning and disposal of physical storage hardware. Ensuring firmware is updated on hardware devices is AWS's responsibility. Customers have no access to or control over physical hardware. Ensuring network cables are category six or higher is AWS's responsibility. Physical networking infrastructure is managed entirely by AWS.

## clf-c02/domain2/q120

Answer: A, C

Programmatic AWS access requires an access key ID to identify the calling entity and a secret access key to sign requests, together authenticating API calls made via the CLI or SDKs.
A primary key is not a valid AWS IAM credential component; it is a database term for a unique row identifier and has no role in AWS programmatic authentication. A user ID is an internal AWS identifier assigned to IAM users for tracking purposes but cannot be supplied as a credential to authenticate programmatic API requests. A secondary key is not a recognized AWS IAM credential type, and no such concept exists in the AWS authentication model for programmatic access.

## clf-c02/domain2/q121

Answer: D

Awareness and training is a shared control because both AWS and the customer must independently ensure their own staff understand their respective security responsibilities, regardless of what the other party does.
Providing a key for Amazon S3 client-side encryption is solely the customer's responsibility, as AWS has no involvement in client-side key generation or management. Configuration of an Amazon EC2 instance is solely the customer's responsibility, as customers control the guest OS and everything installed on it. Environmental controls of physical AWS data centers are solely AWS's responsibility, as customers have no access to or involvement in physical facility management.

## clf-c02/domain2/q126

Answer: B, E

Granting least privilege access ensures IAM users only have the permissions they need, reducing the blast radius of a compromised account, and activating MFA for privileged users adds a critical second authentication factor that protects against stolen credentials. Both directly protect access to an AWS account.
Enabling AWS CloudTrail records API calls and account activity for auditing and compliance, and while it improves visibility into account actions after the fact, it does not prevent unauthorised access and is therefore not a security measure that protects access. Creating one IAM user shared across many developers is a security anti-pattern because it prevents individual accountability, makes credential rotation difficult, and means that a single compromised credential grants access to everyone sharing that account. Enabling Amazon CloudFront provides a content delivery network for distributing web content globally, and has no connection to protecting access to an AWS account.

## clf-c02/domain2/q144

Answer: D

Under the Shared Responsibility Model, backing up EBS volumes through snapshots is the customer's responsibility, as AWS does not automatically back up EBS volumes on the customer's behalf.
Ensuring network connectivity from AWS to the internet is entirely AWS's responsibility, as AWS manages and maintains the underlying network infrastructure that connects its services to the public internet. Patching and fixing flaws within the AWS Cloud infrastructure is entirely AWS's responsibility, as customers have no access to the underlying hardware, hypervisors, or physical networking components. Ensuring the physical security of cloud data centers is entirely AWS's responsibility, covering access controls, surveillance, and protection of the facilities that house AWS infrastructure.

## clf-c02/domain2/q150

Answer: B, D

Enabling MFA requires a second factor beyond the password to complete sign-in, and configuring a strong password policy enforces complexity, length, and rotation requirements. Both directly strengthen AWS account logon security.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and has no role in controlling or securing account logon processes. Amazon Cognito manages user authentication and access for customer-facing applications through user pools and identity pools, and is designed for application-level user management rather than securing AWS account logons directly. AWS Organizations is an account management service for centrally governing and consolidating multiple AWS accounts, and does not itself provide logon security features for individual account access.

## clf-c02/domain2/q158

Answer: B

AWS Config continuously records configuration changes to AWS resources and maintains a history of those changes, enabling audit and compliance reviews of how resources have been configured over time.
AWS Shield is a managed DDoS protection service that safeguards AWS applications against distributed denial-of-service attacks, and has no capability to track or audit resource configuration changes. AWS Identity and Access Management (IAM) is a service for controlling who can authenticate and what actions they are authorised to perform, and manages permissions and identities rather than recording configuration changes to AWS resources. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security testing tool rather than a configuration change tracking or auditing service.

## clf-c02/domain2/q162

Answer: B

With Amazon EC2, the customer is responsible for the guest operating system including configuration, security patching, and networking setup, as AWS only manages the underlying physical infrastructure.
Amazon RDS is a fully managed relational database service where AWS handles operating system patching, database engine updates, and infrastructure maintenance on the customer's behalf. Amazon ElastiCache is a fully managed in-memory caching service where AWS manages the underlying operating system and infrastructure, removing those responsibilities from the customer entirely. AWS Fargate is a serverless compute engine for containers where AWS manages the underlying infrastructure and operating system, meaning the customer only needs to manage their container images and application code.

## clf-c02/domain2/q163

Answer: D, E

MFA adds a second authentication factor beyond a password, and enforcing password strength and expiration policies reduce the risk of credential compromise. Both are supported IAM security methods that directly protect IAM user accounts.
Amazon Rekognition is a machine learning service for analyzing images and videos to detect objects, faces, and text, and has no role in adding security to IAM user authentication. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service rather than a mechanism for securing IAM user accounts. Security groups act as virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and operate at the network layer rather than the IAM authentication layer.

## clf-c02/domain2/q169

Answer: B

AWS Trusted Advisor automatically scans your account and flags security groups with unrestricted access (0.0.0.0/0) to specific ports as part of its Security category checks, making it the simplest and most direct approach without manual investigation.
Manually reviewing inbound rules for each security group in the EC2 console to look for 0.0.0.0/0 entries would work but is time-consuming and error-prone at scale, making it far less simple than using Trusted Advisor's automated check. The AWS IAM console manages identities, users, roles, and permissions, and does not contain security group configurations or inbound traffic rules, making it the wrong place to check for unrestricted port access. Creating a custom AWS Config rule that invokes a Lambda function to review firewall rules would provide automated ongoing compliance checks but requires significant setup effort, making it far more complex than running the existing Trusted Advisor check.

## clf-c02/domain2/q170

Answer: B, C

AWS Trusted Advisor includes security checks that flag vulnerabilities such as open security groups, and AWS provides data encryption capabilities through services like KMS and native encryption across storage and database services. Both are genuine AWS security-related offerings.
Multi-factor authentication physical tokens are hardware MFA devices that customers purchase independently rather than a service provided by AWS; customers configure them with their accounts but AWS does not supply or manufacture the hardware tokens. Automated penetration testing is not an AWS service offering; AWS permits customers to conduct their own penetration testing on permitted services, but AWS does not perform automated penetration testing on customer workloads as a service. Amazon S3 copyrighted content detection is not an AWS service; Amazon Macie detects sensitive data categories such as PII in S3, but copyright detection is not within the scope of available AWS security services.

## clf-c02/domain2/q171

Answer: A, D

AWS WAF filters malicious HTTP and HTTPS traffic at the application layer by blocking requests that match defined rules, and Amazon CloudFront integrates with AWS Shield to absorb volumetric DDoS attacks at edge locations before they reach origin servers. Both directly provide DDoS mitigation features.
Amazon DynamoDB is a fully managed NoSQL database service, and while AWS protects the underlying infrastructure it runs on, DynamoDB itself is not a service that provides DDoS mitigation features. Amazon EC2 provides virtual compute instances and does not include built-in DDoS mitigation; customers can configure security groups and use additional services like Shield and WAF to protect applications running on EC2. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not provide DDoS mitigation capabilities.

## clf-c02/domain2/q175

Answer: A

AWS Artifact is a self-service portal that provides on-demand access to AWS security and compliance documents such as SOC reports, ISO certifications, PCI attestations, and other auditor-issued compliance materials.
Configuration management details are not available from Artifact; AWS Config tracks resource configuration history and CloudTrail logs API activity, but neither is reached through Artifact. Training materials come from AWS Training and Certification and AWS Skill Builder, not Artifact, which holds only compliance documents. A security assessment of deployed applications is performed by Amazon Inspector, which scans EC2 instances and container images for vulnerabilities, not by Artifact.

## clf-c02/domain2/q179

Answer: C

IAM policies can be applied directly to IAM users or groups to control exactly who can access an S3 bucket and what operations they can perform, providing fine-grained access control that limits access to specific users.
Signing in with AWS account credentials provides root-level access to all S3 buckets by default rather than limiting access to specific users; root credentials should never be used for day-to-day access and do not restrict bucket access to particular individuals. Enabling S3 versioning preserves multiple versions of objects to protect against accidental deletion, and is a data recovery feature rather than an access restriction mechanism that limits which users can access the bucket. Setting a bucket policy to make the bucket private removes public access, but without specifying allowed principals it does not grant access to any specific users; additional policy statements identifying particular IAM principals are required to limit access to specific users.

## clf-c02/domain2/q181

Answer: C

AWS Artifact is the dedicated self-service portal for accessing AWS compliance documentation, including SOC 1, SOC 2, ISO 27001, and PCI DSS reports, allowing customers to download these documents for their own audit and compliance purposes.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network exposure risks, and does not provide or store AWS compliance certifications or SOC reports. AWS CloudTrail logs all API calls and management events in an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS compliance certifications or third-party audit reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a repository of compliance reports.

## clf-c02/domain2/q182

Answer: C

Under the shared responsibility model, AWS is responsible for securing the underlying hypervisor that runs EC2 virtual machines, as this forms part of the infrastructure layer that customers have no access to or control over.
Encrypting client-side data is the customer's responsibility, as AWS has no involvement in data that is encrypted before being sent to AWS services. Configuring IAM roles is the customer's responsibility, as customers define and manage the permissions that control what actions users and services can perform within their account. Setting user password policies is the customer's responsibility, as customers control the IAM password policies that govern how their users authenticate to the AWS Management Console.

## clf-c02/domain2/q183

Answer: B, E

Customers are responsible for patching the operating systems running on their EC2 instances and for configuring security groups to control inbound and outbound traffic within their AWS environment, both sitting on the customer side of the model.
Firmware upgrades of network infrastructure are entirely AWS's responsibility, as customers have no access to or control over the physical networking equipment that underpins the AWS Cloud. Patching the underlying hypervisor is entirely AWS's responsibility, as the virtualization layer sits below the operating system and is managed exclusively by AWS. Physical security of data centers is entirely AWS's responsibility, covering access controls, surveillance, and protection of the facilities that house AWS infrastructure.

## clf-c02/domain2/q190

Answer: D

AWS Shield provides always-on DDoS protection at no extra cost for all AWS customers, automatically detecting and mitigating the most common volumetric and protocol-based DDoS attacks without any customer configuration.
AWS WAF is a web application firewall that filters application-layer HTTP and HTTPS traffic based on configurable rules, and while it helps mitigate application-layer attacks, it is a separate service from Shield and requires customer configuration rather than providing automatic always-on protection. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts, and is an alerting and detection service rather than a service that actively blocks DDoS traffic. AWS CloudTrail records API calls and management events for auditing and compliance purposes, and has no capability to detect or protect against distributed denial of service attacks.

## clf-c02/domain2/q199

Answer: A, B

AWS Trusted Advisor provides automated security checks identifying vulnerabilities such as unrestricted security group access and missing MFA, and Amazon Inspector performs automated security assessments of EC2 instances to identify vulnerabilities and unintended network access. Both help ensure proper security settings.
Amazon SNS is a fully managed publish/subscribe messaging service for sending notifications to subscribers, and does not evaluate or ensure AWS security settings or configurations. Amazon CloudWatch monitors operational metrics and logs for observability and alerting, and while it can trigger notifications on specific metrics or log patterns, it does not actively assess or validate AWS resource security configurations. The Concierge Support Team assists Enterprise support plan customers with billing and account management, and does not perform technical security assessments or review resource security settings.

## clf-c02/domain2/q200

Answer: D

AWS Multi-Factor Authentication adds a second layer of security by requiring a one-time code from a hardware or virtual device in addition to a username and password, providing an additional level of security above the default username and password mechanism.
Encrypted keys refer to cryptographic keys used for data encryption purposes such as those managed by AWS KMS, and while they protect stored data, they do not provide an additional authentication mechanism for user login security. Email verification is used to confirm ownership of an email address during account setup or password recovery flows, and is not an ongoing additional security layer applied on top of username and password for AWS console logins. AWS KMS is a key management service for creating and managing cryptographic keys used to encrypt data at rest and in transit, and does not add authentication factors to the login process.

## clf-c02/domain2/q204

Answer: C

AWS's Acceptable Use Policy allows customers to perform penetration testing on their own EC2 instances and certain other permitted services without prior authorisation from AWS, provided the testing complies with the AUP conditions.
Penetration testing is not prohibited in AWS; the Acceptable Use Policy explicitly permits customers to conduct penetration testing on their own resources within defined guidelines, making the claim that it is not allowed incorrect. AWS does not perform automated penetration testing on behalf of customers; Amazon Inspector performs automated security assessments for vulnerabilities and network exposure, but this is not the same as penetration testing, and AWS does not conduct adversarial testing of customer infrastructure. AWS customers are permitted to perform penetration testing on their own services and resources, not only on services managed by AWS; the restriction is that testing must target the customer's own resources rather than AWS shared infrastructure.

## clf-c02/domain2/q208

Answer: B, E

Customers are responsible for protecting the confidentiality of data in transit using encryption such as HTTPS/TLS on connections to Amazon S3, and for patching operating systems and applications installed on Amazon EC2 instances as part of managing their guest environment.
Managing environmental events at AWS data centers, including power, cooling, fire suppression, and natural disaster response, is entirely AWS's responsibility as part of securing the physical infrastructure that customers never interact with. Controlling physical access to AWS Regions and data center facilities is AWS's responsibility; customers have no access to physical infrastructure and rely on AWS to implement badge-based entry, biometric controls, and security staff. Ensuring that the underlying EC2 host is configured properly falls under AWS's responsibility; customers manage the guest operating system and above, while AWS is responsible for the hypervisor, host hardware, and underlying virtualization layer.

## clf-c02/domain2/q211

Answer: C

AWS Access Keys, consisting of an access key ID and a secret access key, are the credentials used to authenticate programmatic API calls, functioning like a username and password for AWS SDKs and CLI.
An instance password refers to the Windows administrator password generated for EC2 Windows instances to enable RDP access, which is a server login credential rather than an API authentication mechanism equivalent to a username and password. Key pairs are RSA public/private key combinations used to authenticate SSH connections to Linux EC2 instances, and while they serve an authentication purpose, they are for instance-level SSH access rather than AWS API and service authentication. MFA is an additional authentication factor added on top of primary credentials such as a username and password, requiring a one-time code from a device, and is a supplementary mechanism rather than a standalone credential pair equivalent to a username and password.

## clf-c02/domain2/q213

Answer: C

AWS Organizations enables you to create a hierarchy of AWS accounts managed from a single master account, applying policies and consolidated billing across all member accounts.
AWS WAF is a web application firewall that filters and blocks malicious web traffic using managed and custom rule sets, and has no role in managing multiple AWS accounts. AWS Trusted Advisor analyzes your AWS environment and provides recommendations across cost optimization, security, and performance, but does not provide centralized management of multiple accounts. AWS Config continuously monitors and records AWS resource configurations for compliance purposes, but operates within individual accounts rather than providing centralized multi-account management.

## clf-c02/domain2/q219

Answer: D

AWS WAF is a web application firewall that lets you create rules to inspect and filter HTTP and HTTPS traffic, blocking common web exploits such as SQL injection and cross-site scripting before they reach your application.
Amazon Cognito is a user identity and authentication service for web and mobile applications that handles user sign-up, sign-in, and access control for application users, and does not inspect or filter HTTP traffic for SQL injection or other web exploits. AWS IAM manages user permissions and access to AWS services and resources, and is an identity and access management service rather than a traffic inspection tool that can block malicious web requests. Amazon Aurora is a relational database service compatible with MySQL and PostgreSQL, and is a managed database offering rather than a security service for filtering web application traffic.

## clf-c02/domain2/q221

Answer: C, E

Creating and managing hypervisors and maintaining physical hardware are solely AWS's responsibility, as customers have no access to or control over the virtualization layer or the underlying infrastructure that powers AWS services.
Monitoring network performance for their own applications and workloads is the customer's responsibility, as AWS provides the tools but customers are accountable for observing and responding to performance within their environment. Installing software on EC2 instances is the customer's responsibility, as customers manage everything above the hypervisor including the operating system, applications, and any software they choose to run. Configuring Access Control Lists is the customer's responsibility, as customers define and manage their own network access rules within their VPC environment.

## clf-c02/domain2/q223

Answer: C

IAM user console access is secured with a user name and password combination as the default credentials, providing the basic authentication required to access the AWS Management Console.
MFA is an optional additional authentication factor that can be layered on top of a username and password to require a one-time code from a device, but it is not the default credential requirement and is configured separately from the primary user name and password. Security tokens are temporary credentials consisting of an access key ID, secret access key, and session token that are issued when an IAM role is assumed, and are used for programmatic and role-based access rather than as default console credentials for IAM user accounts. Access keys consisting of an access key ID and secret access key are the credentials used for programmatic API and CLI access, not for logging into the AWS Management Console, which uses user name and password.

## clf-c02/domain2/q226

Answer: D, E

Hardware patching and maintenance of the physical servers that run AWS services, and securing the global physical infrastructure including data centers, power, cooling, and networking, are entirely AWS's responsibility under the shared responsibility model.
Encryption of EBS volumes is a customer responsibility that involves enabling EBS encryption at the volume or account level and selecting appropriate KMS keys to protect data at rest on block storage volumes. VPC security, including the configuration of security groups, network ACLs, and route tables, is the customer's responsibility as it governs how network traffic flows within and to the customer's own virtual private cloud. Access permissions, including creating IAM users, groups, roles, and attaching policies that control who can access which AWS services and resources, are entirely the customer's responsibility to define and manage.

## clf-c02/domain2/q229

Answer: A, E

AWS CloudTrail records all API calls and resource changes for auditing, and AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules. Together they are the primary change management and auditing tools in AWS.
Amazon Comprehend is a natural language processing service that uses machine learning to extract insights such as entities, sentiment, and key phrases from text, and is an AI analytics service with no capability to audit or monitor resource configuration changes. AWS Transit Gateway connects VPCs and on-premises networks through a central hub, providing network routing and connectivity rather than auditing or change management functionality. AWS X-Ray is an application performance tracing service that analyzes requests as they flow through distributed applications, and is a debugging and performance tool rather than an infrastructure change auditing service.

## clf-c02/domain2/q231

Answer: D

AWS CloudTrail logs all API activity and account events, creating a complete audit trail that helps organizations demonstrate compliance with regulatory requirements and investigate security incidents.
Amazon CloudFront is a global content delivery network that caches and distributes web content to users at low latency through edge locations, and is a performance and distribution service with no capability to record audit logs or help with regulatory compliance. AWS Migration Hub provides a central dashboard for tracking the progress of application migrations to AWS, and is a migration management tool rather than a compliance or audit service. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, providing visibility into performance and operational health, but it does not create the comprehensive API audit trail needed for regulatory compliance.

## clf-c02/domain2/q236

Answer: C

Security groups act as a stateful virtual firewall directly associated with EC2 instances, evaluating and filtering inbound and outbound traffic based on protocol, port, and source or destination rules defined by the customer.
AWS X-Ray is an application tracing and debugging service that analyzes requests as they flow through distributed applications to identify performance bottlenecks and errors, and has no capability to filter or control network traffic to EC2 instances. Network ACLs are stateless firewalls that operate at the subnet level rather than the EC2 instance level, applying rules to all traffic entering or leaving a subnet without tracking connection state, and are not directly associated with individual instances. VPC Flow Logs capture metadata about the IP traffic flowing to and from network interfaces within a VPC, providing visibility for analysis and troubleshooting, but they record traffic information rather than filter or block incoming requests.

## clf-c02/domain2/q238

Answer: A, C

Under the Shared Responsibility Model for Amazon RDS, the customer is responsible for designing the database schema and managing database-level settings such as parameters and user permissions.
Performing backups is managed by AWS for RDS, which automates backup retention and point-in-time recovery without requiring the customer to manually initiate or manage backup processes. Patching the database software is entirely AWS's responsibility for RDS, as AWS handles all engine-level patching and maintenance windows as part of the managed service. Installing the database software is entirely AWS's responsibility for RDS, as AWS provisions, installs, and maintains the underlying database engine on the customer's behalf.

## clf-c02/domain2/q252

Answer: A

AWS Identity and Access Management allows administrators to create users, groups, and roles with fine-grained permission policies that control exactly which AWS services and actions each developer or system can access across all AWS products.
Amazon RDS is a fully managed relational database service for running databases such as MySQL, PostgreSQL, and Oracle in the cloud, and is a data storage service rather than a tool for controlling developer access to AWS products. Network Access Control Lists are stateless subnet-level firewalls within a VPC that control inbound and outbound network traffic based on IP address and port rules, and are a network security mechanism rather than a service for managing developer permissions across AWS products. Amazon EMR is a managed cloud big data platform for running large-scale distributed data processing jobs using frameworks such as Apache Spark and Hadoop, and is a data processing service rather than an access management solution.

## clf-c02/domain2/q258

Answer: C

Amazon Inspector automatically assesses EC2 instances for unintended network access and known software vulnerabilities by scanning network configurations and installed packages against vulnerability databases, generating prioritized findings.
Amazon Kinesis is a real-time data streaming service for ingesting, processing, and analyzing streaming data at scale, and has no capability to perform security assessments or network vulnerability scans of EC2 instances. Security groups act as stateful virtual firewalls that control which traffic is allowed to reach EC2 instances based on defined rules, and are a traffic filtering mechanism rather than a service that performs automated vulnerability assessments. AWS Network Access Control Lists are stateless subnet-level firewalls that allow or deny traffic based on IP address and port rules, and are a network traffic control mechanism rather than an assessment service that identifies vulnerabilities.

## clf-c02/domain2/q259

Answer: D, E

Physical controls such as data center physical security and hardware protection, and environmental controls such as power, cooling, and fire suppression, are entirely managed by AWS and fully inherited by customers who have no access to or responsibility for these areas.
Patch management is a shared control where AWS patches the underlying infrastructure and managed services, while customers retain responsibility for patching their own operating systems and applications. Database controls are a shared control where AWS manages the database engine in fully managed services, while customers remain responsible for access management, schema design, and data handling. Awareness and training is a shared control where AWS trains its own employees, while customers are independently responsible for training their own staff on security and compliance practices.

## clf-c02/domain2/q269

Answer: B, E

Security groups are stateful instance-level firewalls that can block unwanted traffic before it reaches EC2 instances, and Network ACLs are stateless subnet-level controls that can block volumetric attack traffic at the network perimeter. Both can help protect EC2 instances from DDoS traffic.
AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys within the AWS Cloud, and is a key management service with no capability to block or mitigate DDoS traffic targeting EC2 instances. AWS Batch is a fully managed batch computing service that dynamically provisions compute resources for batch jobs, and is a job scheduling and compute service with no network traffic filtering or DDoS protection capability. AWS IAM manages user permissions and access to AWS services and resources, and is an identity and access management service rather than a network defense tool that can block DDoS traffic.

## clf-c02/domain2/q280

Answer: A, E

Network ACLs are stateless subnet-level firewalls that evaluate all inbound and outbound traffic based on numbered rules, and security groups are stateful instance-level firewalls that control traffic to and from EC2 instances. Both are used to control network traffic in AWS.
Key pairs are RSA public/private key combinations used to authenticate SSH connections to EC2 instances, and are an instance access credential rather than a network traffic control mechanism. Access keys consisting of an access key ID and secret access key are used to authenticate programmatic API calls to AWS services, and are an API authentication credential rather than a tool for controlling network traffic within a VPC. IAM policies are JSON documents that define permissions for users, groups, and roles to access AWS services and resources, and operate at the API authorisation layer rather than controlling IP-level network traffic flow.

## clf-c02/domain2/q292

Answer: B

AWS decommissions storage devices using industry-standard techniques such as DoD 5220.22-M or NIST 800-88 to ensure that data cannot be recovered from retired hardware, fulfilling their security of the cloud obligations under the shared responsibility model.
AWS does not sell old storage devices to other hosting providers, as doing so would create an unacceptable risk of data exposure; decommissioned devices are physically destroyed or securely wiped following strict protocols before disposal. AWS does not use third-party audits to verify data removal on old devices; rather, AWS performs the decommissioning itself using documented internal processes and the resulting policies and certifications are available to customers through AWS Artifact. AWS does not return old storage devices to the hardware vendors for resale, as the devices contain customer data that must be securely destroyed before any transfer outside AWS's direct control.

## clf-c02/domain2/q293

Answer: B, D

AWS Certificate Manager is the primary service for provisioning, managing, and deploying SSL/TLS certificates for use with AWS services such as CloudFront and Elastic Load Balancing. AWS IAM also supports uploading and storing SSL server certificates that can be deployed to services not yet supported by ACM, making both valid options.
Amazon Route 53 is a DNS and domain registration service that manages how traffic is routed to resources, and has no capability to provision or deploy SSL certificates. AWS Directory Service is a managed Microsoft Active Directory service used for identity management, and is unrelated to SSL certificate provisioning. AWS Config is a compliance and configuration monitoring service that tracks resource configuration changes, and does not provision or deploy SSL certificates.

## clf-c02/domain2/q295

Answer: B, D

After migrating to AWS Lambda, AWS takes full responsibility for capacity management by automatically scaling functions based on demand, and for operating system maintenance as Lambda runs entirely on AWS-managed infrastructure with no customer access to the underlying OS.
Application management remains the customer's responsibility after migration, as customers are always accountable for the code they write, deploy, and maintain within their Lambda functions. Access control remains the customer's responsibility, as customers must configure IAM roles, permissions, and resource policies to control who and what can invoke their Lambda functions. Data management remains the customer's responsibility, as customers control what data their functions process, where it is stored, and how it is handled throughout its lifecycle.

## clf-c02/domain2/q300

Answer: C

AWS Identity and Access Management allows administrators to create users, groups, roles, and policies that control who can access which AWS services and resources, making it the primary service for managing user permissions in AWS.
AWS Key Management Service creates and manages cryptographic keys for encrypting and decrypting data, and is a data protection service rather than an access permission management tool for controlling which users can access AWS resources. AWS CloudTrail records all API calls and management events for auditing and compliance purposes, providing visibility into who did what and when, but it records activity rather than managing or enforcing user permissions. Amazon CloudWatch monitors operational metrics and events for AWS resources and applications, providing observability into performance and operational health, but has no capability to manage user access permissions to AWS services.

## clf-c02/domain2/q302

Answer: C

AWS CloudTrail records every API call made in your AWS account, including the identity of the caller, timestamp, and parameters, making it the primary service for tracking resource changes via API history.
AWS Config tracks the configuration state of AWS resources over time and evaluates them against compliance rules, but it records configuration changes rather than the underlying API calls that caused them. Amazon CloudWatch is a monitoring and observability service that collects metrics, logs, and alarms from AWS resources, and does not record API call history or track who made changes to resources. AWS CloudFormation is an infrastructure-as-code service that provisions and manages AWS resources through templates, and does not record or track API call history across an account.

## clf-c02/domain2/q305

Answer: C

AWS recommends rotating access keys regularly to limit the window of exposure if a key is ever compromised, as shorter-lived credentials reduce the risk of unauthorised access going undetected.
Deleting all access keys and using passwords instead is not a valid approach, as passwords are used for console access while access keys are required for programmatic access through the CLI and API, and both have legitimate roles in a well-managed AWS account. Sharing access keys only with trusted people still violates the principle of least privilege, as access keys should be scoped to individual IAM users or roles rather than shared between people. Saving access keys within application code is a significant security risk as code repositories can be exposed publicly or internally, and AWS recommends using IAM roles for applications running on AWS resources instead of embedding credentials in code.

## clf-c02/domain2/q306

Answer: D

AWS IAM Multi-Factor Authentication adds a second verification layer requiring a one-time code from a hardware or virtual device on top of the username and password, providing an additional authentication factor that significantly increases account security.
Encryption is a data protection mechanism used to secure data at rest or in transit, and while it protects the confidentiality of stored information, it does not add an authentication layer on top of username and password for account login. AWS Access Advisor shows which AWS services IAM users and roles have accessed and when, helping administrators reduce permissions to only those actually used, but it is a permissions visibility tool rather than an authentication security mechanism. Least privilege access is a permissions management principle that involves granting users only the minimum permissions needed for their tasks, reducing the blast radius of compromised credentials, but it does not add an additional authentication factor on top of the login process.

## clf-c02/domain2/q312

Answer: C, D

For fully managed services like Amazon DynamoDB, AWS is responsible for patching the database software and maintaining the underlying operating system, as customers have no access to the infrastructure layer beneath the service.
Protecting credentials is the customer's responsibility, as customers manage their own IAM users, access keys, and authentication mechanisms. Logging access activity is the customer's responsibility, as customers must enable and configure AWS CloudTrail and DynamoDB Streams if they want to capture access logs. Creating access policies is the customer's responsibility, as customers define and manage the IAM policies that control who can access their DynamoDB tables and what actions they can perform.

## clf-c02/domain2/q316

Answer: D

AWS CloudTrail records all API calls and management events in an AWS account including S3 bucket deletion events, capturing who performed the action, the source IP address, and the timestamp, making it the correct service for identifying who deleted the buckets.
SNS logs is not a recognized AWS service or log type; Amazon SNS is a messaging service for sending notifications and does not produce logs of S3 API activity or deletion events. SQS logs is not a recognized AWS service or log type; Amazon SQS is a managed message queue service for decoupling application components and does not produce logs of S3 management activity. CloudWatch Logs collects and stores log data from AWS services and applications for monitoring and analysis, but S3 bucket deletion events are management events captured by CloudTrail rather than CloudWatch, making CloudWatch Logs the wrong place to identify who deleted S3 buckets.

## clf-c02/domain2/q319

Answer: D

Shared controls are responsibilities where both AWS and the customer independently apply controls in their own respective domains, such as AWS patching its infrastructure while the customer patches their guest operating system.
Controls solely the responsibility of the customer describes customer-specific controls, not shared controls, as these apply only to the customer's side of the model. Controls that a customer inherits from AWS describes inherited controls, where compliance certifications and physical security measures are passed down from AWS to the customer, which is a separate category from shared controls. Controls that apply to both the infrastructure and customer layers is a misleading description because shared controls do not mean the same single control applies at both layers, but rather that each party manages their own version of the same type of control independently.

## clf-c02/domain2/q321

Answer: A, E

Customers using Amazon EC2 are responsible for managing user access to their EC2 instances, including configuring operating system users and SSH keys, and for protecting data at rest and in transit on those instances through encryption and access controls.
Preventing physical access to EC2 hardware is AWS's responsibility as customers have no access to or visibility into the physical data center facilities where EC2 instances run. Patching the network infrastructure is AWS's responsibility as the underlying physical and virtual networking components that connect EC2 instances are managed and maintained entirely by AWS. Managing the hypervisor is AWS's responsibility as the virtualization layer that abstracts physical hardware into EC2 instances is part of the AWS infrastructure that customers cannot access or modify.

## clf-c02/domain2/q323

Answer: A, E

Amazon Inspector automatically assesses applications for vulnerabilities and deviations from best practices, and AWS Config continuously monitors resource configurations and evaluates them against compliance rules. Both are purpose-built for security analysis and regulatory compliance auditing.
AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance, but offers high-level checks and guidance rather than the deep automated security assessments and compliance rule evaluation that Inspector and Config provide. AWS Batch is a managed service for running batch computing workloads at scale, and is a job scheduling and compute service with no security analysis or compliance auditing capability. Amazon ECS is a container orchestration service that manages the deployment and scaling of containerised applications, and is a compute service with no security analysis or compliance auditing capability.

## clf-c02/domain2/q332

Answer: A, C

Amazon S3 versioning retains multiple versions of objects, protecting against accidental deletion and allowing restoration of previous versions, and S3 permissions through IAM policies and bucket policies control who can access and modify objects. Both help protect data at rest on Amazon S3.
Deduplication is a storage optimization technique that removes duplicate copies of data to save space, and is not a data protection mechanism for Amazon S3; S3 does not expose deduplication as a security feature. Decryption is the process of converting encrypted data back to its original form, and while decryption is part of an encryption workflow, enabling decryption alone does not protect data at rest and is not a data protection mechanism for S3. Conversion refers to changing data formats or types, and has no relevance to protecting data stored in Amazon S3.

## clf-c02/domain2/q336

Answer: C, E

Data center operations including physical facility management, power, cooling, and hardware decommissioning, and infrastructure security including the physical and virtual networking, hypervisor, and server hardware, are entirely AWS's responsibility and are not tasks the customer performs.
Running penetration tests is the customer's own responsibility; AWS allows customers to conduct penetration testing on their own resources following the Acceptable Use Policy, but the decision to run tests and the tests themselves are not something AWS performs for customers. Reserving capacity, such as purchasing Reserved Instances or Savings Plans for predictable workloads, is a customer decision and action taken to optimize costs rather than an AWS-managed task. Auditing and regulatory compliance is a shared responsibility; AWS provides compliance reports and certifications through AWS Artifact, but customers are responsible for applying those to their own applications and ensuring their workloads meet regulatory requirements.

## clf-c02/domain2/q341

Answer: A

AWS Key Management Service lets you create, manage, and control cryptographic keys used to encrypt your data across AWS services, providing centralized key management with audit logging via CloudTrail.
AWS Service Control Policies are organizational policies used within AWS Organizations to restrict the maximum permissions available to accounts in an organization, and are an access governance tool rather than a key management service for encryption keys. Multi-Factor Authentication adds a second verification factor to the login process requiring a code from a hardware or virtual device, and is an authentication security mechanism rather than a service for managing encryption keys. Amazon Macie uses machine learning to automatically discover and protect sensitive data in Amazon S3, and is a data classification and protection service rather than a key management service for creating and controlling encryption keys.

## clf-c02/domain2/q342

Answer: B

AWS Artifact is a self-service portal for on-demand access to AWS compliance reports including SOC and PCI reports, and agreement documents such as Business Associate Addenda, making it the correct service for downloading AWS SOC and PCI compliance reports.
AWS Well-Architected Tool is a service that helps you review the state of your workloads and compare them against AWS architectural best practices across the six pillars, and is a workload review and guidance tool rather than a compliance report repository. AWS Glue is a fully managed extract, transform, and load service for preparing and transforming data for analytics, and is a data integration service with no connection to compliance documentation. Amazon Chime is a unified communications service for online meetings, video conferencing, and chat, and has no relationship to compliance reports or AWS certification documents.

## clf-c02/domain2/q345

Answer: A, C

AWS offers access control through IAM policies, security groups, and network ACLs to restrict who can reach your data, and data encryption at rest and in transit to protect data even if it is intercepted or accessed without authorisation. Both are purpose-built data protection features.
Physical MFA devices add a second layer of authentication to protect account and user access, but they secure who can log in rather than directly protecting the data itself once access is granted. Unlimited storage is a capacity characteristic of services such as Amazon S3, and is a storage scaling feature with no data protection or security capability. Load balancing distributes incoming traffic across multiple targets to improve availability and performance, and is a resilience and throughput feature with no role in protecting data from unauthorised access or exposure.

## clf-c02/domain2/q348

Answer: A, C

The AWS CLI provides command-line access to IAM for creating users, assigning permissions, and managing credentials, and AWS SDKs allow programmatic integration with IAM in application code to automate identity and access management operations. Both are valid methods for interacting with IAM.
AWS Security Groups are virtual firewalls that control inbound and outbound network traffic at the EC2 instance level, and are a network security component rather than a method for interacting with IAM. AWS Network Access Control Lists are stateless firewalls that control traffic at the subnet level within a VPC, and are a network traffic filtering mechanism rather than an interface for managing IAM identities or permissions. AWS CodeCommit is a fully managed source control service for hosting Git repositories, and is a code collaboration tool with no connection to interacting with IAM beyond using IAM for access control.

## clf-c02/domain2/q349

Answer: C, D

IAM Users represent individual people or applications with specific credentials and permissions, and IAM Roles provide temporary security credentials that can be assumed by users, services, or AWS resources. Both are types of IAM identities.
AWS Resource Groups organize AWS resources by tags or CloudFormation stacks to make it easier to manage and automate operations across groups of resources, and are not IAM identities that can be used for authentication or permission assignment. IAM Policies are JSON documents that define permissions specifying allowed or denied actions on AWS resources, and are permission documents attached to identities rather than identity types themselves. AWS Organizations is a service for managing multiple AWS accounts under a central structure for consolidated billing and governance, and is an account management service rather than an IAM identity type.

## clf-c02/domain2/q351

Answer: B

AWS publishes Security Bulletins to notify customers about security and privacy events affecting AWS services, providing details on vulnerabilities and recommended actions.
AWS Certificate Manager is a service that provisions and manages SSL/TLS certificates for use with AWS resources, and is not a channel through which AWS communicates security or privacy event notifications to customers. The AWS Management Console is a web-based interface for accessing and managing AWS services, and while customers can view some account-level alerts there, it is not the mechanism AWS uses to publish security and privacy event notifications. AWS Compliance Resources are documents and reports such as audit certifications and compliance guides that help customers understand AWS's regulatory posture, and are not used to notify customers about specific security or privacy events.

## clf-c02/domain2/q352

Answer: C

IAM Roles provide temporary security credentials that expire automatically, making them the best choice for granting short-term or temporary access to AWS resources without sharing long-term credentials.
IAM Users are identities with permanent, long-term credentials such as passwords and access keys, and while permissions can be granted or revoked, users themselves represent persistent identities rather than a mechanism designed specifically for temporary access. Key pairs are RSA public/private key combinations used to authenticate SSH connections to EC2 Linux instances, and are an instance access mechanism rather than an IAM feature designed for granting temporary access to AWS services and resources. IAM Groups are collections of IAM users that share the same attached policies, and are used to manage permissions for multiple users collectively rather than for granting temporary access to any single entity.

## clf-c02/domain2/q355

Answer: C

Requiring MFA for all IAM users adds a second verification step beyond a password, significantly reducing the risk of unauthorised access even if a user's password is stolen or guessed, making it an effective control for securing the AWS account.
Restricting all API calls through SDKs or CLI would completely prevent programmatic and automated access to AWS services, making it operationally unworkable for development and automation workflows rather than a practical security measure. Creating a single IAM account per department shared across all staff removes individual accountability, makes it impossible to trace actions to specific users, and means a single compromised password grants access to everyone in the department, making this a security anti-pattern rather than a security improvement. Setting up two login passwords is not a feature AWS supports; AWS accounts use a single password for console access, and improved security beyond the password is achieved through MFA rather than multiple passwords.

## clf-c02/domain2/q361

Answer: A, E

Building an application schema is an application development task that customers perform as part of managing their applications in the cloud, and encrypting file systems on EC2 instances to protect data at rest is a customer responsibility for security in the cloud. Both fall within the customer's side of the shared responsibility model.
Replacing physical hardware is entirely AWS's responsibility as customers have no access to or interaction with the physical servers, storage devices, and networking equipment in AWS data centers. Creating a new hypervisor is AWS's responsibility as the virtualization layer that abstracts physical hardware into virtual instances is part of the AWS-managed infrastructure that customers cannot access or modify. Patch management of the underlying infrastructure, including the host operating systems, hypervisor, and physical network equipment, is AWS's responsibility, whereas customers are responsible for patching the guest operating system on their own EC2 instances.

## clf-c02/domain2/q362

Answer: B

A U2F Security Key is a physical hardware device that authenticates via USB or NFC using cryptographic protocols, providing a hardware-based second factor for AWS MFA that protects accounts from phishing and credential theft.
AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys for data encryption, and is a key management service rather than an MFA device used to authenticate AWS account logins. AWS Access Keys consisting of an access key ID and secret access key are credentials used for programmatic API and CLI access, and are a programmatic authentication mechanism rather than an MFA device that adds a second factor to console login. AWS Key Pairs are RSA public/private key combinations used to authenticate SSH connections to Linux EC2 instances, and are an instance-level access mechanism rather than an MFA device for AWS account authentication.

## clf-c02/domain2/q367

Answer: D

By default, new IAM users have no permissions attached to them, meaning all actions are implicitly denied until explicit permissions are granted through policies, which is why the new administrator cannot create EBS snapshots or S3 buckets.
EBS and S3 are not accessible only to the root account owner; they can be accessed by any IAM user, group, or role that has been granted the appropriate permissions through IAM policies, making this statement factually incorrect. A new IAM user does not need to contact AWS Support to activate their account; IAM users are created and active immediately, and the issue is the absence of permissions rather than an account activation requirement. There is no inherent storage limit in S3 that would prevent creating a new bucket for snapshots; S3 scales automatically to accommodate any amount of data, and the inability to create the bucket is due to missing permissions rather than a storage capacity issue.

## clf-c02/domain2/q368

Answer: A

AWS CloudTrail records all API calls and management events in an AWS account including who accessed which resources, from what IP address, and at what time, providing exactly the information an auditor needs to review access logs.
Amazon CloudFront is a content delivery network that caches and distributes web content to users at low latency through edge locations, and is a performance optimization service with no capability to log all accesses to AWS account resources. AWS CloudFormation is an infrastructure as code service for provisioning and managing AWS resources through templates, and is a provisioning and automation tool rather than a service that records access logs to AWS resources. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and while it can collect application logs and service metrics, it does not provide the comprehensive API call audit trail that records all AWS resource accesses the way CloudTrail does.

## clf-c02/domain2/q369

Answer: B

AWS Directory Service provides managed Microsoft Active Directory in the AWS Cloud, allowing organizations to connect their AWS resources with an existing on-premises Active Directory so users can access AWS applications using their established corporate credentials.
AWS IAM Identity Center provides single sign-on access to multiple AWS accounts and business applications, but does not provide the managed directory infrastructure needed to extend on-premises Active Directory into AWS. Amazon Cognito provides user identity and authentication for customer-facing web and mobile applications, and is not designed for corporate directory integration with AWS resources. AWS Secrets Manager stores, rotates, and retrieves credentials and secrets programmatically, but does not manage directory services or user authentication against Active Directory.

## clf-c02/domain2/q375

Answer: B

AWS Certificate Manager lets you provision, manage, and deploy SSL/TLS certificates for use with AWS services such as Elastic Load Balancers and CloudFront distributions, offering free public certificates that renew automatically.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and has no capability to provision or manage SSL/TLS certificates. Amazon Detective helps analyze and visualise security data to investigate the root cause of suspicious activity, providing forensic investigation capabilities rather than SSL/TLS certificate provisioning. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block common web exploits, and is a traffic filtering service rather than a certificate provisioning service.

## clf-c02/domain2/q380

Answer: C

For a specific employee requiring long-term access, an IAM user is the appropriate identity type, and attaching a policy scoped only to Amazon DynamoDB follows the principle of least privilege by granting only the permissions needed for that role.
Creating an IAM role and attaching DynamoDB access permissions would be appropriate for applications or services that need temporary access to DynamoDB, but for a specific long-term employee, an IAM user is the correct identity type rather than a role designed for temporary credential assumption. Creating an IAM role with Administrator access permissions would grant the new employee unrestricted access to all AWS services and resources, violating the principle of least privilege and posing an unnecessary security risk. Creating an IAM user with Administrator access permissions would grant unrestricted access to all AWS services rather than scoping permissions to only Amazon DynamoDB, directly violating the principle of least privilege.

## clf-c02/domain2/q381

Answer: C

IAM Roles provide temporary security credentials that are automatically rotated when assumed, eliminating the need to embed long-term access keys in application code and reducing the risk of credential exposure if the application is compromised.
Generating new IAM access keys every time permissions are delegated would result in a large number of static, long-term credentials that must be tracked and managed, increasing the risk of credential exposure rather than reducing it, and is not a security best practice for applications on EC2. Storing required AWS credentials directly in application code is a serious security anti-pattern that risks credential exposure through code repositories, log files, or application errors, making it the opposite of a best practice. Applications running on EC2 frequently need to interact with other AWS services such as S3, DynamoDB, or SQS to function correctly, making the assumption that no permissions are needed factually incorrect for most real-world applications.

## clf-c02/domain2/q384

Answer: B, C

Virtual MFA can be enabled through AWS IAM, which provides the console interface for assigning and configuring MFA devices for users, and through the AWS CLI, which allows MFA settings to be managed programmatically.
Amazon Connect is a cloud-based contact center service for handling customer communications, entirely unrelated to authentication or MFA configuration. Amazon SNS is a notification service for sending messages to subscribers and has no role in enabling or managing MFA. Amazon VPC is a virtual private network service for isolating and configuring cloud network infrastructure, unrelated to user authentication settings.

## clf-c02/domain2/q387

Answer: D, E

If unrecognized resources appear in your AWS account, this may indicate a security compromise where an attacker has gained access and is creating resources, so you should change your root account password and access keys immediately to revoke the attacker's access and protect the account.
Closing the account immediately would permanently terminate all resources and data without first investigating the extent of the compromise or recovering any workloads, making it a disproportionate response before proper incident response steps have been completed. Removing all IAM users from the account would lock out your legitimate team members and prevent any investigation or remediation work from being performed, making incident response significantly harder without actually addressing the underlying security compromise. Opening a new root account does not address the compromised account, as the original account with its resources and data would still be exposed; incident response requires securing the existing account rather than abandoning it.

## clf-c02/domain2/q395

Answer: C

Amazon Cognito supports federated identity authentication, allowing users to sign in with their existing Amazon, Apple, Facebook, or Google accounts and exchange those tokens for AWS credentials, making it the correct service for social identity provider integration.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is not a service for enabling user authentication with social identity providers. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and SSO with corporate credentials, and is designed for workforce identity rather than customer-facing social identity provider authentication. AWS IAM manages user identities and permissions for accessing AWS services and resources, and while IAM can grant permissions to users authenticated through Cognito, it does not itself handle federated sign-in with Amazon, Apple, Facebook, or Google.

## clf-c02/domain2/q403

Answer: A

The AWS account owner holds the root user credentials and has full administrative access to all resources in the account, making them the only entity with the authority to grant full administrative permissions to other users or teams through IAM policies.
An AWS Technical Account Manager is an AWS employee assigned to help Enterprise support plan customers with architectural guidance and support, and does not have the ability to grant permissions within a customer's AWS account. The AWS Security team manages AWS's own internal security posture and is not involved in configuring IAM permissions within individual customer accounts. AWS Cloud Support Engineers provide technical support for resolving issues and answering questions about AWS services, and do not have access to configure IAM policies or grant permissions within customer accounts.

## clf-c02/domain2/q410

Answer: B

AWS shared responsibility means the customer is responsible for securing what runs on EC2, including the operating system and applications, which requires regularly applying security patches to close vulnerabilities that could be exploited by attackers.
Instance store volumes provide temporary, high-speed local storage that is deleted when the instance stops or is terminated, making them inappropriate for storing login data that must persist across instance restarts or replacements. Deploying critical application components in a single trusted Availability Zone reduces fault tolerance and does not improve security; best practice is to distribute across multiple Availability Zones for resilience, and no AZ is inherently more trusted than another within the same region. Amazon Athena is a serverless query service for analyzing data stored in S3 using SQL, and does not track API calls; AWS CloudTrail is the correct service for recording API activity across an AWS account.

## clf-c02/domain2/q414

Answer: A

Deleting root user access keys removes a persistent attack vector, since the root account has unrestricted access to all AWS services and resources, and AWS best practice recommends using IAM users for daily tasks and eliminating root access keys entirely to protect the account.
Applying MFA for the root account is correct but the second part of the option is wrong; AWS recommends enabling MFA on the root account but using it as infrequently as possible and relying on IAM users for day-to-day work, not using the root account for all tasks. Accessing the root account only from a personal mobile phone does not constitute a recognized security control; MFA using an authenticator app on a mobile device is recommended, but restricting access to a specific physical device is not an AWS security best practice and introduces its own risks. Sharing your AWS account password or access keys with trusted persons violates fundamental security principles; credentials should never be shared as this removes individual accountability and increases the risk of credential exposure.

## clf-c02/domain2/q416

Answer: B

The Principle of Least Privilege means granting each IAM user only the minimum permissions necessary to perform their assigned job functions, reducing the impact of any accidental or malicious use of credentials.
Attaching a separate IAM policy to each individual account is a valid approach for highly differentiated permissions but is operationally complex; using IAM groups to assign shared policies to all DevOps team members with similar roles is the recommended approach for teams rather than managing policies per user individually. For security purposes, you should not withhold all permissions from the DevOps team; the team needs appropriate permissions to perform their infrastructure management tasks, and the goal is to define those permissions carefully rather than provide none at all. Creating six different IAM passwords involves setting distinct password requirements per user, but password variation does not address the core security concern of permission scope; applying least privilege principles to what each user is allowed to do is the AWS recommendation.

## clf-c02/domain2/q424

Answer: A, D

AWS Config continuously monitors and records resource configurations to evaluate compliance against desired rules, and AWS Trusted Advisor provides real-time checks across security, performance, cost, and fault tolerance categories. Both provide real-time auditing capabilities.
Amazon Redshift is a fully managed cloud data warehouse service for running analytical queries on large datasets, and is a data analytics service rather than a real-time auditing tool for compliance or vulnerability assessment. Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that enables application messaging and decoupling, and is a messaging infrastructure service with no auditing or compliance checking capability. Amazon Cognito is a user identity and authentication service for web and mobile applications that handles sign-up, sign-in, and access control, and is an identity service rather than a compliance auditing or vulnerability assessment tool.

## clf-c02/domain2/q428

Answer: B

Penetration testing is the practice of simulating cyberattacks against your own systems to discover exploitable security vulnerabilities before malicious attackers can find and use them, allowing you to remediate weaknesses proactively.
Testing application response time from different locations describes performance and latency testing, which evaluates how quickly an application responds to requests from various geographic locations rather than identifying security vulnerabilities that attackers could exploit. Testing instances to check for unhealthy ones describes health checking or monitoring, which verifies that compute instances are operational and responsive rather than assessing the security posture of the network for exploitable weaknesses. Testing software for bugs and errors describes functional or quality assurance testing, which validates that code behaves as expected rather than specifically probing for security vulnerabilities that an attacker could use to gain unauthorised access.

## clf-c02/domain2/q443

Answer: C, D

Enabling S3 encryption through server-side encryption with S3-managed keys, KMS keys, or customer-provided keys protects object confidentiality at rest, and encrypting data before uploading it provides client-side encryption that ensures data is protected before it ever leaves the client. Both are valid approaches to securing sensitive data in Amazon S3.
Deleting encryption keys once data is encrypted would permanently prevent decryption of the stored data, making it impossible to read or use the data again; encryption keys must be retained and managed carefully to ensure continued access to encrypted data. AWS does not automatically handle all security concerns by default; customers are responsible for configuring appropriate encryption, access controls, and bucket policies to protect their data, as the shared responsibility model requires active customer participation in data security. Deleting all IAM users with access to S3 would prevent all legitimate users from accessing the data and disrupt normal operations; proper access control involves granting least privilege permissions to the appropriate users rather than eliminating all access.

## clf-c02/domain2/q450

Answer: A

AWS Artifact provides on-demand, self-service access to AWS compliance reports and auditor-issued certifications such as SOC, PCI DSS, and ISO documents, directly from the AWS Management Console without needing to contact AWS support.
AWS Config continuously monitors and records resource configurations against compliance rules to help manage configuration drift and evaluate resource compliance, and is a resource configuration compliance tool rather than a repository of AWS auditor-issued certifications. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications to support observability and alerting, and has no connection to providing access to AWS compliance reports or third-party audit certifications. AWS CloudTrail records all API calls and management events across an AWS account for auditing and security analysis, and produces customer-specific activity logs rather than auditor-issued AWS compliance certifications.

## clf-c02/domain2/q455

Answer: A

EC2 Dedicated Hosts provide physical servers fully dedicated to your use, giving you visibility and control over instance placement on hardware that is not shared with other AWS customers, satisfying strict compliance and regulatory requirements for physical isolation.
EC2 Reserved Instances are a pricing model that provides a significant discount in exchange for a commitment to use a specific instance type for one or three years, and they do not guarantee that the underlying hardware is dedicated to a single customer; reserved instances can run on shared multi-tenant hardware. EC2 Spot Instances allow you to use spare AWS capacity at a reduced price, with the caveat that they can be interrupted when AWS needs the capacity back, and they do not provide dedicated physical hardware or compliance guarantees about hardware isolation. EC2 On-Demand Instances allow you to pay for compute capacity by the hour or second without any upfront commitments, and they run on shared multi-tenant hardware rather than dedicated servers, making them unsuitable for compliance requirements mandating physical hardware dedication.

## clf-c02/domain2/q458

Answer: D

An IAM Policy is a JSON document that defines permissions by specifying allowed or denied actions on AWS resources, and can be attached directly to an IAM user to grant specific access rights.
IAM Identity is not a standalone IAM construct used to assign permissions; AWS IAM Identity Center is a separate service for managing workforce access across multiple accounts, and does not refer to a permission assignment mechanism within IAM itself. An IAM Group is a collection of IAM users that share the same attached policies, and while attaching a policy to a group affects all its members, the group itself is not what assigns permissions directly to an individual user. An IAM Role is an identity that defines a set of permissions and is assumed temporarily by users, services, or applications, and is not attached directly to a user the way a policy is.

## clf-c02/domain2/q463

Answer: A, E

AWS KMS provides centralized software-based key management with AWS-managed infrastructure and integrates natively with most AWS services for encryption at rest, and AWS CloudHSM provides dedicated hardware security modules for customers requiring hardware-based key control for regulatory compliance. Both are valid services for managing encryption keys in the AWS Cloud.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a key management service for creating and storing encryption keys. AWS CodeDeploy is an automated deployment service that delivers application code to EC2 instances, Lambda functions, and on-premises servers, and is a deployment automation tool with no encryption key management capability. AWS CodeCommit is a fully managed source control service for hosting Git repositories for version-controlled code storage, and is a code collaboration tool rather than an encryption key management service.

## clf-c02/domain2/q466

Answer: A

AWS Identity and Access Management is the service that provides centralized control over authentication and authorisation for AWS resources, fulfilling the same identity management role in the cloud that an on-premises operations team performs in a traditional data center.
AWS Outposts extends AWS infrastructure and services to on-premises locations and is a compute and storage solution rather than an identity management service. AWS Directory Service provides managed Microsoft Active Directory integration for enterprise identity, which can complement IAM but is a specialized service for organizations needing AD integration rather than the core AWS identity management service. Amazon Redshift is a fully managed cloud data warehousing service designed for analytical queries on large datasets and has no capability to manage user identities or control access to AWS services.

## clf-c02/domain2/q468

Answer: B

The IAM credential report provides a comprehensive list of all IAM users in an AWS account along with the status of their credentials including passwords, access keys, MFA status, and last used dates, making it the correct tool for auditing user credentials.
AWS Trusted Advisor provides automated checks across security, performance, cost, and fault tolerance categories and includes some IAM-related security checks, but does not generate a downloadable report listing all users and their individual credential status details. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and has no capability to list IAM users or report on the status of their credentials such as access keys and MFA devices. AWS CloudTrail records all API calls and management events for auditing purposes, and while it logs IAM-related actions, it does not provide a consolidated report of all current users and the live status of their credentials.

## clf-c02/domain2/q469

Answer: C

AWS CloudHSM provides dedicated, single-tenant hardware security modules in the AWS Cloud, giving you full control over encryption key generation and management with FIPS 140-2 Level 3 validated hardware for customers requiring hardware-based key control.
AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to generate or manage encryption keys. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service rather than a general-purpose encryption key generation service. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block web exploits, and is a traffic filtering service with no capability to generate or manage customer encryption keys.

## clf-c02/domain2/q473

Answer: D

The AWS Acceptable Use Policy outlines prohibited uses of AWS services, including activities such as sending spam, hosting illegal content, or launching attacks, and applies to all AWS customers and users.
AWS Service Control Policies are permission guardrails applied within AWS Organizations to restrict what actions accounts can perform, not a document describing prohibited uses of AWS services to external customers. AWS Artifact is a self-service portal for accessing AWS compliance reports and security documentation such as SOC reports and ISO certifications, not a resource for understanding usage restrictions. AWS Budgets is a cost management tool for setting spending thresholds and receiving alerts, unrelated to acceptable use or prohibited activities.

## clf-c02/domain2/q474

Answer: A, D

AWS documentation provides comprehensive technical guides and API references for all AWS services at no cost and is freely accessible to any user, and AWS discussion forums allow any user to post questions and share knowledge about AWS services at no charge. Both are free security resources.
AWS Support Center provides technical case support that requires a paid support plan to submit cases, and while some basic content is available for free, the case submission feature for getting direct engineering assistance is not a free resource available to all users without a qualifying support plan. AWS Managed Services provides ongoing management of AWS infrastructure on behalf of enterprise customers for a fee, and is a paid service rather than a free security resource available to any user. Amazon Inspector is an automated vulnerability assessment service that requires configuration and generates findings, and while there is a free trial period, it is a paid service rather than a free resource available to all users without any cost.

## clf-c02/domain2/q476

Answer: A

Under the Shared Responsibility Model, AWS is responsible for securing the physical infrastructure, including Regions, Availability Zones, and edge locations that make up the AWS global network.
Performing auditing tasks is the customer's responsibility. Customers are responsible for auditing their own resource usage, access logs, and compliance activities. Monitoring AWS resources usage is the customer's responsibility. Tools like CloudWatch are available but it is the customer who configures and acts on monitoring. Securing access to AWS resources is the customer's responsibility. Managing IAM users, roles, and permissions falls under security in the cloud, not security of the cloud.

## clf-c02/domain2/q479

Answer: C

AWS CloudHSM provides dedicated, single-tenant hardware security modules within the AWS Cloud, giving customers full control over key generation and management on physical HSM hardware that only they can access, satisfying strict regulatory requirements for hardware-based key custody.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials, API keys, and OAuth tokens, and is a secrets management service rather than a service for generating customer-controlled encryption keys on dedicated hardware. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to encrypt data in transit, and is a certificate management service that does not provide customer-controlled encryption keys on dedicated hardware. AWS KMS is a managed service that generates and manages encryption keys using a software-based service backed by hardware that AWS manages and shares across multiple customers, and does not provide the dedicated single-tenant hardware access that CloudHSM offers.

## clf-c02/domain2/q480

Answer: C

Amazon DynamoDB is a fully managed NoSQL database service where AWS handles all scaling automatically, including read and write capacity adjustments, so customers do not need to manage or plan for database scaling themselves.
The customer's security team focuses on security policies, access controls, and compliance rather than the operational scaling of a managed database service, and DynamoDB's autoscaling is handled by AWS infrastructure rather than any customer team. The development team builds and maintains application code, and while they configure DynamoDB table settings during development, the actual scaling of a fully managed service is performed automatically by AWS rather than manually by developers. The internal DevOps team manages infrastructure, deployments, and operational workflows, but the scaling of a fully managed service like DynamoDB is handled automatically by AWS and does not require DevOps intervention.

## clf-c02/domain2/q487

Answer: A

Identity federation allows users to sign into AWS using credentials from an external identity provider such as Active Directory or SAML, eliminating the need to create separate IAM users for each corporate employee.
Access keys are long-term credentials consisting of an access key ID and secret used for programmatic access to AWS via the CLI or API, and are not a mechanism for signing into AWS with corporate credentials. IAM Permissions define what actions an authenticated user or role is allowed to perform on AWS resources, and are an authorisation mechanism rather than a feature that enables corporate credential sign-in. AWS WAF rules define conditions for filtering web traffic to protect applications from common exploits, and are a web security feature with no connection to identity or authentication.

## clf-c02/domain2/q488

Answer: C, D

Data center security controls and environmental controls are fully inherited from AWS because customers have no physical access to AWS facilities and take on zero responsibility for managing them.
Awareness and Training this is a shared control where both AWS and the customer independently maintain their own training programs for their respective workforces, so customers do not fully inherit it from AWS. Communications controls this is also a shared control, with each party responsible for securing and managing communications within their own environment. Resource Configuration Management customers are responsible for configuring the AWS resources they deploy, such as security groups, IAM policies, and application settings, making this a customer-managed control rather than an inherited one.

## clf-c02/domain2/q491

Answer: B, D

Implementing strong identity foundations through least privilege and appropriate credential management, and enabling traceability by monitoring, alerting, and auditing all actions and resource changes, are two of the seven security design principles of the Well-Architected Framework.
Using the same AWS account for all workloads in a single environment contradicts the security principle of applying security at all layers and using multiple accounts to isolate workloads, and is an anti-pattern rather than a security design principle. Replacing IAM users with API keys as the primary access mechanism would use long-term credentials for all access rather than temporary credentials through roles, which is the opposite of the principle favoring short-term credentials and role-based access. Granting root user access to all authorised users contradicts the principle of granting least privilege and protecting root account credentials, as the root user should be used minimally and its credentials never shared.

## clf-c02/domain2/q493

Answer: B

Security groups attached to an RDS instance act as a virtual firewall controlling which IP address ranges and EC2 instances are allowed to establish connections to the database, restricting network access to only authorised sources.
Managing user access and encryption keys describes AWS IAM and AWS KMS respectively, which are separate services for identity management and key management rather than functions provided by security groups attached to an RDS instance. Deploying SSL/TLS certificates for database connections is performed by AWS Certificate Manager and the RDS parameter group configuration, not by security groups, which control network connectivity rather than certificate provisioning. Distributing incoming traffic across multiple targets describes an Elastic Load Balancer, which routes requests to multiple backend instances, and is not a function of security groups attached to a database instance.

## clf-c02/domain2/q496

Answer: D

Security groups control inbound and outbound traffic at the EC2 instance level with stateful evaluation, and Network ACLs control traffic at the subnet level with stateless rule evaluation. Checking both gives a complete picture of what traffic is allowed to and from EC2 instances in the VPC.
Network ACLs and Traffic Manager is not a valid combination for VPC traffic analysis; AWS Traffic Manager does not exist as an AWS service name, and the correct subnet-level control is Network ACLs rather than a non-existent Traffic Manager. Network ACLs and Subnets is partially correct in that subnets are VPC components, but subnets themselves are network segments rather than traffic control mechanisms, and checking subnets does not tell you what traffic rules are applied; you need to check the ACLs attached to those subnets. Security groups and Internet Gateways is partially correct in that Internet Gateways allow internet traffic into the VPC, but they do not define granular allow/deny rules for instance-level traffic; checking security groups alone misses the subnet-level controls provided by Network ACLs.

## clf-c02/domain2/q499

Answer: B

Under the shared responsibility model, customers are responsible for patching and maintaining any software they install on EC2 instances, including database software, operating systems, and applications.
AWS does not manage everything related to EC2 operating systems. The guest operating system, including configuration, patching, and security, is the customer's responsibility, while AWS manages only the underlying physical infrastructure. Server-side encryption is not automatically the responsibility of AWS. Customers choose whether to enable encryption and can manage their own keys through AWS KMS, making encryption a shared responsibility depending on how it is configured. AWS is not responsible for the security of customer applications. Application-level security, including code quality, access controls, and data handling, is entirely the customer's responsibility under the shared responsibility model.

## clf-c02/domain2/q507

Answer: A, B

An IAM user is a permanent identity associated with one specific person and has long-term credentials such as a password and access keys, while an IAM role provides temporary credentials and can be assumed by multiple users, services, or applications that need it.
The option stating that a role is uniquely associated with only one person and a user is assumable by anyone reverses the correct relationship; IAM users represent individual people with their own credentials, while roles are designed to be assumed by anyone or any service that requires the permissions they define. The option stating that IAM users have temporary credentials and roles have permanent credentials is the opposite of the correct relationship; IAM users have long-term permanent credentials while roles issue temporary credentials that expire automatically when the session ends. IAM users and roles are not priced differently from each other; there is no direct cost associated with creating IAM users or roles, and the claim that users are more cost effective is not a meaningful comparison.

## clf-c02/domain2/q509

Answer: B

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads using machine learning and threat intelligence to identify suspicious activity such as attacker reconnaissance, compromised instances, or unusual API calls.
Notifying customers about abuse events once they are reported is the function of the AWS Abuse Team, which handles reports of AWS resources being used for malicious activity and communicates with affected account holders, rather than a capability of GuardDuty. Helping customers identify the root cause of potential security issues describes Amazon Detective, which analyzes and visualises security data from GuardDuty and CloudTrail to trace the origin and scope of suspicious activity rather than detecting threats in real time. Checking security groups for rules that allow unrestricted access to AWS resources is a function of AWS Trusted Advisor, which performs security checks including identification of overly permissive security group configurations, not GuardDuty.

## clf-c02/domain2/q516

Answer: B, D

IAM users and the AWS account root user are both identities that can be issued long-lived access key IDs and secret access keys for programmatic access to AWS resources via the CLI or SDKs.
An IAM group is a collection of IAM users used to manage shared permissions collectively, and is not an identity that can authenticate or be issued access keys of any kind. An IAM role uses temporary security credentials that are automatically issued and rotated when the role is assumed, and does not support long-lived access keys. An AWS Technical Account Manager is an AWS support professional assigned to Enterprise support plan customers, and is a person rather than an IAM identity construct that can hold or be issued access keys.

## clf-c02/domain2/q523

Answer: D

Amazon CloudFront integrates natively with AWS Shield for DDoS protection at the network layer and with AWS WAF for application-layer traffic filtering, providing a layered defense against both network and application layer DDoS attacks at the edge.
Amazon EFS is a fully managed elastic file system for providing shared file storage to EC2 instances and other compute services, and is a storage service with no capability to integrate with Shield or WAF for DDoS protection. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service rather than a service that integrates with Shield and WAF for traffic protection. AWS Systems Manager provides operational tools for managing AWS resources at scale including patching, configuration management, and session management, and is an operations service rather than a content delivery or traffic filtering service.

## clf-c02/domain2/q524

Answer: B

AWS KMS manages the encryption keys used for EBS volume encryption, handling key creation, storage, rotation, and access control, integrating transparently with EBS to encrypt data at rest.
AWS WAF is a web application firewall that filters HTTP and HTTPS traffic to block common web exploits such as SQL injection and cross-site scripting, and is a traffic filtering service with no role in managing encryption keys for EBS volumes. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification service for S3 rather than a key management service for EBS encryption. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and is a security monitoring service rather than a key management service for encrypting EBS volumes.

## clf-c02/domain2/q525

Answer: D, E

Rotating all access keys immediately invalidates any keys the former administrator may have copied or retained, and changing the root account email and password with MFA enabled prevents root-level access using any credentials the administrator may have had.
Downloading attached policies to a safe place does not address the immediate security risk; the priority is to revoke the former administrator's access rather than preserving policy documentation, and policies can be reviewed from the console at any time. Deleting all IAM accounts and recreating them would lock out the entire team immediately and disrupt operations without actually addressing whether the root account is compromised; the root account password change must take priority. Using CloudWatch to check all API calls made since the administrator was fired is a useful forensic step for understanding what actions were taken, but it is a post-incident investigation activity rather than an immediate protective measure that should come before securing credentials.

## clf-c02/domain2/q531

Answer: B, C

Customers must properly configure AWS services to meet PCI DSS standards as AWS's compliance certifications cover the infrastructure layer but not the customer's specific service configurations, and customers must restrict cardholder data access and maintain an information security policy as these are customer responsibilities under PCI DSS.
Not all AWS services are PCI DSS compliant by default; only specific AWS services are in scope for PCI compliance, and customers must verify that the services they use are in scope and configured correctly to maintain a PCI-compliant environment. Configuring the underlying AWS infrastructure to meet PCI DSS requirements is not the customer's responsibility; AWS manages and maintains the physical infrastructure, hardware, and network to meet PCI standards, and customers are responsible only for how they configure the services built on top of that infrastructure. Ensuring that all PCI DSS physical security requirements are met is AWS's responsibility; the physical security of data centers, including access controls, surveillance, and hardware handling, is managed by AWS under the shared responsibility model.

## clf-c02/domain2/q535

Answer: B

Since 2019, AWS allows customers to perform penetration testing on permitted services including EC2, RDS, CloudFront, and API Gateway without prior AWS approval, so customers should follow their own internal security review and authorisation process before conducting tests.
Amazon Inspector is an automated vulnerability assessment service that scans for known vulnerabilities and network misconfigurations, but it is not a penetration testing tool and using it does not substitute for or require notification to AWS support before conducting actual penetration testing. AWS no longer requires customers to notify AWS support before conducting penetration testing on permitted services; the policy changed to allow testing without prior approval, so notifying and then conducting testing immediately is based on an outdated requirement. Requesting and waiting for approval from AWS support before conducting penetration testing is no longer required for permitted services; AWS updated its policy to allow customers to test their own resources without prior approval, removing the requirement for a formal approval process.

## clf-c02/domain2/q550

Answer: C

Updating the host firmware on EC2 physical servers is AWS's responsibility, as customers have no access to or control over the underlying hardware beneath their instances.
Granting access to individuals and services is the customer's responsibility, as customers manage their own IAM users, roles, and permissions within their AWS account. Encrypting data in transit is the customer's responsibility, as customers decide whether and how to implement encryption for their own data using HTTPS, TLS, or other mechanisms. Updating operating systems is the customer's responsibility on services like EC2, where customers control the guest OS and are accountable for keeping it patched and up to date.

## clf-c02/domain2/q553

Answer: B

Managing edge locations, the physical infrastructure used by CloudFront and other services, is solely AWS's responsibility as part of its obligation to operate and maintain the global infrastructure underpinning its services.
Application security is the customer's responsibility under the Shared Responsibility Model, as customers are accountable for securing the code, configurations, and access controls within their own applications. Patch management is a shared control where AWS patches the underlying infrastructure and managed services, while customers retain responsibility for patching their own operating systems and applications. Client-side data is the customer's responsibility, as customers control how their data is classified, encrypted, and managed on the client side regardless of which AWS services they use.

## clf-c02/domain2/q555

Answer: A

AWS Trusted Advisor checks your security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports such as SSH and RDP, flagging potential security risks in its Security category checks.
Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and while it identifies network reachability issues, the simplest tool for checking security groups for unrestricted access is Trusted Advisor. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a tool that audits security group configurations for overly permissive rules. AWS CloudTrail records all API calls and management events for auditing, capturing who created or modified security group rules and when, but it records actions after the fact rather than proactively identifying groups with unrestricted access.

## clf-c02/domain2/q564

Answer: B, D

Customers are responsible for encrypting data on the client side before sending it to AWS, and for configuring Network ACLs to control inbound and outbound traffic at the subnet level in their VPC.
Patching operating system components for Amazon RDS is entirely AWS's responsibility, as RDS is a managed service where AWS handles all underlying OS and database engine patching on the customer's behalf. Training data center staff is entirely AWS's responsibility, as customers have no access to or involvement in the physical facilities and operations teams that run AWS infrastructure. Maintaining environmental controls within a data center such as power, cooling, and fire suppression is entirely AWS's responsibility and is fully inherited by customers under the model.

## clf-c02/domain2/q565

Answer: B

Patch management is a shared control. AWS patches the underlying infrastructure and managed service platforms, while customers are responsible for patching their own guest operating systems and applications.
Physical controls are AWS's responsibility exclusively, covering physical security of data centers and hardware. Zone security is also AWS's responsibility, covering the physical and network isolation between Availability Zones. Data center auditing is AWS's responsibility, though customers can request compliance reports via AWS Artifact.

## clf-c02/domain2/q573

Answer: A, E

AWS WAF creates rules to block requests from specific IP addresses, networks, or matching certain patterns, filtering malicious web traffic at the application layer, and Network ACLs are stateless subnet-level firewalls that can block traffic from specific IP ranges at the network layer. Both can enhance network security by blocking requests from particular networks.
AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and while it identifies insecure configurations, it does not itself block network requests or actively enforce traffic rules. AWS Direct Connect provides a dedicated private network connection between on-premises data centers and AWS, and is a connectivity service rather than a tool for blocking or filtering web application traffic. AWS Organizations manages multiple AWS accounts under a central structure for governance and consolidated billing, and does not have the capability to block network traffic from specific IP ranges for web applications.

## clf-c02/domain2/q575

Answer: B

AWS CloudTrail continuously logs all account activity and API calls across AWS infrastructure, providing a complete audit trail that supports risk auditing, compliance monitoring, and security analysis.
Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational visibility into performance and health, and while it can monitor logs, it does not record API calls or user actions for risk auditing and compliance purposes. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and focuses on resource configuration changes rather than logging user actions and API calls for risk auditing. AWS Health provides personalized alerts and remediation guidance when AWS is experiencing events that may affect your resources, and is a service health notification tool rather than an account activity logging or risk auditing service.

## clf-c02/domain2/q576

Answer: A

AWS Artifact is the self-service portal where customers can download AWS compliance and certification reports including SOC, PCI, ISO, and HIPAA eligibility documentation without needing to contact AWS directly.
AWS Concierge is a dedicated support resource for Enterprise support plan customers that assists with billing and account management, and is not a portal for downloading compliance reports or technical certification documents. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate provisioning service rather than a repository of AWS compliance and audit reports. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and while it includes security checks, it does not provide downloadable AWS compliance certification reports.

## clf-c02/domain2/q581

Answer: B

Data encryption is the customer's responsibility under the shared responsibility model. AWS provides the tools and services to enable encryption, such as AWS KMS and native encryption options across storage services, but the customer decides whether to enable encryption and manages the keys and access policies.
Physical access controls at AWS data centers are entirely AWS's responsibility; customers have no access to the physical facilities and rely on AWS to implement and enforce physical security measures. Secure disposal of storage devices is AWS's responsibility, as customers never have physical possession of AWS hardware and AWS follows industry standards for decommissioning and disposing of storage media. Environmental risk management for the AWS infrastructure, including temperature control, humidity, and fire suppression in data centers, is entirely AWS's responsibility as part of securing the underlying physical infrastructure.

## clf-c02/domain2/q587

Answer: A

AWS Artifact provides on-demand access to AWS compliance reports and certifications including SOC, PCI DSS, ISO, and HIPAA documents, available directly from the AWS Management Console without needing to engage AWS support.
AWS Lambda is a serverless compute service that runs code in response to events without requiring server provisioning or management, and is a compute service with no connection to compliance reports or certification documentation. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces customer-specific vulnerability findings rather than AWS compliance certifications. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services, and is a certificate management service rather than a repository of compliance reports or regulatory certifications.

## clf-c02/domain2/q589

Answer: A

Attaching an IAM policy to an IAM group applies those permissions to all users in the group simultaneously, making it the most efficient way to manage common access controls for a large number of users without configuring each user individually.
Applying an IAM policy to an IAM role would affect entities that assume that role, such as applications or services, rather than applying consistent controls directly to a large set of named users who need the same permissions. Applying the same IAM policy to all IAM users individually would achieve the desired result but requires editing each user's policy separately, which is time-consuming and error-prone at scale compared to using a group. Applying an IAM policy to an Amazon Cognito user pool affects application users authenticating through Cognito rather than IAM users managing AWS resources, and is used for application-level access control rather than AWS service permission management.

## clf-c02/domain2/q618

Answer: D

Auditing physical data center assets including hardware inventory, facility inspections, and physical access logs is entirely AWS's responsibility under the shared responsibility model, as customers never have physical access to or visibility into AWS data center infrastructure.
Patching the operating system software on EC2 instances is the customer's responsibility under the shared responsibility model, as AWS manages the underlying hypervisor and hardware but customers are responsible for maintaining the guest operating system on their virtual machines. Encrypting data at rest and in transit is the customer's responsibility; AWS provides the tools and services to enable encryption such as KMS and ACM, but customers must decide what to encrypt and configure it appropriately. Enforcing multi-factor authentication for IAM users and the root account is the customer's responsibility, as AWS provides MFA functionality but customers must enable and configure it for their account and users.

## clf-c02/domain2/q628

Answer: C

Physical and environmental controls including data center security, cooling systems, fire suppression, and power management are entirely AWS's responsibility, as customers have no access to or involvement in managing AWS physical infrastructure.
Patching of the guest operating system on EC2 instances is the customer's responsibility; AWS manages the underlying hardware and hypervisor but customers are responsible for keeping the operating system and applications on their instances up to date. Security awareness and training for employees and users of the AWS environment is the customer's responsibility; AWS provides security best practice guidance and training resources, but the organization's own training program for its staff is a customer obligation. Developing an IAM password policy is the customer's responsibility; AWS provides IAM with configurable password policy settings, but defining and enforcing the specific password requirements for an organization's IAM users is a customer configuration task.

## clf-c02/domain2/q633

Answer: B

IAM Groups allow you to attach permission policies to the group, and all users added to that group automatically inherit those permissions, making it the IAM feature used to associate a set of permissions with multiple users at once.
Multi-factor authentication adds a second verification layer beyond passwords to secure individual user logins, and is an authentication security mechanism rather than a feature for associating a set of permissions with multiple users simultaneously. Password policies define password complexity, rotation, and reuse rules for IAM user accounts, and are an authentication credential management feature rather than a mechanism for associating permissions with multiple users. Access keys consisting of an access key ID and secret access key are programmatic credentials for CLI and API access associated with individual IAM users, and are an authentication mechanism rather than a feature for associating permissions with groups of users.

## clf-c02/domain2/q635

Answer: B

AWS Directory Service integrates with Microsoft Active Directory, enabling single sign-on to the AWS Management Console using existing corporate usernames and passwords without creating separate IAM users for each employee.
Amazon Connect is a cloud-based contact center service that handles customer interactions through voice and chat channels, and has no capability to enable corporate credential federation or single sign-on authentication to the AWS Management Console. Amazon Pinpoint is an outbound communications service for sending targeted messages via email, SMS, and push notifications to application users, and is a marketing and engagement service with no connection to SSO or corporate identity federation for console access. Amazon Rekognition is a machine learning service for analyzing images and videos to detect objects, faces, and scenes, and is a visual analysis service with no role in enabling corporate credential single sign-on.

## clf-c02/domain2/q637

Answer: A, C

The AWS Compliance program allows customers to inherit AWS's third-party certifications and audit results, reducing the time and cost of their own compliance efforts. It also assures customers that AWS maintains physical security and data protection standards at the infrastructure level.
AWS is not solely responsible for maintaining compliance framework documentation - compliance is a shared responsibility, and customers remain responsible for ensuring their own workloads meet applicable regulations. AWS does not guarantee alignment with frameworks simply because other cloud providers use them - its compliance programs are based on relevant industry standards and regulatory requirements. AWS does not make binding commitments to automatically adopt any new compliance framework that becomes relevant to customer workloads.

## clf-c02/domain2/q638

Answer: B

AWS Artifact provides on-demand, self-service access to AWS compliance reports and certifications including SOC, PCI DSS, ISO, and HIPAA documentation, directly from the AWS Management Console.
AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access management service rather than a repository of compliance reports or certifications. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity using machine learning and threat intelligence, and is a security monitoring service rather than a compliance report portal. AWS KMS is a key management service for creating and managing encryption keys used to protect data at rest and in transit, and is an encryption infrastructure service rather than a service providing access to compliance documentation.

## clf-c02/domain2/q639

Answer: A

Security management of the data center is an operational control customers fully inherit from AWS, meaning AWS performs all physical security operations and customers benefit from this protection without any action required on their part.
Patch management is a shared control where AWS patches the infrastructure and managed services it operates, while customers are responsible for patching the operating systems and applications running on their own EC2 instances and other customer-managed resources. Configuration management is also a shared control where AWS maintains the configuration of its own infrastructure components while customers are responsible for configuring their own operating systems, applications, and AWS services to meet their security and operational requirements. User and access management is the customer's responsibility; customers create and manage IAM users, groups, roles, and policies, and are fully accountable for who has access to their AWS resources and what those identities are permitted to do.

## clf-c02/domain2/q641

Answer: B, C

Customers are responsible for managing VPC network access control lists to define inbound and outbound traffic rules at the subnet level, and for encrypting their own data in transit using TLS and at rest using services such as KMS and S3 server-side encryption.
Maintaining the underlying EC2 hardware including servers, storage, and networking infrastructure is entirely AWS's responsibility, as customers have no physical access to the data center equipment that hosts EC2 instances. Replacing failed hard disk drives is AWS's responsibility as part of managing the physical infrastructure, and customers experience this transparently through AWS's hardware redundancy and replacement processes without any action required. Deploying hardware in different Availability Zones is an AWS infrastructure responsibility; AWS designs and maintains the physical separation of AZs, while customers choose which AZ to deploy their resources in but do not control the underlying hardware deployment.

## clf-c02/domain2/q646

Answer: A

Security groups act as virtual firewalls for EC2 instances, controlling inbound and outbound traffic at the instance level by evaluating rules based on protocol, port, and source or destination, providing the primary network security mechanism for EC2 instance access.
Securing AWS user accounts with IAM policies is the function of AWS Identity and Access Management, which controls which users can access which AWS services and what actions they can perform, rather than a function of security groups which operate at the network traffic level. Providing DDoS protection is the function of AWS Shield, which provides managed distributed denial of service mitigation at the network and transport layers, rather than security groups which evaluate individual connection attempts based on rules. Using Amazon CloudFront to protect EC2 instances involves routing traffic through CloudFront's edge network with Shield and WAF integrations, and is a separate architectural pattern rather than a function performed by security groups directly.

## clf-c02/domain2/q652

Answer: D

On AWS, users can gather asset metadata reliably by making a few API calls using services such as AWS Config, Systems Manager Inventory, or the AWS CLI, providing comprehensive and up-to-date information about all resources across an account.
AWS does not provide a pre-built Configuration Management Database that customers maintain; AWS Config tracks resource configurations automatically, but maintaining a traditional CMDB requires third-party tooling or custom development rather than being a built-in AWS service offering. AWS does not perform infrastructure discovery scans on the customer's behalf; services like AWS Config and Systems Manager provide discovery capabilities, but these are tools customers use themselves rather than automated scans performed by AWS on the customer's account. Amazon EC2 does not automatically generate asset reports and place them in S3; while instances report some metadata, comprehensive asset reporting requires active use of AWS management services like Config, Systems Manager, or the CLI rather than automatic report generation.

## clf-c02/domain2/q654

Answer: C

Least privilege access means granting IAM users only the minimum permissions they need to perform their specific assigned tasks, reducing the risk of accidental or intentional misuse of AWS resources through overly broad permission grants.
Restricted access is a general term that implies limiting access, but it does not specifically capture the principle of granting the minimum required permissions; least privilege is the precise IAM concept that defines permissions based on task requirements rather than broadly restricting access. As-needed access is an informal description that partially captures the idea of granting permissions when needed, but least privilege is the established AWS and security industry term for the principle of granting minimum necessary permissions. Token access refers to the use of temporary security tokens issued when IAM roles are assumed, and describes a credential mechanism rather than the principle of scoping permissions to what is required for a task.

## clf-c02/domain2/q656

Answer: C

Configuring the operating system, network settings, and firewall rules on EC2 instances falls within the customer's responsibility under the shared responsibility model, as AWS provides the underlying infrastructure while customers are responsible for what they install and configure on top of it.
Securing the hardware, software, facilities, and networks that run all AWS products and services is AWS's responsibility under the shared responsibility model, as customers have no access to or control over the physical and virtual infrastructure that AWS manages. Providing compliance certificates, reports, and documentation to customers under NDA is a service AWS provides through AWS Artifact, not a customer responsibility; customers access these documents rather than create or provide them. Obtaining industry certifications and third-party attestations for the AWS infrastructure is AWS's responsibility, as AWS undergoes independent audits for certifications such as ISO, SOC, and PCI DSS that apply to the infrastructure layer rather than being a customer obligation.

## clf-c02/domain2/q657

Answer: B

AWS Trusted Advisor inspects your AWS environment and provides real-time recommendations across security, cost optimization, performance, fault tolerance, and service limits, directly guiding customers toward security best practices.
Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications including CPU utilization, error rates, and custom metrics, and is an observability service rather than a service that provides security best practice guidance. AWS Config continuously monitors and records resource configurations against desired state rules, and is a compliance evaluation service rather than a service that provides proactive guidance on security best practices. AWS CloudTrail records all API calls and management events for auditing and compliance purposes, and is an activity logging service rather than a service that provides real-time guidance on improving the security posture of an AWS environment.

## clf-c02/domain2/q659

Answer: C, E

Customers are responsible for managing encryption of their data at rest and in transit including configuring encryption settings and managing KMS keys, and for configuring firewall rules through security groups and Network ACLs to control traffic to their resources.
Virtualization management is not a standard shared responsibility category; the underlying virtualization infrastructure including the hypervisor is AWS's responsibility, while customers manage the virtual machines that run on top of it rather than the visualisation layer itself. Hardware management including physical servers, storage devices, and networking equipment is entirely AWS's responsibility as customers have no access to or interaction with the physical infrastructure in AWS data centers. Facilities management including data center physical security, power, and cooling is entirely AWS's responsibility as customers never have physical access to or involvement in managing the facilities that house AWS infrastructure.

## clf-c02/domain2/q661

Answer: C

Updating the firmware on EC2 host hardware is AWS's responsibility, as customers have no access to the physical servers and AWS manages all maintenance of the hardware layer including firmware updates for security and performance improvements.
Updating network ACLs to block traffic to vulnerable ports is the customer's responsibility; customers configure their VPC network ACLs to define which traffic is allowed or denied at the subnet level as part of their security configuration. Patching operating systems running on EC2 instances is the customer's responsibility; AWS manages the underlying hypervisor and host hardware, but the guest operating system and its patches are the customer's obligation. Updating security group rules to block traffic to vulnerable ports is the customer's responsibility; customers define and maintain security group rules to control which traffic reaches their EC2 instances as part of their network security configuration.

## clf-c02/domain2/q663

Answer: D

Least privilege means granting only the minimum permissions required to perform a specific task, ensuring that IAM users cannot access resources or perform actions beyond what their job requires, minimizing the risk of misuse.
Granting permissions to a single user only describes individual rather than shared access, but does not capture the concept of scoping permissions to the minimum required; least privilege is about the breadth of permissions granted rather than the number of users receiving them. Granting permissions using IAM policies only is a description of the mechanism for assigning permissions in AWS, but does not define the principle of least privilege, which is about minimizing the scope of those permissions rather than the method of granting them. Granting AdministratorAccess permissions to trustworthy users is the opposite of least privilege; administrator access grants unrestricted access to all AWS services and resources, which far exceeds the minimum permissions needed for most tasks regardless of how trustworthy the user is.

## clf-c02/domain2/q683

Answer: D

AWS Artifact is a self-service portal providing on-demand access to AWS compliance reports and certifications including SOC, PCI, and ISO documents, making it the purpose-built service for customers requiring on-demand access to compliance reports.
AWS Config continuously monitors and records resource configurations to evaluate compliance against desired rules, and is a resource configuration compliance tool rather than a portal for downloading AWS auditor-issued compliance reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for use with AWS services to protect data in transit, and is a certificate provisioning and management service rather than a compliance documentation repository. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces customer-specific assessment findings rather than AWS compliance reports.

## clf-c02/domain2/q692

Answer: D

AWS is responsible for managing the physical and virtual network infrastructure that underpins its global cloud, including the routers, switches, and physical cabling that connect data centers, Availability Zones, and Regions.
Configuring Amazon VPC is the customer's responsibility; customers define their VPC IP address ranges, subnets, route tables, internet gateways, and security settings as part of their network design within AWS. Managing application code is entirely the customer's responsibility; AWS provides the compute and runtime services, but the application logic, code quality, and updates are owned and maintained by the customer. Maintaining application traffic, including managing load balancers, CDN configurations, and DNS routing, is the customer's responsibility for their own applications, though AWS manages the underlying network infrastructure those services run on.

## clf-c02/domain2/q694

Answer: B

AWS Trusted Advisor scans your security groups and flags those that grant unrestricted internet access (0.0.0.0/0) to specific ports such as SSH, RDP, and common database ports, helping identify and close potential security vulnerabilities.
AWS Organizations manages multiple AWS accounts under a central structure for consolidated billing and governance with service control policies, and does not have the capability to inspect individual security group rules or identify overly permissive internet access configurations. AWS Usage Reports provide data about AWS service usage and costs, and are billing and consumption tracking tools rather than security assessment tools that evaluate network access control configurations. The Amazon EC2 dashboard displays information about running instances, instance types, and their states, and while security groups are visible in the console, the dashboard does not automatically identify which groups grant unrestricted internet access the way Trusted Advisor's automated check does.

## clf-c02/domain2/q697

Answer: B

AWS is responsible for physically destroying storage media at end of life using industry-standard techniques to prevent data leakage, following secure decommissioning procedures as part of their data center operations under the shared responsibility model.
Setting up IAM users and groups is the customer's responsibility; customers define their own identity and access management structure including creating users, assigning them to groups, and attaching policies that control what each identity can access. Patching guest operating systems on EC2 instances is the customer's responsibility; AWS manages the underlying host hardware and hypervisor, but the operating system running inside the virtual machine must be patched and maintained by the customer. Configuring security settings on EC2 instances including firewall rules, operating system hardening, and application security configurations is the customer's responsibility as part of securing what they deploy and manage on AWS compute resources.

## clf-c02/domain2/q702

Answer: A, E

When an account is suspected compromised, immediately rotating all passwords and access keys invalidates potentially stolen credentials, and contacting AWS Support provides assistance with the investigation and remediation of the compromise.
Removing MFA tokens would reduce account security at precisely the moment it is most needed, as MFA provides an additional authentication barrier that helps prevent unauthorised access even if credentials have been stolen. Moving resources to a different AWS Region does not address the underlying compromise and has no effect on the attacker's ability to access the account using stolen credentials. Deleting AWS CloudTrail resources would destroy the audit trail needed to investigate how the compromise occurred and what actions the attacker took, making remediation significantly harder.

## clf-c02/domain2/q705

Answer: C

An IAM role is an entity that defines a set of permissions for making AWS service requests, and unlike an IAM user it does not have permanent credentials; instead it provides temporary security credentials to whoever or whatever assumes it.
A user associated with an AWS resource describes an IAM user or service account assigned to interact with specific resources, but this does not capture the defining characteristic of an IAM role, which is that it can be assumed temporarily by multiple different entities rather than being permanently associated with a single one. A group associated with an AWS resource describes an IAM group used to manage shared permissions for multiple users, not a role, which is assumed dynamically by users, services, or applications that need its permissions temporarily. An authentication credential associated with an MFA token describes a multi-factor authentication mechanism, not an IAM role, which is an identity type that provides temporary credentials and permissions rather than being a specific authentication token.

## clf-c02/domain2/q717

Answer: D

AWS Config continuously monitors and records AWS resource configurations, tracking changes over time and evaluating configurations against desired state compliance rules, making it the correct service for auditing and monitoring resource changes.
AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories by analyzing your AWS environment, and is an advisory tool rather than a service that specifically records and audits individual resource configuration changes over time. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts and workloads, and is a security monitoring service rather than a resource configuration change auditing tool. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and produces security assessment findings rather than tracking and auditing resource configuration changes.

## clf-c02/domain2/q722

Answer: D

The AWS Abuse Team handles reports of AWS resources being used in malicious activities including DDoS attacks, and should be the first point of contact when AWS-owned IP addresses are identified as participating in an attack, as they can investigate and stop the misuse.
AWS Premium Support assists paying customers with technical issues and architectural guidance related to their own AWS environment, but is not the designated channel for reporting abuse originating from AWS IP addresses belonging to other accounts. The AWS Technical Account Manager is a support resource for Enterprise plan customers providing proactive guidance and operational reviews, but is not the appropriate contact for reporting external abuse incidents involving AWS infrastructure. AWS Solutions Architects help customers design architectures and optimize workloads, and are not the contact for reporting security incidents or abuse involving AWS infrastructure and IP addresses.

## clf-c02/domain2/q727

Answer: B

AWS Artifact provides on-demand access to AWS security and compliance reports including SOC, PCI, ISO, and other certifications, available directly from the AWS Management Console to help customers meet their own regulatory requirements.
AWS CloudTrail records all API calls and management events for auditing and compliance purposes, and produces customer-specific activity logs rather than AWS security certification reports issued by third-party auditors. AWS Health provides personalized alerts about AWS events that may affect a customer's specific resources or service availability, and is a service health and notification tool rather than a repository of compliance reports. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability and alerting service rather than a source of AWS security and compliance documentation.

## clf-c02/domain2/q730

Answer: C

Amazon VPC provides Network Access Control Lists that act as stateless firewalls at the subnet level, controlling inbound and outbound traffic to harden network connectivity for EC2 instances, as well as security groups at the instance level for additional control.
AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access control service rather than a network security component that provides inbound and outbound traffic filtering via ACLs. Amazon Connect is a cloud-based contact center service for handling customer interactions through voice and chat, and is a communications service with no connection to VPC networking or network ACL configuration. Amazon API Gateway is a fully managed service for creating, publishing, and managing APIs, and is an application integration layer rather than a VPC networking component that provides network ACLs to control connectivity.

## clf-c02/domain2/q733

Answer: B

AWS is responsible for the physical security of its global infrastructure, including the data centers, networking hardware, and facilities, as customers have no access to or control over any physical component of the AWS environment.
Lifecycle management of IAM credentials including creating, rotating, and deleting access keys and passwords for IAM users is the customer's responsibility, as customers define and manage the identities used to access their AWS resources. Encryption of Amazon EBS volumes is the customer's responsibility; while AWS provides KMS for key management and EBS supports encryption, customers must choose to enable encryption and configure the appropriate keys for their volumes. Firewall configuration through security groups and network ACLs is the customer's responsibility as part of securing network access to their own resources within their VPC.

## clf-c02/domain2/q735

Answer: C

Firewall configuration through security groups and network ACLs, which customers define to control inbound and outbound traffic to their resources, is the customer's responsibility and is an example of security performed within the cloud on the customer's side of the shared responsibility model.
Managing edge locations is AWS's responsibility; AWS operates the global network of edge locations for CloudFront and other services, and customers benefit from these locations without being responsible for their management or security. Physical security of AWS data centers and hardware is entirely AWS's responsibility as customers never have physical access to the facilities where AWS infrastructure runs. Global infrastructure, including the physical data centers, Availability Zones, and Regions, is designed, built, and operated by AWS, and maintaining its security and availability is an AWS responsibility rather than a customer one.

## clf-c02/domain2/q740

Answer: D

AWS WAF lets you create rules to block requests from specific IP addresses or ranges, inspect request content, and filter traffic patterns, providing effective application-layer protection against repeated malicious requests from known IP addresses.
AWS IAM manages user identities and permissions for accessing AWS services and resources, and is an access control service rather than a service that can block malicious HTTP traffic targeting a web application. Amazon GuardDuty is a threat detection service that uses machine learning to identify malicious activity and anomalous behavior in AWS accounts, and while it can detect suspicious patterns, it does not actively block or filter web application traffic in real time. Amazon SNS is a fully managed publish/subscribe messaging service for sending notifications to subscribers, and is a messaging and notification service with no capability to inspect or block malicious web traffic patterns.

## clf-c02/domain2/q746

Answer: D

Amazon Inspector automatically assesses EC2 instances for unintended network access by analyzing network configurations and known software vulnerabilities by scanning installed packages against vulnerability databases, generating prioritized security assessment reports.
EC2 security groups are virtual firewalls that control which traffic is allowed to reach EC2 instances based on defined rules, and are a preventive network control rather than an automated assessment service that identifies vulnerabilities and generates reports. AWS Config continuously monitors and records resource configurations against desired state compliance rules, and is a configuration compliance evaluation service rather than a vulnerability assessment tool that scans for network exposure or software weaknesses. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification and protection service for S3 rather than a service that assesses EC2 instances for network access vulnerabilities.

## clf-c02/domain2/q748

Answer: B

AWS Marketplace is a digital catalog where users can find, purchase, and deploy third-party software solutions from independent software vendors that are vetted by AWS, including security tools such as firewalls, intrusion detection, and compliance products.
AWS Service Catalog allows organizations to create and manage catalogs of approved IT services for internal use within their own AWS environment, and is an internal governance tool for managing approved product portfolios rather than a public catalog of third-party security vendors. AWS Quick Start provides pre-built, automated deployments of popular technologies using AWS CloudFormation templates, and is a deployment acceleration resource rather than a catalog of third-party security solution providers. AWS CodeDeploy is an automated deployment service that delivers application code to EC2 instances, Lambda functions, and on-premises servers, and is a deployment automation tool with no connection to browsing or purchasing third-party security solutions.

## clf-c02/domain2/q755

Answer: C

Security and compliance is a shared responsibility between AWS and the customer; AWS secures the underlying cloud infrastructure while customers are responsible for securing their workloads, data, and configurations built on top of it.
The customer alone being responsible for security and compliance is incorrect; under the shared responsibility model, AWS manages security of the cloud infrastructure including physical data centers, hypervisor, and global network, which are entirely outside customer control. AWS alone being responsible for security and compliance is incorrect; customers must actively manage security in the cloud including IAM policies, encryption configuration, network security, and application security, all of which AWS cannot control or configure on the customer's behalf. AWS sharing responsibility with a relevant governing body is not how the shared responsibility model works; the model divides responsibility between AWS and the customer based on which layer of the stack each party controls, with no involvement from external regulatory bodies in the operational security responsibility.

## clf-c02/domain2/q757

Answer: C

AWS Key Management Service manages the encryption keys used for EBS volume encryption, handling key creation, rotation, and access control, integrating transparently with EBS to protect data at rest.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and clients, and is a certificate management service rather than a key management service for EBS volume encryption at rest. AWS Systems Manager provides operational management tools for EC2 instances and other resources including patching, configuration management, and session management, and is an operations service rather than an encryption key management service for EBS volumes. AWS Config continuously monitors and records resource configurations against desired state compliance rules, and is a configuration compliance evaluation service rather than an encryption key management service.

## clf-c02/domain2/q760

Answer: B

AWS Shield Standard provides automatic DDoS protection at no extra cost for all AWS customers, automatically detecting and mitigating common network and transport layer attacks including UDP floods and SYN floods without any configuration required.
WAF rules are managed by AWS WAF, which is a separate service from Shield that filters application-layer HTTP and HTTPS traffic based on configurable rules, and AWS Shield Standard does not provide WAF rule functionality. IAM permissions and access to resources are managed by AWS Identity and Access Management, which controls who can access which AWS services, and have no connection to the DDoS protection that AWS Shield provides. Data encryption is provided by services such as AWS KMS, S3 server-side encryption, and EBS encryption, and has no relationship to AWS Shield, which is specifically a DDoS mitigation service.

## clf-c02/domain2/q766

Answer: C

Application security, including securing application code, data access controls, and authentication configurations, is the customer's responsibility under the shared responsibility model as it falls within the customer's side of the stack that AWS cannot access or control.
Virtualization infrastructure including the hypervisor that abstracts physical hardware into virtual machines is managed and secured entirely by AWS as part of its security of the cloud obligations, and customers have no access to or responsibility for this layer. Network infrastructure including the global network connecting AWS Regions, Availability Zones, and edge locations is owned and maintained by AWS and is not a customer responsibility, as customers configure virtual networking within their VPC but do not manage the underlying physical network. Physical security of hardware including data center access controls, server security, and decommissioning of physical equipment is entirely AWS's responsibility as customers have no access to or interaction with AWS physical facilities.

## clf-c02/domain2/q770

Answer: A

The AWS Abuse Team should be contacted when AWS resources or IP addresses are being used for malicious purposes such as hosting spam, conducting DDoS attacks, or distributing malware, as they are the designated channel for investigating and stopping such misuse.
AWS Shield provides managed DDoS protection that automatically detects and mitigates DDoS attacks against your own resources, and is a protective service for your own infrastructure rather than a channel for reporting AWS resources being abused by others. AWS Support assists customers with technical issues and questions about their own AWS environment, but is not the designated channel for reporting that AWS infrastructure belonging to other accounts is being used for malicious purposes. AWS Developer Forums are community discussion spaces where developers share knowledge and ask questions about AWS services, and are not an appropriate reporting channel for security incidents involving malicious use of AWS resources.

## clf-c02/domain2/q771

Answer: A

AWS CloudTrail records all API calls and user actions in the AWS Management Console, providing a complete audit trail of account changes for security analysis and compliance.
Amazon Simple Notification Service is a fully managed pub/sub messaging service that delivers notifications to subscribers such as Lambda functions, HTTP endpoints, and email addresses, and has no capability to record or track user account changes within the AWS Management Console. VPC Flow Logs capture information about IP traffic flowing to and from network interfaces within a VPC, and is a network traffic logging feature that records connection-level data rather than user actions or account changes in the console. AWS CloudHSM provides dedicated hardware security modules for generating and managing cryptographic keys, and is a key management and encryption service with no capability to track or audit user activity within the AWS Management Console.

## clf-c02/domain2/q777

Answer: B

Maintaining physical hardware including servers, storage devices, and networking equipment in data centers is exclusively AWS's responsibility, as customers have no access to or interaction with the physical infrastructure that powers AWS services.
Configuring third-party applications deployed on AWS resources is the customer's responsibility; AWS provides the compute, storage, and networking infrastructure, but customers are responsible for installing, configuring, and securing any third-party software they choose to run on that infrastructure. Securing application access and data, including setting up appropriate IAM policies, encryption configurations, and access controls for applications and data stored in AWS, is the customer's responsibility as part of security in the cloud. Managing custom Amazon Machine Images including creating, maintaining, and updating AMIs used to launch EC2 instances is the customer's responsibility as part of managing their own compute environment.

## clf-c02/domain2/q779

Answer: C

Enabling Multi-Factor Authentication adds a second verification layer beyond a password, requiring a time-based one-time code from a hardware or virtual device to complete login, providing an additional layer of security for AWS Management Console access.
AWS Cloud Directory is a managed directory service for building cloud-native directories that organize hierarchical data such as organizational structures and device registries, and is not a mechanism for adding a login security layer to the AWS Management Console. Auditing IAM roles reviews what permissions have been granted across an account, which is a governance activity that helps identify excessive permissions but does not add an additional authentication step to the login process itself. Enabling AWS CloudTrail records API calls and account activity for auditing and compliance, and while it improves visibility into who did what after login, it does not add any additional layer of security to the login authentication process.

## clf-c02/domain2/q780

Answer: B

AWS CloudTrail logs all API calls including EC2 instance terminations, recording which IAM user or role made the call, the source IP address, and the timestamp, making it the purpose-built service for identifying who performed a specific action in an AWS account.
Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and does not record API call identity or attribution information for specific actions such as instance terminations. AWS X-Ray is a distributed tracing service that analyzes and debugs the performance of applications by mapping requests as they flow through application components, and is a performance analysis tool with no API call logging or user attribution capability. AWS Identity and Access Management defines and manages permissions for users and roles, controlling what actions they are allowed to perform, but does not itself log or record which user made a specific API call or when.

## clf-c02/domain2/q782

Answer: D

The AWS Acceptable Use Policy defines what activities are prohibited on AWS infrastructure including illegal content hosting, network attacks, and sending spam, and is the authoritative reference for customers seeking to understand what actions are not permitted.
AWS Trusted Advisor provides automated recommendations for improving the security, cost efficiency, performance, and fault tolerance of AWS environments, and is an advisory tool rather than a document defining prohibited uses of the AWS platform. AWS IAM manages user identities and permissions to control which AWS services and resources users can access, and is an access management service rather than a policy document listing prohibited infrastructure activities. The AWS Billing Console displays cost and usage data, invoices, and payment information for an AWS account, and is a financial management interface with no connection to defining or documenting prohibited uses of AWS infrastructure.

## clf-c02/domain2/q786

Answer: A, B

Requiring password rotation after a specified period limits how long any compromised password remains valid, and preventing password reuse ensures users cannot immediately revert to previously exposed credentials after a required change.
Recommending the same password across AWS and other sites creates a significant security risk through credential reuse, as a breach of any other site would then compromise the AWS account; password uniqueness for each service is a fundamental security best practice. Requiring IAM users to store passwords in raw unencrypted text would expose those passwords to anyone who gains access to wherever they are stored, creating severe security vulnerabilities; passwords should be kept confidential and never stored in plain text. Disabling MFA for IAM users removes a critical second authentication factor, leaving accounts protected only by passwords and significantly increasing the risk of unauthorised access if credentials are compromised.

## clf-c02/domain2/q793

Answer: B

Intrusion attempts originating from AWS IP addresses are abuse scenarios that should be reported to the AWS Abuse Team, which investigates misuse of AWS resources for malicious activities such as hacking, phishing, and denial of service attacks.
An Availability Zone service disruption is an infrastructure availability issue that should be monitored through the AWS Health Dashboard and reported to AWS Support if it is causing operational impact, rather than being an abuse scenario for the Abuse Team. A user having trouble accessing an S3 bucket from an AWS IP address is a technical access or permission issue that should be investigated by checking IAM policies, bucket policies, and VPC configurations, and addressed through AWS Support if needed rather than reported to the Abuse Team. A user needing to change payment methods due to a compromise is a billing and account security matter that should be handled through the AWS Management Console or by contacting AWS Customer Service for billing assistance.

## clf-c02/domain2/q796

Answer: B, D

Subnets divide a VPC's IP address range into segments that organize resources and define routing boundaries within the VPC, and internet gateways enable communication between resources in a VPC and the internet. Both are fundamental VPC components.
Objects is an Amazon S3 term for the data items stored within S3 buckets, and is a storage abstraction concept with no connection to Amazon VPC networking components such as subnets, route tables, or gateways. Buckets are Amazon S3 containers for storing objects and are the primary storage unit in the S3 service, and are not components of Amazon VPC, which is a virtual network service rather than an object storage service. Access keys are IAM credentials consisting of an access key ID and secret access key used for programmatic API and CLI authentication, and are identity management constructs rather than VPC networking components.

## clf-c02/domain2/q800

Answer: C

AWS KMS lets users create and manage cryptographic keys for encrypting and decrypting data across AWS services, providing centralized key lifecycle management with audit logging of key usage via CloudTrail.
Creating and managing AWS access keys for the root user is done through the IAM section of the AWS Management Console, and access keys are authentication credentials rather than cryptographic keys managed by KMS. Creating and managing AWS access keys for IAM users is performed through the IAM console or CLI, and access keys are programmatic authentication credentials unrelated to the encryption key management function of AWS KMS. Creating and managing keys for multi-factor authentication involves configuring virtual or hardware MFA devices in the IAM console, and MFA tokens are authentication mechanisms rather than cryptographic keys for data encryption and decryption.

## clf-c02/domain2/q806

Answer: D

VPC Flow Logs capture metadata about the IP traffic going to and from network interfaces in a VPC, providing visibility into traffic patterns for security analysis, compliance auditing, and connectivity troubleshooting.
Security groups act as stateful virtual firewalls at the EC2 instance level that control which traffic is allowed in and out based on defined rules, but they filter traffic rather than capturing or logging information about it. Elastic network interfaces are virtual network cards that attach to EC2 instances to provide network connectivity, and are a networking component rather than a feature for capturing or recording IP traffic data. Network ACLs act as stateless firewalls at the subnet level that allow or deny traffic based on IP address and port rules, but like security groups they filter traffic rather than capture or log information about it.

## clf-c02/domain2/q808

Answer: C, E

AWS KMS generates and manages encryption keys through a software-based, AWS-managed infrastructure, and AWS CloudHSM provides dedicated hardware security modules that give customers full control over key generation and management. Both services provide ways to generate encryption keys that can be used to encrypt data.
Amazon Macie uses machine learning to discover and classify sensitive data in Amazon S3, and is a data classification service rather than a key generation service that provides encryption keys for protecting data. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit, and does not generate general-purpose encryption keys for use in protecting customer data at rest. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and while it uses encryption to protect stored secrets, it is not a service that generates encryption keys for customers to use in their own data encryption workflows.

## clf-c02/domain2/q811

Answer: B

AWS CloudHSM provides dedicated, single-tenant hardware security modules within the AWS Cloud that meet FIPS 140-2 Level 3 compliance requirements, offering complete customer control over key generation and management on dedicated hardware for organizations with strict contractual or regulatory mandates.
AWS Secrets Manager stores, rotates, and manages secrets such as database credentials and API keys; it handles the secret lifecycle rather than providing dedicated hardware appliances. AWS KMS uses HSMs but shares the underlying hardware across customers, so it does not offer the dedicated single-tenant hardware that some contractual or regulatory requirements mandate. AWS Directory Service provides managed Microsoft Active Directory for identity management and single sign-on, with no connection to hardware security modules or key management.

## clf-c02/domain2/q812

Answer: B, E

Customers manage security group and ACL configurations to control inbound and outbound network access to their resources as part of securing their network environment, and are responsible for patching the guest operating system on EC2 instances including applying security updates and vulnerability patches.
Decommissioning physical storage devices including secure data erasure and physical destruction is entirely AWS's responsibility as part of managing the physical infrastructure in data centers that customers never access. Controlling physical access to AWS data centers including badge readers, biometrics, and surveillance is entirely AWS's responsibility as customers have no presence in or access to the facilities where AWS hardware is located. Patch management for the Amazon RDS instance operating system is AWS's responsibility as RDS is a managed service where AWS handles the underlying database engine patching, OS patching, and maintenance; customers only need to manage patching of databases they run on EC2 themselves.

## clf-c02/domain2/q815

Answer: D

When running applications in the AWS Cloud, users are responsible for managing application software updates, including patches, version upgrades, and security fixes for their own application code.
Managing physical hardware is entirely AWS's responsibility, as customers have no access to the underlying physical servers, networking equipment, or data center infrastructure that runs AWS services. Updating the underlying hypervisor is AWS's responsibility, as the virtualization layer that runs EC2 instances is part of the infrastructure that AWS owns and maintains on behalf of all customers. Providing a list of users approved for data center access is AWS's responsibility, as AWS manages all physical access controls to its data centers and customers have no role in determining who can enter AWS facilities.

## clf-c02/domain2/q819

Answer: C

Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts, CloudTrail event logs, VPC Flow Logs, and DNS logs using machine learning and threat intelligence to identify malicious activity and unauthorised behavior.
AWS CloudTrail records all API calls and management events in an AWS account for auditing and compliance purposes, and provides the raw activity data that GuardDuty analyzes, but CloudTrail itself does not identify or alert on malicious or unauthorised activities. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories including security checks for open ports and missing MFA, but does not continuously monitor for active threats or ongoing malicious behavior in accounts. Amazon Macie uses machine learning to discover and classify sensitive data stored in Amazon S3, and is a data classification and protection service rather than a real-time threat detection service monitoring account-wide activity.

## clf-c02/domain2/q822

Answer: C

When a customer runs a Docker container on Amazon EC2, AWS is responsible for the physical infrastructure layer, which includes performing hardware maintenance in the AWS facilities that run the AWS Cloud.
Scaling the web application and services developed with Docker is the customer's responsibility, as EC2-based container workloads require the customer to configure scaling through services such as EC2 Auto Scaling or Amazon ECS. Provisioning or scheduling containers to run on clusters and maintaining their availability is also the customer's responsibility when running Docker directly on EC2, as the customer manages the container runtime and orchestration layer rather than AWS. Managing the guest operating system including updates and security patches is the customer's responsibility for EC2 instances, as the Shared Responsibility Model places operating system management firmly with the customer for IaaS services.

## clf-c02/domain2/q824

Answer: A, D

Applying least privilege permissions ensures IAM users and roles have only the access they need to perform their tasks, and using IAM roles for applications running on EC2 instances avoids embedding long-term credentials in code. Both are IAM security best practices.
Sharing credentials between users contradicts IAM best practices; each user should have their own unique credentials to maintain individual accountability and allow precise permission scoping, and sharing credentials prevents tracking who performed which actions. Storing access keys in plaintext on EC2 instances is a security anti-pattern that risks credential exposure through instance metadata, log files, or shared access to the instance; IAM roles should be used instead to provide temporary credentials automatically. Using the root user account for all administrative tasks contradicts IAM best practices; the root account should be used only for tasks that specifically require it, and IAM users with appropriate permissions should be used for all regular administrative activities.

## clf-c02/domain2/q825

Answer: B

VPC Flow Logs capture metadata about IP traffic flowing to and from network interfaces in an Amazon VPC, recording information about source and destination IP addresses, ports, protocols, and whether traffic was allowed or rejected.
AWS CloudTrail records API calls and management events across an AWS account, capturing who made requests and what changes were made to AWS resources, but does not capture network-level packet flow data between instances the way VPC Flow Logs do. AWS Config continuously monitors and records AWS resource configurations and evaluates them against compliance rules, and is a configuration state tracking service rather than a network traffic capture and logging service. Amazon CloudWatch collects operational metrics, logs, and events from AWS resources and applications for monitoring and alerting purposes, and while it can collect application-level logs, it does not capture the IP traffic flow data between network interfaces that VPC Flow Logs provide.

## clf-c02/domain2/q828

Answer: A

Amazon CloudWatch can monitor for root user console sign-in events through CloudTrail integration, and can be configured to send alerts via SNS when the root user logs in, enabling security teams to detect and respond to unexpected root account access.
AWS CloudTrail records all API calls and management events including root user sign-ins, and is the source of the sign-in event data, but does not itself send alerts or notifications when specific events occur without integration with CloudWatch Events or EventBridge. AWS Config continuously monitors resource configurations and evaluates compliance, and while it tracks resource state changes, it is not used to send real-time alerts for specific account login events such as root user console sign-ins. AWS Artifact provides on-demand access to AWS compliance reports and certifications, and is a documentation portal with no capability to monitor or alert on AWS account activity or login events.

## clf-c02/domain2/q839

Answer: C, E

Customers are responsible for configuration management of their own applications, including how those applications are set up and maintained, and for configuring security groups that control network access to their resources. Both fall on the customer side of the shared responsibility model.
Infrastructure facilities access management refers to physical access controls for AWS data centers, which is entirely AWS's responsibility as customers have no access to or control over the physical facilities hosting their workloads. Cloud infrastructure hardware lifecycle management covers the procurement, maintenance, and decommissioning of physical servers and networking equipment, which AWS manages on behalf of all customers without any customer involvement. Networking infrastructure protection refers to securing the underlying global network that connects AWS Regions, Availability Zones, and edge locations, which is AWS's responsibility as part of its security of the cloud obligations.

## clf-c02/domain2/q843

Answer: B, C

AWS is responsible for protecting against IP spoofing and packet sniffing at the network level as part of securing the infrastructure, and for patching the underlying operating system of managed RDS instances as RDS is a fully managed service where AWS handles database engine and OS patching.
Running a virus scan on EC2 instances is the customer's responsibility as the customer manages the guest operating system and installed software on their EC2 instances, including security tooling to detect malicious software. Encrypting communication between EC2 instances and the Elastic Load Balancer requires customer configuration of SSL/TLS settings in the application and load balancer, as the customer controls their own application architecture and must choose to enable encrypted communications. Configuring security groups and network ACLs for EC2 instances is the customer's responsibility for defining which network traffic is allowed to and from their own compute resources within the VPC.

## clf-c02/domain2/q846

Answer: A

S3 Block Public Access is an account-level or bucket-level setting that overrides any policies or ACLs that would grant public access, ensuring no objects in the bucket can be made public regardless of how they are uploaded.
Holding a team meeting relies on human awareness and voluntary compliance, which does not technically enforce the restriction and cannot guarantee that public objects will never be uploaded. Requiring manual approval before uploading is not a native S3 feature and introduces an unscalable manual process that still does not technically prevent public objects from being created. Creating a custom monitoring service to detect and remove public uploads introduces unnecessary complexity, delay between upload and remediation, and relies on reactive rather than preventive controls, making it far less reliable than the built-in Block Public Access setting.

## clf-c02/domain2/q849

Answer: A

Patching the guest operating system for Amazon RDS is AWS's responsibility, as RDS is a fully managed database service where AWS handles all underlying infrastructure maintenance including OS patches and database engine updates.
The customer is not responsible for patching the guest OS in Amazon RDS because RDS abstracts the infrastructure layer completely; unlike EC2 where customers manage the operating system, RDS instances have their OS managed and patched by AWS as part of the managed service model. The AWS compliance team does not patch RDS operating systems; patching is performed by the RDS service engineering team as part of routine managed service maintenance, not by a compliance function within AWS. AWS Trusted Advisor provides recommendations and best practice checks across security, cost, performance, and fault tolerance, but does not perform operational tasks such as patching database instance operating systems.

## clf-c02/domain2/q855

Answer: C

Customers are responsible for installing operating system security patches on their Amazon EC2 instances, including any database software running on those instances, as the guest operating system falls within the customer responsibility boundary under the shared responsibility model.
Installing security patches for the Xen and KVM hypervisors is an AWS responsibility, as AWS owns and manages the virtualization layer that sits between the physical hardware and the customer's instances, and customers have no access to or visibility of the hypervisor. Installing operating system patches for Amazon DynamoDB is an AWS responsibility, as DynamoDB is a fully managed service where AWS handles all underlying infrastructure, operating system, and database engine maintenance on the customer's behalf. Installing operating system security patches for Amazon RDS database instances is an AWS responsibility, as RDS is a fully managed relational database service where AWS manages the operating system and database engine patching, leaving customers responsible only for their data and application-level configurations.

## clf-c02/domain2/q857

Answer: B

Under the Shared Responsibility Model, the customer is responsible for security and patching of the guest operating system on EC2 instances, including applying security updates and configuring the OS, as AWS only manages the infrastructure beneath the hypervisor.
AWS Support provides technical assistance and guidance to customers experiencing issues with their AWS environment, but is not responsible for patching or securing operating systems on customer instances. AWS Systems Manager can assist customers in automating patch management tasks on EC2 instances, but it is a tool that helps customers fulfill their own patching responsibility rather than shifting that responsibility to AWS. AWS Config records and evaluates configuration changes to AWS resources for compliance purposes, and does not perform or take responsibility for operating system patching on EC2 instances.

## clf-c02/domain2/q858

Answer: C

AWS Identity and Access Management is the service that allows you to create and manage AWS users and groups, assign permissions through policies, and control which users have access to which AWS services and resources securely.
Amazon Cognito is an identity service for web and mobile application users that enables sign-up, sign-in, and federated access with external identity providers, and is designed for application-level user management rather than managing AWS service access for administrators. AWS Single Sign-On, now called AWS IAM Identity Center, provides single sign-on access to multiple AWS accounts and applications using one set of credentials, and while it builds on IAM, the foundational service for creating and managing users and groups within AWS is IAM itself. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and integrates with IAM for AWS console access, but the primary service for creating and managing the users, groups, and access controls used within AWS itself is IAM.

## clf-c02/domain2/q859

Answer: B

AWS Artifact is the self-service portal that provides on-demand access to AWS security and compliance documentation including SOC reports, ISO certifications, PCI attestations, and other compliance materials available directly from the AWS console.
AWS Trusted Advisor provides automated recommendations and checks across security, cost, performance, and fault tolerance categories to help improve your AWS environment, and is an advisory service rather than a documentation and compliance report portal. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and produces customer-specific assessment findings rather than AWS security and compliance documentation. Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and is an observability and alerting service rather than a source of AWS compliance documentation.

## clf-c02/domain2/q862

Answer: C

AWS Trusted Advisor provides a report-style dashboard of check results across security, cost, performance, fault tolerance, and service limits, including key security checks such as MFA on root account, exposed access keys, and open security groups.
Amazon QuickSight is a business intelligence and data visualisation service for creating dashboards and reports from data sources, and while it can display data, it does not provide automated AWS security check results or account-level security status summaries. AWS CloudTrail trails record API calls and account activity for auditing purposes, and while they capture security-relevant events, they produce raw logs rather than a summarized status report of key security check findings. The IAM credential report lists all IAM users and the status of their credentials including password age, access key status, and MFA enablement, and while it is a useful security tool, it covers only IAM credential status rather than the broader set of key security checks that Trusted Advisor evaluates.

## clf-c02/domain2/q865

Answer: A

Using AWS Config to record, audit, and evaluate changes to resources is an example of enabling traceability, which is a core design principle of the Security pillar focused on monitoring and detective controls.
Operational Excellence focuses on running and improving operations through automation and responding to events, not on detective monitoring of resource changes for traceability. Performance Efficiency focuses on using computing resources efficiently to meet workload requirements as demand changes over time. Cost Optimization focuses on eliminating unnecessary spend and selecting the right resource types to reduce overall costs.

## clf-c02/domain2/q873

Answer: A, C

Customers are responsible for setting up server-side encryption on S3 buckets to protect data at rest, and for configuring network and firewall settings such as security groups and NACLs to control traffic to their resources. Both fall within the customer's side of the Shared Responsibility Model.
Amazon RDS instance patching is AWS's responsibility for managed database services, as AWS handles all engine-level patching and maintenance windows without customer involvement. Physical security of data center facilities is exclusively AWS's responsibility, covering the buildings, hardware, and environmental controls that customers have no access to. Compute capacity availability is AWS's responsibility, as AWS manages the underlying infrastructure to ensure that compute resources remain available for customers to provision and use.

## clf-c02/domain2/q880

Answer: C

Security groups act as a virtual firewall at the EC2 instance level, controlling inbound and outbound traffic for one or more instances by evaluating rules based on protocol, port, and source and destination.
Access keys are long-term credentials consisting of an access key ID and secret used for programmatic access to AWS via the CLI or API, and are an authentication mechanism with no connection to network traffic control. Virtual private gateways are the AWS-side endpoint of a site-to-site VPN connection that enables encrypted communication between a VPC and an on-premises network, and are a connectivity component rather than a traffic filtering mechanism at the instance level. Access Control Lists operate as stateless firewalls at the subnet level rather than the instance level, applying inbound and outbound rules to all traffic entering or leaving a subnet without tracking connection state the way security groups do.

## clf-c02/domain2/q883

Answer: B

AWS Organizations Service Control Policies allow organizations to define and enforce the maximum permissions available to all accounts within an organization or specific organizational units, restricting which AWS services, resources, and API actions users in those accounts can access.
AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules to block common web exploits such as SQL injection and cross-site scripting, and operates at the application traffic layer rather than restricting access to AWS services and API actions for IAM users. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is a detection and alerting service rather than a service that restricts which AWS services and API actions users can invoke. AWS Firewall Manager centrally manages AWS WAF rules, Shield protections, and security group policies across multiple accounts in an organization, and is a security management layer rather than a service that enforces IAM-level API action restrictions.

## clf-c02/domain2/q884

Answer: A

AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports, certifications, and agreements, making it the best resource for users seeking compliance-related information and documentation about AWS.
AWS CloudTrail records all API calls and management events in an AWS account for auditing and forensic purposes, and is an activity logging service rather than a source of compliance reports or certification documentation about AWS infrastructure. The Amazon Inspector console provides vulnerability assessment findings for EC2 instances and container images, and is a security assessment tool for customer workloads rather than a repository of AWS-level compliance information and reports. AWS Support provides technical assistance and guidance for using AWS services, and while support engineers can answer compliance-related questions, the self-service repository for compliance documentation and formal reports is AWS Artifact.

## clf-c02/domain2/q889

Answer: C

AWS KMS manages encryption keys and integrates natively with CloudTrail to encrypt log files stored in S3, ensuring that CloudTrail log data is protected at rest using KMS-managed keys.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and end users, and is a certificate management service rather than a service for encrypting data received and stored by CloudTrail. Amazon Macie uses machine learning to discover and classify sensitive data stored in S3, and while it can identify sensitive content in CloudTrail logs stored in S3, it does not perform the encryption of that data. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to encrypt data stored by CloudTrail or any other AWS service.

## clf-c02/domain2/q895

Answer: C

Amazon Macie uses machine learning to automatically discover and classify sensitive data in Amazon S3 including personally identifiable information and user credentials, detecting potential data leaks and inadvertent exposure of sensitive data.
Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and focuses on detecting security threats rather than identifying specific sensitive data types stored in S3. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and network misconfigurations, and does not classify or detect sensitive data such as PII stored in S3. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service with no capability to discover or detect data leaks of personally identifiable information.

## clf-c02/domain2/q898

Answer: C

Disabling and removing unnecessary IAM user credentials including inactive access keys and old passwords reduces the attack surface by eliminating credentials that could be exploited if compromised, making it an IAM security best practice.
Assigning the same permissions to all IAM users regardless of their roles violates the principle of least privilege and creates unnecessary risk by giving every user access to resources they do not need, which is an anti-pattern rather than a security best practice. Creating access keys for all IAM users by default creates unnecessary long-term credentials for users who may only need console access, increasing the risk of credential exposure without a corresponding operational benefit. Using a single shared IAM user for all team members removes individual accountability and prevents identifying which specific person performed an action, contradicting the IAM best practice of using individual accounts with unique credentials.

## clf-c02/domain2/q901

Answer: A

AWS Shield Advanced provides expanded DDoS protection with real-time attack visibility, access to the DDoS Response Team, and cost protection for scaling costs incurred during attacks, meeting the requirements for protection against expanded DDoS attacks with dedicated response assistance.
AWS WAF filters HTTP and HTTPS traffic at the application layer based on configurable rules, and while it helps mitigate application-layer attacks and integrates with Shield Advanced, it does not on its own provide the expanded DDoS protection and dedicated response team access that the question requires. Amazon GuardDuty detects threats and malicious activity in AWS accounts using machine learning, and while it can identify DDoS-related anomalies, it is a detection service rather than an active DDoS mitigation service with a dedicated response team. AWS Trusted Advisor provides automated security, cost, performance, and fault tolerance recommendations, and is an advisory tool with no capability to protect against or respond to distributed denial of service attacks.

## clf-c02/domain2/q903

Answer: D, E

Customers are responsible for securing data in transit by implementing encryption such as TLS/SSL to protect data as it moves between systems, and for data integrity authentication to verify that data has not been tampered with. Both fall within the customer's side of the Shared Responsibility Model.
Physical and environmental security of data centers is exclusively AWS's responsibility, covering the buildings, power, cooling, and physical access controls that customers have no involvement in. Physical network devices including firewalls are AWS's responsibility, as customers manage virtual networking constructs such as security groups and NACLs but have no access to the underlying physical network hardware. Storage device decommissioning is AWS's responsibility, as AWS manages the secure disposal and destruction of physical storage media when it reaches end of life.

## clf-c02/domain2/q906

Answer: C

An IAM role attached to an EC2 instance provides temporary security credentials to applications running on that instance, allowing them to make authenticated AWS API calls to S3 without requiring hardcoded access keys in the application code.
AWS CloudTrail records API calls and management events for auditing purposes, and while it logs the S3 write operations, it does not itself grant the permissions or credentials that allow an application to authenticate and write data to S3. An S3 bucket policy can grant permissions for a specific EC2 instance to write to a bucket, but the instance still needs valid AWS credentials to authenticate those requests, and an IAM role attached to the instance is the recommended way to provide those credentials securely. An IAM user with programmatic access could provide access keys for the application to use, but storing long-term access keys in application code or on the instance is a security anti-pattern; IAM roles provide temporary credentials automatically and are the recommended approach.

## clf-c02/domain2/q912

Answer: A, C

Closing an AWS account and changing the AWS Support plan are tasks that can only be performed by the root user, as these are account-level actions that AWS reserves exclusively for the account owner to prevent unauthorised changes to fundamental account settings.
Creating a new IAM policy can be performed by any IAM user or role that has been granted the appropriate IAM permissions, and does not require root user credentials. Attaching a role to an Amazon EC2 instance can be performed by any IAM user or role with the necessary EC2 and IAM permissions, and is a routine operational task that does not require root access. Generating access keys for IAM users can be performed by IAM administrators with the appropriate permissions, and is not restricted to the root user account.

## clf-c02/domain2/q917

Answer: C

AWS Artifact provides on-demand access to AWS compliance reports such as PCI DSS and SOC reports, and AWS agreements such as the Business Associate Addendum, making it the purpose-built service for companies requiring compliance documentation when handling sensitive data like credit card information.
AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate management service with no capability to provide compliance reports or AWS agreements. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and is a resource configuration auditing tool rather than a repository of AWS compliance documentation and agreements. AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and captures operational audit logs rather than providing access to AWS compliance reports or legal agreements.

## clf-c02/domain2/q919

Answer: B

AWS CloudTrail records all API calls and account activity including unauthorised or unusual API calls, making it the correct service for tracking API calls that may indicate unauthorised access or activity in an AWS environment.
Amazon CloudWatch monitors operational metrics, logs, and events for AWS resources and applications, and while CloudWatch can receive CloudTrail events and trigger alarms, it does not itself track or record API call history to identify unauthorised API actions. Amazon Detective analyzes and visualises security data from multiple sources to investigate the root cause of suspicious activity, and uses CloudTrail data as one of its inputs, but is an investigation tool that builds on top of CloudTrail rather than performing the original API call recording. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and is an advisory tool rather than a service that tracks or records API activity.

## clf-c02/domain2/q920

Answer: B

AWS Config continuously monitors resource configurations, evaluates them against compliance rules, tracks changes over time, and sends notifications when resources change or become non-compliant, making it the purpose-built service for ongoing audit, compliance evaluation, and change notification requirements.
AWS Trusted Advisor inspects your AWS environment and provides automated recommendations across security, cost, performance, and fault tolerance, but delivers periodic advisory checks rather than continuously tracking individual resource configuration changes and sending notifications when specific resources become non-compliant. AWS Resource Access Manager enables sharing of AWS resources such as subnets and Transit Gateways across AWS accounts within an organization, and is a resource sharing service with no capability to audit configurations or notify on compliance violations. AWS Systems Manager provides operational tools for managing and automating tasks across AWS resources including patching, parameter storage, and run commands, and while it can automate remediation it does not continuously evaluate resource configurations against compliance rules or send notifications when resources change.

## clf-c02/domain2/q924

Answer: B

Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data including PII stored in Amazon S3, providing visibility into data security risks and detecting potential data leaks.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not discover or classify sensitive data stored in Amazon S3. Amazon GuardDuty is a threat detection service that monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning and threat intelligence, and is a threat detection service rather than a data classification and protection service for sensitive data in S3. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a secrets lifecycle management service rather than a service for automatically discovering and classifying sensitive data stored in S3.

## clf-c02/domain2/q928

Answer: C

AWS Security Bulletins provide timely notifications about newly discovered security vulnerabilities and recommended remediation actions for AWS services, making them the most effective resource for staying up to date on AWS security announcements.
The AWS Health Dashboard provides personalized alerts about events that may affect a customer's specific AWS resources and service availability, and while it includes health events for security issues, the dedicated source for proactive AWS security announcements and vulnerability disclosures is the AWS Security Bulletins page. AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no connection to security announcements or vulnerability notifications. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities, and generates findings about the customer's own resources rather than providing AWS-level security announcements.

## clf-c02/domain2/q931

Answer: C

AWS Artifact provides on-demand access to AWS security and compliance reports including SOC, PCI DSS, ISO, and HIPAA documentation, available for download directly from the AWS Management Console without contacting AWS.
Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability and alerting service rather than a repository of AWS security and compliance reports. AWS CloudTrail records all API calls and management events across an AWS account for auditing purposes, and produces customer-specific activity logs rather than AWS security certification and compliance documentation. Amazon GuardDuty is a threat detection service that continuously monitors accounts and workloads for malicious activity, and is a real-time security monitoring service rather than a source of downloadable compliance reports.

## clf-c02/domain2/q936

Answer: A

AWS Artifact provides on-demand access to AWS compliance reports and certifications such as SOC 2 documents, allowing auditors and customers to download them directly from the console without requesting them through AWS Support.
AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories for improving an AWS environment, and is an advisory tool rather than a compliance documentation repository. AWS Config continuously monitors and records resource configurations against compliance rules, and is a resource configuration compliance evaluation service rather than a portal for downloading AWS-level compliance certifications. Amazon S3 is an object storage service for storing and retrieving data, and while AWS Artifact downloads documents stored in S3 on the backend, S3 itself is not the portal customers use to find and download compliance documentation.

## clf-c02/domain2/q941

Answer: A

The Principal element in an S3 bucket policy specifies who is allowed or denied access, and holds the user, account, role, or service details that describe the identity being granted or denied permissions.
Action specifies which S3 operations are permitted or denied, such as s3:GetObject or s3:PutObject, and defines what the principal can do rather than identifying who the principal is. Resource specifies which S3 bucket or objects the policy applies to, identifying the target of the policy rather than the identity being granted access. Statement is the top-level container element that wraps the individual policy blocks including Principal, Action, Effect, and Resource, and is the structural wrapper rather than the element that holds user details.

## clf-c02/domain2/q945

Answer: D

AWS is responsible for the security of the underlying infrastructure including the data center physical security, hardware, and the software that runs the hypervisor and global network components, as these are outside the customer's control.
Managing application access rights for users accessing customer-built applications is the customer's responsibility, as customers control who can access their applications through application-level authentication and authorisation mechanisms. Keeping the operating system on Amazon EC2 instances up to date by applying security patches is the customer's responsibility, as the guest OS running inside EC2 virtual machines must be maintained by the customer who has administrative access to it. Configuring client-side data encryption to protect data before it is sent to AWS services is the customer's responsibility for data that requires end-to-end protection, as the customer controls the encryption process on their own systems before data leaves their environment.

## clf-c02/domain2/q954

Answer: B

AWS Config continuously monitors and records configuration changes to AWS resources and evaluates those changes against compliance rules, identifying non-compliant resources and enabling auditing of the configuration history for compliance purposes.
Amazon CloudWatch monitors operational metrics, logs, and events for performance and observability, and while it can trigger alarms on unusual activity, it does not track resource configuration changes or evaluate compliance against desired configuration states. AWS CloudTrail records all API calls and management events for auditing, and while it logs who made configuration changes and when, it does not evaluate whether those configurations comply with defined rules the way Config does. Amazon Inspector is an automated vulnerability assessment service for EC2 instances and container images that identifies software vulnerabilities and unintended network access, and is not a resource configuration tracking and compliance evaluation service.

## clf-c02/domain2/q959

Answer: A, E

Granting the developer access only to the resources needed follows the principle of least privilege, and ensuring a minimum password length enforces credential security requirements. Both are IAM security best practices for onboarding new developers.
Sharing the AWS account root user credentials with any individual is a critical security violation, as the root user has unrestricted access to all AWS services and resources and should be protected and used only for tasks that specifically require it. Adding the developer to the administrator's group grants unrestricted access to all AWS services and resources, which directly violates the principle of least privilege and is not a security best practice for a new developer whose access requirements are specific to their role. Configuring a password policy that prevents the developer from changing their own password is a security anti-pattern, as the ability to change passwords is necessary for credential hygiene and periodic rotation.

## clf-c02/domain2/q962

Answer: B

Maintaining physical and environmental controls, including data center power, cooling, fire suppression, and physical security, becomes AWS's responsibility once a workload is migrated to the cloud.
Patching the guest operating system remains the customer's responsibility after migration to AWS. For services such as EC2, customers retain full control over the operating system and are responsible for applying updates and patches. Protecting communications and maintaining zone security is a shared responsibility that customers retain ownership of, including configuring network security controls such as security groups, network ACLs, and encryption in transit for their applications. Patching specific applications is always the customer's responsibility regardless of the deployment model, as AWS has no visibility into the application software customers choose to run on their infrastructure.

## clf-c02/domain2/q969

Answer: C

IAM password policies allow administrators to enforce password complexity requirements such as minimum length, character type requirements, and expiration intervals, ensuring all IAM users must create passwords that meet the defined standards.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a secrets lifecycle management service rather than a tool for setting password complexity requirements for AWS Management Console users. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and has no capability to enforce password requirements for AWS console users. AWS Directory Service provides managed Microsoft Active Directory for enterprise identity management and domain joining, and while it can enforce password policies for Active Directory users, the correct service for enforcing password requirements for IAM users accessing the AWS Management Console is the IAM password policy.

## clf-c02/domain2/q970

Answer: A

Managing application data encryption and configuring security for their own applications are customer responsibilities under the shared responsibility model, as customers control their own data and application layer while AWS manages the underlying infrastructure.
Securing the infrastructure that runs all AWS Cloud services including physical servers, networking hardware, and data center facilities is entirely AWS's responsibility as part of the security of the cloud. Providing the physical security of global data centers including perimeter access controls, surveillance, and environmental protections is entirely AWS's responsibility as customers never have access to the physical facilities. Maintaining the hardware that provides the foundation of the global infrastructure including servers, storage devices, and networking equipment is entirely AWS's responsibility as part of owning and operating the physical cloud infrastructure.

## clf-c02/domain2/q971

Answer: D

Deploying applications on the correct services in compliance with PCI DSS requirements is the customer's responsibility, as customers must choose PCI-eligible AWS services and configure them correctly to meet the applicable PCI DSS controls on the customer's side of the shared responsibility model.
AWS does not ensure that all physical facilities and data centers meet PCI requirements on the customer's behalf; rather, AWS obtains and maintains PCI DSS certification for its infrastructure, and this certification is available to customers through AWS Artifact as evidence that the underlying platform is PCI-compliant. AWS does not patch all AWS systems used in the environment on the customer's behalf; for managed services AWS handles patching, but for services like EC2 the customer is responsible for patching the guest operating system and any installed software. Configuring network ACLs on AWS on the customer's behalf is not an AWS responsibility; customers configure their own VPC network ACLs to control traffic as part of their PCI-compliant network security architecture.

## clf-c02/domain2/q977

Answer: A, C

AWS Shield provides automatic DDoS mitigation at the network and transport layers, and Amazon CloudFront absorbs and distributes traffic at edge locations, reducing the impact of volumetric attacks before they reach the application origin. Both help protect against DDoS attacks.
AWS CloudTrail records API calls and management events for auditing purposes, and while it logs account activity, it has no capability to detect or mitigate active DDoS attacks against a web application. AWS Support Center is a portal for submitting and managing support cases, and is not a technical service that provides protection against or mitigation of DDoS attacks. The AWS Health Dashboard provides real-time and historical status information about AWS services and personalized event alerts, and is a monitoring and notification tool rather than a service that actively protects applications from DDoS attacks.

## clf-c02/domain2/q978

Answer: D

AWS Artifact provides on-demand, self-service access to AWS compliance control reports including SOC, PCI, ISO, and HIPAA documentation directly from the AWS Management Console without requiring a request through AWS Support.
AWS Config tracks the configuration state of resources and audits how those configurations change over time, and is a resource configuration auditing service rather than a portal for downloading compliance control reports. Amazon GuardDuty is a threat detection service that uses machine learning to monitor accounts and workloads for malicious activity, and is security focused rather than a compliance documentation portal. AWS Trusted Advisor inspects an account and provides best practice recommendations across cost optimization, performance, security, fault tolerance, and service limits, and is an advisory tool rather than a source of compliance control reports.

## clf-c02/domain2/q979

Answer: B, E

An IAM policy that grants Amazon RDS access can be attached directly to the specific IAM user, limiting that employee's AWS permissions to only the RDS actions specified in the policy and no other services.
Creating a separate AWS account for the user would be an excessive measure for granting one employee RDS access, as it introduces administrative overhead for account management and does not simplify access control compared to using an IAM policy within the existing account. Creating an IAM user with full administrator access would grant unrestricted access to all AWS services and resources, directly violating the principle of least privilege and creating unnecessary security risk for a user who only needs access to RDS. Placing all existing IAM users into a new IAM group with RDS access would grant RDS permissions to the entire user population rather than limiting access to the single employee who requires it, which contradicts the goal of providing targeted access.

## clf-c02/domain2/q980

Answer: A

AWS Config records configuration changes, evaluates them against compliance rules, and can trigger automated remediation actions when resources become non-compliant, meeting all three requirements of recording, evaluating, and remediating.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to record configuration changes or trigger compliance remediation. AWS CloudTrail logs all API calls and account activity for auditing purposes, and while it records who made changes and when, it does not evaluate resources against compliance rules or trigger remediation actions. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and offers advisory guidance rather than automated compliance rule evaluation or remediation capability.

## clf-c02/domain2/q984

Answer: B

Patching the database and operating system on EC2-hosted databases is the customer's responsibility when using Amazon RDS is a managed service where AWS handles patching; however the question asks about RDS specifically. Under the RDS model, configuring security groups to control network access to the RDS instance is the customer's responsibility as customers define which EC2 instances and IP addresses can connect to their database.
Installing the database software on the underlying server is not the customer's responsibility for Amazon RDS; AWS manages the database engine installation, configuration, and updates as part of the fully managed service offering. Patching the underlying operating system of the RDS instance is AWS's responsibility; RDS is a managed service where AWS performs OS and database engine patching automatically without customer involvement. Replacing failed database hardware is AWS's responsibility as part of managing the physical infrastructure; customers benefit from AWS's hardware redundancy and replacement processes transparently without any action required on their part.

## clf-c02/domain2/q985

Answer: B

AWS Lambda is a serverless compute service where AWS manages the underlying infrastructure, and the customer's responsibility is limited to managing their application code, including writing, deploying, and maintaining the functions that run on the platform.
Operating system configuration is AWS's responsibility for Lambda, as the service abstracts away the underlying compute infrastructure entirely and customers have no access to or control over the operating system. Platform management is also AWS's responsibility for Lambda, as AWS handles the runtime environment, scaling, availability, and maintenance of the serverless platform on the customer's behalf. Code encryption is not a customer responsibility in the sense described, as AWS encrypts Lambda function code at rest by default, and while customers can optionally use their own KMS keys, encryption is handled automatically by AWS rather than being a customer-managed task.

## clf-c02/domain2/q992

Answer: D

AWS Trusted Advisor identifies potential security vulnerabilities by checking for common misconfigurations such as unrestricted security group access, missing MFA on the root account, and publicly accessible S3 buckets, helping customers address security weaknesses proactively.
Amazon Detective is an investigation service that analyzes security data from GuardDuty, CloudTrail, and VPC Flow Logs to help security teams investigate the root cause of suspicious activity, and is a forensic investigation tool rather than a service for identifying security vulnerabilities in an AWS account configuration. Amazon Macie uses machine learning to discover and classify sensitive data in Amazon S3, and is a data classification service for detecting potential data exposure rather than a tool for auditing account-wide security configurations and vulnerabilities. AWS Shield provides managed DDoS protection at the network and transport layers, and is a traffic protection service rather than a security vulnerability identification tool.

## clf-c02/domain2/q997

Answer: B

AWS Artifact provides on-demand access to AWS compliance reports including SOC, PCI, ISO, and other certifications, available for download directly from the AWS Management Console.
AWS Secrets Manager stores, rotates, and manages access to secrets such as database credentials and API keys, and is a credentials management service with no capability to retrieve or provide compliance documentation. AWS Security Hub provides a centralized view of security alerts and compliance status across an AWS environment by aggregating findings from multiple security services, and is a security posture management tool rather than a repository of AWS compliance reports. AWS Certificate Manager provisions and manages SSL/TLS certificates for encrypting data in transit between applications and users, and is a certificate management service with no connection to compliance report retrieval.

## clf-c02/domain2/q998

Answer: B

AWS WAF protects web applications behind Application Load Balancers from common exploits like SQL injection and cross-site scripting by filtering malicious HTTP requests based on custom rules.
Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior, and is a detection and alerting service rather than a tool for filtering malicious web requests at the application layer. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool with no capability to intercept or block malicious web traffic. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a vulnerability scanning tool rather than a web traffic filtering service.

## clf-c02/domain2/q1001

Answer: C

The IAM credential report is a downloadable CSV file that lists all IAM users in the account along with the status of their credentials including passwords, access keys, MFA devices, and last-used timestamps, providing exactly what is needed for a user access audit.
AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules, and is a resource configuration compliance tool rather than an IAM user listing service. Amazon CloudWatch monitors operational metrics and logs for AWS resources and applications, and is an observability service rather than a source of IAM user account information or credential status reports. AWS CloudTrail records all API calls and management events including IAM-related actions, and while it logs who created users and when, it does not provide a current consolidated list of all users and their credential status in the way the credential report does.

## clf-c02/domain2/q1004

Answer: C

AWS Config continuously monitors and records resource configuration changes and evaluates them against compliance rules, generating a complete history of configuration changes that auditors and compliance teams can use to demonstrate adherence to standards.
AWS CloudTrail records all API calls and account activity for auditing and forensic purposes, and while it captures who made configuration changes and when, it does not evaluate whether those configurations comply with defined rules or provide the configuration state history that Config does. Amazon Inspector is an automated vulnerability assessment service for EC2 instances and container images that identifies software vulnerabilities and network misconfigurations, and is a security scanning tool rather than a resource configuration tracking and compliance evaluation feature. AWS Trusted Advisor provides automated recommendations across security, cost, performance, and fault tolerance categories, and is an advisory tool rather than a resource configuration change tracking and compliance evaluation service.

## clf-c02/domain2/q1006

Answer: D

The principle of least privilege requires granting only the permissions necessary for a user to perform their specific job function, which means applying IAM policies only to the users who actually require those permissions rather than broadly assigning permissions across all users.
Applying an IAM policy to an IAM group and limiting the size of the group addresses group management rather than least privilege, as the size of a group has no bearing on whether permissions are appropriately scoped to what users actually need. Requiring MFA for all IAM users is an authentication security best practice that protects against compromised credentials, but it does not relate to scoping permissions to the minimum required level. Requiring IAM users with different permissions to have multiple passwords conflates authentication with authorisation, and having multiple passwords does not control or limit what actions a user is permitted to perform.

## clf-c02/domain2/q1010

Answer: C

AWS WAF is a web application firewall that inspects HTTP and HTTPS traffic and can be configured with rules to detect and block SQL injection attempts before they reach the application.
Amazon VPC provides network isolation and security controls at the infrastructure level through security groups and network ACLs, but does not inspect application-layer HTTP traffic content for SQL injection patterns the way WAF does. AWS Shield provides managed DDoS protection at the network and transport layers to defend against volumetric attacks, and is not designed to inspect or block application-layer exploits such as SQL injection. AWS CloudTrail records API calls and management events for auditing purposes, and while it logs activity in the AWS environment, it does not inspect web application traffic or block SQL injection attacks.

## clf-c02/domain2/q1104

Answer: C

AWS Audit Manager continuously collects evidence from AWS services, maps it to compliance framework controls such as PCI DSS and GDPR, and organizes it into audit-ready reports, automating much of the manual effort involved in compliance assessments.
AWS Artifact provides on-demand access to AWS compliance reports and certifications such as SOC and ISO documents, but it does not assess a customer's own environment or collect evidence for customer-specific compliance audits. AWS Config records and evaluates resource configurations against compliance rules, and while it contributes evidence that Audit Manager can consume, it does not itself organize findings into structured audit reports mapped to compliance frameworks. Amazon Inspector scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a vulnerability scanning tool rather than a compliance audit evidence collection service.

## clf-c02/domain2/q1105

Answer: B

AWS Audit Manager automates evidence collection from multiple AWS sources including CloudTrail logs, Config evaluations, and Security Hub findings, and organizes this evidence into assessment reports that map directly to compliance framework requirements, significantly reducing audit preparation effort.
AWS CloudTrail records API calls and management events across an AWS account for auditing and forensic analysis, but it captures raw activity logs rather than organizing them into structured compliance assessment reports. AWS Trusted Advisor provides automated best-practice checks across security, cost, performance, and fault tolerance categories, but delivers advisory recommendations rather than structured audit evidence mapped to compliance frameworks. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services into a centralized dashboard, but it is a security posture management tool rather than a compliance audit preparation and evidence collection service.

## clf-c02/domain3/q001

Answer: D

The AWS Management Console is the web-based graphical interface used to manage and interact with AWS resources directly from a browser.
The AWS CLI is a command-line tool that allows users to interact with AWS services through typed commands in a terminal, not through a web-based graphical interface. The AWS API provides programmatic access to AWS services through HTTP requests made directly by applications or scripts, and has no graphical user interface. The AWS SDK provides libraries and tools for interacting with AWS services through application code in languages such as Python, Java, and JavaScript, and is not a user-facing interface for managing resources.

## clf-c02/domain3/q002

Answer: D

Horizontal scaling means adding more instances of the same size to distribute load, while vertical scaling means increasing the capacity of a single instance.
Replacing an existing instance with a larger one is vertical scaling, not horizontal. Increasing the compute capacity of a single instance describes vertical scaling, which is the opposite of horizontal scaling. Adding more RAM to a single instance is another form of vertical scaling, as it increases the power of one instance rather than adding more instances.

## clf-c02/domain3/q007

Answer: C

Deploying across multiple Regions and Availability Zones provides the highest level of availability by protecting against both Availability Zone-level failures and Region-level failures simultaneously.
Deploying across multiple Availability Zones and edge locations adds content delivery reach through CloudFront but does not protect application infrastructure against a Regional failure. Deploying across multiple Availability Zones and subnets improves resilience against isolated failures within a Region, but a Regional outage would still affect the entire deployment. Deploying across multiple VPCs and subnets creates network segmentation within a Region but provides no geographic redundancy against Availability Zone or Regional failures.

## clf-c02/domain3/q008

Answer: A, E

AWS Snowball Edge includes built-in compute capabilities that allow customers to process and analyze data locally before transferring it to AWS, and securely transfers large amounts of data into and out of AWS using a rugged physical appliance.
A catalog of third-party software solutions describes AWS Marketplace, which is a digital catalog for finding and deploying software from independent vendors. A hybrid cloud storage between on-premises environments and AWS describes AWS Storage Gateway, which provides ongoing hybrid connectivity between local environments and AWS cloud storage. An exabyte-scale data transfer service describes AWS Snowmobile, which is a separate Snow Family service designed for migrating extremely large datasets using a secure shipping container rather than an appliance.

## clf-c02/domain3/q012

Answer: B

AWS Database Migration Service is purpose-built for migrating databases to AWS with minimal downtime, keeping the source database fully operational throughout the migration process.
AWS OpsWorks (deprecated) is a configuration management service using Chef and Puppet for automating server configuration and has no capability for database migration. AWS Server Migration Service is designed for migrating virtual machines from on-premises environments to AWS, not for migrating databases. AWS Application Discovery Service helps plan migrations by collecting data about on-premises servers and dependencies, but does not perform the actual migration of databases or any other workloads.

## clf-c02/domain3/q018

Answer: A, B

EBS snapshots create point-in-time backups of your volume stored durably in Amazon S3, allowing data to be restored if a volume is lost or corrupted. Enabling encryption at rest protects the data stored on EBS volumes from unauthorised access using AWS KMS managed keys.
Replicating EBS volumes across multiple Availability Zones improves availability but does not protect against accidental deletion or data corruption, as a replicated volume would reflect the same corrupted state. Using AWS Backup automates backup management across multiple AWS services but is not itself a direct method of keeping EBS data safe without also taking snapshots. Increasing the size of an EBS volume adds storage capacity but has no effect on data protection or security.

## clf-c02/domain3/q021

Answer: C

CloudFront delivers content from edge locations, a global network of points of presence that cache content close to end users to minimize latency.
AWS Global Accelerator also uses the AWS global network to improve performance for global users, but it routes traffic to optimal regional endpoints rather than caching content at edge locations, making it a different service with a different mechanism. AWS Regions are geographic areas containing multiple Availability Zones where customers deploy workloads, and CloudFront does not distribute content by routing requests to a Region in the way a standard application deployment would. AWS Availability Zones are isolated data center clusters within a Region used for redundancy and fault tolerance, and are not the mechanism CloudFront uses to cache and serve content to global users.

## clf-c02/domain3/q024

Answer: C

Amazon S3 Glacier Deep Archive is the lowest-cost AWS storage class, designed for data that is rarely accessed and can tolerate retrieval times of hours, making it ideal for compliance archives that may never be needed.
S3 Intelligent-Tiering automatically moves data between access tiers based on usage patterns, but it is better suited for data with unpredictable access frequency rather than data that is known upfront to be rarely accessed. Amazon S3 Standard provides low-latency, high-throughput object storage for frequently accessed data, making it more expensive than necessary for videos that will rarely if ever be retrieved. Amazon EBS provides block storage volumes attached to EC2 instances for active workloads, and is not a cost-effective solution for long-term archival of infrequently accessed video files.

## clf-c02/domain3/q025

Answer: A

Amazon Route 53 is the scalable and highly available Domain Name System service provided by AWS, used to route end users to applications by translating domain names to IP addresses.
AWS Config continuously tracks and records the configuration of AWS resources to assess compliance and detect changes, and has no DNS or traffic routing capability. Amazon CloudFront is a content delivery network that caches and distributes content at edge locations worldwide to reduce latency, and while it works alongside Route 53 in many architectures it is a content delivery service rather than a DNS service. Amazon EMR is a managed cluster platform for processing large volumes of data using big data frameworks such as Hadoop and Spark, and has no connection to DNS or network routing.

## clf-c02/domain3/q027

Answer: D

Amazon ElastiCache is an in-memory caching service that provides sub-millisecond response times for frequently accessed data, making it the purpose-built solution for optimizing application response time in a two-tier web architecture.
AWS OpsWorks (deprecated) is a configuration management service that automates server setup and maintenance using Chef and Puppet, and has no capability to store data or improve application response times through caching. AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage integration, and is a storage bridging service rather than a low-latency caching layer for web application data. Amazon EBS provides persistent block storage volumes that attach directly to EC2 instances for low-latency disk access, and while it offers faster access than object storage, it does not provide the sub-millisecond in-memory performance that ElastiCache delivers for frequently accessed data.

## clf-c02/domain3/q030

Answer: D

Amazon CloudFront is AWS's global CDN service that caches and delivers content from edge locations worldwide, reducing latency for end users regardless of their location.
AWS VPN creates encrypted network connections between on-premises infrastructure and AWS over the public internet, and has no content delivery or caching capability. AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, and is a connectivity service rather than a content delivery network. AWS Regions are geographic areas containing multiple Availability Zones where AWS infrastructure is hosted, and are a component of global infrastructure rather than a CDN service.

## clf-c02/domain3/q033

Answer: B

Amazon DynamoDB is a fully managed NoSQL key-value and document database designed for applications that need fast, flexible, schema-less data storage.
Amazon Aurora is a fully managed relational database compatible with MySQL and PostgreSQL that uses structured schemas and SQL, and does not support NoSQL data models. Amazon Elastic Block Store provides block storage volumes that attach to EC2 instances for use as persistent disks, and is a storage service with no database capability of any kind. Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is not a NoSQL database.

## clf-c02/domain3/q039

Answer: A, B

Elastic Load Balancing automatically detects unhealthy instances and stops sending traffic to them, while Auto Scaling automatically replaces failed instances, together eliminating single points of failure through automated detection and recovery.
Amazon Athena is a serverless query service for analyzing data stored in S3 using standard SQL and has no role in detecting or recovering from infrastructure failures. Amazon Elastic Container Registry is a managed container image registry for storing and managing Docker images, unrelated to failure detection or automated recovery. Amazon EC2 provides the virtual server instances themselves but does not natively automate the detection of or response to failures without ELB and Auto Scaling configured around it.

## clf-c02/domain3/q040

Answer: D

Amazon CloudFront is a CDN that caches video content at edge locations around the world, delivering it to viewers from the nearest location and achieving high transfer speeds globally.
Amazon SNS is a pub/sub messaging service for sending notifications to multiple subscribers and has no role in delivering or streaming video content globally. Amazon Kinesis Video Streams ingests and processes live video streams from devices for real-time analysis and storage, but is not a content delivery service for distributing pre-recorded video to global audiences with high transfer speeds. AWS CloudFormation is an infrastructure-as-code service for provisioning AWS resources through templates, and has no capability to deliver or accelerate content to global users.

## clf-c02/domain3/q041

Answer: B

Amazon Aurora is a MySQL-compatible managed relational database that automatically handles backups, replication, and failover, unlike running MySQL on EC2 where the customer manages everything themselves.
A MySQL database installed on an EC2 instance is a self-managed deployment where the customer is responsible for configuring and running their own backup processes, with no automated backup capability provided by AWS. Amazon DynamoDB is a fully managed NoSQL key-value and document database that is not MySQL-compatible and is not suited to replacing a relational MySQL database layer. Amazon Neptune is a fully managed graph database service designed for highly connected datasets such as social networks and knowledge graphs, and is not a relational database option for MySQL workloads.

## clf-c02/domain3/q042

Answer: A

AWS CloudFormation lets you define your entire AWS infrastructure as code using JSON or YAML templates, enabling repeatable and automated provisioning of resources without manual configuration.
AWS Config continuously monitors and records the configuration state of AWS resources and evaluates them against desired settings, but it does not provision or manage infrastructure. Amazon SES is a cloud-based email sending and receiving service, entirely unrelated to infrastructure management. Amazon EMR is a managed big data processing service for running frameworks such as Apache Spark and Hadoop, unrelated to infrastructure as code.

## clf-c02/domain3/q044

Answer: A, E

AWS Health Dashboard provides a personalized view of how AWS service events affect your specific resources, and detailed troubleshooting guidance to help you respond to and resolve those events.
Health checks for Auto Scaling instances are a feature of Amazon EC2 Auto Scaling that monitors instance health and replaces unhealthy instances automatically, and are not a capability of the AWS Health Dashboard. Recommendations for cost optimization are provided by AWS Trusted Advisor, which inspects your environment and suggests ways to reduce spending, and are not a feature of the AWS Health Dashboard. A dashboard detailing vulnerabilities in applications describes Amazon Inspector, which scans for software vulnerabilities and unintended network exposure, and is not a function of the AWS Health Dashboard.

## clf-c02/domain3/q045

Answer: C

Amazon CloudWatch collects and monitors metrics, logs, and events from EC2 instances, enabling you to set alarms and visualise performance data to diagnose availability and performance issues affecting your application.
AWS Lambda is a serverless compute service that runs code in response to events and has no capability for monitoring the performance or availability of EC2 instances. AWS Config records and evaluates configuration changes to AWS resources for compliance and auditing purposes, but does not collect performance metrics or help troubleshoot availability issues. AWS CloudTrail records API calls and user activity across your AWS account for auditing and governance purposes, but does not monitor instance performance metrics or application availability.

## clf-c02/domain3/q047

Answer: B, D

Amazon S3 cannot run applications or backend systems, as it is an object storage service rather than a compute platform. Running applications and backend systems is the function of services such as Amazon EC2 and AWS Lambda. Amazon S3 scales automatically rather than manually, so the claim that it scales manually is factually incorrect and therefore not a genuine benefit.
Amazon S3 does provide virtually unlimited storage for any type of data as objects, making option A a true statement and therefore not the answer. Amazon S3 stores any number of objects but does impose a 5 TB size limit per individual object, making option C an accurate description of its behavior. Amazon S3 is designed to provide 99.999999999% durability for objects stored across its infrastructure, making option E a genuine and well-known benefit.

## clf-c02/domain3/q053

Answer: D, E

Amazon CloudWatch Logs supports real-time monitoring of log data and configurable retention periods, allowing you to control exactly how long log data is kept before it is automatically deleted.
Amazon SNS is a notification and messaging service that can be triggered by CloudWatch alarms, but summarizing log data is not a native feature of CloudWatch Logs. Amazon CloudWatch Logs is not free, as charges apply based on the volume of data ingested, stored, and analyzed. Amazon OpenSearch Service is a separate analytics service that can be integrated with CloudWatch Logs as a destination, but free OpenSearch analytics is not a native feature of CloudWatch Logs.

## clf-c02/domain3/q054

Answer: C

AWS Lambda is a fully managed serverless compute service where you upload your code and AWS handles all underlying infrastructure, patching, and scaling automatically, with no server management required from the customer.
Amazon Simple Workflow Service is a workflow orchestration service for coordinating tasks across distributed application components, and is not a compute service that provides or manages underlying infrastructure. Amazon EC2 provides virtual servers with full operating system access, but requires the customer to manage the guest operating system, patching, and capacity configuration, making it a customer-managed rather than a fully AWS-managed compute service. Amazon Aurora is a fully managed relational database service compatible with MySQL and PostgreSQL, and is a database service rather than a compute service.

## clf-c02/domain3/q055

Answer: B

AWS Lambda runs code in response to events without requiring any server provisioning or management, directly eliminating the physical compute footprint that developers would otherwise need to maintain.
Amazon EC2 provides virtual servers where customers are responsible for provisioning and managing the underlying instances, making it a server-based rather than serverless solution. Amazon DynamoDB is a fully managed NoSQL database service and does not provide compute execution for running application code. AWS CodeBuild is a fully managed build service for compiling source code and running tests, not a serverless compute service for running application logic.

## clf-c02/domain3/q063

Answer: B, E

Amazon RDS supports frequent read/write operations on relational data with full ACID transaction support, making it well suited for applications with constantly changing structured data. Amazon EFS provides a shared network file system with concurrent read/write access for multiple EC2 instances, making it appropriate for workloads that require continuous file-level changes.
Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and does not support the frequent read/write operations that constantly changing data requires. AWS Snowball is a physical device used to transfer large volumes of data into or out of AWS and has no capability to serve as a read/write data store for active workloads. Amazon Redshift is a data warehouse service optimized for running complex analytical queries across large datasets, not for handling frequent transactional read/write operations on constantly changing data.

## clf-c02/domain3/q067

Answer: A

Amazon Route 53 is AWS's managed DNS web service that translates domain names into IP addresses and also provides traffic routing policies, health checks, and domain registration.
Amazon Neptune is a fully managed graph database service for applications that work with highly connected datasets, unrelated to DNS or traffic routing. Amazon SageMaker is a managed machine learning platform for building, training, and deploying ML models, entirely unrelated to DNS. Amazon Lightsail provides simplified virtual private servers with pre-configured compute and networking for straightforward workloads, not a DNS service.

## clf-c02/domain3/q070

Answer: C

Amazon ElastiCache provides in-memory caching using Redis or Memcached, storing frequently queried results so applications can retrieve them without hitting the database repeatedly, dramatically reducing database load.
Amazon Machine Learning is a service for building and training machine learning models and has no role in database caching or query result storage. Amazon SQS is a fully managed message queuing service for decoupling application components, not for caching database query results. Amazon EC2 Instance Store is ephemeral block storage attached directly to an EC2 instance that does not persist beyond the instance lifecycle and is not designed for shared caching of database results.

## clf-c02/domain3/q073

Answer: B

Amazon EC2 Auto Scaling monitors demand and automatically adds or removes EC2 instances to maintain performance and minimize cost, freeing teams from manual capacity management so they can focus on their applications.
Elastic Load Balancing distributes incoming traffic across existing EC2 instances to prevent any single instance from being overwhelmed, but does not add or remove instances in response to changes in demand. Amazon Route 53 is a DNS and domain routing service that directs users to application endpoints and has no role in provisioning or removing compute capacity. Amazon CloudFront is a content delivery network that caches and serves content from edge locations closer to end users, and does not manage or scale EC2 instance capacity.

## clf-c02/domain3/q076

Answer: D

Amazon Athena lets you run standard SQL queries directly against data stored in S3 without loading it into a database first, making it the purpose-built service for querying datasets directly from S3.
AWS Glue is a serverless ETL service for discovering, preparing, and transforming data for analytics pipelines, not for running ad hoc SQL queries directly against S3. Amazon EMR provides managed clusters for processing large datasets using frameworks like Spark and Hadoop, but requires provisioning infrastructure rather than querying S3 directly with standard SQL. Amazon CloudSearch is a managed search service for adding full-text search functionality to applications and has no capability for SQL-based data querying.

## clf-c02/domain3/q081

Answer: C

AWS Lambda is a serverless compute service that runs code in response to events without requiring you to provision or manage any underlying servers.
Amazon EMR is a managed cluster platform that runs big data frameworks such as Hadoop and Spark on provisioned EC2 instances, and is not a serverless service. Elastic Load Balancing distributes incoming traffic across multiple targets such as EC2 instances, and is a traffic management service rather than a compute platform of any kind. Amazon EC2 provides virtual servers in the cloud that require you to provision, configure, and manage the underlying instances, making it the opposite of a serverless compute service.

## clf-c02/domain3/q085

Answer: D

Auto Scaling monitors load and automatically adjusts the number of compute instances to match demand, ensuring capacity scales up during peak periods and scales back down when demand drops, without any manual intervention.
Load balancing distributes incoming traffic across existing compute instances to prevent any single instance from being overwhelmed, but does not add or remove capacity in response to changing load. Automatic failover redirects traffic to a healthy instance or resource when a failure is detected, which addresses availability rather than capacity adjustment. Round robin is a traffic distribution method that cycles requests evenly across a set of servers, and like load balancing, manages traffic distribution rather than adjusting the number of available compute instances.

## clf-c02/domain3/q086

Answer: B

Amazon DynamoDB is AWS's fully managed NoSQL database service that supports key-value and document data structures, designed for applications requiring consistent single-digit millisecond performance at any scale.
Amazon Redshift is a fully managed data warehouse service designed for running complex analytical queries across large volumes of structured data, not a NoSQL database for key-value or document storage. Amazon Aurora is a fully managed relational database engine compatible with MySQL and PostgreSQL, and uses SQL-based structured schemas rather than the flexible NoSQL data models that DynamoDB provides. Amazon RDS for MariaDB is a managed relational database service running the MariaDB engine, which uses structured SQL tables and is not a NoSQL database service.

## clf-c02/domain3/q087

Answer: B

Regions are geographic areas that contain multiple Availability Zones. Each AZ consists of one or more data centers, and edge locations are separate points of presence used by CloudFront, independent of AZs.
Data centers contain regions reverses the hierarchy. Data centers sit inside AZs, which sit inside Regions. Availability Zones contain edge locations is false. Edge locations are separate infrastructure from AZs and exist independently across the globe. Edge locations contain regions is false. Edge locations are smaller points of presence and have no containing relationship with Regions.

## clf-c02/domain3/q088

Answer: A

Using many instances in parallel applies horizontal scaling, a core AWS architecture principle that distributes workloads across multiple instances simultaneously for greater speed and cost efficiency than sequential processing.
Using a single large instance during off-peak hours applies vertical scaling and sequential processing, which contradicts AWS architecture principles favoring parallelism and does not reduce total processing time. Using dedicated hardware provides physical server isolation for compliance or licensing requirements but does not improve throughput for large-scale parallel workloads. Using a large GPU instance type optimizes for graphics processing performance on a single instance rather than distributing the workload across multiple parallel instances.

## clf-c02/domain3/q089

Answer: A, B

Microsoft SQL Server can be hosted on Amazon EC2 instances where the customer installs and manages the database themselves, or via Amazon RDS for SQL Server where AWS manages the underlying infrastructure, patching, and backups as a fully managed service.
Amazon Aurora supports MySQL and PostgreSQL-compatible database engines only and does not support Microsoft SQL Server. Amazon Redshift is a data warehouse service optimized for analytical queries on large datasets, not a relational database engine for hosting SQL Server workloads. Amazon S3 is an object storage service and cannot host or run a relational database engine.

## clf-c02/domain3/q093

Answer: B

Amazon Rekognition automatically analyzes images and videos to detect objects, scenes, faces, text, and activities using machine learning, eliminating the time that would otherwise be spent on manual image review or building custom ML pipelines.
Automatic watermarking of images is not a feature of Amazon Rekognition, which is an analysis and detection service rather than an image editing or rights management tool. Resizing millions of images automatically is not a Rekognition capability and describes an image processing task better suited to a custom solution or a service like AWS Lambda with an image library. Amazon Rekognition does not use Amazon Mechanical Turk or involve human bidding on jobs, as its detection capabilities are fully automated through deep learning models without human intervention.

## clf-c02/domain3/q094

Answer: A

AWS Auto Scaling automatically adjusts the number of EC2 instances based on defined policies, eliminating the need for manual capacity planning decisions and ensuring the application always has the right amount of compute capacity.
Amazon Redshift is a fully managed data warehouse service designed for running analytical queries across large datasets, and has no capability to automatically scale application infrastructure. AWS CloudTrail is a logging and auditing service that records API calls and account activity across an AWS environment, and does not manage or adjust application capacity. AWS Lambda is a serverless compute service that runs code in response to events without provisioning servers, but it is an event-driven execution environment rather than a service that scales existing application infrastructure up and down.

## clf-c02/domain3/q095

Answer: B

With Amazon RDS, AWS manages the underlying operating system patching, backups, and maintenance windows, freeing customers from OS-level administration while customers retain responsibility for their data, schema, and database-level configuration.
AWS does not manage the data stored in RDS tables, as customers retain full responsibility for the data they load, modify, and delete within their databases. RDS does not automatically scale instance types on demand, as customers must manually resize instances or enable storage autoscaling, unlike serverless services such as DynamoDB which scale automatically. AWS does not manage the database type in RDS, as customers choose and remain responsible for selecting the database engine such as MySQL, PostgreSQL, or Oracle when creating an instance.

## clf-c02/domain3/q098

Answer: C

Amazon S3 stores objects with real-time access, supports versioning to track and restore previous versions, and offers lifecycle policies to manage object transitions, making it the service that matches all three described capabilities.
Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and can tolerate retrieval times of hours, and does not provide the real-time access or versioning capabilities the question describes. AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage for ongoing integration, and is not an object storage service with versioning or lifecycle management. Amazon EBS provides persistent block storage volumes that attach to EC2 instances, and does not store objects or support versioning and lifecycle policies.

## clf-c02/domain3/q108

Answer: C

AWS Regions are available globally and customers can begin provisioning resources in any Region at any time through the console, CLI, or API without any additional agreements or setup required.
Contacting an AWS Account Manager to sign a new contract is not required because AWS uses a self-service, pay-as-you-go model with no per-Region contracts. Availability Zones are fixed infrastructure components within a Region and cannot be moved or reassigned. The AWS Management Console is a web-based interface accessed through a browser and does not require a separate download for each Region.

## clf-c02/domain3/q109

Answer: B

Elastic Load Balancers automatically distribute incoming traffic across multiple registered targets and adapt to constantly changing network traffic patterns without requiring manual intervention, ensuring no single target becomes a bottleneck.
Elastic Load Balancers do not convert between Application Load Balancers and Classic Load Balancers; these are distinct load balancer types that cannot be converted to one another, and migration requires deploying a new load balancer rather than in-place conversion. ELB does not itself adjust the number of compute instances; that is the responsibility of Auto Scaling groups working in conjunction with a load balancer. Elastic Load Balancing is not provided at no charge; there are per-hour charges for each load balancer plus data processing charges, making cost a factor when designing load-balanced architectures.

## clf-c02/domain3/q111

Answer: A

Amazon S3 Standard provides durable, highly available object storage with immediate millisecond retrieval, and is more cost-effective than EBS for backup storage while meeting the immediate retrieval requirement.
Amazon S3 Glacier Flexible Retrieval is designed for long-term archival storage at very low cost, and retrieval takes from minutes to hours, making it unsuitable for backups that require immediate access. Amazon EBS provides persistent block storage volumes attached directly to EC2 instances for low-latency disk access, and is significantly more expensive per gigabyte than S3 for storing backup data. Amazon EC2 Instance Store provides temporary block storage physically attached to the host machine, and is ephemeral storage that is lost when the instance stops, making it entirely unsuitable for durable backup storage.

## clf-c02/domain3/q116

Answer: D

Amazon RDS is a fully managed relational database service that supports multiple database engines including MySQL, PostgreSQL, Oracle, and SQL Server, handling provisioning, patching, backups, and high availability automatically.
AWS Batch is a fully managed service for running large-scale batch computing jobs across dynamically provisioned compute resources, and has no database hosting capability. AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports and security documentation, and is entirely unrelated to database hosting. AWS Data Pipeline (deprecated) is an orchestration service for scheduling and automating the movement and transformation of data between AWS services and on-premises sources, and is not a service for hosting or managing databases.

## clf-c02/domain3/q119

Answer: D

Amazon Elastic File System (EFS) is a managed NFS file system that can be mounted simultaneously by multiple Linux EC2 instances and accessed from on-premises servers, providing simple, scalable shared file storage.
Amazon S3 is an object storage service designed for storing and retrieving files via HTTP APIs, and does not provide a mountable shared file system for Linux servers. Amazon S3 Glacier is an archival storage class within Amazon S3 designed for long-term data retention with infrequent access, and has no shared file system capability. Amazon Elastic Block Store (EBS) provides block-level storage volumes that attach to a single EC2 instance at a time, and cannot be shared across multiple servers simultaneously.

## clf-c02/domain3/q122

Answer: B

EC2 instance store provides ephemeral block storage that is physically attached to the host machine and is permanently deleted when the instance is stopped or terminated, making it suitable only for temporary data.
Amazon EBS volumes are persistent block storage that exist independently of the instance lifecycle, so data is retained even after the instance is stopped or terminated. Amazon EFS is a persistent shared file system that remains available across multiple instances and is not tied to the lifecycle of any single instance. Amazon S3 is persistent object storage that exists independently of any compute instance and retains data until explicitly deleted.

## clf-c02/domain3/q124

Answer: C

AWS Step Functions, Amazon DynamoDB, and Amazon SNS are all fully serverless services that require no server provisioning and scale automatically, making this the only group composed entirely of serverless services.
Amazon EC2 requires customers to provision and manage virtual server instances, and while Amazon S3 and Athena are serverless, EC2 disqualifies this group. Amazon EMR requires provisioning and managing clusters of servers for big data processing, disqualifying this group even though Kinesis and SQS are serverless. Amazon EC2 is not a serverless service, which disqualifies this group regardless of whether Athena and Cognito qualify individually.

## clf-c02/domain3/q127

Answer: D

AWS CloudFormation allows you to define AWS infrastructure in JSON or YAML templates, enabling repeatable and automated provisioning of entire environments through infrastructure as code.
AWS CodePipeline automates the stages of a software release pipeline including source, build, and deploy phases, but does not provision or manage AWS infrastructure through templates. AWS CodeDeploy automates the deployment of application code to EC2 instances, Lambda functions, and on-premises servers, and does not manage infrastructure provisioning. AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, and is a networking service entirely unrelated to infrastructure as code.

## clf-c02/domain3/q129

Answer: A

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that automatically scales storage and can handle high throughput, making it the purpose-built choice for a MySQL workload that needs to scale easily.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is not a relational database engine compatible with MySQL workloads. Amazon DynamoDB is a fully managed NoSQL key-value and document database, and does not support MySQL or relational data models. Amazon ElastiCache is a managed in-memory caching service designed to accelerate application performance by storing frequently accessed data in memory, and is not a relational database capable of running MySQL workloads.

## clf-c02/domain3/q134

Answer: B

Amazon S3 Glacier is designed for long-term archival and data backup at very low storage costs, making it the purpose-built service for retaining backups cheaply over extended periods.
Amazon RDS is a fully managed relational database service for active transactional workloads, and is not designed for storing infrequently accessed backup archives at low cost. AWS Snowball is a physical data transport device used for migrating large volumes of data into or out of AWS, and is a migration tool rather than a long-term storage service. Amazon EBS provides persistent block storage volumes attached to EC2 instances for low-latency disk access, and is significantly more expensive per gigabyte than S3 Glacier for storing backup data that is accessed infrequently.

## clf-c02/domain3/q138

Answer: B, D

Edge locations deliver cached content geographically close to end users to reduce latency, and they absorb repeated requests by serving cached responses so that fewer requests reach the origin server.
Hosting applications compute resources for running applications are provided by EC2 instances and other services in AWS Regions and Availability Zones, not at edge locations. Running NoSQL database caching services managed database and caching services such as DynamoDB and ElastiCache run in Regions, not at edge locations. Sending notification messages to end users message delivery to end users is handled by services like Amazon SNS, which operates from Regional endpoints, not edge locations.

## clf-c02/domain3/q149

Answer: D

AWS CodeCommit is a fully managed Git-based source control service designed specifically for software version control, allowing teams to securely store and manage their code repositories.
AWS CodeBuild is a fully managed build service that compiles source code and runs tests to produce deployment-ready packages, but its primary purpose is building and testing code rather than storing and versioning it. AWS CLI is a command-line tool for interacting with and managing AWS services and resources, and is not a source control or version management service. Amazon Cognito is a user identity and authentication service for web and mobile applications, and has no connection to software version control.

## clf-c02/domain3/q151

Answer: A

An Availability Zone consists of one or more discrete data centers with independent power and networking, interconnected to other AZs within the same Region via low-latency links.
Edge locations are separate points of presence used for content delivery and caching, not data center clusters with redundant infrastructure. A Region is the broader geographic area that contains multiple Availability Zones, not the data center cluster itself. Private networking is not a component of the AWS global infrastructure hierarchy.

## clf-c02/domain3/q154

Answer: B

Edge locations cache content geographically close to end users, reducing round-trip distance and lowering latency to improve performance for global applications.
Host Amazon EC2 instances closer to users. EC2 instances run in Regions and AZs, not at edge locations. Cache frequently changing data without reaching the origin server. Edge locations cache static or infrequently changing content, not frequently changing data. Refresh data changes daily. Edge locations serve cached content based on TTL settings, not on a fixed daily refresh cycle.

## clf-c02/domain3/q164

Answer: C

AWS Storage Gateway is a hybrid storage service that integrates on-premises environments with AWS cloud storage, presenting cloud storage as local file shares, volumes, or tape to on-premises applications.
Amazon S3 Glacier is an archival storage class within Amazon S3 designed for long-term data retention with infrequent access, and does not provide a hybrid storage integration layer for on-premises applications. AWS Snowball is a physical data transfer device used to move large volumes of data into or out of AWS, and is a migration tool rather than an ongoing hybrid storage service. Amazon Elastic Block Store (EBS) provides block-level storage volumes that attach to EC2 instances within AWS, and cannot be accessed directly by on-premises applications as a seamless cloud storage extension.

## clf-c02/domain3/q166

Answer: B

AWS Regions are the physical, geographically distributed components of the AWS Global Infrastructure, each containing multiple Availability Zones that provide redundancy and fault isolation.
Amazon Alexa is a voice assistant service that enables conversational interactions with applications, and is not a component of the physical infrastructure that underpins AWS. Amazon Lightsail is a simplified compute service designed for developers who need an easy way to launch virtual servers and applications, and is not an infrastructure component. AWS Organizations is an account management service that enables centralized governance and billing across multiple AWS accounts, and is not part of the AWS Global Infrastructure.

## clf-c02/domain3/q168

Answer: B, D

A site-to-site VPN through a virtual private gateway provides an encrypted tunnel over the internet between on-premises and the VPC, and AWS Direct Connect provides a dedicated private network link, both extending the on-premises network into AWS.
AWS Service Catalog is a tool for managing and provisioning approved IT service portfolios within an organization, and has no capability to identify or connect on-premises resources to a VPC. Amazon Athena is a serverless query service that analyzes data stored in Amazon S3, and cannot query data directly from on-premises database servers. Amazon CloudFront is a content delivery network that caches and distributes content globally, and is not a mechanism for restricting or routing access between on-premises servers and a VPC.

## clf-c02/domain3/q172

Answer: B

An Amazon Machine Image is a pre-configured template containing the operating system, application server, and application code used to launch a new EC2 instance in a consistent, known state.
Amazon EBS is a block storage service that provides persistent volumes to attach to EC2 instances, not a template for launching pre-configured instances. AWS Systems Manager provides operational tools for managing, patching, and automating tasks on running EC2 instances, but does not launch pre-configured instances. Amazon AppStream 2.0 is an application streaming service that delivers desktop applications to users through a browser, entirely unrelated to EC2 instance configuration.

## clf-c02/domain3/q178

Answer: B

EC2 Auto Scaling groups span multiple Availability Zones and automatically add or replace instances when existing ones fail or become unhealthy, maintaining the desired capacity and enabling high availability.
Auto Scaling groups operate within a single Region across multiple Availability Zones, and do not automatically add instances across multiple Regions in response to global demand. Enabling static content to reside closer to end users describes a content delivery network such as Amazon CloudFront, not a capability of EC2 Auto Scaling groups. Distributing incoming requests across a tier of web server instances describes the function of a load balancer such as an Application Load Balancer, which is a separate service that works alongside but is distinct from Auto Scaling groups.

## clf-c02/domain3/q184

Answer: D

Amazon Redshift is a fully managed, petabyte-scale data warehouse service designed for running complex analytical queries across large datasets, making it the purpose-built solution for scalable data warehousing.
Amazon S3 is an object storage service for storing and retrieving any type of data, not a data warehouse for running analytical queries. Amazon DynamoDB is a NoSQL key-value and document database optimized for high-speed transactional workloads, not for complex analytical queries across large datasets. Amazon Kinesis is a service for collecting, processing, and analyzing real-time streaming data, not for warehousing and querying historical datasets.

## clf-c02/domain3/q185

Answer: B, D

AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, and AWS Storage Gateway integrates on-premises storage environments with cloud storage, both directly extending an on-premises architecture into the AWS Cloud.
Amazon EBS is a block storage service for EC2 instances that operates entirely within AWS and has no on-premises connectivity function. Amazon CloudFront is a content delivery network that caches and distributes content globally but does not connect or extend on-premises networks to AWS. Amazon Connect is a cloud-based contact center service for managing customer communications and is unrelated to hybrid network or storage connectivity.

## clf-c02/domain3/q192

Answer: D

EC2 with EBS is the right choice because EBS volumes persist independently from the instance. When the instance is stopped nightly, the data on EBS is retained.
Amazon Redshift is a fully managed data warehouse service optimized for analytical SQL queries across large datasets, and as a managed service it cannot be stopped on a nightly schedule the way an EC2 instance can, making it unsuitable for a workload with a nightly shutdown requirement. Amazon DynamoDB is a fully managed NoSQL database service that scales automatically and operates continuously as a managed service, and cannot be stopped on a schedule for maintenance or cost-saving purposes. Amazon EC2 with Amazon EC2 instance store provides temporary block storage that is physically attached to the host machine, and this storage is lost when the instance is stopped, making it unsuitable for a database that requires data persistence across nightly shutdowns.

## clf-c02/domain3/q194

Answer: D

Amazon S3 is AWS's object storage service where each item is stored as an object containing data, metadata, and a unique key within a bucket, making it suitable for storing any type of file at virtually unlimited scale.
Amazon EBS provides block storage volumes that are attached to EC2 instances for use as persistent disks, and operates at the block level rather than the object level. Amazon Instance Store provides temporary block storage physically attached to the host server, which is lost when the instance stops and is not object-level storage. Amazon EFS provides a managed file storage system that can be mounted across multiple EC2 instances simultaneously, and operates at the file level rather than the object level.

## clf-c02/domain3/q195

Answer: C

AWS Auto Scaling monitors application metrics and automatically adjusts the number of EC2 instances to match demand, ensuring you are not paying for idle capacity.
AWS Elastic Load Balancer distributes incoming traffic across multiple targets such as EC2 instances to improve availability and fault tolerance, but does not adjust the number of instances in response to demand changes. AWS Budgets lets you set cost and usage thresholds and receive alerts when those thresholds are exceeded, and while it can alert you to over-spending it cannot itself add or remove EC2 instances to match required demand. AWS Cost Explorer provides visualisation and analysis of AWS spending patterns over time, and is a cost analysis tool rather than a service that automatically adjusts compute capacity.

## clf-c02/domain3/q196

Answer: A

S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns, optimizing costs when access frequency is unpredictable without incurring retrieval fees.
Amazon S3 Glacier Flexible Retrieval is designed for archival data that is rarely accessed and can tolerate retrieval times ranging from minutes to hours, making it unsuitable for data with unpredictable but potentially frequent access needs. Amazon S3 Standard is optimized for frequently accessed data and charges a higher storage price, making it cost-inefficient for data with unpredictable patterns that may include long periods of inactivity. Amazon S3 Standard-Infrequent Access is designed for data that is accessed less frequently but requires rapid retrieval when needed, and incurs retrieval fees that make it costly when access patterns are unpredictable.

## clf-c02/domain3/q197

Answer: A

Amazon DynamoDB is a fully managed NoSQL database that natively supports key-value and document data models, making it ideal for uploading and retrieving data structured as key-value pairs.
Amazon Aurora is a fully managed relational database engine compatible with MySQL and PostgreSQL that uses structured SQL schemas, and does not support the flexible key-value data model that DynamoDB provides. Amazon Redshift is a fully managed data warehouse service designed for running complex analytical queries across large volumes of structured data, and is not a key-value database. Amazon RDS is a managed relational database service supporting multiple SQL engines, and uses structured table-based schemas rather than the key-value data model.

## clf-c02/domain3/q202

Answer: A

Amazon RDS is a fully managed relational database service where AWS handles configuration, backups, patching, and failover, freeing the DBA to focus on data architecture and performance.
Amazon Redshift is a data warehousing service designed for analytics, not transactional relational database workloads. Amazon DynamoDB is a NoSQL key-value database and would not be a like-for-like replacement for a MySQL relational workload. Amazon CloudWatch is a monitoring and observability service, not a database service.

## clf-c02/domain3/q205

Answer: A

Amazon SQS is a fully managed message queuing service that stores messages even when the consuming component is unavailable, preventing message loss in distributed architectures.
Amazon SES is an email sending and receiving service designed for transactional and marketing communications, and does not queue messages between software components to prevent loss during failures. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and has no role in storing or managing messages between application components. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is not a message queuing or application integration service.

## clf-c02/domain3/q207

Answer: D

Amazon VPC (Virtual Private Cloud) creates a logically isolated, private virtual network dedicated to your AWS account, where you control IP addressing, subnets, routing, and gateways.
AWS VPN establishes an encrypted connection over the public internet between your on-premises network and an existing VPC, but is a connectivity feature rather than the virtual network itself. AWS Subnets are subdivisions of a VPC's IP address range used to organize resources within a VPC, not a standalone networking service. AWS Dedicated Hosts are physical servers with EC2 instance capacity allocated exclusively to your account for compute workloads, not a networking or virtual network construct.

## clf-c02/domain3/q209

Answer: D, E

Amazon EC2 provides resizable virtual servers that run applications on managed compute infrastructure, and AWS Lambda runs code as serverless functions in response to events, making both compute resources.
Amazon VPC is a networking service that provides logically isolated network environments within AWS, and does not itself execute code or provide compute capacity. Amazon CloudWatch is a monitoring and observability service that collects metrics, logs, and events from AWS resources, and has no compute execution capability. Amazon S3 is an object storage service designed for storing and retrieving data, and does not provide any compute or code execution functionality.

## clf-c02/domain3/q210

Answer: C

Amazon S3 is designed for storing and retrieving any amount of unstructured data, including photos and videos, with high durability and scalability, making it the purpose-built object storage solution for this use case.
Amazon EBS provides persistent block storage volumes that attach directly to EC2 instances, and is designed for low-latency disk access rather than storing and serving large volumes of unstructured media objects. Amazon SQS is a fully managed message queuing service for decoupling application components, and is a messaging service with no capability to store or retrieve files. Amazon EC2 Instance Store provides temporary block storage physically attached to the host machine running an EC2 instance, and is ephemeral storage that is lost when the instance stops, making it entirely unsuitable for persistent photo and video storage.

## clf-c02/domain3/q212

Answer: A

Amazon ElastiCache provides in-memory caching using Redis or Memcached engines, storing frequently accessed data in RAM and delivering sub-millisecond read latency for read-heavy applications.
A managed relational database service describes Amazon RDS, which handles structured data with SQL-based querying rather than in-memory caching. An online software store that allows customers to launch pre-configured software describes AWS Marketplace, not a caching service. A domain name system in the cloud describes Amazon Route 53, which handles DNS routing and domain registration rather than in-memory data caching.

## clf-c02/domain3/q217

Answer: A

AWS Direct Connect provides a dedicated, private physical network connection from your on-premises data center to AWS, bypassing the public internet to deliver more consistent bandwidth, lower latency, and increased reliability for hybrid cloud workloads.
Amazon CloudFront is a content delivery network that caches and distributes web content to end users from edge locations worldwide, and is a content delivery service rather than a private network connectivity solution for data centers. AWS Snowball is a physical data transfer device used to move large volumes of data into or out of AWS by shipping the device, designed for one-time or periodic bulk data transfers rather than ongoing private network connectivity. Amazon Route 53 is a scalable DNS service that translates domain names to IP addresses and supports routing policies, and is a DNS management service with no capability to establish dedicated network links between on-premises infrastructure and AWS.

## clf-c02/domain3/q218

Answer: B

Amazon VPC lets you provision logically isolated network environments within AWS with full control over IP ranges, subnets, routing tables, and gateways, allowing you to run completely separate network configurations for different projects.
Internet gateways enable outbound and inbound internet access within a VPC but are a component of a VPC rather than a mechanism for isolating entire network configurations. Security groups control inbound and outbound traffic at the instance level and operate within a VPC, so they filter traffic but do not provide network-level isolation between projects. Amazon CloudFront is a content delivery network for caching and distributing content globally, unrelated to network isolation or configuration management.

## clf-c02/domain3/q220

Answer: A

Amazon EMR is a managed big data platform that runs distributed processing frameworks such as Apache Hadoop and Spark, making it the purpose-built service for analyzing and processing large volumes of data at scale.
Amazon MQ is a managed message broker service for applications that use open-standard messaging protocols such as AMQP and MQTT, and is a messaging integration tool with no data processing or analytics capability. Amazon SNS is a fully managed pub/sub notification service for delivering messages to subscribers such as Lambda functions, email addresses, and HTTP endpoints, and has no capability to process or analyze large datasets. Amazon SQS is a fully managed message queuing service that decouples application components by holding messages in a queue for asynchronous processing, and is an application integration tool rather than a data analytics service.

## clf-c02/domain3/q222

Answer: C

Amazon EC2 gives customers the highest level of control over virtual infrastructure, including choice of operating system, instance type, networking, storage, and the ability to install and configure any software on the underlying instance.
Amazon Redshift is a fully managed data warehouse service where AWS abstracts and manages the underlying infrastructure, leaving customers responsible only for their data and queries rather than the virtual infrastructure itself. Amazon DynamoDB is a fully managed NoSQL database service where AWS handles all infrastructure, patching, and scaling automatically, giving customers no visibility or control over the underlying virtual infrastructure. Amazon RDS is a fully managed relational database service where AWS manages the operating system, database engine patching, and underlying infrastructure, abstracting those layers away from the customer entirely.

## clf-c02/domain3/q224

Answer: D

An Amazon Machine Image is a template containing the operating system, application software, and configuration needed to launch an EC2 instance, directly equivalent to the on-premises practice of spinning up multiple virtual servers from a single template.
IAM is an identity and access management service that controls permissions and user access within AWS, and has no role in creating or launching virtual server instances. An internet gateway is a VPC component that enables communication between resources inside a VPC and the public internet, and is unrelated to server provisioning or templating. An EBS snapshot is a point-in-time backup of a storage volume used for data recovery purposes, not a template for launching new instances with a defined operating system and configuration.

## clf-c02/domain3/q228

Answer: C

Edge locations cache and deliver content with low latency to global users and also improve upload performance through services like S3 Transfer Acceleration, but they do not distribute traffic across multiple compute instances. Distributing traffic across instances is the function of Elastic Load Balancing, making C the statement that does not describe an edge location benefit.
Caching the most recent responses is a genuine edge location benefit, as CloudFront stores copies of content closer to end users to reduce origin fetches. Improving upload performance for end users is a genuine edge location benefit, as S3 Transfer Acceleration routes uploads through the nearest edge location for faster transfer. Distributing content to global users with low latency is the primary purpose of edge locations and a core CloudFront benefit.

## clf-c02/domain3/q230

Answer: A

Amazon ECS is a fully managed container orchestration service that allows you to run and manage Docker containers on a cluster of EC2 instances or using AWS Fargate for serverless compute.
AWS Data Pipeline (deprecated) is a service for orchestrating and automating the movement and transformation of data between AWS services, not for running containerised applications. AWS Cloud9 is a cloud-based integrated development environment for writing and debugging code, unrelated to container orchestration. AWS Health Dashboard provides alerts and guidance when AWS service events may affect your resources, not a compute or container service.

## clf-c02/domain3/q232

Answer: B

Using the right S3 storage class for each use case, such as S3 Standard for frequently accessed data, S3 Standard-Infrequent Access for less frequent access, and S3 Glacier for archival, is the most effective way to reduce S3 storage costs.
Using S3 Lifecycle policies to automatically transition old objects to Amazon S3 Glacier reduces storage costs for archived data, but applies only to objects that qualify for archival rather than optimizing the full range of S3 storage costs across all use cases. S3 does not charge differently based on which Availability Zone a bucket is associated with, and selecting a different Availability Zone has no effect on S3 pricing. Moving data from S3 Standard to Amazon EBS would increase costs significantly, as EBS is block storage attached to EC2 instances and charges per provisioned gigabyte regardless of actual usage, making it far more expensive than S3 for object storage.

## clf-c02/domain3/q233

Answer: B, C

AWS Auto Scaling automatically adds or removes instances based on demand, maintaining availability when traffic spikes or instances fail. Elastic Load Balancer distributes traffic across healthy instances and integrates with Auto Scaling to replace unhealthy ones, together providing a highly available and fault-tolerant architecture.
AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is a connectivity service rather than a tool for maintaining application availability or fault tolerance. AWS CloudFormation provisions and manages infrastructure through templates, and while it can deploy highly available architectures, it does not itself maintain availability or respond to failures at runtime. Network ACLs control inbound and outbound traffic at the subnet level for security purposes, and do not contribute to availability or fault tolerance.

## clf-c02/domain3/q235

Answer: A

S3 Transfer Acceleration uses CloudFront's globally distributed edge locations as entry points for uploads to S3, routing data over AWS's optimized backbone network to reach the target S3 bucket faster than a standard upload.
AWS WAF is a web application firewall that filters and monitors HTTP traffic to protect web applications from common exploits, and has no file transfer or upload acceleration capability. AWS Snowmobile is a physical data transport service using a shipping container-sized device designed for exabyte-scale migrations, not for accelerating online uploads to S3. AWS Snowball is a physical data transfer appliance used for large-scale offline data migrations, and does not leverage edge locations or accelerate internet-based uploads.

## clf-c02/domain3/q237

Answer: B, E

AWS Global Accelerator improves global application performance by routing user traffic through the AWS private backbone network to the nearest healthy endpoint, reducing internet latency, and Amazon CloudFront caches and serves content from edge locations worldwide, bringing content closer to users and reducing latency for global audiences.
AWS KMS is an encryption key management service for creating and controlling cryptographic keys used to protect data, and has no capability to improve application performance or reduce latency. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is designed for hybrid connectivity rather than improving performance for global end users. AWS Glue is a managed ETL service for discovering, preparing, and transforming data for analytics workloads, and is a data integration service with no application performance or latency capability.

## clf-c02/domain3/q239

Answer: C

Amazon RDS is the appropriate service for migrating structured relational data, supporting multiple SQL engines including MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB in a managed environment that mirrors on-premises relational database setups.
Amazon DynamoDB is a NoSQL key-value and document database designed for unstructured or semi-structured data, making it unsuitable for migrating structured relational workloads. Amazon SNS is a managed messaging and notification service used for pub/sub communication between applications, and has no database capability. Amazon ElastiCache is an in-memory caching service used to accelerate application performance, not a relational database for storing and migrating structured data.

## clf-c02/domain3/q241

Answer: B

AWS Lambda is a serverless compute service that runs your code in response to events without requiring you to provision, manage, or scale any servers or infrastructure, eliminating all administrative burden.
Amazon Lightsail is a simplified compute service for deploying virtual servers, containers, and web applications with minimal configuration, but it still involves provisioning and managing server-based resources rather than being a truly serverless service. Amazon RDS is a fully managed relational database service, but managed does not mean serverless and customers still select and provision database instances with associated compute resources. Amazon EC2 provides virtual servers in the cloud that require you to provision, configure, and manage the underlying instances, making it the opposite of a serverless service with no administrative burden.

## clf-c02/domain3/q243

Answer: A, C

Amazon EFS is a fully managed, scalable NFS file system that can be mounted by multiple EC2 instances simultaneously, and Amazon EBS provides block storage volumes that attach to individual EC2 instances. Both are storage services where files can be stored in AWS.
Amazon SNS is a fully managed publish/subscribe messaging service used to send notifications to subscribers such as Lambda functions, HTTP endpoints, and email addresses, and is a messaging service rather than a file storage service. Amazon ECS is a fully managed container orchestration service for running containerised applications using Docker containers, and is a compute service for running application workloads rather than a storage service. Amazon EMR is a managed big data platform for processing large-scale datasets using frameworks such as Apache Spark and Hadoop, and is a data processing service rather than a storage destination for files.

## clf-c02/domain3/q244

Answer: A

Amazon SQS is a fully managed message queuing service that stores messages reliably until they are processed, ensuring no message is lost even if one or more components in a distributed system temporarily fail.
AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage use cases, and has no message queuing or delivery capability. Amazon Simple Email Service is a cloud-based email sending and receiving service designed for transactional and marketing emails, not for queuing messages between distributed application components. Amazon S3 is an object storage service for storing and retrieving files, and does not provide message queuing or guaranteed delivery between distributed systems.

## clf-c02/domain3/q247

Answer: B

Amazon RDS database instances use Amazon EBS volumes as their primary storage layer, providing persistent block-level storage that persists independently of the database instance lifecycle.
Amazon S3 Glacier is an archival storage service designed for long-term data retention at low cost and is not used as active storage for running database instances. Amazon EFS is a shared file system service mountable across multiple EC2 instances and is not the primary storage layer for RDS. Amazon S3 is an object storage service accessed via API and is not used as block-level storage for database instances.

## clf-c02/domain3/q248

Answer: B

AWS X-Ray provides distributed tracing for microservices applications, allowing developers to visualise the end-to-end path of requests, identify bottlenecks, and diagnose the root cause of performance and latency issues.
AWS CodePipeline automates the steps of a continuous delivery pipeline for releasing application code, including building, testing, and deploying, and is a CI/CD automation tool with no capability to trace requests or diagnose runtime performance issues. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security tool rather than a performance troubleshooting service. AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and does not trace application requests or provide visibility into latency and performance bottlenecks within microservices.

## clf-c02/domain3/q249

Answer: C, E

Amazon S3 stores data redundantly across multiple facilities within a Region by default, providing native Multi-AZ durability without any customer configuration. Amazon DynamoDB automatically replicates data across multiple Availability Zones within a Region, making Multi-AZ fault tolerance a built-in characteristic of the service.
Amazon Redshift is a data warehouse service that deploys into a single AZ by default and requires additional configuration such as Multi-AZ deployment or snapshot restore to achieve cross-AZ resilience. AWS Snowball is a physical data transfer device used to move large amounts of data into or out of AWS and has no relevance to Multi-AZ fault tolerance as a cloud service. Amazon EBS volumes are confined to a single Availability Zone by default and must be explicitly snapshotted and restored or replicated to achieve availability across AZs.

## clf-c02/domain3/q250

Answer: B, D

Multi-AZ Deployment maintains a synchronous standby replica in a separate Availability Zone with automatic failover if the primary instance fails, and Read Replicas can be promoted to a standalone database to restore availability for read-heavy workloads, both being Amazon RDS features that directly improve database availability.
AWS Regions are a geographic infrastructure concept and not a feature within Amazon RDS that can be enabled to improve the availability of an existing database instance. Automatic patching is a maintenance feature that keeps the database engine up to date, reducing admin burden, but it does not contribute to availability during failures or outages. Edge locations are points of presence used by CloudFront for content caching and delivery, and are not a component or feature of Amazon RDS in any way.

## clf-c02/domain3/q251

Answer: D

Creating a CloudFront distribution caches content at edge locations near Asian users, dramatically reducing round-trip latency without needing to move or replicate the origin infrastructure.
Replicating resources across multiple Availability Zones within the same Region improves availability but does not reduce geographic latency for users in Asia. Migrating to a hosting provider in Asia would reduce latency but introduces significant operational complexity and is not an AWS solution. Recreating the website content has no effect on network latency and does not address the geographic distance between the origin and end users.

## clf-c02/domain3/q256

Answer: A, C

Amazon S3 Glacier is designed for data that is infrequently accessed but must be retained for long periods, making active archives kept for compliance or historical reference and long-term analytic data retained for future analysis the primary use cases.
Dynamic website assets require fast, frequent access with millisecond retrieval times, making S3 Standard the appropriate storage class rather than Glacier's archival retrieval model. Active databases require real-time read and write operations that are incompatible with Glacier's retrieval delays, making services such as RDS or DynamoDB the appropriate choice. Cached data requires sub-millisecond access speeds to serve its purpose of accelerating application performance, making a service such as ElastiCache the appropriate solution rather than an archival storage class.

## clf-c02/domain3/q257

Answer: A

AWS Elastic Beanstalk is a Platform as a Service offering that automatically handles deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring, allowing developers to upload their application code and have the platform manage the infrastructure.
Amazon ECS is the container orchestration service that runs Docker containers and is the compute engine for containerised workloads, but it is not an abstraction that automatically manages deployment and infrastructure for general applications in the way Beanstalk does. A scalable file storage solution describes Amazon EFS, which provides shared NFS storage for EC2 instances; Elastic Beanstalk is a deployment and management platform, not a storage service. A NoSQL database service describes Amazon DynamoDB, which provides fully managed key-value and document storage; Elastic Beanstalk is a deployment platform rather than a database.

## clf-c02/domain3/q265

Answer: D

The AWS CLI is a unified tool that enables customers to manage AWS services and automate tasks via scripts and command-line commands, providing programmatic access to the full range of AWS functionality.
The AWS Console is a web-based graphical interface for managing AWS services through a browser, and does not support script-based automation or command-line interaction. AWS Service Catalog is a tool for creating and managing approved portfolios of IT products within an organization, and is not used for scripting or direct resource management. AWS OpsWorks (deprecated) is a configuration management service that uses Chef and Puppet to automate server configuration and deployment, and is not a general-purpose scripting tool for managing all AWS services.

## clf-c02/domain3/q266

Answer: C, E

AWS Direct Connect establishes a dedicated private physical connection between on-premises infrastructure and AWS, and AWS VPN creates an encrypted tunnel over the public internet. Both are the standard connectivity options for building hybrid cloud architectures that link on-premises environments with AWS.
AWS Artifact is a self-service portal for accessing AWS compliance reports and security certifications, and has no role in establishing network connectivity between on-premises environments and AWS. AWS Cloud9 is a browser-based integrated development environment for writing and running code, and is not a connectivity or networking service. AWS CloudTrail records API calls and account activity for auditing and governance purposes, and does not provide network connectivity between on-premises infrastructure and the AWS Cloud.

## clf-c02/domain3/q267

Answer: D

An Application Load Balancer operates at Layer 7 and distributes incoming HTTP and HTTPS traffic across EC2 instances based on rules such as URL path or host header, making it the correct choice for evenly distributing web application traffic.
AWS EC2 Auto Recovery monitors individual instances and restores them if they fail, but does not distribute traffic across multiple instances. AWS Auto Scaling adjusts the number of running instances based on demand but does not handle traffic distribution across existing instances. AWS Network Load Balancer operates at Layer 4 and is optimized for TCP and UDP traffic requiring ultra-high performance, not for general HTTP web application traffic distribution.

## clf-c02/domain3/q268

Answer: B

Amazon Aurora is a MySQL and PostgreSQL-compatible managed relational database that automatically scales storage as needed, making it the purpose-built solution for applications requiring MySQL compatibility with automatic capacity scaling.
Amazon Neptune is a fully managed graph database service designed for storing and querying highly connected data such as social networks and knowledge graphs, and is not a MySQL-compatible relational database. Amazon RDS for SQL Server is a managed relational database running Microsoft's SQL Server engine, which is not MySQL-compatible and does not automatically scale storage capacity on demand. Amazon RDS for PostgreSQL is a managed relational database running the PostgreSQL engine which, while sharing some compatibility with Aurora, does not auto-scale storage the way Aurora does.

## clf-c02/domain3/q270

Answer: A

Amazon Redshift is a fully managed, petabyte-scale data warehouse optimized for complex analytical queries on large structured datasets using columnar storage and massively parallel processing.
Amazon Kinesis is a service for ingesting and processing real-time streaming data, not a data warehouse for analytical queries on large stored datasets. Amazon DynamoDB is a NoSQL database optimized for high-speed key-value and document workloads, not for complex analytical queries across large datasets. Amazon RDS is a managed relational database service designed for transactional workloads, not for the petabyte-scale analytical query performance that a data warehouse provides.

## clf-c02/domain3/q274

Answer: D

Creating an AMI from a configured EC2 instance captures its operating system, software, and settings as a reusable template, allowing you to launch new instances with identical configurations at any time.
Creating an AWS Config template manages compliance rules and configuration drift detection, not instance images or replication. Creating an EBS Snapshot backs up the data on a volume but does not capture the full instance configuration including the OS and software settings needed to launch an identical instance. Installing Aurora on EC2 is not a valid approach, as Aurora is a managed database service that runs on AWS infrastructure and is not installed on customer EC2 instances.

## clf-c02/domain3/q277

Answer: A, C

Amazon RDS reduces the administrative burden of database management by handling routine tasks such as backups, patching, and failover automatically, and allows you to resize compute capacity to match changing workload demands.
Complete control over the underlying host is a characteristic of Amazon EC2, where customers manage the operating system directly. RDS abstracts the host away entirely and does not expose it to the customer. RDS requires manual instance type changes rather than scaling automatically in response to demand, so it does not auto-scale to larger or smaller instance types. Document and key-value data structures are supported by Amazon DynamoDB, a NoSQL service, whereas RDS is relational and uses structured SQL schemas.

## clf-c02/domain3/q278

Answer: D

AWS Site-to-Site VPN uses IPSec to create an encrypted tunnel between an on-premises network and an AWS VPC over the public internet, providing secure connectivity without dedicated physical infrastructure.
Internet Gateway connects a VPC to the public internet for inbound and outbound traffic, but does not establish encrypted tunnels to on-premises networks. AWS IQ is a marketplace for connecting customers with AWS-certified experts for professional services, unrelated to network connectivity. AWS Direct Connect provides a dedicated private circuit between on-premises infrastructure and AWS, but does not use IPSec and does not travel over the public internet.

## clf-c02/domain3/q282

Answer: D

AWS Health Dashboard provides real-time status information about all AWS services across all AWS Regions, allowing anyone to check the current operational health of the AWS infrastructure.
AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal use and self-service provisioning, and has no connection to displaying the current status of AWS services globally. AWS Management Console is the web-based interface for accessing and managing AWS services, and while it provides access to many dashboards it is not itself the service that publishes current status information about AWS infrastructure health. Amazon CloudWatch collects metrics, logs, and event data from your own AWS resources and applications to provide operational monitoring and alerting, and is a customer-facing monitoring tool rather than a service that publishes the health status of AWS infrastructure itself.

## clf-c02/domain3/q283

Answer: A

AWS SDKs are available for multiple programming languages including Python, Java, JavaScript, and .NET, providing libraries that allow developers to interact with and call AWS services programmatically from within their application code.
AWS Command Line Interface is a tool for interacting with AWS services through terminal commands and scripts, and is not designed for calling AWS services from within application code written in a programming language. AWS CodeDeploy is a deployment service that automates the release of application code to EC2 instances, Lambda functions, and on-premises servers, and has no role in enabling programmatic access to AWS services from application code. AWS Management Console is a web-based graphical interface for managing AWS services through a browser, and does not provide programmatic access from programming languages.

## clf-c02/domain3/q284

Answer: B

Amazon Route 53 provides domain name registration in addition to DNS routing, health checks, and traffic management, making it the only AWS service that can register a new domain name.
Amazon Personalize is a machine learning service that provides personalized product and content recommendations, and has no domain registration or DNS functionality. AWS KMS is a key management service used to create and control encryption keys for securing data, and is unrelated to domain registration. AWS Config tracks and records AWS resource configurations and evaluates them against compliance rules, and has no domain registration capability.

## clf-c02/domain3/q285

Answer: A, D

AWS CloudFormation lets teams define infrastructure as code in templates that can be version-controlled and deployed automatically, and AWS Elastic Beanstalk abstracts infrastructure management so developers can deploy applications simply by uploading their code. Both directly accelerate application deployment.
AWS Migration Hub provides a central location for tracking the progress of application migrations to AWS, and is a migration monitoring tool rather than an automation tool for deploying applications faster. AWS IAM is an identity and access management service for controlling who can access AWS resources and what actions they can perform, and is a security and permissions service with no application deployment or automation capability. Amazon Macie is a data security service that uses machine learning to automatically discover and protect sensitive data stored in Amazon S3, and is entirely unrelated to application deployment or automation.

## clf-c02/domain3/q287

Answer: B

AWS Transit Gateway acts as a central network hub that connects hundreds or thousands of VPCs across multiple Regions through a single managed gateway, eliminating the complexity of managing individual point-to-point connections.
VPC Peering creates individual one-to-one connections between VPC pairs, which becomes unmanageable at scale with hundreds of VPCs. Amazon Connect is a cloud-based contact center service for managing customer communications and has nothing to do with network connectivity. Security Groups are instance-level firewalls that control inbound and outbound traffic rules and do not manage connections between VPCs.

## clf-c02/domain3/q289

Answer: A

Multiple Availability Zones within a Region are geographically separated, each with independent power, cooling, and networking, so a failure in one AZ does not affect others, allowing customers to build resilient and highly available architectures.
Deploying across multiple Availability Zones does not lower total cost, as running resources in multiple AZs typically increases cost compared to a single AZ deployment. Multiple Availability Zones provide redundancy within a Region but do not provide global reach, which requires deploying across multiple Regions or using a content delivery network. The number of Availability Zones in a Region does not increase the storage capacity available, as storage capacity is determined by the services and configurations a customer selects rather than the AZ count.

## clf-c02/domain3/q294

Answer: B, C

Amazon S3 automatically scales to handle any amount of data and any request rate without manual intervention, and AWS Lambda scales automatically from zero to thousands of concurrent executions in response to incoming events.
Amazon EC2 does not scale automatically by default and requires customers to configure Auto Scaling groups to add or remove instances based on demand. Amazon EMR requires customers to manually resize clusters or configure managed scaling policies, and does not scale automatically without intervention. Amazon EBS volumes are fixed in size when provisioned and must be manually resized, and do not scale automatically in response to usage.

## clf-c02/domain3/q296

Answer: D

Elastic Load Balancers continuously monitor the health of registered targets and only route traffic to instances that pass health checks, ensuring unhealthy targets do not receive requests.
Distributing traffic across multiple S3 buckets describes a function that ELBs do not perform, as Elastic Load Balancers route traffic to compute targets such as EC2 instances, containers, and Lambda functions rather than object storage buckets. Replicating data to multiple Availability Zones is a feature of services such as Amazon RDS Multi-AZ, which synchronously replicates database data across AZs, and is not a function of Elastic Load Balancers. Creating database Read Replicas is a feature of Amazon RDS that offloads read traffic from a primary database instance, and is entirely unrelated to load balancing or application traffic routing.

## clf-c02/domain3/q298

Answer: C

AWS Snowmobile is an exabyte-scale data transfer service delivered as a ruggedised 45-foot shipping container, capable of transferring up to 100 petabytes per unit, making it the appropriate choice for a 60 petabyte migration.
AWS Snowball is a physical data transport device suited for transferring up to 80 terabytes per device, which is far below the 60 petabyte requirement and would require an impractical number of devices compared to Snowmobile. Amazon S3 Transfer Acceleration speeds up uploads to S3 by routing traffic through CloudFront edge locations over the internet, but is not suitable for petabyte-scale data migrations where physical transport is required. Amazon VPC is a networking service for provisioning isolated virtual networks within AWS, and has no role in physically or programmatically transferring large datasets into AWS.

## clf-c02/domain3/q299

Answer: A

Amazon S3 Glacier provides low-cost archival storage with retrieval options including Expedited (1 to 5 minutes), Standard (3 to 5 hours), and Bulk (5 to 12 hours). For a five-hour retrieval requirement, S3 Glacier Standard retrieval meets the SLA at the lowest cost.
Amazon EFS is a managed shared network file system that provides concurrent file access from multiple instances, and is designed for active file workloads rather than long-term archival storage where cost is the primary concern. Amazon S3 Standard provides durable, highly available object storage with immediate millisecond retrieval, and while it meets the retrieval requirement it is significantly more expensive per gigabyte than S3 Glacier for storing five years of infrequently accessed archival data. Amazon EBS provides persistent block storage volumes attached directly to EC2 instances for low-latency disk access, and is a compute-attached storage service not designed for long-term archival or for storing data independently of a running instance.

## clf-c02/domain3/q304

Answer: A, D

Amazon S3 can host static websites by serving HTML, CSS, and JavaScript files directly, and it serves as an origin store for Amazon CloudFront, delivering media content globally through edge caching.
Hosting websites that require sustained high CPU utilization describes a compute-intensive workload that requires EC2 instances or similar compute services, as S3 is an object storage service with no CPU processing capability. Cost-effective database and log storage conflates two different use cases, as S3 can store log files but is not a database service and purpose-built database services such as RDS or DynamoDB are more appropriate for structured data. Processing data streams at any scale describes the function of Amazon Kinesis, which is designed for real-time data stream ingestion and processing, not Amazon S3.

## clf-c02/domain3/q308

Answer: C

Amazon EBS provides high-performance block storage volumes that attach directly to EC2 instances, delivering the low-latency I/O needed for databases with high read/write activity.
AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage, and is not designed for high-performance database workloads requiring low-latency block storage. Amazon S3 is an object storage service optimized for storing and retrieving large amounts of unstructured data, and does not provide the low-latency block-level I/O that databases with high read/write activity require. Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and can tolerate retrieval times of hours, making it entirely unsuitable for active database workloads.

## clf-c02/domain3/q310

Answer: A

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database that delivers up to five times the throughput of standard MySQL, with the reliability and availability of a commercial database at a fraction of the cost.
Amazon Redshift is a fully managed data warehouse service optimized for running complex analytical queries across large datasets, and is not a MySQL-compatible relational database designed for high-throughput transactional workloads. Amazon DynamoDB is a fully managed NoSQL database that supports key-value and document data models, and does not offer MySQL compatibility or the relational capabilities that Aurora provides. Amazon Neptune is a fully managed graph database service designed for storing and querying highly connected data, and has no MySQL compatibility or relation to the performance characteristics described.

## clf-c02/domain3/q311

Answer: C

AWS Service Catalog allows organizations to create and manage approved catalogs of IT services, enabling standardized governance and self-service deployment of commonly used resources across the organization.
Providing descriptions and use cases for AWS services describes the function of the AWS documentation and the AWS console service pages, not AWS Service Catalog, which is a governance and deployment tool rather than an informational reference resource. Enabling customers to explore different catalogs of AWS services describes the AWS Marketplace, where customers can find and purchase third-party software and services, rather than AWS Service Catalog, which manages internally approved IT products. Allowing developers to deploy infrastructure using familiar programming languages describes the AWS Cloud Development Kit, which lets developers define cloud infrastructure in languages such as Python, TypeScript, and Java, and is a developer tooling service rather than a catalog management and governance platform.

## clf-c02/domain3/q313

Answer: B

AWS Application Discovery Service collects information about on-premises servers, including configuration, usage, and dependencies, to help plan and prioritize migration to the AWS Cloud.
AWS Snowball is a physical device used to transfer large volumes of data into AWS and is a data transfer tool rather than a migration planning service. AWS Database Migration Service migrates databases to AWS with minimal downtime, but handles the execution of database migrations rather than the discovery and planning phase. AWS Migration Hub provides a central location to track the progress of migrations across multiple AWS and partner tools, but it monitors migration status rather than collecting the server data needed to plan a migration.

## clf-c02/domain3/q315

Answer: C

An AWS Region is a physical geographic location that contains a collection of Availability Zones, each consisting of one or more discrete data centers with redundant power, networking, and connectivity.
A geographical location with a collection of edge locations confuses Regions with the CloudFront edge network, which is a separate layer of infrastructure distributed independently of Regions. A virtual network dedicated only to a single AWS customer describes an Amazon VPC, not a Region, as Regions are shared physical infrastructure used by all AWS customers. A country where AWS infrastructure exists is too broad and inaccurate, as multiple Regions can exist within the same country and a Region is a specific defined geographic area, not a national boundary.

## clf-c02/domain3/q317

Answer: C, D

The number of reads and writes per second determines throughput requirements and helps identify whether a database needs to handle high-volume transactional workloads, and the nature of the queries determines whether a relational database for complex joins or a NoSQL database for simple key-value lookups is the better fit.
Availability Zones are an infrastructure consideration for deploying databases with high availability and redundancy, but they do not influence which database technology or engine is appropriate for a given workload. Data sovereignty refers to legal and regulatory requirements about where data must be stored geographically, which affects Region selection but does not determine the appropriate database technology for a workload. Software bugs are a development and quality assurance concern unrelated to the criteria used to select an appropriate database technology.

## clf-c02/domain3/q324

Answer: A

Amazon EC2 provides virtual servers that customers manage, including the operating system and software stack. It is a server-based compute service, not a serverless one. AWS Lambda is the serverless compute service where AWS manages all underlying infrastructure.
Amazon EC2 does eliminate the need to invest in hardware upfront, as customers pay only for the compute capacity they use rather than purchasing and maintaining physical servers. Amazon EC2 does allow customers to launch as many or as few virtual servers as needed, scaling capacity up or down in response to changing requirements. Amazon EC2 does offer scalable computing, enabling customers to increase or decrease capacity within minutes to match workload demands.

## clf-c02/domain3/q325

Answer: A

AWS Lambda is a serverless compute service that runs code in response to events such as HTTP requests, file uploads, or database changes, without requiring you to provision or manage servers.
Amazon CloudWatch is a monitoring and observability service that collects metrics and logs from AWS resources, and does not execute application code. AWS Elastic Beanstalk is a platform service that deploys and manages web applications by automatically provisioning the underlying infrastructure, but it runs continuously on provisioned servers rather than executing code only in response to events. Amazon EC2 provides virtual servers where customers are responsible for provisioning and managing the instances, making it a server-based solution rather than an event-driven serverless compute service.

## clf-c02/domain3/q326

Answer: D

Amazon EC2 instances are virtual servers in the AWS Cloud that provide resizable compute capacity, allowing customers to run applications on AWS infrastructure just as they would on physical servers.
Amazon EBS Snapshots are point-in-time backups of EBS storage volumes, not virtual servers. Amazon VPC is a networking service that provides an isolated virtual network environment within AWS, not a virtual server. Amazon Lightsail also provides virtual servers but is designed for simpler workloads with a more limited and fixed configuration, whereas EC2 offers the full range of instance types and customization options comparable to traditional IT virtual server offerings.

## clf-c02/domain3/q331

Answer: A, D

Amazon DynamoDB automatically scales throughput capacity to handle traffic fluctuations and delivers consistent single-digit millisecond latency at any scale, making it ideal for high-performance applications.
Providing resizable instances describes the EC2 model of vertical scaling, whereas DynamoDB is serverless and has no concept of instances that customers provision or resize. DynamoDB is a NoSQL database service that supports key-value and document data models only, and does not support relational data models. DynamoDB is a proprietary AWS NoSQL service and does not support or run third-party database engines such as CouchDB or MongoDB.

## clf-c02/domain3/q337

Answer: C

Amazon Simple Notification Service supports sending SMS text messages to over 200 countries worldwide, in addition to push notifications and email, making it the purpose-built solution for promotional messaging at scale.
Amazon Simple Email Service is an email sending service designed for transactional and marketing email communications, and does not support SMS text messaging. Amazon Simple Storage Service is an object storage service for storing and retrieving data such as files, images, and backups, and has no messaging or SMS capability of any kind. Amazon Simple Queue Service is a fully managed message queuing service that enables decoupling of application components by passing messages between them, and is an application integration tool rather than a service for sending SMS messages to end users.

## clf-c02/domain3/q338

Answer: C, E

AWS CloudFormation can define and provision RDS instances through infrastructure-as-code templates, and the AWS Management Console provides a graphical interface for creating RDS instances directly.
AWS CodeDeploy is a deployment service that automates releasing application code to compute targets such as EC2 instances and Lambda functions, and has no capability to create or provision RDS database instances. AWS Quick Starts are pre-built deployment templates that help customers launch AWS environments following best practices, but they are a reference architecture resource rather than a service that directly creates or provisions RDS instances. AWS DMS migrates existing databases to AWS with minimal downtime, and is a migration tool rather than a service for creating new RDS instances from scratch.

## clf-c02/domain3/q350

Answer: D

Amazon RDS Read Replicas create read-only copies of your database that handle read queries, offloading read traffic from the primary instance and improving overall application performance.
Database Snapshots are point-in-time backups of an RDS instance stored in Amazon S3, used for data recovery and restoration rather than for distributing or offloading read activity. Multi-AZ Deployments maintain a synchronous standby replica of the database in a different Availability Zone for high availability and automatic failover, but the standby instance does not serve read traffic and exists solely for redundancy. Automated Backups enable point-in-time recovery by continuously backing up the database and transaction logs, and are a data protection feature rather than a mechanism for offloading read activity.

## clf-c02/domain3/q353

Answer: B

An Application Load Balancer distributes incoming HTTP and HTTPS traffic across multiple EC2 instances, automatically routing requests to healthy targets and balancing the load evenly across the fleet.
AWS Global Accelerator improves the availability and performance of applications for global users by routing traffic through the AWS global network to the nearest healthy endpoint, and is a global traffic routing service rather than a tool for distributing load evenly across instances within a single deployment. Amazon CloudFront is a content delivery network that caches and serves content from edge locations worldwide to reduce latency for end users, and is a content distribution service rather than a load balancing solution for distributing application traffic across EC2 instances. AWS Transit Gateway acts as a central network hub connecting multiple VPCs and on-premises networks, and is a network connectivity service with no capability to distribute application traffic across compute instances.

## clf-c02/domain3/q354

Answer: C

Infrastructure as code uses tools such as AWS CloudFormation to define and provision AWS resources programmatically through templates, eliminating manual console steps and making environment creation repeatable, consistent, and automated.
Software test automation tools are used to automate testing of application code, such as running unit tests or integration tests, and do not address the provisioning and configuration of AWS infrastructure. AWS CodeDeploy is a deployment service that automates application deployments to EC2 instances, Lambda functions, or on-premises servers; it handles application code deployment but does not provision or configure the underlying AWS infrastructure environment. Migrating applications to a dedicated host changes the underlying physical server isolation model for compliance or licensing purposes, but does not automate or codify the process of creating and updating the AWS environment.

## clf-c02/domain3/q357

Answer: B, C

Data sovereignty requirements dictate that data must stay in specific geographic locations for legal or regulatory reasons, and pricing varies between Regions, making both critical factors when choosing where to deploy AWS resources.
All AWS Regions are built to the same security standards, so the security level of a Region is not a differentiating factor when selecting where to deploy. The planned number of VPCs is an architectural decision made after Region selection and has no bearing on which Region to choose. Geographic proximity to the company's location is not a primary selection factor, as latency considerations relate to where end users are located rather than where the company itself is based.

## clf-c02/domain3/q358

Answer: C

Amazon ElastiCache is a managed in-memory caching service supporting Redis and Memcached that stores frequently accessed data in memory, delivering sub-millisecond response times for read-heavy applications such as a financial services web application backed by MySQL.
Amazon Elastic File System is a managed shared network file system designed for concurrent access from multiple compute instances, and is a file storage service with no in-memory caching capability. Amazon Neptune is a fully managed graph database service optimized for storing and querying highly connected data such as social networks and knowledge graphs, and is a specialized database rather than an in-memory caching layer. Amazon DynamoDB Accelerator (DAX) is an in-memory caching service specifically designed to accelerate Amazon DynamoDB read performance, and is tightly coupled to DynamoDB rather than being a general-purpose caching layer compatible with a MySQL database.

## clf-c02/domain3/q359

Answer: B

Auto Scaling Groups automatically adjust the number of EC2 instances across multiple Availability Zones based on demand, increasing both application availability and fault tolerance by ensuring capacity matches load.
Caching responses at global edge locations to reduce latency describes Amazon CloudFront, not Auto Scaling Groups, which have no caching capability. Auto Scaling Groups operate within a single Region and cannot scale EC2 instances across multiple Regions, so cross-region latency reduction is not a function they provide. Distributing application traffic across multiple Availability Zones describes Elastic Load Balancing, which works alongside Auto Scaling Groups but is a separate service responsible for traffic distribution.

## clf-c02/domain3/q363

Answer: B

AWS Elastic Beanstalk is a managed application deployment service that provisions the underlying infrastructure, handles deployment, capacity provisioning, load balancing, and auto scaling, enabling rapid deployment of existing .NET applications with minimal configuration.
Amazon SNS is a publish/subscribe messaging service used to fan out notifications to subscribers such as email, SMS, or other applications, and does not provide any capability to deploy or run application code. AWS Systems Manager is an operations management service used for tasks such as patching, inventory, and configuration management of existing resources, and is not a platform for deploying .NET applications. AWS Trusted Advisor is an advisory service that inspects your AWS environment and provides recommendations on cost optimization, performance, security, and fault tolerance, and cannot be used to deploy applications.

## clf-c02/domain3/q365

Answer: B

AWS Storage Gateway connects on-premises environments to AWS cloud storage, providing a hybrid storage solution that allows organizations to extend their existing on-premises storage infrastructure to AWS in a cost-effective way by tiering infrequently accessed data to the cloud.
AWS Transfer Family provides managed file transfer workflows using SFTP, FTPS, and FTP protocols to move files directly into and out of Amazon S3 or EFS, and is a data transfer service rather than a hybrid storage extension solution for on-premises environments. Amazon Aurora is a fully managed, high-performance relational database engine compatible with MySQL and PostgreSQL, and is a database service rather than a storage extension solution for on-premises data. Amazon EFS is a managed, scalable NFS file system accessible by multiple EC2 instances in the cloud, and while it provides file storage, it is a cloud-native service rather than a gateway for extending on-premises storage capacity to AWS.

## clf-c02/domain3/q366

Answer: A

Amazon S3 provides virtually unlimited object storage that scales automatically with usage and charges only for what you store, making it ideal for cloud storage platforms that need elastic capacity at low cost.
Amazon Elastic Block Store provides persistent block storage volumes that attach directly to EC2 instances for low-latency disk access, and has a fixed provisioned capacity model where you pay for the volume size you provision rather than scaling automatically based on objects stored. Amazon Elastic Container Service is a container orchestration service that manages the deployment and scaling of containerised applications, and is a compute service rather than a storage service for an object storage platform. AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage integration, and is designed for bridging on-premises infrastructure with AWS rather than serving as the underlying storage for a cloud-native storage platform.

## clf-c02/domain3/q374

Answer: B, C

AWS Lambda runs code in response to events without requiring any server provisioning or management, and Amazon DynamoDB is a fully managed NoSQL database that scales automatically without customers needing to manage any underlying infrastructure. Both are serverless services where AWS manages all underlying infrastructure.
Amazon EC2 provides virtual servers where customers are responsible for provisioning, configuring, and managing the instances, making it a server-based rather than serverless compute service. Amazon EMR runs big data processing frameworks on provisioned clusters of EC2 instances, requiring customers to manage the underlying cluster infrastructure rather than abstracting it away. Amazon RDS is a managed relational database service, but customers must select and manage the underlying instance type, size, and maintenance windows, meaning it is a managed rather than fully serverless service.

## clf-c02/domain3/q376

Answer: B

AWS Systems Manager provides a suite of tools for automating operational tasks across EC2 instances at scale, including configuration management, patch management, run command execution, and inventory collection without needing to log into individual instances.
AWS Config records and evaluates configuration changes to AWS resources for compliance and auditing purposes, but does not automate configuration or patching of instances. AWS Auto Scaling automatically adjusts the number of EC2 instances based on demand but does not manage instance configuration or patching. AWS CloudFormation automates the provisioning of AWS infrastructure through templates but does not handle ongoing configuration management or patching of running instances.

## clf-c02/domain3/q377

Answer: C

Amazon S3 stores objects that can be made publicly accessible via unique URLs, making it the standard AWS service for hosting and serving downloadable content over the internet.
Amazon EBS provides block storage volumes that attach to individual EC2 instances and are not accessible directly over the internet as downloadable objects. Amazon EFS provides a shared file system mountable across EC2 instances via NFS protocol and is not designed for serving objects as publicly downloadable content over the internet. Amazon Instance Store provides temporary block storage physically attached to the host server running an EC2 instance, is ephemeral by nature, and cannot be accessed over the internet.

## clf-c02/domain3/q378

Answer: B

Amazon CloudWatch monitors HTTP and HTTPS requests forwarded to CloudFront distributions, providing metrics such as request count, error rates, and latency that can be visualised and used to set alarms.
AWS WAF is a web application firewall that filters and blocks malicious HTTP and HTTPS requests based on defined rules, but it inspects and controls traffic rather than monitoring and reporting on request metrics. AWS Cloud9 is a cloud-based integrated development environment for writing, running, and debugging code, and has no monitoring or traffic analysis capability. AWS CloudTrail records API calls and account activity across AWS services for auditing and compliance purposes, and does not monitor HTTP and HTTPS request metrics for CloudFront distributions.

## clf-c02/domain3/q383

Answer: A

Amazon SQS is a fully managed message queuing service that decouples application components by allowing each component to send and receive messages independently, enabling a monolithic application to be broken into loosely coupled parts that communicate asynchronously.
Amazon SNS is a publish/subscribe messaging service that broadcasts messages to multiple subscribers simultaneously, which is useful for fan-out notification patterns but is not the primary service for decoupling monolithic application components through asynchronous message queuing. Amazon EventBridge is a serverless event bus that routes events between AWS services, SaaS applications, and custom applications based on event patterns; while it supports decoupled architectures, it is event-driven routing rather than a message queue for decoupling component dependencies in a monolithic application. AWS Step Functions is a serverless workflow orchestration service that coordinates multiple AWS services into structured workflows, which handles workflow state management rather than providing the message queuing mechanism needed to decouple monolithic application components.

## clf-c02/domain3/q385

Answer: D

Running multiple EC2 instances in parallel distributes the processing of large binary files across many machines simultaneously, completing the work faster than scaling a single instance vertically.
Vertically scaling EC2 instances increases the power of a single machine, which has practical limits and does not distribute the workload across multiple processors simultaneously, making it less efficient for large parallel processing tasks. Running RDS instances in parallel is not applicable to processing binary files, as RDS is a relational database service designed for structured data storage and querying rather than file processing workloads. Vertically scaling RDS instances increases database capacity and performance, which is also irrelevant to processing binary files as RDS serves no role in compute-based file processing tasks.

## clf-c02/domain3/q389

Answer: A

Amazon EFS provides a fully managed NFS file system that can be mounted concurrently by thousands of EC2 instances, enabling shared file storage across multiple servers simultaneously.
Amazon S3 is an object storage service accessed via API or HTTP rather than mounted as a file system, and does not support NFS protocol or concurrent mounting by EC2 instances. Amazon EBS provides block storage volumes that can only be attached to a single EC2 instance at a time and does not support concurrent mounting across multiple instances. AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage and is not designed for concurrent NFS mounting across EC2 instances.

## clf-c02/domain3/q390

Answer: D

Low-latency links between Availability Zones within a Region enable synchronous data replication, meaning data written in one AZ is immediately confirmed as written in another before the operation completes, supporting high availability within a Region.
Creating a private connection to a data center describes AWS Direct Connect, which is a separate networking service and has nothing to do with the internal links between Availability Zones. Achieving global high availability requires deploying across multiple Regions rather than relying on AZ links within a single Region, which only provides availability at a regional level. Automating the provisioning of compute resources describes services like EC2 Auto Scaling and is unrelated to the low-latency connectivity that exists between Availability Zones.

## clf-c02/domain3/q391

Answer: B, E

AWS Lambda natively supports multiple programming languages including Node.js, Python, Java, Go, and .NET, and can support virtually any other language through custom runtimes via the Lambda Runtime API.
Lambda only supporting Python and Node.js is false, as Lambda has native support for a broad range of languages without any third-party plugins. Lambda being AWS's proprietary programming language is false, as Lambda is a compute service that runs code written in standard programming languages, not a language itself. Lambda not supporting programming languages is false and contradicts how the service works, as running code in a supported language is its core function.

## clf-c02/domain3/q392

Answer: B, C

AWS X-Ray traces user requests as they travel through your application, helping you identify performance bottlenecks and errors, and providing the visibility needed to improve overall application performance.
Automatically decoupling application components describes a design architecture pattern, not a capability of any single AWS service. AWS X-Ray observes and analyzes existing application behavior but does not modify application architecture. Deploying applications to Amazon EC2 instances describes AWS CodeDeploy, which automates application deployments to compute services including EC2. Deploying applications to on-premises servers also describes AWS CodeDeploy, which supports deployment targets beyond AWS including on-premises servers, making it unrelated to application tracing or performance analysis.

## clf-c02/domain3/q393

Answer: D

An Availability Zone is an isolated data center location within an AWS Region with independent power, cooling, and networking, while edge locations are separate infrastructure points distributed across hundreds of cities worldwide to serve content closer to end users.
Edge locations are located in separate Availability Zones worldwide to serve global customers edge locations are an independent layer of infrastructure and are not located within or associated with Availability Zones. An availability zone exists within an edge location to distribute content globally with low latency the relationship is inverted here, and Availability Zones are part of Regions, not contained within edge locations. An Availability Zone is a geographic location where AWS provides multiple, physically separated and isolated edge locations this confuses the definition of an Availability Zone with that of a Region, and edge locations are not nested inside Availability Zones.

## clf-c02/domain3/q396

Answer: A

AWS CloudFormation lets you define your entire infrastructure as reusable templates in JSON or YAML, enabling consistent and repeatable provisioning of the same resource configurations across multiple projects.
AWS Config continuously monitors and records the configuration state of existing AWS resources and evaluates them against desired settings, but does not provision infrastructure from templates. AWS CloudTrail records API calls and user activity across your AWS account for auditing and compliance purposes, unrelated to infrastructure provisioning. AWS Auto Scaling automatically adjusts the number of compute resources in response to demand but does not define or provision infrastructure configurations as reusable templates.

## clf-c02/domain3/q398

Answer: B, C

Microsoft SQL Server can run on Amazon EC2 as a self-managed installation with full OS-level control, or on Amazon RDS as a fully managed engine where AWS handles patching, backups, and high availability automatically.
AWS Fargate is a serverless compute engine for running containers and does not support running a SQL Server database directly as a managed or self-managed database engine. AWS Database Migration Service is used to migrate databases from one source to a target with minimal downtime, but it is a migration tool rather than a platform for running SQL Server on an ongoing basis. AWS Lambda is a serverless function execution service that runs event-driven code and is not designed to host or run database engines such as SQL Server.

## clf-c02/domain3/q399

Answer: B

Amazon Route 53 performs health checks on endpoints, monitoring their availability and automatically routing traffic away from unhealthy resources to maintain application uptime through DNS failover.
AWS CloudFormation provisions and manages AWS infrastructure using code-based templates, and does not monitor endpoint availability or route traffic. Amazon CloudWatch monitors metrics, logs, and alarms for AWS resources, but does not perform DNS-based routing or redirect traffic away from unhealthy endpoints. Amazon Aurora is a managed relational database engine and has no endpoint monitoring or traffic routing capability.

## clf-c02/domain3/q400

Answer: D

Amazon Rekognition uses deep learning to analyze images and videos, providing facial recognition, object detection, and scene analysis capabilities that can automate tasks like photo tagging.
Amazon Comprehend is a natural language processing service that analyzes and extracts meaning from written text, and has no capability to process images or perform facial recognition. Amazon Textract extracts printed text, handwriting, and structured data from scanned documents and images, but does not perform facial recognition or analyze visual scenes. Amazon Polly is a text-to-speech service that converts written text into natural-sounding audio, and has no image analysis or facial recognition capability.

## clf-c02/domain3/q401

Answer: A, E

Amazon Neptune is a fully managed graph database, and Amazon RDS for MySQL is a fully managed relational database, with AWS handling provisioning, patching, backups, and recovery for both.
Amazon CloudSearch is a managed search service for building search functionality into applications, and is not a database service. Microsoft SQL Server on Amazon EC2 is a self-managed database deployment where the customer is responsible for installation, patching, backups, and maintenance, making it the opposite of an AWS-managed database. MySQL on Amazon EC2 is also a self-managed deployment with the same customer responsibilities, and does not benefit from the managed database features that AWS provides through RDS.

## clf-c02/domain3/q404

Answer: B

AWS Application Migration Service automates the migration of on-premises server workloads to AWS by continuously replicating source servers and allowing cutover with minimal downtime, making it the recommended service for large-scale server migrations.
AWS File Transfer Acceleration is not a real AWS service and does not exist in the AWS service catalog. AWS Database Migration Service is purpose-built for migrating databases rather than entire server workloads, making it too narrow for general on-premises workload migration. AWS Application Discovery Service gathers information about on-premises environments to help plan migrations but does not perform the migration itself.

## clf-c02/domain3/q405

Answer: C, D

AWS CloudFormation allows you to model your entire infrastructure in a JSON or YAML text file, and automates the provisioning and updating of resources in a safe, controlled, and repeatable manner.
Deploying applications without worrying about underlying infrastructure describes AWS Elastic Beanstalk, which abstracts infrastructure management for application deployment, not CloudFormation. Applying advanced IAM security features automatically is not a CloudFormation capability, as IAM policies and security configurations must still be defined and managed by the customer. Compiling and building application code is a function of build tools such as AWS CodeBuild, not CloudFormation, which deals with infrastructure provisioning rather than application code.

## clf-c02/domain3/q407

Answer: A

AWS Elastic Disaster Recovery continuously replicates machines into a staging area in another AWS Region and can launch fully provisioned instances within minutes during an outage, providing fast cross-Region failover.
AWS Application Migration Service is a server migration tool designed to move workloads to AWS, not to maintain a live standby environment for disaster recovery purposes. AWS Backup is a centralized backup service that automates data protection across AWS services, but does not maintain a continuously replicated standby environment that can be activated within minutes. AWS Glue is a serverless data integration service used for ETL workloads and data cataloguing, and has no disaster recovery or replication capability.

## clf-c02/domain3/q408

Answer: D

S3 Standard is designed for frequently accessed data with low latency and high throughput, making it the most appropriate storage class for static assets on a popular e-commerce site with consistent, stable access patterns.
S3 Standard-IA is designed for data that is accessed infrequently but requires rapid access when needed, and carries a per-retrieval charge that makes it more expensive than S3 Standard for assets that are accessed consistently and frequently. S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns, making it better suited for data with unpredictable or unknown access frequency rather than assets with stable, predictable demand. S3 Glacier Deep Archive is the lowest-cost storage class designed for long-term archival of data that is rarely if ever accessed, and is entirely unsuitable for serving live website assets that require immediate low-latency retrieval.

## clf-c02/domain3/q409

Answer: B

Storing backups in another AWS Region places your data in a completely separate geographic location, protecting against Region-level disasters such as natural catastrophes or widespread outages.
Edge locations are points of presence used by services such as Amazon CloudFront to cache and deliver content to users with low latency, and are not storage locations where backups can be created or maintained. A VPC is a logically isolated virtual network within a single AWS Region, and storing data in another VPC does not place it in a different geographical location. An Availability Zone is a physically separate data center within a single AWS Region, and while storing backups in another AZ improves resilience against localised failures, it does not satisfy the requirement for a different geographical location as multiple AZs share the same Region.

## clf-c02/domain3/q412

Answer: D

Amazon RDS Multi-AZ maintains a synchronous standby replica in a different Availability Zone and automatically fails over to it if the primary database becomes unresponsive, minimizing downtime.
RDS Single-AZ deploys the database in a single Availability Zone with no standby instance, meaning there is no automatic failover if the primary database becomes unavailable. RDS Read Replicas create read-only copies of the database to offload read traffic from the primary instance, but they are not synchronised in real time and do not provide automatic failover for high availability. RDS Snapshots are point-in-time backups used for data recovery and restoration, and cannot perform automatic failover in response to a database failure.

## clf-c02/domain3/q421

Answer: A

AWS Auto Scaling automatically adjusts the number of EC2 instances in response to real-time demand, adding capacity during traffic spikes like flash sales and removing it when demand drops to control costs.
Amazon EC2 provides the virtual server instances that run the application, but on its own it does not automatically add or remove capacity in response to traffic fluctuations. Amazon Elastic File System is a managed shared file storage service for use with EC2 and other compute services, unrelated to dynamic compute scaling. Amazon ElastiCache is an in-memory caching service for improving database and application read performance, not a service for dynamically adjusting compute capacity.

## clf-c02/domain3/q422

Answer: B

Amazon VPC gives customers complete control over their virtual networking environment, including selection of IP address ranges, creation of subnets, and configuration of route tables and network gateways.
Controlling user interactions with AWS resources is the function of AWS IAM, which manages permissions and access policies, not Amazon VPC. AWS is not responsible for all management and configuration of Amazon VPC, as customers retain full responsibility for configuring their own subnets, route tables, security groups, and network ACLs. Reviewing AWS architecture and adopting best practices describes the AWS Well-Architected Tool, not Amazon VPC, which is a networking service rather than an architectural review service.

## clf-c02/domain3/q425

Answer: C

AWS Systems Manager provides a suite of tools to automate the configuration, maintenance, and management of EC2 instances at scale, including applying configuration policies, running commands across fleets, and maintaining desired state without manual intervention.
AWS OpsWorks (deprecated) was a configuration management service using Puppet and Chef that has been discontinued by AWS as of May 2024 and is no longer available. AWS CloudFormation automates the provisioning of AWS infrastructure using templates, but operates at the infrastructure level rather than managing the ongoing configuration of running instances. AWS CloudTrail records API calls and account activity for auditing and compliance purposes, and has no server configuration or automation capability.

## clf-c02/domain3/q427

Answer: A, E

Amazon RDS runs on provisioned database server instances that customers select and manage, and Amazon EMR runs on clusters of EC2 instances for big data processing, making both server-based services.
Amazon DynamoDB is a fully serverless NoSQL database that scales automatically without any server provisioning or management required. AWS Lambda is a serverless compute service that runs code in response to events without requiring customers to provision or manage any servers. AWS Fargate is a serverless compute engine for containers that removes the need to provision or manage the underlying EC2 instances.

## clf-c02/domain3/q429

Answer: C, D

Amazon EMR provides a managed cluster platform for running big data frameworks like Apache Spark and Hadoop, enabling both the analysis and processing of extremely large datasets at scale.
Backing up extremely large amounts of data at very low costs describes Amazon S3 combined with S3 Glacier storage classes, which are purpose-built for durable, low-cost data storage and archival. Moving exabyte-scale data from on-premises data centers into AWS describes AWS Snowmobile, which is a physical data transfer service for migrating extremely large datasets using a secure shipping container. Running and managing Docker containers describes Amazon ECS or AWS Fargate, which are container orchestration services unrelated to big data processing frameworks.

## clf-c02/domain3/q431

Answer: D

AWS Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring, allowing developers without cloud infrastructure experience to deploy and manage applications without needing to understand the underlying infrastructure.
AWS Fargate is a serverless compute engine for containers that removes the need to manage servers for containerised workloads, but it requires knowledge of container concepts and configuration, making it more complex to adopt for developers without cloud experience compared to the abstraction Beanstalk provides. AWS Batch manages the infrastructure required to run batch computing jobs at scale, and is designed for processing large numbers of batch workloads rather than helping developers quickly deploy and manage general-purpose applications. Amazon Personalize is a fully managed machine learning service that builds real-time personalization and recommendation systems, and is an AI/ML service for a specific use case rather than a general application deployment and management platform.

## clf-c02/domain3/q433

Answer: A, C

For Amazon RDS, AWS handles the initial database setup including provisioning and configuration, and manages the underlying operating system including patching and maintenance, removing these operational burdens from the customer.
Network traffic protection is a shared responsibility where customers configure security groups and NACLs to control traffic to their RDS instances, rather than AWS managing this on the customer's behalf. Access management is the customer's responsibility, as customers control their own IAM policies and database user credentials. Management of firewall rules is the customer's responsibility, as customers define the security group rules that control inbound and outbound access to their RDS instances.

## clf-c02/domain3/q435

Answer: A

AWS Direct Connect establishes a dedicated private network connection between an on-premises data center and AWS, providing consistent throughput and lower latency than internet-based connections, making it the right choice for daily large-scale business-critical data transfers.
Amazon Comprehend is a natural language processing service for extracting insights and relationships from text and has no role in network connectivity or data transfer. AWS Snowmobile is a physical data transfer service for one-time migration of extremely large datasets to AWS, not for recurring daily transfers requiring a consistent network connection. AWS VPN establishes an encrypted connection over the public internet, which does not provide the consistent throughput and reliability guarantees required for business-critical daily large data transfers.

## clf-c02/domain3/q436

Answer: C

AWS Storage Gateway integrates on-premises IT environments with AWS cloud storage by providing standard storage protocols such as NFS, SMB, and iSCSI that connect local applications seamlessly to S3, EBS, or Glacier.
Automating the process of building, maintaining, and running ETL jobs describes AWS Glue, which is a serverless data integration service for preparing and transforming data for analytics pipelines. Providing physical devices to migrate data from on-premises to AWS describes the AWS Snow Family, specifically AWS Snowball or Snowmobile, which are physical appliances for bulk data transfer rather than ongoing hybrid storage integration. Providing hardware-based key storage for regulatory compliance describes AWS CloudHSM, which is a dedicated hardware security module for generating and managing cryptographic keys.

## clf-c02/domain3/q437

Answer: B

Amazon S3 Standard-Infrequent Access offers lower storage costs than S3 Standard while still providing immediate, millisecond retrieval, making it cost-effective for backups that are accessed infrequently but need to be available instantly.
Amazon S3 Glacier Deep Archive is the lowest-cost storage class for long-term archival data that is accessed very rarely, with retrieval times of 12 hours or more, making it unsuitable for backups that require immediate retrieval. Amazon S3 Glacier provides low-cost archival storage with retrieval options ranging from minutes to hours depending on the retrieval tier selected, and while less expensive than S3 Standard it does not provide the immediate millisecond retrieval required for backup recovery. Instance Store provides temporary block storage physically attached to the host machine running an EC2 instance, and is ephemeral storage that is lost when the instance stops, making it entirely unsuitable for durable backup storage.

## clf-c02/domain3/q438

Answer: A

AWS Global Accelerator uses the AWS global network to route user traffic to the optimal healthy endpoint based on performance, geography, and health checks, improving application performance and availability for global users.
AWS Data Pipeline (deprecated) is a service for orchestrating and automating the movement and transformation of data between AWS services, unrelated to traffic routing or application performance. Amazon DynamoDB Accelerator is an in-memory cache specifically for DynamoDB that reduces read latency for database queries, not a service for routing application traffic to optimal endpoints. Amazon S3 Transfer Acceleration speeds up uploads to S3 buckets by routing traffic through CloudFront edge locations, which is specific to S3 data transfer and not a general application traffic routing solution.

## clf-c02/domain3/q440

Answer: C, D

Amazon Route 53 is a scalable DNS service that translates domain names to IP addresses, and it manages global application traffic through routing policies including latency-based, geolocation, weighted, and failover routing.
Point-to-point connectivity between an on-premises data center and AWS describes AWS Direct Connect, which provides a dedicated private network link between on-premises infrastructure and AWS. Detecting configuration changes in the AWS environment describes AWS Config, which continuously monitors and records resource configurations and evaluates them against desired settings. Providing infrastructure security optimization recommendations describes AWS Trusted Advisor, which analyzes your environment against best practice checks across security, cost, performance, and fault tolerance.

## clf-c02/domain3/q441

Answer: D

AWS Snowball is a physical data transfer device that moves up to 80 TB per device, making it cost-effective for transferring 200 TB of data without relying on slow or expensive network transfers.
AWS Snowmobile is designed for migrations at exabyte scale, typically 10 PB or more, making it far more than necessary and not cost-effective for a 200 TB transfer. AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, but transferring 200 TB over a network connection would be slow and costly compared to physical data transport. AWS DMS is purpose-built for migrating databases rather than transferring large volumes of unstructured data between on-premises locations and AWS.

## clf-c02/domain3/q442

Answer: D

Amazon ElastiCache for Redis is an in-memory data store that delivers sub-millisecond response times, making it the appropriate choice for a real-time IoT application requiring extremely low latency.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is designed for throughput-oriented batch analytics rather than sub-millisecond real-time data access. Amazon Athena is a serverless query service that analyzes data stored in Amazon S3 using SQL, and involves query execution times measured in seconds rather than the sub-millisecond latency that real-time IoT applications require. AWS Cloud9 is a cloud-based integrated development environment for writing, running, and debugging code, and is a developer tool with no data storage or low-latency serving capability.

## clf-c02/domain3/q444

Answer: D

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces deployment-ready software packages without requiring you to manage build servers.
AWS CodeDeploy automates the deployment of applications to EC2 instances, Lambda functions, and on-premises servers, but does not compile or test code. AWS CodeCommit is a managed source control service for hosting Git repositories, used for storing and versioning code rather than building or testing it. AWS CodePipeline orchestrates the stages of a release pipeline including source, build, and deploy phases, but delegates the actual compilation and testing to CodeBuild rather than performing it directly.

## clf-c02/domain3/q446

Answer: B, E

Amazon CloudFront is a CDN that caches content at edge locations worldwide, increasing application availability through redundant caching and delivering content to end users with low latency regardless of their location.
Tracking user activity and API usage across an AWS account describes AWS CloudTrail, an audit logging service that is unrelated to content delivery or edge caching. Faster disaster recovery is a benefit associated with multi-region architecture and services like AWS Backup or Route 53 failover routing, not a capability provided by a content delivery network. Storing archived data at very low costs describes Amazon S3 Glacier, an archival storage service with no content delivery or edge caching capability.

## clf-c02/domain3/q447

Answer: B

Amazon Connect is a cloud-based contact center service that lets you set up a customer service center in minutes with pay-per-use pricing and no infrastructure to manage, making it the purpose-built solution for replacing a traditional contact center.
Amazon Lightsail is a simplified cloud platform for deploying small applications and websites with predictable pricing, and has no contact center or customer communication functionality. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is a networking service entirely unrelated to contact center operations. AWS Elastic Beanstalk is a PaaS service for deploying and managing web applications, not a contact center or customer service platform.

## clf-c02/domain3/q451

Answer: A

AWS Resource Groups let you create logical groups of resources based on tags, enabling you to view and manage resources for each environment such as development, testing, and production from a custom console view.
AWS Placement Groups control how EC2 instances are physically placed on underlying hardware to optimize for latency or availability, and have no role in organizing or viewing resources by environment. AWS Management Console is the web-based interface for accessing all AWS services, but it does not provide custom grouped views per environment on its own. AWS Tag Editor is a tool for finding and managing tags across resources, but it does not create custom console views for grouped resource management.

## clf-c02/domain3/q452

Answer: B

Amazon CloudWatch collects and monitors metrics from EC2 instances including CPU utilization, disk I/O, and network traffic, providing visibility into instance performance and health.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not collect performance metrics. AWS CloudFormation is an infrastructure-as-code service that provisions and manages AWS resources through templates, and has no monitoring or metrics collection capability. AWS CloudTrail records API calls and account activity across AWS services for auditing and compliance purposes, and does not collect instance-level performance metrics.

## clf-c02/domain3/q453

Answer: B

AWS X-Ray traces requests as they travel through your application, identifying performance bottlenecks and helping you pinpoint the root cause of long load times and latency issues.
Amazon Detective is a security investigation service that analyzes and visualises data from AWS logs to help identify the root cause of security findings and suspicious activity, and has no capability to diagnose application performance issues or load times. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services and third-party tools into a centralized dashboard, and is a security posture management tool rather than an application performance diagnostics service. AWS Shield is a managed DDoS protection service that safeguards applications against distributed denial-of-service attacks, and does not address application performance bottlenecks or load time issues.

## clf-c02/domain3/q454

Answer: B, C

AWS Fargate runs containers without requiring you to provision or manage the underlying servers, and AWS Lambda runs code in response to events without provisioning any infrastructure. Both are serverless compute services where AWS handles all underlying infrastructure management.
Amazon EC2 provides virtual servers where customers are responsible for provisioning, configuring, and managing the instances, making it a server-based rather than serverless compute service. Amazon ECS is a container orchestration service that, when used without Fargate, requires customers to manage the underlying EC2 instances in the cluster. Amazon EMR is a managed big data processing service that runs on provisioned clusters of EC2 instances, not a serverless compute resource.

## clf-c02/domain3/q457

Answer: B

Amazon RDS is a managed relational database service that supports ACID transactions natively through engines such as MySQL, PostgreSQL, Oracle, and SQL Server, making it ideal for financial applications requiring data consistency.
Amazon Redshift is a cloud data warehouse service optimized for analytical queries across large datasets, and while it has some transactional support it is not designed for the high-volume ACID transaction processing required by financial applications. AWS CloudHSM is a hardware security module service that provides dedicated cryptographic key storage and processing, and has no database or transaction management capability. AWS DMS is a database migration service used to move data between database platforms, and is not a database engine that can host or process application transactions.

## clf-c02/domain3/q460

Answer: D

Teradata is not a supported engine in Amazon RDS. The supported engines are PostgreSQL, Oracle, Microsoft SQL Server, MySQL, MariaDB, and Amazon Aurora.
PostgreSQL is a fully supported RDS engine available for both standard and Aurora deployments. Oracle is a supported RDS engine, allowing customers to run Oracle databases on managed infrastructure. Microsoft SQL Server is a supported RDS engine, available across several editions including Express, Web, Standard, and Enterprise.

## clf-c02/domain3/q461

Answer: A

AWS Database Migration Service is purpose-built for migrating databases from on-premises to AWS, supporting both homogeneous migrations such as MySQL to MySQL and heterogeneous migrations between different database engines, with minimal downtime during the migration.
Amazon S3 Transfer Acceleration uses CloudFront edge locations to speed up uploads of data to S3 and is a file transfer acceleration feature rather than a database migration service. AWS Directory Service provides managed Microsoft Active Directory integration for enterprise identity management and has no capability to migrate or replicate relational or NoSQL database data. AWS Transit Gateway connects multiple VPCs and on-premises networks through a central hub for network routing and connectivity, and is a networking service that facilitates traffic routing rather than a database migration tool.

## clf-c02/domain3/q462

Answer: A

Amazon Lightsail provides pre-configured blueprints including a one-click WordPress installation, making it the easiest option for new customers who want a simple website without managing underlying infrastructure.
Installing WordPress on an EC2 instance requires manually provisioning a server, configuring networking, installing a web stack, and managing ongoing maintenance, making it significantly more complex than Lightsail for a simple use case. Amazon S3 can host static websites but does not support WordPress, which requires server-side processing and a database. AWS CDK is an infrastructure as code framework for defining cloud resources programmatically and cannot directly host websites or applications.

## clf-c02/domain3/q464

Answer: A

Amazon EC2 provides virtual servers with full operating system-level access, allowing you to install and run any custom database software of your choice on the underlying instance.
Amazon Cognito is a user identity and authentication service for web and mobile applications that manages user sign-up, sign-in, and access control, and has no capability to host or run database software. Amazon RDS is a managed relational database service that supports specific pre-configured database engines such as MySQL, PostgreSQL, and SQL Server, and does not allow you to install or run custom database software outside of those supported engines. Amazon Inspector is an automated security assessment service that scans AWS workloads for software vulnerabilities and unintended network exposure, and has no role in hosting or running database software.

## clf-c02/domain3/q465

Answer: A

AWS Auto Scaling dynamically adjusts the number of EC2 instances based on real-time demand metrics such as CPU and memory utilization, automatically adding or removing capacity as workload requirements change.
Elastic Load Balancing distributes incoming traffic across multiple targets to improve availability and prevent any single instance from being overwhelmed, but it does not add or remove compute resources in response to changing CPU and RAM requirements. Amazon Route 53 is a DNS and traffic routing service that resolves domain names and directs users to application endpoints, and has no capability to provision or adjust compute resources. Amazon Elastic Container Service is a container orchestration service for running and managing containerised applications, and while it can scale tasks, it is not the purpose-built solution for dynamically adjusting EC2 compute resources based on unpredictable load.

## clf-c02/domain3/q471

Answer: B, C

Amazon S3 automatically replicates objects across a minimum of three Availability Zones within a Region, and DynamoDB replicates data across multiple AZs by default, both providing built-in fault tolerance.
Instance Store is temporary block storage attached directly to the host EC2 instance. It is not replicated and data is lost if the instance stops or fails. Amazon Route 53 is a DNS and traffic routing service and does not replicate data across AZs in the same way. AWS VPN is a network connectivity service for securely connecting on-premises networks to AWS, unrelated to data replication.

## clf-c02/domain3/q475

Answer: A

S3 Versioning keeps every version of every object in the bucket, so even if an object is accidentally deleted, the previous version is retained and can be restored to recover the data.
Configuring S3 Bucket Policies controls who has permission to access, upload, or delete objects in a bucket, but does not preserve deleted objects or maintain previous versions for recovery. Configuring S3 Lifecycle Policies automates the transition of objects between storage classes or schedules their expiration after a defined period, which can actually result in objects being deleted rather than protecting them from accidental deletion. Disabling S3 Cross-Region Replication removes the ability to copy objects to a bucket in another Region for redundancy purposes, and has no effect on preventing or recovering from accidental deletion in the source bucket.

## clf-c02/domain3/q478

Answer: D

AWS Lambda functions cannot be invoked directly from a mobile app without using an intermediary API layer such as Amazon API Gateway or AWS AppSync; direct invocation from arbitrary external code is not supported, making this statement false rather than a genuine benefit.
Lambda running code without provisioning or managing servers is a genuine benefit; it eliminates the need to select, patch, or maintain underlying compute infrastructure. Lambda does provide resizable compute capacity, automatically scaling from a few requests per day to thousands per second based on the incoming trigger volume. There is genuinely no charge when Lambda code is not running; billing is based on the number of requests and the duration of execution, making it cost-free during idle periods.

## clf-c02/domain3/q483

Answer: B

Amazon Redshift is a fully managed petabyte-scale cloud data warehouse that uses columnar storage and parallel query execution to deliver fast analytics on large datasets.
AWS Shield is a managed DDoS protection service that safeguards AWS applications against distributed denial-of-service attacks, and has no connection to data storage or analytics. Amazon RDS is a fully managed relational database service supporting transactional workloads, and is designed for operational databases with frequent read/write activity rather than the large-scale analytical query workloads that a data warehouse serves. Amazon Comprehend is a natural language processing service that analyzes written text to extract insights such as sentiment, entities, and key phrases, and is an AI service with no data warehousing capability.

## clf-c02/domain3/q485

Answer: B

AWS CodeCommit is a fully managed source control service that hosts private Git repositories, providing secure storage, versioning, and collaboration features for application code.
AWS CodePipeline automates the steps of a continuous delivery pipeline for releasing application code, including building, testing, and deploying, and is a CI/CD orchestration tool rather than a repository management service for storing and versioning code. AWS X-Ray provides distributed tracing for applications to visualise request paths and diagnose latency and performance issues, and has no source control or repository management capability. Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and is a security tool entirely unrelated to code storage or versioning.

## clf-c02/domain3/q486

Answer: D

Amazon Route 53 supports latency-based routing, which directs user requests to the AWS Region that provides the lowest latency for the end user, routing traffic to the endpoint that will respond fastest based on measured network conditions.
Amazon CloudFront is a content delivery network that caches content at edge locations to reduce latency for end users, but it caches static and dynamic content rather than routing application traffic to the nearest Region based on latency measurements. AWS Global Accelerator improves global application availability and performance by routing traffic over the AWS global network to the nearest healthy endpoint, and while it also reduces latency, the question specifically asks about routing end users to the nearest AWS Region. AWS Direct Connect provides a dedicated private network connection between an on-premises data center and AWS, reducing latency on hybrid workloads, but it does not route end users to the nearest AWS Region for cloud-hosted applications.

## clf-c02/domain3/q490

Answer: A, E

Storing media assets in the Region closest to end users reduces the physical distance data must travel, and using Amazon CloudFront with S3 caches content at edge locations worldwide, both directly reducing retrieval latency for end users.
Adding an EBS volume and increasing server capacity addresses storage and compute performance but does not reduce the network distance between the origin and end users. Replicating assets across multiple Availability Zones improves availability and fault tolerance within a Region but does not reduce latency for geographically distant users. Amazon Elastic Transcoder converts media files into different formats for playback on various devices and has no effect on the latency of content delivery to end users.

## clf-c02/domain3/q494

Answer: A

The EC2 launch type runs containers on EC2 instances that you provision and manage, giving you full visibility and control over the underlying server cluster including instance types, operating system, and cluster configuration.
The Fargate launch type is a serverless compute engine for containers where AWS manages the underlying infrastructure completely, abstracting away the server cluster so customers have no visibility or control over the underlying servers, which is the opposite of what the compliance requirement demands. Lightsail launch type is not a valid ECS launch type; Amazon Lightsail is a simplified compute and hosting service for straightforward workloads and is not an ECS launch option. Lambda launch type is not a valid ECS launch type; AWS Lambda runs serverless functions in response to events and is not a launch mechanism for ECS containerised applications.

## clf-c02/domain3/q498

Answer: B

AWS Elastic Beanstalk automatically handles deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring, letting you focus on writing code rather than managing infrastructure.
Amazon Simple Storage Service is an object storage service for storing and retrieving data, and has no capability to deploy or scale application code. AWS CodeCommit is a managed Git-based source control service for storing and versioning code repositories, and is a version control tool rather than a deployment or scaling service. Amazon Elastic File System is a managed shared network file system for use with AWS compute services, and is a storage service with no application deployment or scaling capability.

## clf-c02/domain3/q500

Answer: A, E

EC2 instances improve fault tolerance through features such as Auto Scaling, Multi-AZ deployment, and Elastic Load Balancing integration, and can be scaled up or down manually in minutes rather than the weeks required to procure and provision physical hardware.
Seamless remote accessibility is available with both traditional servers and EC2 instances and is not a differentiating benefit of EC2 over physical hardware. Preventing unauthorised users from accessing your network is a security responsibility that applies equally to both environments and is not an inherent EC2 advantage over traditional servers. Automatic data backups are not provided by EC2 by default, as customers must configure backup solutions such as AWS Backup or EBS snapshots separately.

## clf-c02/domain3/q502

Answer: A

AWS Control Tower automates the setup of a secure, well-architected multi-account environment based on AWS best practices, providing pre-configured guardrails and a landing zone dashboard for centralized governance.
Amazon Macie is a data security service that uses machine learning to discover and protect sensitive data stored in Amazon S3, and has no role in multi-account environment setup or governance. AWS Systems Manager Patch Manager automates the patching of operating systems and applications on EC2 instances and is not related to account architecture or multi-account management. AWS Security Hub aggregates and prioritizes security findings from multiple AWS services into a centralized dashboard, but does not set up or manage multi-account environments.

## clf-c02/domain3/q503

Answer: C

Amazon CloudWatch Alarms let you define thresholds on metrics such as CPU utilization and trigger notifications or automated actions when the threshold is breached, making it the purpose-built solution for alerting when CPU usage exceeds 60%.
Amazon CloudFront is a content delivery network that caches and distributes content at edge locations worldwide to reduce latency for end users, and has no capability to monitor instance-level performance metrics such as CPU usage. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance and detect configuration changes, and does not monitor real-time performance metrics or support CPU threshold alerting. Amazon Simple Notification Service is a messaging service that delivers notifications to subscribers, and while it can be used alongside CloudWatch to deliver alerts, it cannot itself monitor or evaluate CPU utilization metrics.

## clf-c02/domain3/q504

Answer: A

Amazon EBS provides persistent block storage volumes that attach to EC2 instances, delivering the consistent low-latency I/O performance needed for databases with frequently changing data.
Amazon RDS is a fully managed relational database service that runs on its own infrastructure, and is not a storage option for a database hosted directly on an EC2 instance. Amazon S3 provides object storage accessible via API calls and is designed for storing files, backups, and static assets rather than serving as the underlying block storage for a database engine running on EC2. Amazon DynamoDB is a fully managed serverless NoSQL database service that runs on AWS infrastructure, and is not a storage volume that can be attached to an EC2 instance.

## clf-c02/domain3/q505

Answer: A

Amazon CloudWatch monitors applications and infrastructure by collecting metrics, logs, and events, providing dashboards and alarms that help SREs identify and respond to operational issues.
Amazon CloudSearch is a managed search service for building search functionality into applications, and is a search indexing tool with no application monitoring or observability capability. Amazon EMR is a managed big data platform for processing large datasets using frameworks such as Apache Hadoop and Spark, and is a data processing service with no application monitoring capability. Amazon CloudHSM provides dedicated hardware security modules for managing cryptographic keys, and is a security and key management service with no role in monitoring application performance or health.

## clf-c02/domain3/q510

Answer: A

Amazon RDS is a managed relational database service that supports SQL queries including joins and complex ACID transactions, making it the right choice for applications with structured, relational data schemas.
Amazon Redshift is a managed data warehouse service that supports SQL and joins but is optimized for analytical queries across large datasets rather than the transactional workloads that require ACID compliance. Amazon DocumentDB is a document database compatible with MongoDB that stores flexible JSON-like data and does not support relational joins or complex multi-table transactions. Amazon DynamoDB is a NoSQL key-value and document database designed for high-throughput low-latency access patterns, and does not support relational joins or complex transactional queries.

## clf-c02/domain3/q512

Answer: C

Amazon S3 Glacier is designed for archival storage and does not provide immediate data retrieval. Retrieval times range from minutes to hours depending on the retrieval option selected, which makes it unsuitable for workloads requiring instant access to data.
Amazon S3 Glacier accepts data in any format and has no requirement for data to be compressed before storage. Amazon S3 Glacier is specifically designed for infrequently accessed archival data, not frequently accessed data, making the claim that it supports frequently accessed data factually incorrect. Amazon S3 Glacier is a standalone storage service accessed directly through the AWS console, API, or S3 lifecycle policies, and does not need to be attached to an EC2 instance to store data.

## clf-c02/domain3/q513

Answer: B

AWS Batch automatically provisions the optimal quantity and type of compute resources based on the volume and requirements of batch jobs, removing the need to manage batch computing infrastructure manually and allowing engineers to focus on their workloads rather than the underlying infrastructure.
Amazon EC2 provides virtual servers that could run batch workloads, but requires engineers to manually provision, configure, and manage the instances and batch scheduling software themselves, which is exactly the problem the scenario describes. Lambda@Edge runs AWS Lambda functions at CloudFront edge locations to process content closer to end users, and is designed for lightweight event-driven tasks rather than large-scale batch computing jobs. AWS Fargate is a serverless compute engine for running containers without managing servers, but is designed for containerised application workloads rather than purpose-built batch job scheduling and management at scale.

## clf-c02/domain3/q518

Answer: C

Amazon Elastic File System (EFS) provides a shared NFS file system that automatically scales and delivers high throughput to multiple EC2 instances concurrently, making it ideal for big data workloads that require parallel access across compute nodes.
Amazon Elastic Block Store provides block storage volumes that attach to a single EC2 instance at a time and cannot be simultaneously shared across multiple compute nodes for parallel access. AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage, and is not designed for high-throughput shared access between EC2 instances. Amazon S3 provides object storage accessible via API calls rather than a mounted file system, and does not deliver the low-latency, high-throughput shared file system access that big data workloads running on EC2 require.

## clf-c02/domain3/q521

Answer: B

Amazon EBS volumes are automatically replicated within their Availability Zone to protect against hardware component failures, ensuring that the data remains durable even if an individual physical drive fails within the underlying infrastructure.
Elasticity refers to the ability to dynamically scale compute resources up or down based on demand, which is a capacity management concept unrelated to the automatic replication of EBS volume data within an AZ. Traceability refers to the ability to audit and log changes to resources and actions performed in an AWS environment, which is a governance and compliance concept rather than a storage characteristic related to data replication. Accessibility refers to the ability to reach or connect to resources, which describes network and permission connectivity rather than the durability protection that replication within an AZ provides for stored data.

## clf-c02/domain3/q526

Answer: A, C

Amazon ElastiCache provides a fully managed in-memory data store supporting Redis and Memcached, caching frequently accessed data to dramatically reduce database query latency and improve web application performance.
Reducing delivery costs using edge locations describes Amazon CloudFront, which caches content geographically closer to users rather than providing in-memory database caching. Providing a Chef-compatible cache describes AWS OpsWorks, which uses Chef and Puppet for configuration management and has no role in in-memory data caching. Distributing requests to multiple instances describes Elastic Load Balancing, which routes incoming traffic across targets rather than storing or caching data in memory.

## clf-c02/domain3/q527

Answer: B, E

EC2 Auto Scaling automatically adjusts the number of instances based on demand, ensuring customers pay only for what they use, and serverless computing charges only for actual execution time with no idle capacity costs, both directly leveraging cloud elasticity to reduce costs.
Deploying across multiple Availability Zones improves availability and fault tolerance but does not dynamically adjust resource capacity in response to demand. Deploying resources in another Region improves geographic reach and disaster recovery but is not a mechanism for elastic cost savings. Elastic Load Balancing distributes incoming traffic across existing instances but does not scale the number of instances up or down based on demand.

## clf-c02/domain3/q529

Answer: D

An Availability Zone is a distinct location within a Region consisting of one or more data centers, designed to be isolated from failures in other AZs through independent power, cooling, and networking.
A single data center completely isolated from other data centers in the same Region is inaccurate, as an AZ can contain multiple data centers and is isolated from failures, not from all connectivity. A collection of data centers distributed across multiple countries describes an AWS Region or the global infrastructure as a whole, not an individual AZ. A logically isolated network of the AWS Cloud describes an Amazon VPC, not an Availability Zone.

## clf-c02/domain3/q532

Answer: B

Amazon S3 is designed to provide virtually unlimited storage capacity. There is no fixed maximum on the total amount of data an account can store, and S3 automatically scales to accommodate any volume of objects.
100 petabytes is a fixed storage limit that does not apply to Amazon S3; individual objects have a maximum size of 5 terabytes, but this is a per-object limit rather than a total account storage cap. 5 terabytes is the maximum size of a single S3 object, not the total storage limit for an account; the total amount of data stored across all objects in an account is not capped. 10 exabytes is a fixed storage limit that does not apply to Amazon S3; the service scales automatically to any volume without a declared maximum.

## clf-c02/domain3/q534

Answer: C

Amazon CloudFront is a global content delivery network that delivers data, videos, applications, and APIs to users worldwide with low latency and high transfer speeds through a network of edge locations.
Amazon Route 53 is a DNS and domain routing service that directs users to application endpoints based on routing policies, but it routes traffic rather than caching and delivering content at edge locations. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and has no role in content delivery or global data transfer. Amazon EC2 provides virtual servers for running applications and workloads, but requires manual configuration to serve content globally and does not natively deliver it with low latency to users worldwide through edge locations.

## clf-c02/domain3/q537

Answer: B

An Availability Zone consists of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities within a Region.
AWS Regions are geographic areas that contain multiple Availability Zones, not individual data center clusters. Edge locations are points of presence used for content delivery and caching, not data center groupings with redundant infrastructure. Amazon CloudFront is a content delivery network service that uses edge locations, not a global infrastructure component in its own right.

## clf-c02/domain3/q538

Answer: B

A minimum of two Availability Zones is required for high availability. If one AZ fails, the application continues operating from the other with minimal disruption.
A minimum of one provides no redundancy. A single AZ failure would take the entire application down. A minimum of three or four or more exceeds the baseline requirement. While deploying across more AZs can increase resilience further, two is the recognized minimum for high availability in AWS architecture.

## clf-c02/domain3/q539

Answer: B

AWS Regions spread across the globe are part of the AWS global infrastructure, which includes Regions, Availability Zones, and edge locations designed to deliver services worldwide.
Agility refers to the speed at which customers can provision resources and iterate on new functionality, which is a cloud adoption benefit rather than a characteristic of physical infrastructure placement. Elasticity refers to dynamically scaling resources up or down in response to demand, which is a compute and capacity concept unrelated to the geographic distribution of Regions. Pay-as-you-go pricing is a billing model where customers pay only for what they consume, which is a commercial benefit rather than an infrastructure concept.

## clf-c02/domain3/q540

Answer: C

Amazon EC2 lets you manually launch virtual server instances with your choice of instance type, operating system, and configuration, providing full control over compute resource provisioning.
Amazon EBS provides persistent block storage volumes that attach to EC2 instances as disks, and is a storage service rather than a compute service capable of launching instances. Amazon S3 is an object storage service for storing and retrieving files and data, and has no capability to launch or run compute instances. Amazon ECS is a container orchestration service that manages the deployment and scaling of containerised applications, and while it does run tasks on underlying compute, it does not manually launch instances based on resource requirements in the way EC2 does.

## clf-c02/domain3/q544

Answer: A

Amazon RDS simplifies relational database administration by automating time-consuming tasks like hardware provisioning, database setup, patching, and backups, letting customers focus on application development rather than infrastructure management.
99.9999999999% reliability and durability is a figure associated with Amazon S3's object durability, not a published SLA for Amazon RDS. Automatically scaling databases for loads describes Amazon Aurora Serverless, which scales compute capacity automatically based on demand, not a default behavior of standard RDS instances. Dynamically adjusting CPU and RAM resources describes the behavior of services with automatic vertical scaling, which RDS does not provide natively as customers must manually modify instance types to change compute resources.

## clf-c02/domain3/q545

Answer: A

Amazon EC2 provides virtual servers with full operating system-level access, allowing you to install, configure, and manage any relational database software yourself, giving you complete control over the database configuration.
Amazon Route 53 is a DNS and traffic routing service that manages domain name resolution and directs users to application endpoints, and has no capability to host or run database software. Amazon ElastiCache is a managed in-memory caching service designed to accelerate application performance by storing frequently accessed data in memory, and is not a relational database platform. Amazon DynamoDB is a fully managed NoSQL key-value and document database service, and is not a relational database and does not support customer-managed database software installation or configuration.

## clf-c02/domain3/q546

Answer: A

Launching instances across multiple Availability Zones within a single Region provides high availability by ensuring that if one Availability Zone experiences a failure, the instances in the remaining zones continue serving traffic without interruption.
Launching Reserved Instances in the same Region and Availability Zone secures a capacity reservation and reduces cost through a billing commitment, but concentrating both instances in a single Availability Zone creates a single point of failure with no availability benefit. Launching instances in multiple Regions but in the same Availability Zone type introduces geographic separation at the Regional level but does not protect against failures within a Region since Availability Zones within each Region remain independent failure domains. Launching Spot Instances in different Availability Zones uses spare EC2 capacity at reduced cost, but Spot Instances can be interrupted by AWS at any time, making them unsuitable as a reliability mechanism for increasing availability.

## clf-c02/domain3/q548

Answer: A, D

AWS VPN creates an encrypted connection over the public internet to connect on-premises networks to a VPC, and AWS Direct Connect establishes a dedicated private physical network connection from an on-premises data center to AWS. Both are services that provide hybrid connectivity between on-premises infrastructure and the AWS Cloud.
Amazon Redshift is a fully managed cloud data warehousing service designed for running analytical SQL queries on large datasets, and is a database service with no capability to connect on-premises networks to AWS. Amazon API Gateway is a fully managed service for creating, publishing, and managing REST, HTTP, and WebSocket APIs, and is an API management service rather than a network connectivity solution for linking on-premises data centers to VPCs.

## clf-c02/domain3/q549

Answer: C

Amazon CloudWatch collects and monitors CPU utilization metrics from EC2 instances by default, and can trigger alarms or display dashboards when usage exceeds defined thresholds.
AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and does not collect or monitor instance-level performance metrics such as CPU usage. VPC Flow Logs capture information about IP traffic flowing to and from network interfaces within a VPC, and is a network traffic logging feature with no capability to monitor compute resource metrics such as CPU utilization. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance and detect configuration changes, and does not monitor real-time performance metrics.

## clf-c02/domain3/q552

Answer: D

Amazon S3 can host static websites by serving HTML, CSS, JavaScript, and media files directly via HTTP, offering a low-cost, highly durable, and scalable solution without needing a web server.
Amazon S3 Glacier is an archival storage service designed for long-term retention of infrequently accessed data and does not support static website hosting or direct HTTP serving of content. Amazon DynamoDB is a fully managed NoSQL database service for storing and querying structured data, and is not a storage service capable of hosting website files. Amazon EFS provides a shared network file system for use with EC2 instances and does not support static website hosting or public HTTP access to files.

## clf-c02/domain3/q558

Answer: D

AWS Systems Manager Patch Manager automates the process of patching managed EC2 instances with security updates on a defined schedule, eliminating the need for manual intervention each time a vendor releases new patches.
Connecting to each database instance individually on a monthly basis to download and apply patches manually is the least efficient approach, requiring significant administrative effort that scales poorly as the number of instances grows. Amazon RDS console patching applies to databases managed by the RDS service, and cannot be used to patch database software running on self-managed EC2 instances where the customer is responsible for the operating system and software. AWS Config is a configuration compliance and change tracking service that can assess whether instances meet a required patch level, but does not itself automate or apply patches to instances.

## clf-c02/domain3/q559

Answer: A

The AWS Software Development Kit provides language-specific libraries and APIs in languages including Python, Java, JavaScript, and Go, allowing developers to integrate AWS service calls directly into application code through programmatic interfaces.
The AWS Management Console is a web-based graphical interface for interacting with AWS services through a browser, not a mechanism that developers embed in application code for programmatic service access. AWS CodePipeline is a continuous delivery service that automates build, test, and deploy stages of a release pipeline, and is a CI/CD tool for application deployment rather than a means for application code to interact with AWS services. AWS Config continuously tracks and records resource configuration changes and evaluates them against compliance rules, and is a governance and compliance service rather than a development tool for enabling application code to call AWS services.

## clf-c02/domain3/q563

Answer: C

Amazon CloudWatch is a monitoring service that acts as a metrics repository, collecting performance and operational data from AWS resources and allowing you to set customizable notification thresholds and alarm channels.
AWS CloudTrail records all API calls and account activity across an AWS environment and produces audit logs for governance and compliance purposes, but does not collect resource performance metrics or send operational alarms. AWS X-Ray traces requests as they travel through distributed application components to identify performance bottlenecks and errors, but is an application debugging tool rather than an infrastructure-wide metrics and alerting service. Amazon Kinesis captures and processes real-time data streams from applications and infrastructure at scale, but is a data streaming and ingestion service rather than a monitoring and observability platform.

## clf-c02/domain3/q570

Answer: B

Elastic Load Balancing automatically scales its request handling capacity in response to incoming application traffic, distributing requests across healthy targets without manual intervention.
AWS CodePipeline automates the stages of a software release pipeline including source, build, and deploy phases, and has no capability for handling or scaling web traffic. Amazon EBS provides block storage volumes attached to EC2 instances that must be manually resized, and does not scale in response to web traffic. AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, and is a networking connectivity service unrelated to web traffic scaling.

## clf-c02/domain3/q571

Answer: D

Amazon S3 provides virtually unlimited, highly durable object storage with 99.999999999% durability, designed for storing and retrieving any amount of data from anywhere on the web.
Amazon Redshift is a managed data warehouse service for running analytical queries on large datasets, not an object storage service. Amazon EFS is a managed shared file system for use with compute instances, providing file storage rather than object storage and not designed for unlimited web-accessible data storage. Amazon ECS is a container orchestration service for running and managing Docker containers, entirely unrelated to object storage.

## clf-c02/domain3/q578

Answer: A

Amazon S3 can serve static websites by hosting HTML, CSS, JavaScript, and image files, delivering them directly via HTTP without needing to run a web server.
Amazon Route 53 is a DNS and domain registration service that routes traffic to endpoints, but does not host or serve website content itself. Amazon QuickSight is a business intelligence and data visualisation service for building dashboards and reports, and has no web hosting capability. AWS X-Ray is an application tracing and debugging service that helps analyze performance of distributed applications, and is entirely unrelated to hosting or serving website content.

## clf-c02/domain3/q580

Answer: B, D

Regions and Availability Zones are the two main building blocks of AWS global infrastructure, with Regions being geographic areas and each Region containing multiple isolated Availability Zones.
Resource groups are a management tool used to organize and tag AWS resources within an account, and are not a component of the physical global infrastructure. Security groups are virtual firewalls that control inbound and outbound traffic for AWS resources, and are a networking feature rather than an infrastructure component. Amazon Machine Images are templates used to launch EC2 instances containing the operating system and configuration, and are a compute feature rather than part of the global infrastructure hierarchy.

## clf-c02/domain3/q584

Answer: A, B

Amazon Route 53 provides DNS services that work across both cloud and on-premises environments, and a Virtual Private Gateway enables encrypted VPN connections between a VPC and an on-premises data center, both making them suitable for hybrid architectures.
Classic Load Balancer distributes traffic across EC2 instances within AWS and operates entirely within the cloud, with no hybrid connectivity capability. Auto Scaling automatically adjusts the number of EC2 instances based on demand within AWS, and does not extend to or integrate with on-premises infrastructure. Amazon CloudWatch default metrics monitor AWS resource performance within the cloud, and while it can be extended to on-premises with a custom agent, it is not itself a hybrid architecture service.

## clf-c02/domain3/q585

Answer: B

Elastic Load Balancing distributes incoming application traffic across multiple EC2 instances or targets, improving availability and fault tolerance by ensuring no single instance is overwhelmed.
Translating a domain name into an IP address using DNS describes the function of Amazon Route 53, which is a DNS routing service and not a traffic distribution service. Collecting metrics on connected EC2 instances describes the function of Amazon CloudWatch, which monitors resource performance and operational data rather than distributing traffic. Automatically adjusting the number of EC2 instances to support incoming traffic describes the function of Amazon EC2 Auto Scaling, which adds or removes instances based on demand rather than distributing traffic across existing instances.

## clf-c02/domain3/q586

Answer: C

Amazon DynamoDB is a fully managed NoSQL database that delivers single-digit millisecond performance at any scale, with built-in security, backup, and in-memory caching.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is a relational columnar store rather than a NoSQL database service. Amazon RDS is a fully managed relational database service supporting engines such as MySQL, PostgreSQL, and SQL Server, and uses structured schemas and SQL rather than the flexible schema-less data models that NoSQL databases provide. Amazon S3 is an object storage service for storing and retrieving files and unstructured data, and while it can store large volumes of data it is not a database service and does not support the query patterns or data models of a NoSQL database.

## clf-c02/domain3/q592

Answer: C

AWS managed services like Amazon ElastiCache and Amazon RDS handle patching and updating the underlying operating systems and database engines, freeing customers from these time-consuming maintenance tasks.
Requiring the customer to monitor and replace failing instances describes the opposite of a managed service benefit, as AWS managed services handle failure detection and recovery automatically, removing that burden from customers. Having better performance than customer-managed services is not guaranteed as a universal benefit, since performance depends on instance type, configuration, and workload rather than simply on whether a service is managed. Not requiring the customer to optimize instance type or size selections is incorrect, as customers are still responsible for choosing the appropriate instance type and size to match their workload requirements even when using managed services.

## clf-c02/domain3/q596

Answer: B, E

Amazon S3 is an object store that provides highly durable storage with 99.999999999% durability, storing data as objects in buckets rather than as files in a file system or blocks on a disk.
A global file system describes Amazon EFS, which provides a shared network file system accessible across multiple EC2 instances, not an object storage service. A local file store describes temporary instance storage such as EC2 instance store volumes, which are physically attached to the host and lost when the instance stops. A network file system also describes Amazon EFS, which mounts as a shared file system over a network connection rather than storing data as objects.

## clf-c02/domain3/q609

Answer: A, C

The AWS Command Line Interface allows command-based interaction with AWS services from a terminal, and AWS Software Development Kits provide programmatic access to AWS services from application code written in multiple programming languages. Both are direct, supported methods for interacting with AWS services.
On-premises refers to infrastructure and software hosted in a company's own physical data center rather than in the cloud, and is a deployment model rather than a method of interacting with AWS services. Software-as-a-service is a cloud delivery model in which software applications are provided over the internet by a vendor, and is a service consumption model rather than a way for customers to interact with AWS services directly. Hybrid refers to an architecture that combines on-premises infrastructure with cloud resources, and is a deployment strategy rather than an interaction method for AWS services.

## clf-c02/domain3/q611

Answer: B, E

Amazon S3 stores video content with high durability and scalability, and Amazon CloudFront caches and delivers that content from edge locations worldwide with low latency, making them the purpose-built combination for serving large-scale online video efficiently.
AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage integration, and is not designed for serving or distributing online video content to end users. Amazon Elastic File System is a managed shared network file system for use with AWS compute services, and is not optimized for delivering large volumes of video content at low latency to a distributed audience. Amazon S3 Glacier is an archival storage service designed for data that is rarely accessed and can tolerate retrieval times of minutes to hours, making it entirely unsuitable for serving online video content that requires immediate low-latency delivery.

## clf-c02/domain3/q615

Answer: C

AWS Health Dashboard provides a personalized, account-specific view of AWS service events affecting your workloads through its "Your account health" section, offering proactive alerts and remediation guidance tailored to your environment.
Amazon CloudWatch monitors metrics, logs, and alarms for resources within a customer's own AWS environment but does not provide alerts about AWS service events affecting your workloads. AWS X-Ray is an application tracing service for analyzing distributed application performance, not a service health monitoring tool. AWS Trusted Advisor analyzes your environment against best practice checks across cost, performance, security, and fault tolerance, but does not provide personalized service health alerts.

## clf-c02/domain3/q616

Answer: B, E

AWS CloudFormation can provision RDS clusters through infrastructure-as-code templates, and the AWS Management Console provides a graphical interface for launching RDS clusters directly, making both valid launch methods.
AWS Concierge is a support service available to enterprise plan customers that assists with billing and account inquiries, and has no capability to provision or launch AWS resources such as RDS clusters. Amazon S3 is an object storage service for storing and retrieving files and data, and cannot be used to launch or provision database clusters. Amazon EC2 Auto Scaling automatically adjusts the number of EC2 compute instances in response to demand, and has no capability to launch or manage RDS database clusters.

## clf-c02/domain3/q620

Answer: C, D

Security Groups and Subnets are both native features of Amazon VPC, with Security Groups controlling traffic at the instance level and Subnets defining IP address ranges and network segmentation within a VPC.
Amazon CloudFront distributions are configured through the CloudFront console and are a separate CDN service with no configuration surface within the Amazon VPC Dashboard. Amazon Route 53 is a DNS and traffic routing service managed through its own console, and is not a feature configured within Amazon VPC. Elastic Load Balancing is a separate service that distributes traffic across targets and is configured through the EC2 or dedicated load balancer console, not through the Amazon VPC Dashboard.

## clf-c02/domain3/q625

Answer: A, D

Amazon Route 53 is a global DNS service that operates without being tied to any single AWS Region, and Amazon CloudFront is a global content delivery network whose edge locations span the globe independently of regional deployments. Both are global services rather than regional.
Amazon EC2 is a regional service; instances are launched in specific Availability Zones within specific Regions, and each EC2 deployment is bound to its Region. Amazon S3 is generally considered a regional service because buckets are created in a specific Region and data resides there by default, even though bucket names are globally unique. Amazon DynamoDB is a regional service where tables are created and data is stored in a specific Region, though Global Tables can replicate across Regions as an additional feature.

## clf-c02/domain3/q636

Answer: D

Availability Zones are multiple, isolated locations within an AWS Region, each with independent power, cooling, and networking, connected to each other by low-latency links for high availability.
AWS Direct Connect is a dedicated private network connection service for linking an on-premises data center to AWS, not an infrastructure component within a Region. Amazon VPCs are virtual private networks that customers configure within a Region to isolate their resources, not physical infrastructure locations. Edge locations are points of presence outside of Regions used for content delivery and caching, not isolated locations within a Region connected by low-latency links.

## clf-c02/domain3/q650

Answer: A

Amazon CloudFront serves content from edge locations closest to each end user, dramatically reducing round-trip latency by caching application data at over 400 points of presence worldwide, so users receive responses from a nearby location rather than the origin in a single Region.
AWS Direct Connect provides a dedicated private network connection from an on-premises data center to AWS, reducing latency on hybrid workloads, but it does not serve application content to end users distributed across the world from a global edge network. Amazon Route 53 with latency-based routing directs users to the nearest AWS Region, which reduces latency compared to serving all users from a single Region, but once the connection reaches the Region it does not cache content at edge locations the way CloudFront does. Amazon S3 Transfer Acceleration uses CloudFront's edge locations to speed up data uploads to S3, but it is an upload acceleration feature rather than a content delivery mechanism that serves application data to end users with low latency.

## clf-c02/domain3/q653

Answer: C

Amazon RDS Cross-Region read replicas create asynchronously replicated copies of a database in a separate AWS Region, providing globally redundant data that can be promoted to a standalone primary in the event of a regional failure.
Snapshots are point-in-time backups stored in S3 that can be copied to another Region for disaster recovery purposes, but they require manual restoration and do not provide a continuously synchronised replica that can be quickly promoted, making them less suitable for global redundancy. Automatic patching and updating is a managed maintenance feature that keeps the database engine and operating system up to date, but it does not replicate data across Regions or contribute to global redundancy. Provisioned IOPS is a storage option that delivers predictable high I/O performance for latency-sensitive workloads, and is a performance configuration rather than a replication or redundancy feature.

## clf-c02/domain3/q658

Answer: D

Amazon EC2 Auto Scaling monitors defined metrics and automatically adjusts the number of EC2 instances up or down based on demand conditions, adding elasticity to the application by ensuring it has the right capacity to handle current workloads.
Resource groups organize AWS resources by tags or CloudFormation stacks to make them easier to manage, automate, and monitor collectively, but they do not add compute capacity or enable dynamic scaling of EC2 instances. Lifecycle policies in the context of Amazon S3 automatically transition objects to different storage classes or expire them after a specified period, and are a storage management feature rather than a compute elasticity mechanism. Application Load Balancer distributes incoming traffic across registered EC2 instances to prevent any single instance from being overwhelmed, but it does not adjust the number of running instances; that capacity change is the role of Auto Scaling.

## clf-c02/domain3/q660

Answer: C

AWS Storage Gateway provides on-premises applications with seamless access to AWS cloud storage through standard protocols such as NFS, SMB, and iSCSI, bridging hybrid storage environments without requiring applications to be rewritten.
AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is a network connectivity service rather than a storage integration service that exposes cloud storage through file protocols. AWS Snowball is a physical data transport device used for migrating large volumes of data into or out of AWS, and is a one-time or periodic data transfer tool rather than a service that provides ongoing seamless access to cloud storage for on-premises applications. AWS Snowball Edge is a physical device that adds local compute and storage capability at the edge for use cases where connectivity is limited or intermittent, and is a portable edge computing device rather than a hybrid storage integration service using standard file protocols.

## clf-c02/domain3/q664

Answer: C

Loose coupling prevents cascading failures because components interact through well-defined interfaces such as queues and APIs rather than direct dependencies, so a failure in one component does not bring down others.
Low-latency request handling is a performance characteristic achieved through infrastructure choices such as edge caching and regional deployment, and is not a benefit of loose coupling as an architectural pattern. Allowing applications to have dependent workflows describes tight coupling, which is the opposite of loose coupling and increases the risk that a failure in one component will impact others. Allowing companies to focus on physical data center operations describes an on-premises operational model, which is the opposite of what cloud adoption enables and is entirely unrelated to loose coupling as a design principle.

## clf-c02/domain3/q665

Answer: B

AWS Direct Connect establishes a dedicated, private network connection between on-premises data centers and AWS, bypassing the public internet to provide consistent performance, lower latency, and enhanced security for hybrid cloud connectivity.
Amazon VPC NAT Gateway allows instances in private subnets to initiate outbound connections to the internet while preventing unsolicited inbound connections, and is an outbound internet access mechanism for private resources rather than a service that facilitates private hybrid connectivity between on-premises and AWS. Amazon S3 Transfer Acceleration speeds up data transfers to and from S3 buckets by routing traffic through AWS CloudFront edge locations, and is a data transfer performance optimization rather than a private hybrid connectivity solution. AWS WAF is a web application firewall that filters HTTP and HTTPS traffic based on defined rules, and is a traffic filtering security service rather than a network connectivity solution for hybrid cloud architecture.

## clf-c02/domain3/q674

Answer: D

Amazon Aurora is a MySQL and PostgreSQL-compatible database that automatically grows storage in increments of 10 GB up to 128 TB, without requiring manual intervention or downtime for storage management.
Amazon EC2 is a virtual server service that provides compute capacity and does not include a built-in database engine or automatic storage scaling. Amazon RDS for MySQL is a managed MySQL database but requires manual storage scaling or the enabling of storage autoscaling as a separate configuration, and does not grow automatically by default in the same way Aurora does. Amazon Lightsail is a simplified cloud platform for deploying small applications and websites and does not offer the automatic storage scaling capabilities described.

## clf-c02/domain3/q675

Answer: C

Amazon VPC peering creates a private networking connection between two VPCs, allowing resources in each VPC to communicate with each other using private IP addresses as if they were on the same network.
Amazon VPC endpoints enable private connectivity between a VPC and supported AWS services without requiring traffic to traverse the public internet, but do not connect two VPCs together. EC2 ClassicLink was a legacy feature that allowed EC2-Classic instances to communicate with VPC resources, not a mechanism for connecting two VPCs to each other. AWS Direct Connect provides a dedicated private circuit between an on-premises data center and AWS, not a connection between two VPCs.

## clf-c02/domain3/q678

Answer: D

AWS Snowmobile is an exabyte-scale data transfer service using a 45-foot shipping container that can move up to 100 PB per trip, designed for the largest possible data migrations to AWS.
AWS Batch is a managed service for running batch computing workloads at scale across EC2 instances, and is a job scheduling and compute service with no capability to physically transport or migrate datasets into AWS. AWS Snowball is a physical data transport device suited for transferring up to 80 TB per device, which at 500 TB would require multiple devices but at exabyte scale is not designed for migrations of that magnitude, where Snowmobile is the appropriate choice. AWS Migration Hub provides a centralized location for tracking the progress of application migrations to AWS using various migration tools, and is a migration monitoring service rather than a physical data transport solution for exabyte-scale datasets.

## clf-c02/domain3/q680

Answer: C, E

Classic Load Balancers are the legacy ELB option supporting HTTP, HTTPS, and TCP traffic, and Application Load Balancers are the modern Layer 7 option for HTTP and HTTPS routing with advanced request-based routing rules, both being official ELB load balancer types.
Public load balancers with AWS Application Auto Scaling capabilities conflates two separate services and does not describe a load balancer type available within ELB. F5 Big-IP and Citrix NetScaler are third-party load balancing products that run on-premises or on EC2, not native ELB load balancer types. Cross-zone load balancers with public and private IPs describes a configuration feature of ELB rather than a distinct load balancer type.

## clf-c02/domain3/q682

Answer: B

Amazon CloudFront caches frequently accessed content at edge locations worldwide, serving responses from the location nearest to the requesting user, which provides the fastest response times for globally distributed users compared to fetching from a single origin Region each time.
AWS CloudTrail records API calls and management events for auditing and compliance across Availability Zones but is not involved in serving application content or reducing response latency for users. AWS CloudFormation provisions and manages infrastructure through code templates and can be deployed across multiple Regions for consistency, but it is an infrastructure provisioning service rather than a content acceleration solution that reduces response times for end users. A virtual private gateway over AWS Direct Connect provides a dedicated private network link between an on-premises environment and an AWS Region, reducing latency on that specific path but not serving application content to globally distributed users at the lowest possible latency.

## clf-c02/domain3/q684

Answer: D

Amazon EC2 provides virtual servers with full OS-level access, allowing you to install and manage any database software yourself with complete control over configuration, tuning, and maintenance.
Amazon Route 53 is a DNS and traffic routing service with no compute capability for hosting or running database software. AWS X-Ray is an application tracing and debugging service for analyzing distributed application performance, unrelated to database hosting. AWS Snowmobile is a physical data transfer service for migrating extremely large datasets to AWS and cannot be used to run or host any software.

## clf-c02/domain3/q699

Answer: D

Amazon CloudFront caches static website content at edge locations worldwide, delivering it to users from the nearest location to reduce latency and increase transfer speeds.
AWS Lambda is a serverless compute service for running event-driven code and has no role in caching or delivering static website content. Amazon DynamoDB Accelerator is an in-memory cache specifically for DynamoDB database queries and is unrelated to static website content delivery. Amazon Route 53 is a DNS and traffic routing service that directs users to the correct endpoint but does not cache or deliver content itself.

## clf-c02/domain3/q700

Answer: A, D

AWS Elastic Beanstalk automates application deployment and scaling by handling the underlying infrastructure provisioning, load balancing, and monitoring automatically. AWS CloudFormation automates infrastructure provisioning through reusable templates, allowing teams to define and deploy AWS resources consistently and repeatedly.
AWS CodeCommit is a managed source control service for hosting private Git repositories and has no role in deploying or managing applications. AWS CodePipeline is a continuous delivery service that orchestrates the stages of a release pipeline, but it coordinates the deployment process rather than managing or automating the deployment environment itself. AWS Config continuously monitors and records AWS resource configurations for compliance purposes and does not manage or automate application deployments.

## clf-c02/domain3/q704

Answer: B

Amazon CloudWatch monitors CPU utilization and other performance metrics from EC2 instances, providing dashboards, alarms, and automated actions based on resource usage thresholds.
AWS CloudTrail records API calls and account activity for auditing and security purposes, and does not collect or display resource performance metrics. AWS Cost and Usage Report provides detailed billing and cost data for AWS services, and has no capability for monitoring compute performance or resource utilization. Amazon SNS is a messaging service that sends notifications and alerts to subscribers, and while it can be triggered by CloudWatch alarms, it does not itself monitor or collect performance metrics.

## clf-c02/domain3/q708

Answer: A, B

AWS Lambda provides serverless compute by running code in response to events without requiring you to provision or manage servers, and Amazon ECS runs containerised applications on managed compute infrastructure. Both are purpose-built AWS compute services.
AWS CodeDeploy automates the deployment of application code to compute targets such as EC2 instances and Lambda functions, and is a deployment automation tool rather than a compute service that provides resources. Amazon S3 Glacier is an archival storage service designed for rarely accessed data with retrieval times ranging from minutes to hours, and is a storage service with no compute capability. AWS Organizations is a account management service for centrally governing and consolidating multiple AWS accounts, and has no compute capability of any kind.

## clf-c02/domain3/q709

Answer: B

AWS CloudFormation enables infrastructure as code by letting you define AWS resources in JSON or YAML templates, automating the provisioning and management of an entire infrastructure stack in a repeatable and consistent way.
Amazon GameLift is a managed service for deploying, operating, and scaling cloud-based game servers, entirely unrelated to infrastructure provisioning. AWS Data Pipeline (deprecated) is a service for orchestrating and automating the movement and transformation of data between AWS services, not for provisioning infrastructure resources. AWS Glue is a managed extract, transform, and load service for preparing and moving data for analytics workloads, unrelated to infrastructure as code.

## clf-c02/domain3/q711

Answer: B

AWS Direct Connect establishes a dedicated private network connection from your internal network to AWS, providing more consistent network performance than internet-based connections.
AWS CloudHSM is a hardware security module service that provides dedicated cryptographic key storage and processing, and has no network connectivity capability. AWS VPN creates an encrypted tunnel over the public internet between on-premises networks and AWS, but does not provide a dedicated private connection with guaranteed bandwidth and consistent performance. Amazon Connect is a cloud-based contact center service that enables customer service operations, and is entirely unrelated to network connectivity between on-premises infrastructure and AWS.

## clf-c02/domain3/q712

Answer: A, B

Amazon CloudFront uses edge locations to cache and deliver content to users from the nearest point of presence, and AWS Shield provides DDoS protection at the edge by inspecting and mitigating attack traffic before it reaches the origin infrastructure.
Amazon EC2 instances are deployed in Availability Zones within AWS Regions, not at edge locations; EC2 is a regional compute service whose instances run in data centers rather than in the edge Points of Presence used by CloudFront and Shield. Amazon RDS is a fully managed relational database service that runs in specific AWS Regions and Availability Zones, not at edge locations, and is a regional service without an edge presence. Amazon ElastiCache provides in-memory caching within AWS Regions to reduce database load, and while it improves latency for applications within a Region, it does not operate at edge locations and is not a globally distributed edge service.

## clf-c02/domain3/q713

Answer: B

AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, making it the purpose-built service for establishing network connectivity in a hybrid architecture.
Amazon VPC provisions an isolated virtual network within AWS for deploying and connecting cloud resources, and while it is a foundational networking component on the AWS side, it does not itself bridge on-premises infrastructure to the AWS Cloud. AWS Directory Service provides managed Microsoft Active Directory in the cloud for identity and access management, and is an authentication and directory tool with no network connectivity capability between on-premises and cloud environments. Amazon API Gateway is a fully managed service for creating, publishing, and managing APIs at scale, and is an application integration service with no capability to establish dedicated network connectivity in a hybrid architecture.

## clf-c02/domain3/q720

Answer: C

Amazon CloudFront is a global CDN that securely delivers data, video, and applications from edge locations closest to users worldwide, minimizing latency and maximizing transfer speeds.
AWS CloudFormation is an infrastructure-as-code service that provisions and manages AWS resources through templates, and has no content delivery or edge caching capability. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, which improves hybrid connectivity but does not deliver content to global end users. Amazon Pinpoint is a customer engagement service used for targeted marketing communications such as email, SMS, and push notifications, and is entirely unrelated to content delivery or network acceleration.

## clf-c02/domain3/q729

Answer: B

AWS Elastic Beanstalk automatically handles capacity provisioning, load balancing, Auto Scaling, and application health monitoring, allowing developers to deploy applications without needing to manage the underlying infrastructure.
AWS Config records and evaluates configuration changes to AWS resources for compliance and auditing purposes and has no role in application deployment or infrastructure provisioning. Amazon Route 53 is a DNS and traffic routing service and does not handle application deployment, load balancing, or health monitoring. Amazon CloudFront is a content delivery network for caching and distributing content globally and is not an application deployment or infrastructure management service.

## clf-c02/domain3/q742

Answer: B

AWS Direct Connect provides a dedicated private physical network connection between on-premises servers and AWS, delivering consistent performance and predictable latency that is not subject to internet congestion.
AWS VPN creates an encrypted tunnel between on-premises infrastructure and AWS but routes traffic over the public internet, meaning performance can vary and it does not provide the dedicated physical link the question requires. Amazon API Gateway is a managed service for creating, publishing, and securing APIs that connect applications to backend services, and has no role in establishing network connectivity between on-premises infrastructure and AWS. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is unrelated to network connectivity or on-premises integration.

## clf-c02/domain3/q743

Answer: A

AWS CloudFormation is designed to model and provision AWS resources using templates, enabling you to define your entire infrastructure stack as code and deploy it in an automated, repeatable way.
Updating application code is handled by developer tools such as AWS CodeDeploy, which manages application deployments to instances and serverless functions. CloudFormation provisions and manages infrastructure resources, not application-level code changes. Setting up data lakes is the function of services such as AWS Lake Formation, which simplifies building, securing, and managing data lakes on AWS. CloudFormation can provision the underlying resources but is not itself a data lake service. Creating reports for billing is the function of AWS Cost Explorer and AWS Billing, which provide visibility into spending and usage across an account. CloudFormation has no reporting or billing capability.

## clf-c02/domain3/q744

Answer: A

Amazon Redshift is a fully managed cloud data warehouse service designed for storing and querying large volumes of structured data, making it an AWS database service.
Amazon Elastic Block Store provides persistent block storage volumes that attach to EC2 instances for use as raw storage, and is not a database service. Amazon S3 Glacier is an archival object storage service designed for long-term retention of infrequently accessed data, not a database for querying or managing structured records. AWS Snowball is a physical edge computing and data transfer device used to move large amounts of data into or out of AWS, and has no role in storing or querying data as a database service.

## clf-c02/domain3/q749

Answer: D

Amazon S3 Glacier provides the lowest-cost storage for long-term data archival, making it ideal for regulatory data that must be retained for years but is rarely accessed.
Amazon S3 Standard provides durable, highly available object storage with immediate millisecond retrieval, and while it meets long-term retention requirements it is significantly more expensive per gigabyte than S3 Glacier for data that is rarely accessed over a seven-year period. AWS Snowball is a physical data transport device used for migrating large volumes of data into or out of AWS, and is a one-time transfer tool rather than a long-term storage service for meeting regulatory retention requirements. Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is designed for active analytical workloads rather than low-cost long-term retention of infrequently accessed regulatory data.

## clf-c02/domain3/q751

Answer: D

AWS Storage Gateway is a hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. It connects your existing on-premises applications and workflows to AWS storage services like Amazon S3, Amazon EBS, and Amazon FSx through standard storage protocols such as NFS, SMB, and iSCSI.
The 99.999999999% (11 nines) durability figure is a specific design characteristic of Amazon S3's object storage, not a guarantee applied to local on-premises hardware. Transporting petabytes of data physically to and from AWS is the primary function of the AWS Snow Family (such as AWS Snowball), whereas Storage Gateway is for ongoing network-based integration. Connecting to multiple Amazon EC2 instances is a feature of shared storage services like Amazon EFS or Amazon FSx, rather than a hybrid connectivity solution for on-premises data centers.

## clf-c02/domain3/q754

Answer: A

AWS Direct Connect provides a consistent dedicated private network connection between on-premises systems and AWS, delivering predictable performance and lower latency than internet-based connections.
AWS VPN creates an encrypted tunnel between on-premises infrastructure and AWS but routes traffic over the public internet, meaning performance can vary and it does not provide the dedicated physical connection the question requires. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is entirely unrelated to network connectivity between on-premises systems and AWS. AWS Data Pipeline (deprecated) is a workflow orchestration service for automating the movement and transformation of data between AWS services and on-premises sources, and is a data processing tool with no network connectivity capability.

## clf-c02/domain3/q759

Answer: B, E

There are hundreds of edge locations worldwide compared to dozens of Regions, and each Region contains multiple Availability Zones, making both counts greater than the number of Regions.
There are more AWS Regions than Availability Zones is false. Every Region contains at least two or three AZs, so AZs always outnumber Regions. An edge location is an Availability Zone is false. Edge locations are separate points of presence used for content delivery and are not part of the AZ infrastructure. There are more AWS Regions than edge locations is false. Edge locations number in the hundreds, far exceeding the number of Regions.

## clf-c02/domain3/q767

Answer: D

Edge locations place cached content closer to users globally through Amazon CloudFront, providing the lowest possible latency regardless of where the origin server is located.
Using a single central Region still requires users in distant locations to route traffic across long network distances, and no single Region can be geographically central to all users worldwide. Adding a second Availability Zone improves availability and fault tolerance within a Region but does not reduce the physical distance between the application and global users. Enabling caching within a single Region keeps cached content in one geographic location, which only benefits users close to that Region rather than reducing latency for users globally.

## clf-c02/domain3/q769

Answer: A

Amazon RDS Multi-AZ deployment maintains a synchronous standby replica in a different Availability Zone and performs automatic failover to the standby with no manual intervention if the primary instance becomes unavailable, providing high availability for database workloads.
Amazon Reserved Instances are a billing model that offers significant discounts in exchange for a one-year or three-year commitment, and are a cost optimization tool rather than a high-availability feature for database instances. Provisioned IOPS storage delivers consistent, low-latency I/O performance for demanding workloads by allocating dedicated I/O capacity, and is a performance optimization option rather than a mechanism for achieving high availability across Availability Zones. Enhanced Monitoring provides granular real-time metrics on the operating system of an RDS instance at intervals as short as one second, enabling detailed performance visibility, but is a monitoring feature rather than a high-availability configuration.

## clf-c02/domain3/q774

Answer: B

AWS Database Migration Service simplifies database migration by managing the data replication from the source to the target with minimal downtime, supporting homogeneous migrations such as Oracle to Oracle and heterogeneous migrations between different database engines.
AWS Storage Gateway connects on-premises environments to AWS cloud storage for hybrid storage use cases, and while it handles data movement, it is a storage integration service for files and block data rather than a service designed to migrate relational databases. Amazon EC2 can host a custom database migration process, but it requires customers to set up, configure, and manage all migration tooling manually, making it far less straightforward than using the purpose-built DMS service. Amazon AppStream 2.0 is a fully managed application streaming service that streams desktop applications from AWS to a user's browser, and is a virtual desktop and application delivery service with no relationship to database migration.

## clf-c02/domain3/q776

Answer: D

Amazon Virtual Private Cloud (Amazon VPC) enables companies to create isolated virtual networks within AWS, with full control over IP addressing, subnets, routing, and network gateways.
AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance and detect configuration changes, and is a governance and auditing tool with no capability to provision or define virtual networks. Amazon Route 53 is a DNS and traffic routing service that resolves domain names and directs users to application endpoints, and is a domain management service rather than a service for creating virtual networks within AWS. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is a hybrid connectivity service for linking external networks to AWS rather than a service for creating virtual networks within AWS itself.

## clf-c02/domain3/q778

Answer: B

Amazon CloudFront uses AWS edge locations, distributed across hundreds of cities worldwide, to cache and deliver content from the location nearest to each user for low-latency delivery.
AWS Regions are geographic areas containing multiple AZs, used for deploying and running workloads, not for edge caching and content delivery. AWS Availability Zones are isolated data center clusters within a Region, used for high availability and redundancy, not content delivery. Amazon VPC is a private virtual network within a Region, used for isolating and controlling network traffic, not for delivering content globally.

## clf-c02/domain3/q781

Answer: A

Amazon SNS delivers notifications triggered by CloudWatch alarms by sending messages to subscribed endpoints such as email addresses, SMS, Lambda functions, SQS queues, and HTTP endpoints, making it the integration point for alarm-based alerting.
AWS CloudTrail records API calls and management events in an AWS account for auditing and compliance, and does not send alerts based on CloudWatch alarms; it is a logging service rather than a notification delivery mechanism. AWS Trusted Advisor inspects your AWS environment against best practice checks across security, cost, performance, and fault tolerance, and while it generates recommendations, it does not integrate with CloudWatch alarms to send triggered alerts. Amazon Route 53 is a scalable DNS service supporting domain registration, routing, and health checks, and while it has its own health check alerting, it does not serve as the notification delivery service for general CloudWatch alarms.

## clf-c02/domain3/q784

Answer: A, C

AWS Auto Scaling automatically replaces unhealthy instances and adjusts capacity, and distributing resources across multiple Availability Zones provides redundancy, both improving availability and reducing the impact of failures.
VPC subnet ACLs are stateless network access control rules that filter traffic at the subnet level, and do not perform health checks or contribute to application availability. CloudWatch alarms send notifications when a metric crosses a threshold but do not automatically remediate failures or restore availability on their own. Points of presence are CloudFront edge locations used for content delivery and caching, not for hosting application tiers or providing redundancy for a three-tier web application.

## clf-c02/domain3/q794

Answer: B, D

AWS Global Accelerator routes traffic over the AWS global network to the optimal endpoint based on health, geography, and routing policies, and Amazon CloudFront caches content at edge locations worldwide. Together they provide low latency and high transfer speeds for a global user base.
Application Load Balancer distributes traffic across targets within an AWS Region, improving availability and performance for applications within a Region, but does not extend reach to global users across multiple geographic locations. AWS Lambda is a serverless compute service that runs code in response to events without managing servers, and is a compute service rather than a global content delivery or traffic acceleration solution. AWS Direct Connect provides a dedicated private network connection from an on-premises data center to AWS for hybrid workloads, and is not a solution for reducing latency for internet-based end users distributed worldwide.

## clf-c02/domain3/q795

Answer: A

AWS Lambda is a serverless compute service that runs code in response to events without requiring you to provision, manage, or scale any underlying server infrastructure.
Amazon EC2 instances are virtual servers that require you to select instance types, manage capacity, and maintain the underlying operating system. Amazon Lightsail provides virtual private servers with pre-configured compute, storage, and networking, making it a server-based service aimed at simpler workloads. Amazon ElastiCache is a managed in-memory caching service that runs on node-based infrastructure within a VPC, not a serverless service.

## clf-c02/domain3/q804

Answer: A, D

AWS VPN creates an encrypted tunnel over the public internet between an on-premises network and an AWS VPC, and AWS Direct Connect establishes a dedicated private physical network connection from an on-premises data center to AWS. Both provide connectivity between on-premises resources and the AWS Cloud.
Amazon Connect is a cloud-based contact center service that enables customer service operations through voice and chat channels, and is a business communications tool rather than a network connectivity solution for linking on-premises infrastructure to AWS. Amazon Cognito provides user identity and authentication services for web and mobile applications, managing user sign-up, sign-in, and access control, and is an identity service rather than a network connectivity solution. AWS Managed Services provides ongoing management of AWS infrastructure to reduce operational overhead, and is an operational management offering rather than a network connectivity service between on-premises environments and the AWS Cloud.

## clf-c02/domain3/q807

Answer: A

Amazon RDS is a managed MySQL-compatible database service that handles routine tasks like provisioning, patching, backups, and recovery, eliminating the need for dedicated Database Administrators to manage these operational responsibilities.
Amazon DynamoDB is a fully managed NoSQL key-value and document database, and while it eliminates DBA overhead it does not support MySQL or relational data models, making it unsuitable as a direct migration target for a MySQL database. Amazon DocumentDB is a managed document database service compatible with MongoDB, and is designed for JSON document workloads rather than relational MySQL database migrations. Amazon ElastiCache is a managed in-memory caching service designed to accelerate application performance by storing frequently accessed data in memory, and is not a relational database service capable of running or replacing a MySQL database.

## clf-c02/domain3/q813

Answer: C

AWS Lambda is designed for event-driven workloads, automatically running code in response to events from services like S3, DynamoDB, API Gateway, and CloudWatch without provisioning servers.
Amazon EC2 provides virtual servers that customers provision and manage continuously, and is designed for workloads that require persistent running instances rather than code that executes only in response to events. AWS Elastic Beanstalk deploys and manages applications on continuously running infrastructure, handling scaling and provisioning automatically, but is not designed for event-driven execution of individual functions. AWS Fargate runs containerised workloads without managing the underlying servers, but containers run as persistent tasks rather than executing in response to individual events the way Lambda functions do.

## clf-c02/domain3/q814

Answer: C

S3 cross-region replication supports buckets owned by a single AWS account or by different accounts, enabling cross-account replication scenarios for data sharing and compliance.
Cross-region replication requires versioning to be enabled on both the source and destination buckets, not disabled, making this option factually incorrect. Cross-region replication is specifically designed to replicate objects between buckets in different AWS Regions, so source and destination buckets must be in different Regions by definition. AWS Regions do not need to be disabled for either account involved in a cross-region replication configuration, as replication works across any enabled Regions without any such restriction.

## clf-c02/domain3/q818

Answer: B

Amazon Route 53 is a DNS service that enables users to register domain names, manage DNS records, and route internet traffic to AWS resources or external endpoints.
Encrypting data in transit is handled by AWS services such as AWS Certificate Manager and AWS KMS, not by Route 53, which manages DNS routing rather than cryptographic operations. Generating and managing SSL certificates is the function of AWS Certificate Manager, which provisions and renews certificates for use with AWS resources, not a capability of Route 53. Establishing a dedicated network connection to AWS is the function of AWS Direct Connect, which provides a private physical link between on-premises infrastructure and AWS, not a DNS or domain registration service.

## clf-c02/domain3/q823

Answer: A

Amazon CloudFront caches content at edge locations worldwide, delivering it from the location nearest to each user, which significantly reduces latency for a website with a global customer base.
AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, which improves connectivity for enterprise networks but does not reduce latency for public internet users accessing a website. Amazon EC2 Auto Scaling adjusts the number of instances based on demand to maintain performance and availability, but does not reduce the geographic distance between the server and global users. AWS Transit Gateway connects VPCs and on-premises networks through a central hub, and is a network routing service with no content delivery or latency optimization capability for end users.

## clf-c02/domain3/q826

Answer: C

AWS Global Accelerator continuously monitors the health of application endpoints and automatically routes incoming user traffic to the nearest healthy endpoint over the AWS global network, improving availability and enabling cross-Region failover without DNS changes.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and does not monitor endpoint health or route application traffic. Amazon CloudWatch collects and monitors metrics, logs, and events from AWS services and applications, and while it can detect and alert on endpoint health issues, it does not itself route application traffic to healthy endpoints. Amazon CloudFront is a content delivery network that caches content at edge locations and improves performance for static and dynamic content delivery, but it does not perform application-level endpoint health monitoring and traffic routing across Regions in the way Global Accelerator does.

## clf-c02/domain3/q830

Answer: A, D

AWS Snowball physically transports large volumes of data to AWS using secure hardware appliances, and AWS DMS migrates databases from on-premises or other sources to AWS with minimal downtime. Both are specifically designed for moving data from on-premises environments to AWS.
AWS Lambda is a serverless compute service for running event-driven code and has no role in data migration or physical data transport. AWS ElastiCache is an in-memory caching service for improving application performance and is not a data migration tool. Amazon API Gateway is a service for creating and managing APIs to expose backend services over HTTP and has no capability for migrating or transporting data from on-premises to AWS.

## clf-c02/domain3/q834

Answer: B

Amazon EC2 Auto Scaling dynamically adjusts the number of EC2 instances based on demand, automatically scaling out to handle traffic spikes and scaling in when demand drops, making it the purpose-built solution for meeting variable workload requirements.
AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and has no capability to adjust or provision resources in response to changes in demand. Amazon Forecast is a machine learning service that generates time-series predictions such as demand or inventory forecasts, and while it can predict future traffic patterns it cannot itself take action to adjust infrastructure resources. AWS Config continuously tracks and records the configuration of AWS resources for compliance and change management purposes, and has no capability to dynamically scale resources in response to traffic or demand changes.

## clf-c02/domain3/q835

Answer: C

AWS VPN creates an encrypted tunnel over the public internet to securely connect on-premises networks or remote users to AWS resources, providing secure connectivity without requiring a dedicated physical line.
Amazon VPC peering connects two VPCs privately within the AWS network, allowing them to communicate with each other, but does not provide connectivity from outside AWS over the public internet. AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS that bypasses the public internet entirely, making it a private rather than internet-based connectivity option. Amazon Pinpoint is a customer engagement service used for sending targeted marketing messages and notifications, and is entirely unrelated to network connectivity.

## clf-c02/domain3/q837

Answer: B

Amazon CloudFront caches frequently accessed static content at edge locations worldwide, serving it from the location nearest to each user to reduce latency for a global audience.
Amazon ElastiCache is an in-memory caching service that reduces database query latency within an application, but it does not cache or distribute content to geographically dispersed users at edge locations. Amazon Elastic File System provides a shared file system for EC2 instances within AWS and does not cache or distribute content to geographically dispersed users. Amazon Elastic Block Store provides block storage volumes that attach to individual EC2 instances and has no capability to cache or deliver content to users in different geographic locations.

## clf-c02/domain3/q838

Answer: A

Amazon CloudWatch monitors EC2 CPU utilization metrics and can display dashboards showing whether an instance has sufficient CPU capacity for its workload, triggering alarms when defined thresholds are exceeded.
AWS Config continuously tracks and records the configuration of AWS resources to assess compliance and detect configuration changes, and does not monitor real-time performance metrics such as CPU utilization. AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and has no capability to monitor instance-level performance metrics. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security tool rather than a performance monitoring service.

## clf-c02/domain3/q842

Answer: B

Amazon EFS provides a fully managed shared NFS file system that multiple EC2 instances can mount and access simultaneously, supporting concurrent read and write operations across instances.
Amazon EBS volumes can only be attached to a single EC2 instance at a time in most configurations, making them unsuitable for shared simultaneous access across multiple instances. Amazon S3 is an object storage service accessible via API calls, not a mountable file system suitable for applications requiring shared concurrent file system access. AWS Artifact is a self-service portal for accessing AWS compliance reports and agreements, entirely unrelated to storage.

## clf-c02/domain3/q850

Answer: A, B

Amazon EC2 instances can be scaled using EC2 Auto Scaling, which automatically adjusts the number of instances based on demand, and Amazon DynamoDB tables can be scaled using Application Auto Scaling to automatically adjust read and write capacity in response to traffic patterns. Both integrate directly with AWS Auto Scaling.
Amazon S3 is an object storage service that scales automatically to accommodate any amount of data without any configuration required, and does not use or require AWS Auto Scaling to manage its capacity. Amazon Route 53 is a DNS and traffic routing service that manages domain name resolution and traffic policies, and has no compute or database capacity that would be managed through AWS Auto Scaling. Amazon Redshift is a managed data warehouse service that has its own concurrency scaling and resizing capabilities built in, and does not integrate with AWS Auto Scaling in the way EC2 and DynamoDB do.

## clf-c02/domain3/q851

Answer: B, D

AWS Global Accelerator improves application availability by routing traffic to healthy endpoints across AWS Regions, and decreases latency by directing users to the optimal endpoint over the AWS global network rather than the public internet.
Reduced cost to run services on AWS is not a benefit of AWS Global Accelerator, which is a network performance and availability service that does not reduce the underlying cost of running compute, storage, or database services on AWS. Higher durability of data stored on AWS is a characteristic of storage services such as Amazon S3, which is designed for 99.999999999 percent durability, and is entirely unrelated to the network traffic routing capabilities of AWS Global Accelerator. Higher security of data stored on AWS is a function of encryption, access control, and compliance services rather than a network routing service, and AWS Global Accelerator does not provide data storage or data security capabilities.

## clf-c02/domain3/q860

Answer: A

Amazon Polly is a text-to-speech service that uses advanced deep learning to convert text into natural-sounding speech in multiple languages and voices.
Amazon Transcribe is a speech-to-text service that converts audio recordings into written text, which is the reverse function of converting text into speech. Amazon Rekognition is a computer vision service that analyzes images and videos to detect objects, faces, and scenes, and has no capability to generate or process speech. Amazon Lex is a service for building conversational interfaces and chatbots using voice and text, but it processes and understands speech as input rather than converting written text into spoken audio output.

## clf-c02/domain3/q864

Answer: C

Edge locations are points of presence in the AWS global infrastructure used by CloudFront and other services to cache copies of content close to end users for faster delivery worldwide.
AWS Regions are geographic areas containing multiple Availability Zones where customers deploy their workloads, and are not designed for content caching or low-latency delivery to end users. Availability Zones are isolated data center clusters within a Region used for redundancy and high availability, not for caching content at the edge. Data centers are the physical facilities that house AWS infrastructure and are not a distinct infrastructure tier that customers interact with directly for content delivery purposes.

## clf-c02/domain3/q866

Answer: B

Amazon DynamoDB is a fully managed non-relational NoSQL database that requires no hardware provisioning, software installation, or database management, and scales automatically to handle any workload.
Amazon RDS is a fully managed relational database service supporting engines such as MySQL, PostgreSQL, and SQL Server, and does not support non-relational data models. Amazon Aurora is a fully managed relational database compatible with MySQL and PostgreSQL, and is also a relational rather than a non-relational database service. Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is a relational service with no non-relational capability.

## clf-c02/domain3/q872

Answer: B, D

AWS Direct Connect provides a dedicated private physical connection between an on-premises network and a VPC, and AWS VPN creates an encrypted tunnel over the public internet between an on-premises network and a VPC. Both are purpose-built network connectivity solutions.
Amazon Route 53 is a DNS and traffic routing service that translates domain names to IP addresses and manages traffic flow, and does not establish network connectivity between on-premises infrastructure and a VPC. AWS Data Pipeline (deprecated) is a workflow orchestration service for automating the movement and transformation of data between AWS services and on-premises sources, and is a data processing tool with no network connectivity capability. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is entirely unrelated to network connectivity.

## clf-c02/domain3/q876

Answer: B

Provisioning resources in the South America (São Paulo) Region places infrastructure geographically close to Brazilian users, directly reducing the network distance and latency compared to routing all traffic to Sydney.
AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, but does not reduce latency for end users accessing a cloud-hosted application over the internet. AWS Transit Gateway connects VPCs and on-premises networks through a central hub, and is not designed to reduce geographic latency for end users accessing applications from distant locations. Launching additional EC2 instances in Sydney increases capacity in Australia but does not reduce the physical distance between the application and Brazilian users, so latency would remain unchanged.

## clf-c02/domain3/q879

Answer: D

AWS Storage Gateway is a hybrid storage service that gives on-premises applications seamless access to AWS cloud storage through standard file, volume, and tape storage protocols.
AWS Backup is a centralized backup service for automating and managing backups of AWS resources, and does not provide on-premises applications with access to cloud storage. Amazon Connect is a cloud-based contact center service for managing customer communications, and is entirely unrelated to storage or hybrid connectivity. AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, but is a networking service rather than a storage integration service.

## clf-c02/domain3/q881

Answer: D

AWS Transit Gateway acts as a central hub that connects multiple VPCs across different Regions and on-premises networks, providing the most efficient way to manage complex network connectivity at scale.
AWS Direct Connect establishes a dedicated private link between on-premises infrastructure and AWS, but does not itself manage connectivity between multiple VPCs across different Regions. AWS VPN creates an encrypted tunnel between on-premises networks and a single VPC, and does not efficiently scale to connect multiple VPCs across multiple Regions from a single connection. AWS Client VPN is an endpoint-based service that enables individual devices to securely access AWS resources remotely, and is not designed for site-to-site or multi-VPC connectivity.

## clf-c02/domain3/q885

Answer: C

Amazon S3 One Zone-Infrequent Access stores data in a single Availability Zone at lower cost with lower resiliency, but provides rapid millisecond access when needed, making it suitable for duplicate backups that can be recreated.
Amazon S3 Standard is designed for frequently accessed data with high durability across multiple AZs, making it more expensive and over-specified for data with lower resiliency requirements such as duplicate backups. Amazon S3 Glacier Deep Archive is designed for long-term archival of data that is rarely accessed, with retrieval times of up to 12 hours, making it unsuitable for workloads requiring rapid access. Amazon S3 Glacier is designed for archival storage with retrieval times ranging from minutes to hours, and does not provide the rapid millisecond access required for the use case described.

## clf-c02/domain3/q888

Answer: B

AWS CloudFormation uses template files to define infrastructure as code, and these templates can be deployed into multiple AWS Regions, creating identical copies of an entire infrastructure stack including all its resources and configurations in each target Region.
Amazon ElastiCache provides in-memory caching for improving application performance by reducing database load, and is a caching service rather than a service for replicating or copying infrastructure resources across Regions. AWS CloudTrail records API calls and management events for auditing and compliance purposes, and while it can be configured to deliver logs to multiple Regions, it does not enable users to create copies of AWS infrastructure resources in other Regions. AWS Systems Manager provides operational management capabilities for AWS resources including patch management, parameter storage, and automation, but does not provide a mechanism for replicating or deploying complete sets of AWS resources across multiple Regions.

## clf-c02/domain3/q891

Answer: A, D

Amazon Lightsail provides simplified virtual private servers for deploying compute workloads, and AWS Batch manages and runs batch computing jobs across dynamically provisioned compute resources. Both are compute services.
AWS Systems Manager is an operations management service for automating configuration, patching, and inventory tasks on EC2 instances, not a compute service that provisions or runs workloads. AWS CloudFormation is an infrastructure as code service for provisioning and managing AWS resources through templates, not a compute service in its own right. Amazon Inspector is an automated vulnerability assessment service that scans EC2 instances and container images for security findings, not a compute service.

## clf-c02/domain3/q900

Answer: B

AWS Transit Gateway acts as a central hub that connects thousands of VPCs and on-premises networks through a single gateway, scaling connectivity far more efficiently than managing individual connections between each network.
VPC peering creates a direct connection between two VPCs but does not scale to thousands of VPCs, as each pair requires its own peering connection and peering is non-transitive. AWS Direct Connect provides a dedicated private circuit between an on-premises data center and AWS but does not connect VPCs to each other. AWS Global Accelerator improves the availability and performance of applications for global users by routing traffic through the AWS global network, but does not provide connectivity between VPCs.

## clf-c02/domain3/q899

Answer: B

AWS Control Tower automates the setup of a secure, multi-account AWS environment using landing zones and guardrails that enforce governance policies, making it the service for automating and managing secure, well-architected multi-account environments.
AWS Config monitors and records resource configurations against compliance rules within accounts, and while it supports governance, it is a per-account compliance evaluation service rather than a service that automates the provisioning and management of entire multi-account environments. AWS Artifact provides on-demand access to AWS compliance reports and certifications, and is a documentation portal rather than a service that automates the creation or management of multi-account AWS environments. AWS CloudFormation is an infrastructure as code service for provisioning AWS resources through templates, and while it can be used to set up environments, it requires custom template development and does not provide the out-of-the-box multi-account governance and guardrails that Control Tower delivers.

## clf-c02/domain3/q905

Answer: C

Amazon ECS is a fully managed container orchestration service that handles installing, operating, and scaling the cluster management infrastructure for running Docker containers, removing the need to manage your own orchestration software.
Amazon ECR is a fully managed container registry for storing, managing, and deploying container images, not a service for running or orchestrating containers. AWS Elastic Beanstalk is a platform-as-a-service for deploying web applications and services, not a dedicated container cluster management solution. Amazon EBS is a block storage service for attaching persistent storage volumes to EC2 instances, unrelated to container orchestration.

## clf-c02/domain3/q908

Answer: B

An internet gateway enables communication between resources in a VPC and the public internet, allowing instances in public subnets to send and receive traffic from the internet.
Creating a VPN connection to the VPC is the function of a Virtual Private Gateway, not an internet gateway, as VPN connections are used to link a VPC to an on-premises network. Imposing bandwidth constraints on internet traffic is not a function of any VPC gateway component, as bandwidth management is handled at the application or network policy level. Load balancing traffic from the internet across EC2 instances is the function of an Elastic Load Balancer, not an internet gateway.

## clf-c02/domain3/q909

Answer: B

Amazon RDS Multi-AZ maintains a synchronous standby replica with the same DNS endpoint in a different Availability Zone, so when a failure occurs the endpoint automatically resolves to the standby without any change to the application connection string or manual intervention.
Using multiple Route 53 routes to a standby database hosted on AWS Storage Gateway is not a viable approach; Storage Gateway is a hybrid storage service rather than a database hosting solution, and this configuration would not maintain the same endpoint or provide automated failover. Adding multiple Application Load Balancers and deploying the database with Elastic Beanstalk would not address database high availability; Beanstalk manages application deployment and ALBs route web traffic, but neither provides the database-level failover with endpoint persistence that the requirement specifies. Deploying a Network Load Balancer across CloudFront origins would not meet this requirement; NLB distributes network traffic to targets, and CloudFront serves web content from edge locations, neither of which applies to maintaining a consistent database instance endpoint with automatic AZ failover.

## clf-c02/domain3/q910

Answer: B

Elastic Load Balancing automatically distributes incoming application traffic across multiple EC2 instances, improving availability and fault tolerance by ensuring no single instance is overwhelmed.
A NAT gateway allows instances in a private subnet to initiate outbound internet traffic while preventing inbound connections, and has no role in distributing traffic across instances. Amazon Athena is an interactive query service for analyzing data stored in S3 using SQL, entirely unrelated to traffic distribution. AWS PrivateLink provides private connectivity between VPCs and AWS services without exposing traffic to the public internet, but does not distribute traffic across compute instances.

## clf-c02/domain3/q915

Answer: C

AWS CodePipeline is a continuous delivery service that automates the build, test, and deploy phases of the application deployment process whenever code changes are made.
AWS AppSync is a managed GraphQL service that enables applications to retrieve and manipulate data from multiple sources through a single API, and has no role in automating application deployment pipelines. AWS Batch is a fully managed service for running large-scale batch computing jobs, and is designed for data processing workloads rather than application deployment automation. AWS DataSync is a data transfer service that automates moving data between on-premises storage and AWS, and has no application deployment or continuous delivery capability.

## clf-c02/domain3/q918

Answer: D

Amazon Route 53 supports multiple routing policies including latency-based routing, geolocation routing, and failover routing that direct application traffic across multiple AWS Regions, enabling global traffic management with health checks and automatic failover.
Amazon AppStream 2.0 is a managed application and desktop streaming service that delivers desktop applications securely through a browser, and is an end-user computing service rather than a networking or traffic management tool for cross-Region application traffic. Amazon VPC provides isolated networking within an AWS Region, including subnets, route tables, security groups, and gateways, but VPC is a regional construct and does not manage application traffic routing between multiple Regions. Elastic Load Balancer distributes incoming traffic across multiple targets within a single AWS Region, and while it supports multi-AZ distribution within a Region, it does not route traffic across multiple different AWS Regions.

## clf-c02/domain3/q921

Answer: B

Amazon S3 cross-region replication automatically copies objects uploaded to a source bucket in one Region to a destination bucket in another Region, ensuring that a backup of the critical data exists in a geographically separate location.
Using Amazon CloudFront to cache data globally distributes content to edge locations for faster access by end users, but CDN caching is not a durable backup mechanism; cached content is temporary and can be evicted, and CloudFront is not designed for storing permanent backup copies of S3 data. AWS Backup can back up data from various AWS services including S3, but for continuous cross-region replication of S3 objects the native S3 cross-region replication feature is the direct, purpose-built solution. Taking Amazon S3 bucket snapshots is not a native S3 feature; S3 does not have a native snapshot capability like EBS, and the correct approach for S3 backup to another Region is cross-region replication rather than snapshots.

## clf-c02/domain3/q925

Answer: C, E

A site-to-site VPN connection requires a customer gateway representing the on-premises VPN device and a virtual private gateway attached to the VPC on the AWS side, together forming the two endpoints of the encrypted tunnel.
An internet gateway connects a VPC to the public internet for general inbound and outbound traffic, and is not a component of a site-to-site VPN connection. A NAT gateway allows resources in a private subnet to initiate outbound internet connections while remaining unreachable from the internet, and has no role in establishing a VPN tunnel between on-premises infrastructure and AWS. A transit gateway acts as a central hub connecting multiple VPCs and on-premises networks together, and while it can be used in more complex VPN architectures, it is not a required component of a basic site-to-site VPN connection.

## clf-c02/domain3/q929

Answer: C

Amazon EBS provides persistent block storage volumes that retain data independently of the EC2 instance lifecycle, making it suitable for file systems, databases, and applications requiring durable storage.
Amazon S3 is an object storage service designed for storing and retrieving files via API, and does not provide a mountable file system for use as persistent block storage. Amazon EC2 instance store provides temporary block storage that is physically attached to the host server and is lost when the instance stops or terminates, making it non-persistent. Amazon ElastiCache is an in-memory caching service used to improve application performance, and has no file system or persistent storage capability.

## clf-c02/domain3/q932

Answer: A, D

AWS Lambda runs code without provisioning or managing servers, and Amazon DynamoDB is a fully managed NoSQL database that scales automatically without any server provisioning, making both fully serverless services.
Amazon OpenSearch Service requires customers to provision and manage clusters of instances, making it a server-based service rather than serverless. AWS Elastic Beanstalk is a platform service that automatically handles deployment and scaling, but still provisions and manages EC2 instances underneath, making it server-based. Amazon Redshift requires customers to provision and manage clusters for data warehousing workloads, and is not a serverless service by default.

## clf-c02/domain3/q933

Answer: A, C

AWS VPN creates encrypted tunnels over the public internet to connect on-premises networks to the AWS network, and AWS Direct Connect provides a dedicated private physical network connection between an on-premises data center and AWS. Both are the standard managed services for extending on-premises infrastructure to the AWS network.
A NAT gateway enables instances in a private subnet to initiate outbound traffic to the internet while preventing inbound connections, and is a VPC networking component rather than a service for connecting on-premises data centers to AWS. Amazon Connect is a cloud-based contact center service for managing customer communications, and has no role in network connectivity or extending on-premises infrastructure to AWS. Amazon Route 53 is a DNS and domain routing service that directs users to application endpoints, and does not establish network connections between on-premises environments and AWS.

## clf-c02/domain3/q938

Answer: A

AWS Snowball can transport up to 80 TB per device and is the most cost-effective physical transport option for 500 TB, requiring only a small number of devices rather than relying on expensive or time-consuming network transfer.
AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS for ongoing hybrid connectivity, and while it offers consistent bandwidth it is designed for continuous network access rather than one-time bulk data transport of hundreds of terabytes. AWS VPN creates an encrypted tunnel between on-premises infrastructure and AWS over the public internet, and is a network connectivity service unsuitable for transferring 500 TB of data due to the time and bandwidth costs involved in moving that volume over the internet. Amazon S3 is the destination storage service for the data rather than the transport mechanism. Uploading 500 TB directly to S3 over the internet would be prohibitively slow and expensive compared to physical transport using AWS Snowball devices.

## clf-c02/domain3/q939

Answer: C

Amazon RDS supports PostgreSQL as a managed database engine, handling automated provisioning, patching, backups, and high availability for online transaction processing workloads.
Amazon DynamoDB is a fully managed NoSQL key-value and document database, not a relational database engine and does not support PostgreSQL or OLTP workloads in the traditional sense. Amazon Athena is an interactive query service for analyzing data stored in S3 using SQL and is not a transactional database. Amazon EMR is a managed big data processing service for running distributed frameworks such as Spark and Hadoop, unrelated to relational database management.

## clf-c02/domain3/q951

Answer: A, D

Amazon RDS provides automated backups with point-in-time recovery and handles software patching of the database engine automatically, freeing teams from these operational tasks that would need to be managed manually on EC2.
Schema management is the responsibility of the customer regardless of whether the database runs on RDS or EC2, as AWS has no visibility into the application's data model or business logic and does not manage database schemas. Indexing of tables is also a customer responsibility on both RDS and EC2, as index design depends on the application's query patterns and must be defined and maintained by the database administrator. ETL management involves extracting, transforming, and loading data between systems, which is handled by dedicated services such as AWS Glue rather than being a feature provided by RDS over EC2.

## clf-c02/domain3/q952

Answer: C

S3 Intelligent-Tiering automatically monitors access patterns and moves objects between a frequent access tier and an infrequent access tier without performance impact or operational overhead, reducing storage costs for data with unpredictable or changing access patterns.
Payment flexibility by reserving storage capacity describes a commitment-based pricing model that does not exist for Amazon S3, which charges based on actual usage rather than reserved capacity. Long-term retention of data by copying it to an encrypted EBS volume is not how S3 Intelligent-Tiering works. EBS is block storage attached to EC2 instances and is entirely separate from S3 storage classes, and Intelligent-Tiering manages data within S3 itself. Secure, durable, and lowest cost storage for data archival describes Amazon S3 Glacier, which is a separate storage class designed specifically for infrequently accessed archival data with retrieval times ranging from minutes to hours, not S3 Intelligent-Tiering.

## clf-c02/domain3/q953

Answer: B

Amazon Redshift is a fully managed cloud data warehouse designed to consolidate data from multiple sources and run complex analytical queries at scale using columnar storage and massively parallel processing.
Amazon DynamoDB is a fully managed NoSQL key-value and document database optimized for high-speed transactional workloads, not for consolidating data from multiple sources into a warehouse for analytics. Amazon Athena is an interactive query service that analyzes data directly in S3 using SQL, but it does not consolidate or store data in a warehouse. Amazon QuickSight is a business intelligence and data visualisation service for building dashboards and reports, not a data warehouse for consolidating data.

## clf-c02/domain3/q960

Answer: D

AWS Snowball is a physical data transport device from the AWS Snow Family designed to transfer petabytes of data in and out of the AWS Cloud, bypassing slow or expensive network transfers for large-scale migrations.
AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage for ongoing integration, and is not designed for bulk petabyte-scale physical data transfer. Amazon S3 Glacier Deep Archive is a low-cost archival storage class for data that is rarely accessed, and has no capability to physically or programmatically transfer large volumes of data into AWS. Amazon Lightsail is a simplified compute service for deploying virtual servers, containers, and web applications with minimal configuration, and has no connection to large-scale data transfer or migration.

## clf-c02/domain3/q961

Answer: B

Amazon Redshift is a fully managed data warehouse service that enables you to run complex analytical queries against petabytes of structured data using SQL, making it the purpose-built solution for data warehousing in the AWS Cloud.
Amazon EFS is a managed shared file system for use with compute instances, providing file storage rather than a data warehousing or analytical query capability. Amazon RDS is a managed relational database service designed for transactional workloads, not for petabyte-scale analytical data warehousing. Amazon VPC is a virtual private network service for isolating and configuring cloud network infrastructure, entirely unrelated to data storage or warehousing.

## clf-c02/domain3/q964

Answer: B

Amazon Connect is a cloud-based contact center service that can be set up in minutes, providing on-demand scalability with pay-per-use pricing for customer service operations.
AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS for hybrid connectivity, and is a networking service with no capability to provide contact center functionality for managing customer communications. AWS Support Center is the portal where AWS customers create, view, and manage their own support cases with AWS, and is an internal support management interface rather than a service for building customer-facing contact centers. AWS Managed Services provides operational management of AWS infrastructure on behalf of enterprise customers including monitoring, patching, and incident management, and is an infrastructure operations service rather than a contact center platform for managing customer interactions.

## clf-c02/domain3/q966

Answer: D

An internet gateway must be attached to a VPC to enable inbound internet access, allowing resources in public subnets to receive incoming traffic from the internet.
A NAT gateway allows resources in private subnets to initiate outbound connections to the internet but does not enable inbound internet traffic to reach resources inside a VPC. A VPC endpoint enables private connectivity between a VPC and supported AWS services without routing traffic over the internet, and has no role in enabling inbound internet access. A VPN connection creates an encrypted tunnel between a VPC and an on-premises or remote network over the public internet, and is not the component that enables general inbound internet access to a VPC.

## clf-c02/domain3/q968

Answer: C

Amazon RDS with Multi-AZ enabled maintains a synchronous standby in a separate Availability Zone and performs automatic failover with no manual intervention, providing high availability that a single EC2-hosted MySQL instance cannot match.
Adding an Application Load Balancer in front of a single EC2 database instance would distribute traffic but there would still be only one database instance, meaning a failure of that instance would take down the database regardless of the load balancer; ALBs distribute traffic across multiple targets and do not themselves provide database high availability. Configuring EC2 Auto Recovery moves a failed instance to new underlying hardware within the same Availability Zone if the underlying hardware fails, but this does not protect against AZ-level failures and involves downtime during recovery rather than the near-instantaneous failover that Multi-AZ RDS provides. Enabling termination protection prevents accidental termination of an EC2 instance through the console or API, but it does not prevent the instance from failing due to software issues, storage problems, or AZ-level events, and does not provide redundancy or automatic recovery.

## clf-c02/domain3/q972

Answer: D

Amazon SQS supports FIFO queues that guarantee messages are processed exactly once in the exact order they are received, making it the correct service for applications that require strict first-in, first-out message ordering with deduplication.
AWS Step Functions is a workflow orchestration service that coordinates distributed application components through visual workflows and state machines, and while it sequences steps in a defined order, it is not a message queuing service for decoupling application components that need to exchange messages in FIFO order. Amazon SNS is a fully managed pub/sub notification service that broadcasts messages to multiple subscribed endpoints simultaneously, and it does not support FIFO guarantees for ordered message delivery between specific senders and receivers. Amazon Kinesis Data Streams is a real-time data streaming service designed for processing large volumes of streaming data from multiple producers, and while it preserves order within a shard, it is designed for high-throughput analytics pipelines rather than application-to-application message queuing with FIFO guarantees.

## clf-c02/domain3/q975

Answer: B

AWS Elastic Beanstalk automatically handles deployment, scaling, load balancing, and monitoring for supported platforms including Node.js, allowing users with limited AWS knowledge to get a scalable application running quickly without configuring the underlying infrastructure.
AWS CloudFormation is an infrastructure as code service for provisioning AWS resources using templates, which requires significant AWS knowledge to use effectively and is not designed for quick application deployment. Amazon EC2 provides raw virtual servers that require manual configuration of the operating system, runtime, networking, and scaling, making it unsuitable for users with limited AWS experience who need a quick deployment. AWS OpsWorks (deprecated) is a configuration management service using Chef and Puppet that requires expertise in those tools to manage application deployments, adding complexity rather than simplifying it.

## clf-c02/domain3/q989

Answer: C

AWS Direct Connect requires an ISP and a colocation facility at an AWS Direct Connect location to establish a dedicated private network connection between on-premises infrastructure and AWS, making it the only option here with those physical prerequisites.
AWS VPN establishes an encrypted connection over the public internet and requires no ISP arrangement or colocation facility beyond a standard internet connection. Amazon Connect is a cloud-based contact center service for managing customer communications and is entirely unrelated to network connectivity or physical infrastructure requirements. An internet gateway is a VPC component that enables communication between resources in a VPC and the public internet and requires no ISP or colocation arrangement to implement.

## clf-c02/domain3/q990

Answer: A, E

Amazon EC2 provides virtual servers for running compute workloads with full control over the operating system and configuration, and AWS Lambda runs code in response to events without provisioning or managing any servers. Both are compute services that execute workloads.
Amazon S3 is an object storage service for storing and retrieving data via API and has no compute execution capability. Amazon Elastic Block Store is a block storage service that provides persistent volumes attached to EC2 instances, not a compute service in its own right. Amazon Cognito is an identity service for managing user authentication and access control for web and mobile applications, unrelated to compute capabilities.

## clf-c02/domain3/q991

Answer: B

AWS CodeCommit is a fully managed source control service that hosts private Git repositories, providing secure storage and version management for source code.
AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces deployment-ready packages, but does not store or manage source code repositories. AWS CodePipeline is a continuous delivery service that automates the stages of a release pipeline, orchestrating build, test, and deploy steps rather than storing or versioning source code. AWS X-Ray is a unified interface for managing software development projects that brings together multiple developer tools, but is a project management layer rather than a dedicated source code repository service.

## clf-c02/domain3/q993

Answer: B

Replicating infrastructure across multiple Availability Zones within a Region provides fault tolerance and business continuity, ensuring operations continue even if one AZ is disrupted by an environmental event.
Edge locations are points of presence used by CloudFront to cache content close to end users, and are not infrastructure components that customers replicate their workloads across for fault tolerance. Regions are the broadest geographic groupings in AWS infrastructure, and while deploying across multiple Regions provides disaster recovery, replicating across Availability Zones within a Region is the standard approach for fault tolerance against environmental disruptions. Amazon Route 53 is a DNS service that routes traffic between endpoints, and is not an infrastructure component that workloads are replicated across.

## clf-c02/domain3/q994

Answer: A

Amazon SNS is a pub/sub messaging service that sends both text (SMS) and email messages from distributed applications to subscribers through topics, making it suitable for sending notifications across multiple channels simultaneously.
Amazon Simple Email Service is a cloud-based email sending service designed for sending marketing, transactional, and bulk email, but it only supports email and cannot send SMS text messages. Amazon CloudWatch alerts trigger notifications when metric thresholds are breached, but CloudWatch itself does not send text or email messages directly to end users from distributed applications. Amazon SQS is a message queuing service that buffers messages between application components to enable asynchronous communication, but it does not send text or email messages to subscribers.

## clf-c02/domain3/q996

Answer: D

AWS Direct Connect establishes a dedicated private physical connection between a remote office and AWS, bypassing the public internet entirely to deliver consistent low-latency performance with predictable throughput.
A VPN tunnel encrypts traffic between a remote office and AWS but routes it over the public internet, meaning latency and performance can vary with internet conditions rather than being guaranteed by a dedicated link. Connecting across the public internet provides no dedicated bandwidth, no privacy guarantees, and no consistent latency, making it unsuitable for workloads requiring reliable, low-latency connectivity to AWS. VPC peering creates a private network connection between two VPCs within AWS to allow direct traffic routing between them, and cannot be used to connect an external remote office to AWS infrastructure.

## clf-c02/domain3/q999

Answer: A

Deploying multiple instances across multiple Availability Zones ensures high availability by providing redundancy, so if one AZ fails, instances in other AZs continue serving traffic without interruption.
Deploying multiple instances in a single Availability Zone improves capacity and performance but provides no protection against an AZ-level failure, leaving the application vulnerable to a single point of failure. Deploying to a compute-optimized EC2 instance in a single Availability Zone addresses performance for compute-intensive workloads but offers no redundancy or fault tolerance. Deploying one EC2 instance in an Auto Scaling group allows the group to replace a failed instance but still leaves a gap in availability while the replacement is provisioned, and does not protect against an AZ failure.

## clf-c02/domain3/q1005

Answer: A

Amazon CloudFront caches images and videos at hundreds of edge locations worldwide, serving content to users from the nearest edge location rather than the origin, which minimizes latency and maximizes transfer speeds in a cost-effective manner for globally distributed audiences.
Storing content on Amazon S3 and enabling cross-region replication copies objects to S3 buckets in other Regions, which improves data availability and durability, but users still retrieve content directly from S3 in a specific Region rather than from a globally distributed edge network, resulting in higher latency than CloudFront provides. Implementing a VPN across multiple AWS Regions creates encrypted network connectivity between Regions or between on-premises environments and AWS, but a VPN is not a mechanism for delivering content to end users with low latency and does not provide edge caching capabilities. Delivering content through AWS PrivateLink provides private connectivity between VPCs and AWS services without traffic traversing the public internet, and is designed for secure service-to-service communication within AWS rather than for delivering content to external users worldwide with low latency.

## clf-c02/domain3/q1008

Answer: C

AWS Transit Gateway acts as a central network hub that connects thousands of VPCs across multiple AWS accounts through a single managed gateway, eliminating the need to manage individual point-to-point connections and significantly reducing operational complexity and cost at scale.
VPC endpoints provide private connectivity between a VPC and supported AWS services without traversing the public internet, but do not connect VPCs to each other. AWS Direct Connect establishes a dedicated private network link between on-premises infrastructure and AWS, making it irrelevant when the goal is interconnecting VPCs that are already within AWS. VPC peering creates individual one-to-one connections between VPC pairs, which becomes unmanageable and costly at scale when thousands of VPCs need to communicate.

## clf-c02/domain3/q1011

Answer: B

AWS Global Accelerator improves availability and performance for global users by directing traffic through the AWS global network infrastructure using Anycast IP addresses to route requests to the optimal endpoint, reducing latency regardless of where users are located.
Amazon CloudFront is a content delivery network that caches and serves static and dynamic content from edge locations close to users, but it is designed for content caching rather than routing live application traffic through the AWS global network to a single hosted endpoint. Amazon Route 53 is a DNS service that resolves domain names to IP addresses and can route traffic using latency-based or geolocation policies, but it operates at the DNS layer rather than directing traffic through the AWS global network infrastructure. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is not a service for improving performance for geographically distributed internet users accessing a cloud-hosted application.

## clf-c02/domain3/q1012

Answer: C

AWS Global Accelerator provides two static Anycast IP addresses that serve as a fixed entry point for applications, routing traffic through the AWS global network to endpoints in the nearest Region for improved performance and availability.
Elastic Load Balancing distributes incoming traffic across multiple targets within a single Region and does not provide static Anycast IP addresses or route traffic across multiple Regions through the AWS global network. Amazon Route 53 is a DNS-based routing service that resolves domain names to IP addresses and can route traffic using policies such as latency-based or geolocation routing, but it operates at the DNS layer rather than providing static Anycast IP addresses as fixed entry points. Amazon CloudFront is a content delivery network that caches and serves content from edge locations close to users, and does not provide static Anycast IP addresses or act as a fixed network entry point for application endpoints.

## clf-c02/domain3/q1013

Answer: C

AWS Outposts is a fully managed service that delivers AWS infrastructure, services, APIs, and tools to a customer's own data center, allowing workloads with strict data residency requirements to remain on-premises while still using AWS managed services.
AWS Wavelength extends AWS compute and storage to the edge of 5G networks for ultra-low latency applications, not for running AWS services inside a customer's own data center. AWS Local Zones place AWS compute, storage, and database services closer to large population centers for latency-sensitive workloads, but the infrastructure remains AWS-owned and operated. AWS Snow Family provides physical devices for edge computing and offline data transfer to and from AWS, not for running a permanent AWS infrastructure deployment on-premises.

## clf-c02/domain3/q1014

Answer: D

AWS Outposts extends native AWS infrastructure, services, and operating models to on-premises locations, data centers, and co-location spaces, providing a truly consistent hybrid experience with the same AWS APIs and tools used in the cloud.
AWS Direct Connect provides a dedicated private network link between on-premises infrastructure and AWS, but does not bring AWS infrastructure physically on-premises. AWS VPN creates encrypted network connections between on-premises environments and AWS over the public internet, and is a connectivity service rather than an infrastructure extension. AWS Storage Gateway connects on-premises storage environments to AWS cloud storage, but only bridges storage and does not extend the full range of native AWS services and infrastructure to on-premises locations.

## clf-c02/domain3/q1016

Answer: B

AWS Local Zones place AWS compute, storage, database, and other select services closer to large population centers and IT hubs where no nearby AWS Region exists, providing single-digit millisecond latency to end users for latency-sensitive applications.
AWS Outposts brings native AWS infrastructure and services into a customer's own on-premises data center, and is designed for workloads that must remain on-premises rather than for extending AWS presence to new metropolitan areas. AWS Wavelength embeds AWS compute and storage within telecommunications providers' 5G networks to deliver ultra-low latency for mobile and connected device use cases, and is specific to 5G edge deployments rather than general metropolitan area coverage. Amazon CloudFront is a content delivery network that caches and distributes content at edge locations worldwide to reduce latency for end users, but it is a content caching service rather than an infrastructure option for running latency-sensitive compute workloads closer to users.

## clf-c02/domain3/q1017

Answer: C

Amazon EventBridge is a serverless event bus that ingests events from your own applications, SaaS providers, and AWS services, and routes them to targets using filtering and routing rules, making it the purpose-built solution for event-driven architectures.
Amazon SNS is a fully managed pub/sub messaging service that pushes notifications to subscribers such as Lambda functions, HTTP endpoints, and email addresses, and is a notification delivery service rather than an event bus capable of routing structured events from SaaS applications with filtering rules. Amazon SQS is a fully managed message queuing service that decouples application components by holding messages in a queue for processing, and is a point-to-point queuing tool rather than a serverless event bus for real-time event routing across multiple services and SaaS integrations. AWS Step Functions is a serverless workflow orchestration service that coordinates the steps of distributed applications using visual state machines, and is a workflow execution tool rather than an event bus.

## clf-c02/domain3/q1018

Answer: B

Amazon EventBridge is a serverless event bus that detects and routes events from AWS services, custom applications, and SaaS partners to targets such as Lambda, SQS, and SNS, enabling event-driven architectures.
Amazon Kinesis is a service for ingesting and processing high-volume real-time streaming data, not for routing discrete events between AWS services. AWS CloudTrail records API calls and account activity for auditing purposes, and does not route events to application targets. Amazon MQ is a managed message broker for applications that use standard messaging protocols, and is not an event routing service for AWS resource state changes.

## clf-c02/domain3/q1023

Answer: B

Amazon Connect is a cloud-based contact center service that makes it easy to set up and manage a customer service center with pay-per-use pricing and no infrastructure to manage.
Amazon Chime was a communications service for video conferencing, messaging, and online meetings that was retired in February 2024, and was designed for internal business collaboration rather than customer-facing contact center operations. AWS Support Center is the portal for managing AWS support cases and accessing technical assistance from AWS, not a service for building customer contact centers. Amazon WorkSpaces is a managed virtual desktop service for delivering cloud-based desktops to end users, unrelated to contact center or customer service capabilities.

## clf-c02/domain3/q1024

Answer: B

Amazon SageMaker is a fully managed machine learning service that provides tools to build, train, and deploy ML models at scale, covering the entire machine learning workflow in a single managed environment.
Amazon Rekognition is a computer vision service that analyzes images and videos to detect faces, objects, and scenes, and does not provide a general-purpose environment for building and training custom ML models. AWS Lambda is a serverless compute service that runs code in response to events, and while it can run inference on pre-built models, it is not designed for building and training machine learning models at scale. Amazon Comprehend is a natural language processing service that extracts meaning and insights from text, and is a pre-built ML service rather than a platform for building and training custom models.

## clf-c02/domain3/q1025

Answer: C

Amazon Rekognition is a deep learning-based image and video analysis service that can automatically detect objects, people, text, scenes, and activities in visual content.
Amazon Comprehend is a natural language processing service that analyzes and extracts meaning from written text, and has no capability to process images or videos. Amazon Transcribe converts spoken audio into written text, and is a speech-to-text service rather than an image or video analysis service. Amazon Textract extracts printed text, handwriting, and structured data from scanned documents and images, but does not detect objects, people, or activities in images and videos the way Rekognition does.

## clf-c02/domain3/q1026

Answer: C

Amazon Comprehend uses natural language processing to analyze text and extract insights such as sentiment, entities, key phrases, and language, making it the purpose-built NLP service for analyzing customer reviews.
Amazon Lex is a service for building conversational interfaces such as chatbots using voice and text, and is a dialogue management tool rather than a text analysis or sentiment extraction service. Amazon Polly is a text-to-speech service that converts written text into lifelike spoken audio, and has no capability to analyze text for sentiment or extract key phrases. Amazon Translate is a neural machine translation service that converts text from one language to another, and is a language conversion tool rather than a service for performing sentiment analysis or key phrase extraction.

## clf-c02/domain3/q1027

Answer: B

Amazon Lex provides deep learning functionality for building conversational interfaces and chatbots using voice and text, and is the same technology that powers Amazon Alexa.
Amazon Polly converts written text into natural-sounding spoken audio and is a text-to-speech service, not a tool for building conversational interfaces that understand and respond to user input. Amazon Transcribe converts spoken audio into written text and is a speech-to-text service, focused on transcription rather than building interactive conversational experiences. Amazon Comprehend analyzes written text using natural language processing to extract meaning, sentiment, and entities, and does not process voice input or enable conversational interactions.

## clf-c02/domain3/q1028

Answer: C

Amazon Polly converts text into lifelike speech using deep learning, supporting dozens of languages and voices to enable developers to build applications that talk.
Amazon Transcribe does the opposite of text-to-speech, converting audio speech into written text, making it unrelated to generating spoken output from written content. Amazon Translate is a neural machine translation service that converts text from one language to another, and has no text-to-speech capability. Amazon Lex is a service for building conversational chatbot interfaces using voice and text, and does not itself convert written text into lifelike speech output.

## clf-c02/domain3/q1029

Answer: C

Amazon Transcribe is an automatic speech recognition service that converts spoken audio into written text, making it the right choice for transcribing customer call recordings.
Amazon Polly performs the reverse function, converting written text into natural-sounding spoken audio, and cannot process audio recordings into text. Amazon Comprehend is a natural language processing service that analyzes and extracts meaning from written text, and requires text as input rather than audio recordings. Amazon Lex is a service for building conversational chatbot interfaces using voice and text, focused on understanding and responding to user input rather than transcribing recorded audio into text.

## clf-c02/domain3/q1030

Answer: D

Amazon Translate uses neural machine translation to deliver fast, high-quality translation of text between different languages.
Amazon Comprehend is a natural language processing service that analyzes written text to extract insights such as sentiment, entities, and key phrases, and does not perform language translation. Amazon Transcribe converts spoken audio into written text, and is a speech-to-text service rather than a translation service. Amazon Lex is a service for building conversational interfaces and chatbots using voice and text, and has no language translation capability.

## clf-c02/domain3/q1031

Answer: B

AWS Fargate is a serverless compute engine for containers that removes the need to provision or manage the underlying server infrastructure, allowing customers to run Docker containers by specifying only CPU and memory requirements.
Amazon EC2 provides virtual server instances that customers must provision, configure, and manage themselves, making it a server-based option that requires infrastructure management. AWS Elastic Beanstalk is a platform service for deploying web applications that abstracts infrastructure management, but is not designed specifically for running Docker containers without infrastructure oversight. Amazon EKS is a managed Kubernetes service for orchestrating containerised workloads, but still requires customers to provision and manage the underlying EC2 node capacity unless explicitly paired with Fargate.

## clf-c02/domain3/q1032

Answer: B

Amazon EKS is a fully managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, or maintain your own Kubernetes control plane.
Amazon ECS is AWS's proprietary container orchestration service that uses its own scheduling and management model rather than Kubernetes, and is not a managed Kubernetes experience. AWS Fargate is a serverless compute engine for containers that removes the need to manage underlying server infrastructure, but is a compute layer rather than a Kubernetes orchestration service. AWS Elastic Beanstalk is a platform service for deploying web applications that abstracts infrastructure management, and is not a container orchestration or Kubernetes service.

## clf-c02/domain3/q1033

Answer: C

Amazon ECS is a fully managed container orchestration service that supports Docker containers and allows scheduling and running containers on a managed cluster of EC2 instances, integrating deeply with the AWS ecosystem.
Amazon EKS is a managed Kubernetes service for orchestrating containerised workloads using Kubernetes rather than ECS's native scheduling. AWS Lambda is a serverless compute service that runs code in response to events without provisioning or managing servers, not a container orchestration platform. AWS Batch is a managed service for running large-scale batch computing jobs and is not designed for general container orchestration or scheduling.

## clf-c02/domain3/q1042

Answer: B

AWS DataSync is a data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS storage services including Amazon S3, Amazon EFS, and Amazon FSx.
AWS Storage Gateway is a hybrid storage service that presents cloud storage as local file shares, volumes, or tape to on-premises applications for ongoing access, rather than automating one-time or scheduled data transfer to S3. AWS Snowball is a physical data transfer device designed for offline bulk data migration where transferring over the network is impractical due to data volume or bandwidth constraints, and does not automate ongoing transfers between on-premises systems and S3. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, which improves network throughput and consistency but does not itself automate or manage the transfer of data between storage systems.

## clf-c02/domain3/q1043

Answer: B

AWS DataSync automatically transfers data between on-premises storage and Amazon EFS or Amazon S3 up to 10 times faster than open-source tools, with built-in encryption, data validation, and network optimization.
AWS Transfer Family provides fully managed file transfer workflows into and out of Amazon S3 and Amazon EFS using protocols such as SFTP, FTPS, and FTP, and is a protocol-based file transfer service rather than a high-speed automated data movement service between on-premises storage and AWS. AWS Migration Hub provides a central location for tracking the progress of application migrations across multiple AWS migration tools, and is a migration monitoring and coordination service rather than a data transfer service. Amazon Kinesis Data Firehose is a fully managed service for loading real-time streaming data into destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service, and is a streaming data ingestion service rather than a tool for transferring files from on-premises storage.

## clf-c02/domain3/q1044

Answer: B

Amazon QuickSight is a cloud-native serverless business intelligence service for creating interactive dashboards and visualisations that can connect to a wide range of data sources including S3, RDS, Redshift, and Athena.
Amazon Athena is an interactive query service for analyzing data stored in S3 using SQL and is a data source that QuickSight can connect to, not a visualisation tool. Amazon Redshift is a managed data warehouse for storing and querying large volumes of structured data, not a business intelligence or dashboard service. AWS Glue is a managed extract, transform, and load service for preparing and moving data between sources, not for creating dashboards or visualisations.

## clf-c02/domain3/q1045

Answer: C

Amazon QuickSight is a serverless business intelligence service that offers pay-per-session pricing and machine learning-powered insights through natural language queries, making it the purpose-built BI tool in the AWS analytics portfolio.
Amazon Redshift is a managed data warehouse service optimized for running analytical SQL queries across large datasets, and is a data storage and querying service rather than a business intelligence or visualisation tool. Amazon EMR is a managed cluster platform for processing large volumes of data using big data frameworks such as Hadoop and Spark, and is a data processing service with no BI or visualisation capability. Amazon Athena is a serverless query service that analyzes data stored in Amazon S3 using SQL, and is a querying tool rather than a business intelligence service with dashboards, visualisations, or ML-powered insights.

## clf-c02/domain3/q1046

Answer: C

AWS Backup is a fully managed service that centralizes and automates data protection across multiple AWS services including Amazon EBS, Amazon RDS, and Amazon DynamoDB, providing a single place to manage backup policies and monitor activity.
AWS Storage Gateway is a hybrid storage service that connects on-premises environments to AWS cloud storage, and is not designed to centrally manage and automate backups across AWS services. Amazon S3 Lifecycle is a configuration feature that automatically transitions objects between S3 storage classes or expires them after a set period, and does not manage backups across other AWS services. AWS CloudFormation is an infrastructure-as-code service that provisions and manages AWS resources through templates, and has no capability to automate or centralize data backup across services.

## clf-c02/domain3/q1047

Answer: B

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the back up of data across AWS services in the cloud and on-premises. It provides a single console to create backup plans (policies) that automate backup scheduling and retention management for multiple services like Amazon EBS, RDS, DynamoDB, EFS, and more.
AWS Systems Manager is a management service used to view and control your AWS infrastructure, focusing on operational tasks like patching and configuration management rather than centralized data backups. Amazon Data Lifecycle Manager (DLM) is designed specifically to automate the creation, retention, and deletion of Amazon EBS snapshots and EBS-backed AMIs; it does not provide a centralized solution for other AWS services. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources, providing a history of resource changes rather than managing backup schedules or policies.

## clf-c02/domain3/q1048

Answer: B

AWS Glue is a fully managed serverless ETL service that crawls data sources, creates a metadata catalog, and prepares and transforms data for analytics workloads.
Amazon Kinesis is a real-time data streaming service designed for ingesting and processing continuous data streams, and is not an ETL service for preparing and transforming data for analytics. Amazon EMR is a big data processing service that runs open-source frameworks such as Apache Hadoop and Spark, and while it can perform transformations it requires significant configuration and cluster management rather than being a fully managed ETL service. AWS Data Pipeline (deprecated) is an orchestration service that automates the movement and transformation of data between AWS services and on-premises sources on a scheduled basis, but it is a workflow orchestration tool rather than a fully managed ETL service purpose-built for analytics preparation.

## clf-c02/domain3/q1049

Answer: B

AWS Glue automatically discovers and catalogs metadata from data sources using crawlers that populate the Glue Data Catalog, and can generate and run ETL scripts to transform data for analytics workloads.
Amazon Athena is a serverless query service that analyzes data stored in Amazon S3 using SQL, and relies on the Glue Data Catalog as its metadata store rather than performing discovery or ETL itself. Amazon Redshift Spectrum is a feature of Amazon Redshift that enables querying data stored in S3 directly from Redshift without loading it, and is a query extension rather than a metadata discovery or ETL service. AWS Lake Formation is a service for building, securing, and managing data lakes on AWS, and while it uses the Glue Data Catalog, it is focused on data lake governance rather than automated metadata discovery or ETL script generation.

## clf-c02/domain3/q1050

Answer: B

Amazon Kinesis is designed to collect, process, and analyze real-time streaming data at scale, making it the right choice for continuously ingesting and processing data from IoT devices as it is generated.
Amazon SQS is a message queuing service that decouples application components by buffering messages between them, but it is designed for asynchronous message delivery between services rather than continuous real-time data stream processing. Amazon SNS is a pub/sub notification service that pushes messages to multiple subscribers simultaneously, and is designed for event notifications and alerts rather than ingesting and processing high-volume continuous data streams. AWS Batch is a managed service for running large-scale batch computing jobs on dynamically provisioned resources, and processes data in scheduled or on-demand batches rather than in real time.

## clf-c02/domain3/q1051

Answer: A

Amazon Kinesis Data Streams continuously captures and processes large volumes of streaming data in real time from sources such as website clickstreams, financial transactions, and social media feeds.
Amazon Simple Queue Service (SQS) is a managed message queuing service used to decouple application components by passing messages between them, and is not designed for high-throughput real-time data stream ingestion at scale. Amazon Redshift is a cloud data warehouse service optimized for running analytical queries across large datasets, and does not ingest or process continuous real-time data streams. AWS Data Pipeline (deprecated) is an orchestration service for scheduling and automating the movement and transformation of data between AWS services and on-premises sources on a batch basis, and is not suited for real-time streaming ingestion.

## clf-c02/domain3/q1052

Answer: B

AWS Database Migration Service helps migrate databases to AWS with minimal downtime by keeping the source database fully operational during the migration process, and supports both homogeneous migrations such as Oracle to Oracle and heterogeneous migrations such as Oracle to Amazon Aurora.
AWS DataSync is a data transfer service that automates moving files and objects between on-premises storage and AWS storage services such as S3 and EFS, and is designed for file and object storage transfer rather than database migration. AWS Application Migration Service automates the migration of on-premises servers and applications to AWS by replicating them at the server level, and is a server migration service rather than a database migration service. AWS Transfer Family provides managed file transfer workflows into and out of Amazon S3 and Amazon EFS using protocols such as SFTP and FTP, and is a file transfer service with no database migration capability.

## clf-c02/domain3/q1053

Answer: B

AWS Database Migration Service supports both homogeneous migrations, such as Oracle to Oracle, and heterogeneous migrations, such as Oracle to Aurora, keeping the source database fully operational during the migration to minimize downtime.
AWS Schema Conversion Tool is used alongside AWS DMS for heterogeneous migrations to convert the source database schema to be compatible with the target database engine, but it does not perform the actual data migration itself. AWS Migration Hub provides a centralized dashboard for tracking the progress of application migrations across multiple AWS migration tools, and is not a database migration service. AWS Snowball Edge is a physical edge computing and data transfer device used to move large volumes of data into AWS when network transfer is impractical, and is not a database migration service.

## clf-c02/domain3/q1054

Answer: B

AWS DMS supports continuous data replication using Change Data Capture, streaming ongoing changes from an on-premises database to an AWS database in near real-time, making it suitable for disaster recovery and data synchronisation scenarios.
AWS Backup creates point-in-time snapshots of AWS resources on a scheduled basis, which provides recovery points but does not continuously replicate live database changes. Amazon RDS Multi-AZ maintains a synchronous standby replica within AWS for high availability and automatic failover, but does not replicate data from on-premises sources. AWS CloudFormation provisions and manages AWS infrastructure using code-based templates, and has no database replication capability.

## clf-c02/domain3/q1067

Answer: C

Amazon Kendra is an intelligent enterprise search service powered by machine learning that allows users to ask questions in natural language and receive precise answers drawn from across multiple data sources such as documents, SharePoint sites, and databases, rather than returning a simple ranked list of matching links.
Amazon Comprehend is a natural language processing service that extracts insights such as sentiment, entities, and key phrases from already-digitised text, but it does not provide a search interface or retrieve answers from a document corpus in response to natural language user queries. Amazon OpenSearch Service is a managed search and analytics engine suited for log analytics, full-text search, and operational monitoring, and returns ranked document matches based on keyword relevance rather than providing the intelligent question-answering and precise answer extraction that Kendra offers through machine learning. Amazon Lex is a service for building conversational chatbots and voice interfaces using automatic speech recognition and natural language understanding, and is designed for managing multi-turn dialogues rather than indexing and searching across enterprise document repositories.

## clf-c02/domain3/q1068

Answer: B

Amazon Kendra uses machine learning to index content from a wide range of enterprise data sources and enables users to search that content by asking natural language questions, with the service intelligently identifying and surfacing the most relevant answers rather than returning a list of documents.
Amazon Transcribe is a speech-to-text service that converts audio recordings and spoken language into written text transcripts, and is an audio processing service with no capability to index enterprise documents or respond to natural language search queries. Amazon Polly is a text-to-speech service that converts written text into lifelike spoken audio output, and is an audio synthesis service rather than a search or document information retrieval service. Amazon Translate is a neural machine translation service for converting text between different languages, and is a language conversion service with no capability to index documents or respond to natural language search queries.

## clf-c02/domain3/q1070

Answer: D

Amazon Neptune is a fully managed graph database service designed specifically for storing and navigating highly connected datasets where the relationships between data points are as important as the data itself, making it the purpose-built choice for use cases such as recommendation engines, social networks, fraud detection, and knowledge graphs.
Amazon RDS is a managed relational database service that uses tables with rows and columns connected through SQL joins to represent relationships, and while it can model connected data, it does not provide the native graph traversal efficiency and flexibility of a dedicated graph database for complex multi-hop relationship queries. Amazon Redshift is a fully managed cloud data warehouse optimized for running analytical queries on large historical datasets for business intelligence and reporting, and is not designed for real-time traversal of highly connected relationship graphs. Amazon DynamoDB is a fully managed NoSQL key-value and document database optimized for high-throughput access to items by primary key, and is not purpose-built for efficiently storing or querying the dense relationship structures characteristic of graph database workloads.

## clf-c02/domain3/q1071

Answer: C

AWS Step Functions is a serverless orchestration service that coordinates multiple AWS services into visual workflows, supporting sequential and parallel execution, error handling, automatic retries, and conditional branching, making it the purpose-built service for building complex multi-step workflows such as order processing pipelines.
Amazon SQS is a managed message queuing service that decouples application components by buffering messages between them, but does not provide workflow orchestration, branching logic, built-in retry handling, or the ability to coordinate a sequence of steps across multiple services in a stateful workflow. Amazon EventBridge is a serverless event bus that routes events between AWS services and applications based on rules, and is designed for event-driven integration and routing rather than for orchestrating complex stateful multi-step workflows with conditional branching and error handling. Amazon SNS is a managed publish/subscribe messaging service that delivers notifications simultaneously to multiple subscribers, and is an event fan-out service rather than an orchestration service capable of managing state, sequencing steps, and handling errors across a multi-step workflow.

## clf-c02/domain3/q1072

Answer: C

AWS IoT Core is a managed cloud service that allows connected devices to interact securely with cloud applications and other devices at scale, handling device authentication, connection management, and message routing to AWS services such as Kinesis and S3 through configurable rules, making it the foundation for connecting IoT devices to the AWS Cloud.
AWS IoT Greengrass is the edge component of the AWS IoT platform that extends cloud capabilities to devices for local processing and offline operation, and works alongside IoT Core rather than replacing it as the primary cloud-side service for managing device connectivity and message routing to AWS. Amazon Kinesis Data Streams is a real-time data streaming service for ingesting and processing high-throughput data, and while it can receive data routed from IoT Core, it is a data processing service rather than a device connectivity and authentication platform. AWS Direct Connect provides a dedicated private network connection between on-premises data centers and AWS, and is a network connectivity service for enterprise infrastructure rather than a platform for managing IoT device connections, authentication, and message routing at scale.

## clf-c02/domain3/q1074

Answer: C

Amazon AppStream 2.0 is a fully managed application streaming service that runs desktop applications on AWS infrastructure and streams the application interface to users' web browsers, allowing customers to use the software without downloading, installing, or managing it on their local devices.
Amazon WorkSpaces is a fully managed virtual desktop service that provides each user with a complete persistent cloud desktop environment, which is more infrastructure than required to deliver a single application through a browser and involves per-user desktop provisioning rather than application-level streaming. Amazon WorkSpaces Web is a low-cost managed service for providing browser-based access to internal websites and SaaS applications from unmanaged devices, and is designed for web content access rather than for streaming full desktop applications running on AWS compute. AWS Amplify is a development framework and hosting service for building and deploying full-stack web and mobile applications, and is a developer toolset rather than an application streaming or virtual desktop delivery service.

## clf-c02/domain3/q1075

Answer: B

Amazon WorkSpaces is a fully managed, secure virtual desktop infrastructure service that provides each user with a persistent cloud desktop accessible from any supported device, allowing companies to replace physical desktop hardware while giving employees a consistent personalized computing environment that follows them wherever they work.
Amazon AppStream 2.0 streams specific desktop applications to a browser without providing a persistent full desktop environment; users cannot install their own applications or maintain personal desktop settings across sessions, making it suited for delivering specific software rather than replacing complete personal computers. Amazon WorkSpaces Web provides browser-based access to internal websites and SaaS applications from unmanaged devices, and is a restricted access solution for web content rather than a complete persistent virtual desktop that replaces a personal computer. Amazon EC2 can run Windows or Linux virtual machines that technically function as desktops, but customers must provision, patch, and manage the instances themselves and build their own desktop management infrastructure rather than using a fully managed desktop service.

## clf-c02/domain3/q1076

Answer: D

Amazon WorkSpaces Web is a low-cost, fully managed service that provides secure browser-based access to internal websites and approved SaaS applications from unmanaged personal devices, with built-in controls that prevent users from downloading, printing, or copying corporate data to their local devices.
Amazon WorkSpaces provides full persistent virtual desktops, which is significantly more capability and cost than required for the sole purpose of providing managed web access, and does not specifically target the use case of restricting data exfiltration from unmanaged personal devices accessing web applications. AWS Client VPN extends full encrypted network access to AWS resources and on-premises systems from user devices, giving the device direct network connectivity rather than providing a controlled browser environment that prevents data from reaching the local device. Amazon AppStream 2.0 streams full desktop applications to a browser and is suited for delivering installed software rather than providing managed, restricted access to internal websites and SaaS applications from unmanaged devices.

## clf-c02/domain3/q1077

Answer: B

AWS Amplify provides a complete set of tools and services for frontend web and mobile developers to build full-stack applications on AWS, offering client libraries for authentication, data APIs, and storage along with a managed continuous deployment hosting service, without requiring developers to configure or manage the underlying cloud infrastructure.
AWS Elastic Beanstalk is a platform as a service that handles deployment and capacity provisioning for backend web applications, but is focused on backend server hosting rather than providing the frontend development libraries, mobile SDKs, and integrated CI/CD hosting pipeline that Amplify delivers for building modern full-stack applications. Amazon Lightsail is a simplified cloud platform for deploying virtual servers, containers, and databases for straightforward workloads, and while it simplifies infrastructure management it does not provide the integrated development framework, authentication library, or automated deployment workflows that Amplify offers. AWS AppSync is a managed GraphQL API service that can serve as the data layer for applications, and while it integrates with Amplify, it is a standalone API service rather than the full-stack development and hosting platform that Amplify provides.

## clf-c02/domain3/q1082

Answer: B

Amazon Simple Email Service (Amazon SES) is a cloud-based email sending service designed for high-volume transactional and application-triggered email delivery, providing the infrastructure, deliverability management, and sending metrics needed to reliably deliver order confirmations, shipping notifications, and password reset messages to customers at scale.
Amazon SNS is a fully managed publish/subscribe messaging service primarily used for sending notifications to application endpoints, Lambda functions, SQS queues, and mobile devices, and while it can deliver email to subscribed addresses, it is not optimized for high-volume transactional email delivery with the deliverability management, bounce handling, and per-message statistics that SES provides. Amazon Connect is a cloud-based contact center service for handling customer service interactions through voice and chat channels, and is a real-time agent communication platform rather than an automated email delivery service for application-triggered messages. Amazon Pinpoint is a customer engagement service for sending targeted messages across multiple channels including email, SMS, and push notifications, and while it supports email, it is oriented toward segmented marketing campaigns rather than high-volume transactional email delivery triggered by individual application events.

## clf-c02/domain3/q1083

Answer: C

Amazon Simple Email Service (Amazon SES) is a scalable, cost-effective email platform that supports both transactional email sending for automated application-triggered messages and bulk email sending for marketing campaigns and newsletters, providing deliverability tools, sending statistics, and reputation management through a unified service.
Amazon SNS is a publish/subscribe messaging service used to deliver notifications to multiple endpoints such as Lambda, SQS, and HTTP, and while it can send email to subscribed addresses as part of a notification workflow, it is not a purpose-built email platform with the bulk sending capabilities, unsubscribe management, and marketing email features that SES provides. Amazon Connect is a cloud-based contact center service for managing voice and chat customer interactions, and is a customer service communication platform rather than an email sending service for either transactional or marketing purposes. Amazon Comprehend is a natural language processing service that extracts insights such as sentiment, entities, and key phrases from text data, and is an analytics service with no capability to send or deliver email messages.

## clf-c02/domain3/q1084

Answer: D

Amazon Textract is a machine learning service that automatically extracts printed text, handwriting, structured tables, and form field data from scanned documents and images, going beyond simple character recognition to understand document structure and the relationships between fields, without requiring custom code or model training.
Amazon Comprehend is a natural language processing service that analyzes already-digitised text to extract entities, sentiment, and key phrases, but does not extract text or structured data from scanned images or PDF documents; it processes text that has already been extracted rather than performing the extraction itself. Amazon Rekognition is a machine learning service for analyzing images and videos to detect objects, scenes, activities, and faces, and while it can detect text in images as a capability, it does not extract structured tables or form fields from scanned business documents the way Textract does. Amazon Transcribe is a speech-to-text service that converts audio and video recordings into written text transcripts, and is designed for processing spoken language in audio files rather than for extracting text and structured data from scanned document images.

## clf-c02/domain3/q1085

Answer: C

AWS AppSync is a fully managed GraphQL service that simplifies building APIs for web and mobile applications, with built-in support for real-time data updates through GraphQL subscriptions that automatically push changes to all connected clients whenever underlying data is modified, making it ideal for collaborative and live-updating applications.
Amazon API Gateway is a fully managed service for creating RESTful, HTTP, and WebSocket APIs, and while WebSocket APIs support two-way communication, API Gateway does not natively provide GraphQL schema management, resolver configuration, or the subscription-based real-time data push model that AppSync delivers for building collaborative applications. Amazon Kinesis is a real-time data streaming service for ingesting and processing high-throughput data streams, and is designed for building data pipelines and analytics rather than for providing a GraphQL API layer with subscription-based real-time updates to application clients. AWS Amplify is a full-stack development framework that provides client-side libraries for connecting applications to AppSync APIs, but Amplify is the frontend tooling layer rather than the managed GraphQL service that hosts the API, manages data sources, and delivers real-time subscriptions to clients.

## clf-c02/domain3/q1106

Answer: B

Amazon FSx for Windows File Server provides a fully managed Windows-native file system built on Windows Server with full SMB protocol support, Active Directory integration, and NTFS, making it the purpose-built service for migrating Windows-based file workloads to AWS.
Amazon EFS is a fully managed NFS file system designed for Linux-based workloads and does not support the SMB protocol required by Windows applications. Amazon S3 is an object storage service accessed via HTTP APIs and is not a file system that supports SMB protocol access for Windows workloads. AWS Storage Gateway provides hybrid cloud storage that connects on-premises environments to AWS storage services, but it is a gateway appliance rather than a fully managed cloud-native file system.

## clf-c02/domain3/q1107

Answer: C

Amazon FSx provides fully managed file systems built on popular third-party and open-source technologies including Lustre for high-performance computing, NetApp ONTAP for enterprise workloads, OpenZFS, and Windows File Server, each optimized for specific workload requirements.
Amazon EBS provides block-level storage volumes attached to individual EC2 instances and is a block storage service rather than a managed file system supporting multiple file system technologies. Amazon S3 is an object storage service designed for storing and retrieving any amount of data via HTTP APIs, and does not provide file system access through protocols like NFS, SMB, or Lustre. Amazon EFS is a managed NFS file system for Linux workloads and supports only the NFS protocol, unlike FSx which offers multiple file system types for different workload requirements.

## clf-c02/domain3/q1108

Answer: B

Amazon WorkSpaces Web provides a fully managed, browser-based service that allows users to securely access internal web applications and SaaS applications from any device with a web browser, without requiring software installation or a full virtual desktop environment.
Amazon WorkSpaces provides fully managed persistent virtual desktops in the cloud, which is a heavier solution than needed for simple web application access and requires a client application to be installed on the device. Amazon AppStream 2.0 streams desktop applications to users through a web browser, but it is designed for streaming full desktop applications rather than providing lightweight secure browser access to web applications. AWS Client VPN provides secure remote access to an AWS network from individual devices, but it requires VPN client software to be installed and configured on each device.

## clf-c02/domain3/q1109

Answer: C

Amazon WorkSpaces Web is a low-cost, fully managed browser-based service specifically designed for securely accessing web applications and websites without the overhead of provisioning and managing full virtual desktop infrastructure.
Amazon AppStream 2.0 is an application streaming service that delivers desktop applications to users through a web browser, and is designed for streaming resource-intensive applications rather than providing lightweight web-only browser access. Amazon WorkSpaces provisions full persistent virtual desktops with a complete operating system environment, which is more than what is needed for web-only application access and carries higher cost and management overhead. AWS Direct Connect establishes a dedicated private network connection between on-premises infrastructure and AWS, and is a networking service with no capability to provide browser-based application access.

## clf-c02/domain3/q1110

Answer: B

AWS License Manager helps customers manage software license entitlements from vendors such as Microsoft, Oracle, and SAP across AWS and on-premises environments, providing centralized tracking and enforcement of licensing rules to prevent compliance violations.
AWS Systems Manager provides operational tools for managing EC2 instances and on-premises servers including patching, automation, and parameter storage, but does not track or enforce software licensing rules. AWS Config records and evaluates the configuration of AWS resources against compliance rules, but it monitors resource configurations rather than tracking software license entitlements and usage. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for deployment on AWS, but it governs which products can be deployed rather than tracking software license compliance.

## clf-c02/domain3/q1111

Answer: C

AWS License Manager enables customers to define licensing rules based on their agreements with software vendors, track license usage across AWS and on-premises environments, and enforce limits to prevent exceeding entitlements, reducing the risk of non-compliance and unexpected licensing costs.
AWS Marketplace is a digital catalog for finding, buying, and deploying third-party software that runs on AWS, and while it handles procurement of new licenses, it does not manage existing license entitlements or enforce usage limits across environments. AWS Organizations is an account management service for centrally governing multiple AWS accounts through policies and consolidated billing, and does not provide software license tracking or enforcement. AWS Trusted Advisor provides automated recommendations for improving security, cost, performance, and fault tolerance of an AWS environment, but does not track or manage software licensing compliance.

## clf-c02/domain3/q1112

Answer: C

Amazon Elastic Container Registry is a fully managed Docker container registry that integrates natively with Amazon ECS and Amazon EKS, providing secure, scalable storage for container images with built-in vulnerability scanning and lifecycle policies.
Amazon S3 is an object storage service that can store any type of file, but it is not a container registry and does not provide the Docker registry API, image layer management, or native container service integration that ECR offers. AWS CodeCommit is a managed Git repository service for storing and versioning source code, not container images, and does not provide Docker registry functionality. AWS CodeArtifact is a managed artifact repository for storing and sharing software packages such as npm, Maven, and Python packages, but it does not support Docker container images.

## clf-c02/domain3/q1113

Answer: B

AWS Elastic Disaster Recovery continuously replicates source servers to AWS using lightweight agents, maintaining a low-cost staging area, and can quickly launch fully provisioned recovery instances in minutes when a disaster occurs, providing an automated and cost-effective disaster recovery solution.
AWS Backup is a centralized backup service that automates and manages backups across AWS services, but it creates point-in-time backups for data recovery rather than providing continuous replication and rapid server recovery for disaster recovery scenarios. Amazon S3 Cross-Region Replication automatically copies S3 objects to a bucket in a different Region for data durability, but it only replicates S3 data and cannot recover full server environments including operating systems and applications. AWS DataSync automates data transfer between on-premises storage and AWS storage services, but it is a data movement tool rather than a disaster recovery service that can launch recovery instances.

## clf-c02/domain3/q1114

Answer: C

AWS Resource Access Manager enables customers to securely share AWS resources such as VPC subnets, Transit Gateways, and Route 53 Resolver rules across AWS accounts within an organization, eliminating the need to create duplicate resources in each account.
AWS Organizations provides centralized management and governance of multiple AWS accounts through service control policies and consolidated billing, but it does not itself provide the mechanism to share specific resources like subnets or Transit Gateways between accounts. VPC Peering creates a networking connection between two VPCs that allows traffic to flow between them, but it is a point-to-point connection and does not share resources like subnets or Transit Gateways across accounts. AWS Control Tower automates the setup and governance of a secure multi-account AWS environment based on best practices, but it is an account governance service that does not provide resource sharing capabilities.

## clf-c02/domain3/q1141

Answer: B

Amazon Q is a generative AI-powered assistant designed for businesses that can be customized with enterprise data to answer questions, generate content, take actions, and automate workflows, providing a ready-to-use AI assistant without requiring machine learning expertise.
Amazon SageMaker AI is a fully managed platform for building, training, and deploying custom machine learning models, which requires data science expertise and is designed for custom ML development rather than a ready-to-use conversational AI assistant. Amazon Lex is a service for building conversational chatbots using voice and text interfaces, but it requires developers to define intents and conversation flows rather than providing a pre-built generative AI assistant that works with enterprise knowledge. Amazon Kendra is an intelligent enterprise search service that indexes documents and returns relevant answers to search queries, but it is a search engine rather than a generative AI assistant that can create content and automate tasks.

## clf-c02/domain4/q006

Answer: B

With consolidated billing, Reserved Instance discounts are automatically shared across all accounts in the organization, so any account can benefit from the hourly cost savings.
The Reserved Instance discounts applying only to the master account is incorrect because consolidated billing specifically shares RI benefits across all member accounts in the organization, not just the account that purchased them. The claim that reserved instances have better performance than On-Demand instances is false because both run on the same underlying AWS infrastructure, and the Reserved Instance pricing model is a billing commitment rather than a different hardware tier. Consolidated billing does provide real cost benefits beyond purely organizational purposes, combining usage for volume discounts and sharing Reserved Instance savings across accounts, so the claim that it is for informational purposes only is incorrect.

## clf-c02/domain4/q009

Answer: B

The AWS Support Concierge, available exclusively on the Enterprise Support plan, is a dedicated team for billing and account inquiries, providing fast and personalized assistance.
AWS Health Dashboard provides real-time and personalized alerts about AWS service events that may affect your resources, and is a service health monitoring tool rather than a billing or account support contact. AWS Customer Service handles general account and billing enquiries for all customers but does not provide the dedicated, personalized support that the Concierge team offers to Enterprise plan holders. AWS Business Support provides 24/7 access to Cloud Support Engineers for technical issues and includes Infrastructure Event Management for an additional fee, but does not include a dedicated Concierge team for billing and account guidance.

## clf-c02/domain4/q016

Answer: D

AWS Cost and Usage Reports provide the most detailed and comprehensive breakdown of actual AWS spending, including EC2 billing activity, by time period and resource.
AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a service for reviewing historical billing activity. The AWS Pricing Calculator estimates future costs for AWS services before provisioning them, and does not provide reports on historical billing activity. AWS Systems Manager provides operational tools for managing and automating tasks across AWS infrastructure, and has no connection to billing reporting or cost analysis.

## clf-c02/domain4/q017

Answer: C

Consolidated billing aggregates usage across all accounts, which can push the combined usage into higher volume tiers and unlock volume discounts that individual accounts would not reach on their own.
AWS services costs are not reduced to half the original price under consolidated billing. Volume discounts apply incrementally based on combined usage tiers and vary by service rather than applying a fixed 50% reduction. Consolidated billing provides genuine cost benefits beyond purely organizational purposes through volume discounts and Reserved Instance sharing, so the claim that it is purely organizational is incorrect. Each AWS account does not receive five times the free-tier services capacity under consolidated billing. The free tier applies per organization rather than per account, and consolidated billing does not multiply free-tier allowances.

## clf-c02/domain4/q020

Answer: A, C

A CloudWatch billing alarm triggers an SNS notification when costs exceed a set threshold, and AWS Budgets lets you set custom cost thresholds with automatic alerts. Both are native AWS tools for cost monitoring.
Amazon Simple Email Service is an email sending service for transactional and marketing communications, and while it can send emails it does not natively monitor AWS billing or trigger alerts based on cost thresholds. AWS CloudTrail records API calls and account activity for auditing purposes, and has no capability to monitor billing thresholds or delete resources in response to cost events. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and has no connection to AWS billing monitoring or cost threshold alerting.

## clf-c02/domain4/q028

Answer: D

On-Demand instances let you run workloads for any duration without long-term commitments or interruptions, making them ideal for short, one-time tasks where continuous availability is required.
Reserved Instances require a minimum one-year commitment and are cost-effective for steady-state workloads running continuously over that period, making them a poor fit for a single-day task where the commitment term would far exceed the actual usage. Spot Instances use spare AWS capacity at a significant discount but can be interrupted by AWS at any time, making them unsuitable for a workload that must run for a full day without interruption. Dedicated Instances run on hardware dedicated to a single customer for compliance or licensing purposes, and while they provide isolation they are more expensive than standard On-Demand Instances and do not offer any advantage for a simple one-day task.

## clf-c02/domain4/q029

Answer: D

Spot Instances use spare AWS capacity at steep discounts and are perfect for fault-tolerant batch jobs like image processing, where interruptions are acceptable and uptime is not critical.
Reserved Instances provide a significant discount over On-Demand pricing for steady-state workloads through a one or three-year commitment, but are not cost-effective for batch workloads that run only periodically and can tolerate interruptions. On-Demand Instances charge the full hourly rate with no discount, making them significantly more expensive than Spot Instances for a batch image processing workload where the timing is flexible. Dedicated Instances run on hardware dedicated to a single customer and are designed for compliance and licensing isolation requirements, not for cost optimization of batch processing workloads.

## clf-c02/domain4/q034

Answer: D

The AWS Technical Account Manager is included in the Enterprise Support plan as the primary dedicated contact who provides proactive guidance and coordinates AWS support across your account.
An AWS IAM user is an identity within an AWS account used to authenticate and authorise access to AWS services, and is not a support contact or a role within the AWS Support organization. An Infrastructure Event Management engineer provides architectural guidance and real-time support during specific planned events under the Enterprise Support plan, but is engaged for specific events rather than serving as the ongoing primary support contact. AWS Consulting Partners are professional services firms in the AWS Partner Network that help customers design and build on AWS, and are external organizations rather than AWS Support personnel assigned to an account.

## clf-c02/domain4/q035

Answer: C

AWS Cost Explorer provides interactive charts and reports that visualise your AWS spending patterns over time, broken down by service, account, or tag.
The Amazon VPC console is a networking tool for managing virtual private clouds, subnets, gateways, and network configuration, and has no connection to billing information or spending distribution. Contacting the AWS Support team provides technical guidance and issue resolution, and is not a self-service mechanism for viewing the distribution of AWS spending across your account. Contacting the AWS Finance team is not a supported customer-facing channel for accessing billing and spending information, which is available directly through the AWS Management Console via Cost Explorer and billing dashboards.

## clf-c02/domain4/q049

Answer: C

AWS Quick Start reference deployments provide automated gold-standard templates that deploy popular IT solutions on AWS in minutes, giving administrators a fast path to production-ready environments built on AWS best practices.
Amazon Aurora is a fully managed relational database compatible with MySQL and PostgreSQL, and is a database service with no capability to deploy or provision third-party technologies or solutions. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and is a monitoring service with no deployment or provisioning capability. AWS OpsWorks (deprecated) was a configuration management service that used Chef and Puppet to automate server configuration, and while it could automate some infrastructure tasks it is not a pre-built deployment resource for rapidly deploying popular third-party technologies with minimal effort. Note: AWS OpsWorks was deprecated in 2024.

## clf-c02/domain4/q050

Answer: D

Convertible Reserved Instances allow you to exchange your reservation for another Convertible RI with different attributes such as instance type, operating system, or tenancy during the term, providing flexibility when workload requirements change.
Scheduled Reserved Instances were a former RI type that allowed you to reserve capacity for specific recurring time windows, and did not support attribute exchanges during the term. Note: Scheduled Reserved Instances have been deprecated by AWS. Standard Reserved Instances offer the highest discount but are fixed to a specific instance family and cannot be exchanged for a different configuration during the reservation period. On-Demand Instances are a separate EC2 purchasing model that charges for compute on an hourly or per-second basis with no commitment, and are not a Reserved Instance type at all.

## clf-c02/domain4/q052

Answer: C

Three-year All Upfront Standard RIs combine the longest commitment term with full prepayment and the Standard type, which together yield the deepest discount compared to On-Demand pricing.
A one-year No Upfront Standard RI offers the lowest upfront cost but provides the smallest discount among the options listed, as the short term and absence of prepayment both reduce the overall savings. A one-year All Upfront Convertible RI benefits from full prepayment but is limited by the shorter term and the Convertible type, which offers less discount than Standard RIs in exchange for flexibility to exchange attributes. A three-year No Upfront Convertible RI benefits from the long commitment term but sacrifices discount depth through both the absence of prepayment and the Convertible type designation, making it less cost-effective than the All Upfront Standard equivalent.

## clf-c02/domain4/q059

Answer: B, E

AWS pricing is pay-as-you-go and variable cost. There are no fixed terms required, no colocation fees, and no mandatory upfront plans.
Fixed-term pricing requires a commitment to a set contract duration, which is the opposite of the AWS pay-as-you-go model where usage can scale up or down at any time without contractual obligations. Colocation refers to housing customer-owned servers in a third-party data center, which is an on-premises model rather than a cloud pricing principle. Planned pricing implies predetermined usage schedules and costs, which contradicts the AWS model where customers pay based on actual consumption without mandatory advance planning.

## clf-c02/domain4/q061

Answer: C

AWS Organizations consolidated billing aggregates usage across all member accounts, qualifying the organization for volume pricing tiers without requiring resource consolidation or upfront RI commitments.
Creating one global account and moving all resources is a high-impact change that would eliminate account-level isolation, security boundaries, and governance, and it is unnecessary because consolidated billing earns the same volume discounts without migration. Reserved Instance pricing locks compute into a specific instance type and term, which lowers cost for predictable workloads but does not provide cross-account volume discounts. The Enterprise Support plan adds Technical Account Managers and premium support, but support tiers do not grant volume discounts on service usage.

## clf-c02/domain4/q062

Answer: C

All Upfront Reserved Instances for a 3-year term provide the maximum possible EC2 discount because you combine the longest commitment term with full prepayment, which together yield the deepest savings compared to On-Demand pricing.
Partial Upfront Reserved Instances for a 1-year term offer a moderate discount, but the shorter term and partial prepayment both reduce the total savings compared to the 3-year All Upfront option. All Upfront Reserved Instances for a 1-year term offer a good discount through full prepayment but are limited by the shorter commitment term, which yields less total savings than a 3-year commitment. No Upfront Reserved Instances for a 3-year term benefit from the long commitment term but forgo the additional discount that comes with upfront payment, making them less cost-effective than All Upfront options.

## clf-c02/domain4/q066

Answer: A, C

AWS Business Support includes 24/7 access to Cloud Support Engineers via phone, email, and chat, plus an unlimited number of support cases and contacts.
Support from a dedicated Technical Account Manager who provides proactive guidance and acts as a primary contact is exclusively available with the AWS Enterprise Support plan and is not included in Business Support. A 15-minute response time for production system interruption cases is an Enterprise Support feature. Business Support provides a one-hour response SLA for production system-down cases, not 15 minutes. Annual operational reviews with AWS Solutions Architects are an Enterprise Support benefit and are not included in the Business Support plan.

## clf-c02/domain4/q068

Answer: A

EC2 Dedicated Hosts provide a physical server dedicated entirely to your use with full visibility into sockets, cores, and host ID, which is required for server-bound software licensing such as BYOL and for certain compliance frameworks that mandate physical isolation.
Dedicated Instances run on hardware dedicated to a single customer but do not provide visibility into the specific physical host, which is required for most per-socket or per-core licensing models and does not satisfy all compliance requirements for physical server isolation. Spot Instances use spare AWS capacity at a significant discount but can be interrupted by AWS at any time, making them unsuitable for workloads with compliance requirements that mandate consistent physical server hosting. Reserved Instances are a pricing commitment for EC2 capacity that can reduce costs over a 1 or 3-year term, but they run on shared infrastructure and do not provide physical server isolation or host-level visibility required for BYOL licensing.

## clf-c02/domain4/q069

Answer: C

Convertible RIs allow you to exchange them for other Convertible RIs of equal or greater value, letting you change instance family, OS, tenancy, or payment option over the term. Standard RIs cannot be exchanged.
Dedicated RIs are a tenancy attribute rather than a separate RI type, allowing the instance to run on hardware dedicated to a single customer, and this designation does not affect whether the RI can be exchanged. Scheduled RIs were a former RI type that allowed reservation of capacity for specific recurring time windows, and did not support attribute exchanges during the term. Note: Scheduled RIs have been deprecated by AWS. Standard RIs provide the highest discount among RI types but are locked to a specific instance family, size, operating system, and tenancy, and cannot be exchanged for a different configuration once purchased.

## clf-c02/domain4/q071

Answer: A, D

Spot Instances are best for non-production applications that can tolerate interruptions and for fault-tolerant, flexible workloads that can checkpoint and resume. Stateful, high-uptime, or sensitive database workloads should not use Spot.
Stateful workloads that maintain persistent connections or application state are not suitable for Spot Instances because an interruption would disrupt that state, requiring complex recovery mechanisms. Applications that cannot have interruptions require guaranteed availability that Spot Instances cannot provide, as AWS may reclaim Spot capacity at any time with a two-minute warning. Sensitive database applications require consistent availability, data integrity, and predictable performance, making them poorly suited to the interruption risk inherent in Spot Instance pricing.

## clf-c02/domain4/q074

Answer: A

Infrastructure Event Management is included at no extra cost only with the AWS Enterprise Support plan, providing architectural guidance and real-time support during planned events such as product launches and traffic spikes.
Business Support customers can access Infrastructure Event Management but must pay an additional fee for each event engagement, making it not included as a standard benefit at no extra cost. Developer Support provides business-hours email access to Cloud Support Engineers for general technical questions and does not include Infrastructure Event Management at any price point. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and does not include any form of event management support.

## clf-c02/domain4/q080

Answer: C

The AWS Pricing Calculator allows users to model AWS service configurations and estimate costs, enabling comparison between on-premises infrastructure costs and projected AWS spending to understand potential savings from migration.
AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost monitoring tool for active AWS workloads rather than a pre-migration savings estimation tool. AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns, and requires active AWS usage to generate data rather than providing pre-migration cost comparisons. The AWS Well-Architected Tool helps review workloads against the six pillars of the Well-Architected Framework to identify architectural risks and improvements, and is not a cost comparison or savings estimation tool.

## clf-c02/domain4/q082

Answer: A

Cost allocation tags are key-value labels attached to AWS resources that enable you to organize and track spending at a granular level by project, team, or environment in Cost Explorer and billing reports.
Consolidated billing combines usage from all member accounts in an AWS Organization to produce a single invoice and qualify for volume discounts, but does not itself provide the granular resource-level categorization that tags enable for detailed cost tracking. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when exceeded, and is a cost governance and alerting tool rather than a mechanism for categorizing and tracking spending at a detailed resource level. AWS Marketplace is a digital catalog for discovering and purchasing third-party software solutions that run on AWS, and has no connection to cost categorization or spending analysis.

## clf-c02/domain4/q083

Answer: B

AWS Trusted Advisor scans your AWS environment and provides recommendations across cost optimization, performance, security, fault tolerance, and service limits, helping save money and improve architecture.
AWS Cost Explorer is a tool for visualising and analyzing historical and forecasted AWS spending patterns, but it does not inspect environments for performance improvement opportunities or architectural recommendations. Consolidated billing is a feature of AWS Organizations that combines charges from multiple accounts into a single bill for simplified payment, and has no environment inspection or recommendation capability. Detailed billing provides granular line-item reports of AWS usage and charges for cost analysis purposes, and does not identify opportunities to save money or improve system performance.

## clf-c02/domain4/q092

Answer: B

A dedicated Technical Account Manager who provides proactive guidance and acts as a primary contact is exclusively available with the AWS Enterprise Support plan.
Developer Support provides business-hours email access to Cloud Support Engineers for general technical questions, and does not include a dedicated Technical Account Manager or any dedicated account management resource. Business Support provides 24/7 access to Cloud Support Engineers via phone, email, and chat plus full Trusted Advisor checks, and while it offers substantial support resources it does not include a dedicated Technical Account Manager. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and includes no dedicated support personnel or account management.

## clf-c02/domain4/q097

Answer: C

AWS Partner Network Consulting Partners are professional services firms that help customers design, build, migrate, and manage AWS workloads. Technology Partners provide software and tools; the Marketplace is for purchasing software.
AWS Partner Network Technology Partners develop software, tools, and services that complement AWS, and are product companies rather than professional services firms that help customers directly design and build workloads from scratch. AWS Marketplace is a digital catalog where customers can discover and purchase third-party software solutions, and is a procurement platform rather than a professional services resource for technical expertise and hands-on workload development. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal use and self-service provisioning, and is an internal governance tool rather than a professional services program.

## clf-c02/domain4/q100

Answer: B

AWS Organizations allows you to create a hierarchy of AWS accounts, consolidate billing across accounts, and apply governance policies through Service Control Policies centrally from a management account.
AWS IAM manages users, roles, and permissions within a single account and cannot manage or consolidate multiple accounts. AWS Schema Conversion Tool is a database migration tool for converting database schemas between different engines, unrelated to account management. AWS Config tracks and records configuration changes to resources within an account, but does not provide multi-account consolidation or governance.

## clf-c02/domain4/q101

Answer: A

AWS shifts infrastructure spending from large upfront capital expenditures to smaller, ongoing operational expenses, directly reducing TCO by eliminating the need to over-provision for peak demand.
Having no responsibility for third-party license costs is not a general AWS benefit, as customers still manage and pay for their own software licenses when running applications on AWS, unless they use AWS-provided licenses through services such as Amazon RDS. AWS does not eliminate operational expenditures. Customers continue to pay ongoing usage-based costs for the AWS services they consume, which are operational expenses rather than capital expenses. AWS does not manage customer applications by default. Application-level management including code, configuration, and updates remains the customer's responsibility under the shared responsibility model.

## clf-c02/domain4/q102

Answer: B, E

AWS Online Tech Talks are live and on-demand webinars that include interactive Q&A sessions, and AWS Classroom Training offers instructor-led courses delivered by certified trainers, both providing structured learning in an instructor-led or live setting.
AWS Trusted Advisor is an automated tool that provides real-time recommendations across cost, security, performance, and fault tolerance, not a learning or training resource. AWS Blog is a self-service publishing channel for news and technical content that customers read independently, not an instructor-led format. AWS Forums is a community-driven discussion platform where customers help each other with questions, not a structured instructor-led learning environment.

## clf-c02/domain4/q106

Answer: A, D

Consolidated billing produces a single combined invoice for all accounts in an AWS Organization, and it pools usage across all accounts to qualify for volume pricing tiers.
Service limits do not automatically increase for all accounts under consolidated billing. Service limit increases must be requested individually through AWS Support on a per-service and per-region basis. Consolidated billing does not provide a fixed discount on the monthly bill. Volume discounts are applied progressively based on combined usage tiers and vary by service rather than applying a uniform percentage reduction. The master account's AWS Support plan is not automatically extended to all member accounts. Each account within an AWS Organization must maintain its own support plan, and support plan costs and benefits remain account-specific.

## clf-c02/domain4/q110

Answer: B

AWS Business Support guarantees a one-hour response time for production system-down cases and provides 24/7 phone, email, and chat access. Developer Support offers business-hours email only; Basic has no case support; Enterprise offers faster response but at higher cost.
Enterprise Support provides faster response times including a 15-minute SLA for business-critical system failures, and also meets the one-hour production system-down SLA, but it is a higher-cost plan than Business Support and therefore not the minimum required. Developer Support provides business-hours email access to Cloud Support Engineers with response times measured in hours rather than one hour, and does not include 24/7 access or a one-hour production system-down SLA. Basic Support provides access to documentation and the seven core Trusted Advisor checks but includes no technical case support and no defined response time SLAs.

## clf-c02/domain4/q112

Answer: C

AWS Professional Services is a global team of experts that helps customers achieve their desired business outcomes on AWS through paid engagements across specialty practice areas including migration, security, and data analytics.
AWS Enterprise Support is a paid support plan that provides access to a Technical Account Manager and 24/7 access to senior cloud support engineers, but it is a support tier rather than a consulting engagement team that works on specialty practice projects. AWS Solutions Architects advise customers on designing well-architected solutions and are available through various AWS programs, but they provide architectural guidance rather than leading paid consulting engagements across specialty practice areas. AWS Account Managers manage the overall commercial relationship between AWS and a customer, but they handle account and sales activities rather than delivering hands-on technical consulting engagements.

## clf-c02/domain4/q113

Answer: C

AWS Business Support is the lowest-cost plan that provides 24/7 phone, email, and chat access to Cloud Support Engineers with a one-hour response SLA for production system interruptions.
Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, but includes no technical case support or access to Cloud Support Engineers. Developer Support provides email access to Cloud Support Engineers during business hours only, and does not include 24/7 phone or chat access or a one-hour production system response SLA. Enterprise Support also provides 24/7 access with faster response times including a 15-minute SLA for business-critical system failures, but is a higher-cost plan than Business Support and therefore not the minimum required to meet these specific requirements.

## clf-c02/domain4/q115

Answer: B, C

Trusted Advisor analyzes your AWS environment and provides cost optimization recommendations based on current usage patterns, and it flags potential security issues caused by overly permissive IAM or resource settings. It does not automatically remediate issues or alert on compromised instances.
Identifying software vulnerabilities in applications running on AWS is the function of Amazon Inspector, which scans EC2 instances and container images for CVEs and unintended network exposure, rather than Trusted Advisor which checks against AWS best practices. Automatically correcting potential security issues is not a function of Trusted Advisor, which provides advisory recommendations and flags concerns but does not take automated remediation actions on your resources. Providing proactive alerting when an EC2 instance has been compromised is the function of Amazon GuardDuty, which uses machine learning and threat intelligence to detect suspicious behavior, rather than Trusted Advisor which performs periodic checks against predefined best practice criteria.

## clf-c02/domain4/q123

Answer: A

Consolidated billing combines usage from all member accounts in an AWS Organization, qualifying the organization for volume pricing tiers that individual accounts might not reach on their own.
Shared access permissions are not a benefit of consolidated billing. Access control is managed through IAM policies, Service Control Policies, and resource-based policies, none of which are affected by enabling consolidated billing. Consolidated billing produces a single invoice for all accounts rather than multiple bills per account, so the option describing multiple bills per account is the opposite of what consolidated billing provides. Consolidated billing does not eliminate the need for tagging. Cost allocation tags remain essential for attributing costs to specific projects, teams, or environments even when usage is aggregated under a single consolidated bill.

## clf-c02/domain4/q125

Answer: C

EC2 Dedicated Hosts provide a physical server dedicated to your use, which is required to use existing per-socket, per-core, or per-VM software licenses. Spot, Reserved, and On-Demand all run on shared or unspecified hardware and do not support license binding to specific physical hosts.
Spot Instances use spare AWS capacity and run on shared infrastructure without any visibility into the underlying physical host, making them entirely unsuitable for licensing models that require binding to a specific physical server. Reserved Instances are a pricing commitment for EC2 capacity that reduces costs over a 1 or 3-year term, but they run on standard shared infrastructure and do not provide the host-level visibility required for most BYOL licensing scenarios. On-Demand Instances charge the full hourly rate with no long-term commitment, and like Reserved Instances they run on shared infrastructure without the physical server visibility and dedication required for server-bound software licenses.

## clf-c02/domain4/q131

Answer: C

The AWS Support Concierge team, dedicated billing and account experts who provide personalized guidance, is available exclusively to Enterprise Support customers.
AWS Trusted Advisor is available in a limited form with Basic and Developer Support providing the seven core checks, and in full with Business and Enterprise Support, so it is not exclusive to Enterprise users. AWS Support cases can be opened by customers on Developer, Business, and Enterprise Support plans, and are not exclusive to Enterprise users. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is an AWS product that customers deploy rather than a support program or resource exclusive to any support tier.

## clf-c02/domain4/q133

Answer: A

EC2 Dedicated Hosts provide physical isolation of the workload on a server dedicated entirely to one customer, which is required for certain compliance mandates or licensing models. This hosting model has a higher cost that must be factored into TCO calculations.
Reserved Instances are a pricing commitment that reduces EC2 costs over a 1 or 3-year term, and while they lower ongoing costs they run on standard shared infrastructure and do not provide the physical isolation that a TCO analysis for compliance-mandated workloads must account for. On-Demand Instances charge the full hourly rate on shared infrastructure with no long-term commitment, and while they are useful for variable workloads they do not provide physical isolation and have higher per-unit costs that would not reflect a compliance-focused TCO calculation. No Upfront Reserved Instances provide a discount over On-Demand through a long-term commitment without any initial payment, but like standard Reserved Instances they run on shared infrastructure and do not account for the physical isolation costs required by compliance mandates.

## clf-c02/domain4/q135

Answer: B

AWS Business Support is the minimum plan that includes 24/7 phone support with a dedicated team of Cloud Support Engineers. Developer Support only provides email during business hours; Basic has no technical phone or case support.
Enterprise Support provides 24/7 phone access and faster response times including a 15-minute SLA for business-critical system failures, but is a higher-cost plan than Business Support and therefore not the minimum required to access phone support. Developer Support provides business-hours email access to Cloud Support Engineers but does not include any phone support at any time. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and includes no phone support or technical case assistance.

## clf-c02/domain4/q136

Answer: D

Spot Instances use spare AWS capacity and can offer discounts of up to 90% compared to On-Demand prices. Reserved Instances offer up to approximately 72% discount; On-Demand is the baseline price; Dedicated Hosts typically cost more than standard options.
Reserved Instances offer savings of up to approximately 72% compared to On-Demand pricing in exchange for a 1 or 3-year commitment, which is a significant discount but substantially less than the up to 90% available through Spot Instances. On-Demand Instances are charged at the standard AWS rate with no discount, as they are the baseline pricing model against which all other purchasing options are measured. Dedicated Hosts are priced at a premium over standard EC2 pricing to account for the dedicated physical infrastructure, making them more expensive rather than cheaper than standard purchasing options.

## clf-c02/domain4/q139

Answer: A

The AWS Pricing Calculator allows customers to model AWS service configurations and estimate costs, enabling comparison with on-premises infrastructure spending to produce detailed reports on projected savings from migration.
AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns with forecasting capability, and requires active AWS usage data to generate analysis rather than providing pre-migration cost estimates. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost monitoring and governance tool rather than a migration savings estimation service. AWS Migration Hub provides a centralized location for tracking the progress of application migrations, and is a migration tracking service rather than a cost estimation tool.

## clf-c02/domain4/q142

Answer: D

AWS Basic Support includes access to AWS documentation, whitepapers, and community Discussion Forums where other users and AWS staff may respond to questions. TAMs are Enterprise-only; Senior Support Engineers are Business and Enterprise-only; Trusted Advisor is limited to basic checks on the free plan.
AWS Senior Support Engineers are Cloud Support Engineers who provide technical assistance and are accessible to Business and Enterprise Support customers, and are not available to Basic Support plan holders. AWS Technical Account Managers are dedicated support professionals exclusive to Enterprise Support customers, and are not included in any lower-tier support plan. AWS Trusted Advisor is available to Basic Support customers but only for the seven core checks, rather than the full suite of checks that requires Business or Enterprise Support.

## clf-c02/domain4/q145

Answer: D

Spot Instances are ideal for flexible, interruptible workloads that can tolerate being interrupted when capacity is reclaimed. High-availability services, production websites, and legacy databases all require consistent availability that Spot Instances cannot guarantee.
Moving a main production website to AWS requires consistent availability and uptime, as any interruption from a Spot Instance reclamation would result in downtime for end users. An application with a 99.999% uptime SLA requires that instances are always available, which Spot Instances cannot guarantee given that AWS may interrupt them at any time with a two-minute warning. A heavily used legacy database running on-premises requires consistent performance and data availability that Spot Instance interruptions would compromise, making this workload unsuitable for the Spot purchasing model.

## clf-c02/domain4/q152

Answer: C

On-Demand pricing means you pay only for the compute time you actually use, with no upfront costs or long-term commitments. Bidding is a Spot Instance feature; daily rate billing and pre-payment are characteristics of other pricing models.
The ability to bid for a lower hourly cost is a characteristic of Spot Instances, which are priced based on spare EC2 capacity, not a feature of On-Demand pricing which has a fixed rate set by AWS. Paying a daily rate regardless of time used describes a fixed daily pricing model, which is not how On-Demand EC2 works. On-Demand pricing charges per second with a one-minute minimum. Pre-paying for instances to receive a lower hourly rate describes Reserved Instance pricing, where customers commit to one or three years in exchange for discounted rates, not the On-Demand model.

## clf-c02/domain4/q157

Answer: D

For steady-state, non-interruptible workloads running over a three-year period, Reserved Instances offer the largest discount compared to On-Demand. Spot Instances can be interrupted; On-Demand has no discount; Dedicated Instances are for isolation, not cost savings.
Amazon EC2 Spot Instances can be interrupted by AWS with a two-minute warning when spare capacity is reclaimed, making them unsuitable for non-interruptible workloads that must remain available at all times. Amazon EC2 Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options rather than providing cost savings. Amazon EC2 On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a steady-state workload running continuously over three years.

## clf-c02/domain4/q160

Answer: B

AWS Organizations consolidated billing pools Reserved Instance usage across all member accounts, so unused RIs in one account can automatically apply to matching usage in another, reducing costs across the organization.
Amazon EC2 Dedicated Instances run on hardware dedicated to a single customer for isolation and licensing purposes, and have no mechanism for sharing Reserved Instance discounts between accounts. The AWS Cost Explorer tool provides visualisation and analysis of AWS spending and usage patterns, and while it can show RI utilization data it cannot itself enable or facilitate RI sharing between accounts. AWS Budgets lets you set custom cost and usage thresholds and receive alerts, and is a monitoring and governance tool with no capability to share Reserved Instance benefits across accounts.

## clf-c02/domain4/q165

Answer: A

AWS Marketplace is the curated digital catalog where independent software vendors list their products, allowing customers to find, test, buy, and deploy software that runs on AWS.
AWS Service Catalog allows organizations to create and manage approved portfolios of IT products for internal deployment, but does not host third-party software listings from independent vendors. AWS Artifact is a self-service portal for accessing AWS compliance reports and security certifications, not a software discovery or procurement platform. Amazon CloudSearch is a managed search service for adding search functionality to applications and has no role in software vendor listings or procurement.

## clf-c02/domain4/q167

Answer: C

Spot Instance pricing fluctuates in real time based on the available supply of spare EC2 capacity and customer demand, which can result in prices up to 90% lower than On-Demand.
On-Demand Instances are charged at a fixed hourly rate set by AWS based on instance type and region, and the price does not vary based on supply and demand or change in real time. Reserved Instances allow customers to commit to a specific instance type for one or three years in exchange for a fixed discounted rate, and the reserved price is locked at purchase and does not fluctuate based on supply and demand. Convertible Reserved Instances are a type of Reserved Instance that can be exchanged for other Convertible RIs with different attributes, and like Standard RIs they are priced at a fixed discounted rate that does not adjust based on supply and demand.

## clf-c02/domain4/q176

Answer: D

AWS leverages economies of scale and a shared infrastructure model to deliver lower variable costs per unit than traditional or virtualized data centers, and its pay-as-you-go model eliminates large upfront capital costs, resulting in both lower variable costs and lower upfront costs.
Greater variable costs and greater upfront costs describes the opposite of the AWS model, which specifically reduces both variable costs through economies of scale and eliminates upfront capital expenditure through pay-as-you-go pricing. Fixed usage costs and lower upfront costs partially describes AWS in that upfront costs are lower, but AWS costs are variable rather than fixed since they scale directly with usage and resource consumption. Lower variable costs and greater upfront costs partially describes the traditional data center model where purchasing hardware requires large upfront investment, but on AWS there are no significant upfront costs as infrastructure is consumed as a service.

## clf-c02/domain4/q180

Answer: C

The AWS Pricing Calculator allows customers to model AWS service configurations and estimate future costs before deploying them, making it the purpose-built tool for forecasting the cost of a new application.
Amazon Aurora Backtrack is a feature that allows an Aurora database to be rewound to a previous point in time without restoring from a backup, and is a database recovery feature with no connection to cost forecasting. Amazon CloudWatch Billing Alarms trigger notifications when actual AWS spending exceeds a defined threshold, and are a cost alerting tool for active workloads rather than a forecasting tool for new applications. AWS Cost and Usage Reports provide the most detailed breakdown of actual AWS charges already incurred, and are a historical cost analysis tool rather than a future cost estimation service.

## clf-c02/domain4/q193

Answer: A

AWS Organizations provides centralized management of multiple AWS accounts, including consolidated billing and the ability to apply Service Control Policies as security guardrails across all accounts.
AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, but operates at the individual account level and does not provide centralized management of billing or security policies across multiple accounts. IAM User Groups are a collection of IAM users that share the same attached policies within a single AWS account, and operate at the account level rather than providing cross-account billing or policy management. AWS Config continuously tracks and records the configuration of AWS resources to assess compliance and detect changes, but operates at the account level and does not provide cross-account billing management or security policy enforcement across an organization.

## clf-c02/domain4/q198

Answer: A

On-Demand EC2 instances have no start-up fee. You simply pay for the compute time you use with no upfront charges. On-Demand instances follow pay-as-you-go pricing, require no commitments, and Linux instances are billed per second.
There is no start-up fee when launching an On-Demand EC2 instance for the first time. AWS charges only for the compute time the instance runs, with no additional fees for initial provisioning or launch. The AWS pay-as-you-go pricing model for On-Demand instances means you are charged only for the time the instance runs, with no additional start-up fees, fixed monthly charges, or minimum usage requirements. With On-Demand instances there are no longer-term commitments or upfront payments required, allowing you to start and stop instances at any time based on your needs. Linux-based EC2 instances are indeed billed per second based on an hourly rate, with a minimum charge of one full minute, which is an accurate statement and not the incorrect one the question asks you to identify.

## clf-c02/domain4/q201

Answer: C

Infrastructure Event Management is an Enterprise Support feature that provides architectural guidance and real-time support during planned events such as product launches and traffic spikes.
AWS Knowledge Center is a publicly accessible library of frequently asked questions and solutions for common AWS issues and use cases, and is a self-service resource rather than a dedicated program that provides personalized architectural guidance during high-traffic events. AWS Health Dashboard sends proactive personalized alerts about AWS events that may affect your resources and provides remediation guidance, but is a monitoring and alerting tool rather than a program for receiving architectural guidance during a planned product launch. AWS Support Concierge Service is available to Enterprise Support customers as a dedicated resource for billing and account inquiries, and does not provide architectural guidance or scaling support for planned traffic events.

## clf-c02/domain4/q214

Answer: B

EC2 Dedicated Hosts provide a physical server dedicated entirely to your use with visibility into sockets and cores, which is required to bring existing per-socket or per-core software licenses under the BYOL model.
Dedicated Instances run on hardware dedicated to a single customer but do not provide visibility into the specific physical host, including socket and core counts, which is required for most per-socket or per-core licensing models. On-Demand Instances are charged at the standard hourly rate on shared infrastructure with full hardware multi-tenancy, and do not provide the physical server dedication or host-level visibility required for any meaningful BYOL scenario. Reserved Instances are a pricing commitment that reduces costs over a one or three-year term, but like On-Demand Instances they run on standard shared infrastructure and do not provide the host-level visibility needed for server-bound software licensing.

## clf-c02/domain4/q234

Answer: A

EC2 Auto Scaling ensures you run only the capacity you need, scaling in during low demand and out during high demand, which directly reduces costs by eliminating over-provisioning.
Using the AWS Network Load Balancer to load balance incoming HTTP requests distributes traffic across instances to improve availability and performance, but does not change the number of running instances or address the underlying cost of over-provisioned capacity. Removing all Cost Allocation Tags reduces billing visibility and the ability to attribute costs to specific projects or teams, but has no effect on the actual AWS charges being incurred. Deploying AWS resources across multiple Availability Zones improves resilience by distributing workloads across separate failure domains, but typically increases costs by running additional redundant resources rather than reducing monthly charges.

## clf-c02/domain4/q240

Answer: A

APN Consulting Partners are professional services firms certified by AWS to design, build, and manage customer workloads on AWS, including solutions that help other customers improve their architectures.
AWS TAM is a Technical Account Manager, which is a direct AWS resource assigned to enterprise support customers rather than an independent partner program a company can join to offer consulting services. APN Technology Partners are companies that provide software products and solutions that run on or integrate with AWS, rather than consulting or professional services that help customers improve their architectures. AWS Professional Services is a global team of AWS experts that works directly with customers on their own projects, and is not a program that external companies can join to deliver services to other customers.

## clf-c02/domain4/q245

Answer: D

The AWS pricing construct for committing to EC2 usage over one or three years in exchange for reduced rates aligns with the principle of 'Save when you reserve.'
'Pay less as AWS grows' refers to the long-term pricing principle where AWS passes economies of scale savings to customers over time as AWS infrastructure expands, rather than describing a specific payment model tied to individual usage commitments. 'Pay as you go' describes the On-Demand pricing model where customers pay only for the resources they consume with no upfront commitment, rather than a model involving a one or three-year term commitment. 'Pay less by using more' describes volume discounts where per-unit costs decrease as total usage increases, such as the tiered pricing on Amazon S3, rather than savings derived from making a time-based usage commitment.

## clf-c02/domain4/q246

Answer: A

Right-sizing, choosing the most appropriate instance type and size for your actual workload, both before migration and after based on real usage, is the most effective way to minimize RDS costs without sacrificing performance.
Using a Multi-Region Active-Passive architecture distributes a workload across two Regions where one serves as a standby for disaster recovery, which increases infrastructure costs by running resources in a second Region rather than minimizing them. Combining On-Demand Capacity Reservations with Savings Plans can reduce EC2 costs for specific use cases but adds billing complexity and is not the primary lever for minimizing RDS costs. Using a Multi-Region Active-Active architecture runs the full workload simultaneously across multiple Regions to serve users with low latency globally, which significantly increases costs rather than minimizing them.

## clf-c02/domain4/q260

Answer: B

For a three-year database commitment, Reserved Instances with Partial Upfront payment offers the best balance of discount depth and manageable cash flow, providing a deeper discount than No Upfront while avoiding the full capital outlay of All Upfront payment.
Reserved Instances with No Upfront payment still provide a discount over On-Demand for a three-year commitment, but the discount is shallower than Partial or All Upfront options because AWS does not receive any payment at the start of the term. On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a steady-state workload running for three years. Spot Instances are not available for Amazon RDS, as RDS is a fully managed database service that does not support the Spot purchasing model.

## clf-c02/domain4/q262

Answer: D, E

AWS Savings Plans are flexible pricing models available for Amazon EC2 and AWS Lambda, offering savings over On-Demand in exchange for a one or three-year usage commitment.
AWS Batch is a managed service for running batch computing workloads at scale, and while it can use EC2 instances that may be covered by Savings Plans, AWS Batch itself as a service is not directly covered by a Savings Plan commitment. AWS Outposts extends AWS infrastructure to customer on-premises environments, and workloads running on Outposts are not covered by Compute Savings Plans in the same way as standard AWS Region deployments. Amazon Lightsail is a simplified compute service with straightforward bundled pricing for virtual servers and web applications, and is not covered by AWS Savings Plans.

## clf-c02/domain4/q264

Answer: A, D

AWS service limits (quotas) apply at the account level and can be increased by submitting a support request to AWS. AWS Trusted Advisor monitors current usage against service limits and alerts you when you approach them.
Service limits apply to the entire AWS account rather than to individual IAM users, so each IAM user does not have their own separate service limit. AWS does impose service limits on all accounts by default, so the claim that there are no service limits is factually incorrect. Amazon Simple Email Service is an email sending service for transactional and marketing communications, and is not responsible for monitoring or sending notifications about service limit usage.

## clf-c02/domain4/q272

Answer: A

Linux-based EC2 instances are billed per second of actual usage, with a minimum charge of one full minute. This granular billing model means short-lived workloads are not over-charged.
Billing on one-hour increments with a daily minimum was the original EC2 billing model before per-second billing was introduced, and significantly over-charges short-lived workloads compared to the current per-second model. Billing on one-minute increments with an hourly minimum would over-charge instances running for less than an hour and is not the current billing model for Linux EC2 instances. Billing on a daily increment with a monthly minimum describes a model that does not exist for EC2 instances and would make short-duration workloads prohibitively expensive compared to the actual per-second billing that applies.

## clf-c02/domain4/q273

Answer: A, B

The EC2 instance type determines the base rate, and the Availability Zone where the instance is provisioned can affect pricing because Spot Instance prices vary by AZ and some On-Demand regional prices differ.
Load balancing distributes incoming traffic across multiple EC2 instances to improve availability, and while Elastic Load Balancers incur their own separate charges, the use of load balancing does not affect the price of the EC2 instances themselves. The number of S3 buckets you have does not affect EC2 instance pricing in any way, as S3 storage costs are calculated separately based on stored data volume and storage class. The number of private IP addresses assigned to an EC2 instance does not affect its pricing, as private IP addresses within a VPC are provided at no additional cost.

## clf-c02/domain4/q275

Answer: B

Service Control Policies in AWS Organizations are permission guardrails applied to accounts or organizational units that restrict which AWS services and actions are available within those accounts, even for root users.
IAM Principals are the entities such as users, roles, and groups that IAM policies are attached to, and are components of the identity and access management system within a single account rather than a mechanism for restricting services and actions across multiple accounts. IAM policies define permissions for users, groups, and roles within an individual AWS account, and while they control access within an account they cannot enforce restrictions that apply across multiple accounts in an AWS Organization the way SCPs can. AWS Fargate is a serverless compute engine for running containers that abstracts the underlying infrastructure management, and is a compute service with no connection to account-level governance or cross-account service restriction.

## clf-c02/domain4/q279

Answer: D

AWS Business Support is the minimum plan that includes 24/7 phone and chat access to Cloud Support Engineers, with a one-hour response SLA for production system-down cases.
Enterprise Support also provides 24/7 phone and chat access to Cloud Support Engineers but is a higher-tier plan than Business Support, making it not the minimum level that satisfies this requirement. Developer Support provides email access to Cloud Support Engineers during business hours only, and does not include 24/7 phone or chat access. Basic Support provides access to documentation, whitepapers, and AWS Trusted Advisor core checks but includes no technical case support or access to Cloud Support Engineers.

## clf-c02/domain4/q281

Answer: B

Spot Instances are ideal for workloads that are fault-tolerant and can handle interruptions, such as media transcoding, which can checkpoint and resume. Since the application is designed to recover quickly from hardware failures, it tolerates interruptions, making Spot Instances the most cost-effective choice.
Reserved Instances provide a significant discount over On-Demand pricing for steady-state workloads through a one or three-year commitment, but are not the most cost-effective option for a fault-tolerant application that qualifies for the deeper discounts available through Spot pricing. On-Demand Instances charge the full hourly rate with no discount, making them significantly more expensive than Spot Instances for a batch workload where cost minimization is the primary goal and interruptions are acceptable. Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options rather than providing cost savings for a fault-tolerant processing workload.

## clf-c02/domain4/q286

Answer: A

AWS Trusted Advisor continuously analyzes your AWS environment and provides specific cost-optimization recommendations such as identifying underutilized EC2 instances, idle load balancers, and unattached EBS volumes.
The AWS Pricing Calculator estimates future costs for new AWS service configurations before provisioning them, and is a planning tool for forecasting spend rather than a service that analyzes existing infrastructure to identify cost-saving opportunities. Amazon QuickSight is a serverless business intelligence service for creating interactive dashboards and visualisations from business data, and has no capability to analyze AWS infrastructure usage or generate cost-optimization recommendations. AWS X-Ray is a distributed tracing service that analyzes and debugs the performance of applications by mapping requests as they flow through application components, and is a performance analysis tool with no cost-optimization or infrastructure analysis capability.

## clf-c02/domain4/q288

Answer: B, D

Reserved Instances require a minimum one-year commitment, which is the primary drawback for teams that need flexibility. The key benefit is a significant discount compared to On-Demand pricing.
Instances being shut down by AWS at any time without notification is a characteristic of Spot Instances, which can be interrupted when AWS reclaims spare capacity, rather than Reserved Instances which continue running based on the customer's control. There is an additional charge for using Dedicated Instances, which run on hardware dedicated to a single customer and are priced at a premium over standard EC2 options, so the claim that there is no additional charge is incorrect. Reserved Instances are best suited for steady-state workloads that run continuously or predictably rather than periodic workloads, because the commitment is for consistent capacity and the discount does not scale down when the instance is not running.

## clf-c02/domain4/q290

Answer: A

For a workload that must always be available but only for two months, On-Demand Instances are the best choice as you pay only for the compute time you use with no long-term commitment, and the short duration does not justify the minimum one-year Reserved Instance term.
Spot Instances can be interrupted by AWS when spare capacity is reclaimed, directly violating the requirement that instances must always be available. Reserved Instances with All Upfront payment require a minimum one-year commitment, which would cost significantly more over just two months than paying On-Demand for that period. Reserved Instances with No Upfront payment also require a minimum one-year commitment, making the total cost over the commitment term far exceed the two-month requirement.

## clf-c02/domain4/q297

Answer: C

EC2 Dedicated Instances run on hardware that is physically isolated at the host level and is not shared with any other AWS customer account, meeting the physical isolation requirement.
On-demand instances run on shared hardware and are billed by the second with no upfront commitment, but do not provide any physical isolation from other AWS customers. Spot instances run on shared spare AWS capacity at discounted rates and offer no hardware isolation or tenancy guarantees. Reserved Instances are a billing and pricing model that offers discounted rates in exchange for a usage commitment, not a tenancy type, and do not guarantee dedicated hardware.

## clf-c02/domain4/q301

Answer: C

The AWS Support Concierge is a dedicated billing and account expert team available exclusively to Enterprise Support customers, providing personalized guidance on billing inquiries and account best practices.
Business Support provides 24/7 access to Cloud Support Engineers for technical issues and includes Infrastructure Event Management for an additional fee, but does not include the dedicated Concierge team for billing and account guidance that is exclusive to Enterprise Support. Developer Support provides business-hours email access to Cloud Support Engineers for general technical questions, and does not include billing specialists or dedicated account management resources. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and includes no dedicated support personnel or specialized billing assistance.

## clf-c02/domain4/q309

Answer: C

AWS Budgets lets you set custom utilization thresholds for Reserved Instances and sends alert notifications when utilization drops below your defined level, helping you identify and address underutilized reservations.
Adding all AWS accounts to an AWS Organization and enabling consolidated billing allows Reserved Instance benefits to be shared across accounts, but turning off Reserved Instance sharing would prevent that benefit rather than helping track underutilized reservations. Amazon Neptune is a fully managed graph database service for applications that work with highly connected datasets, and has no capability to track Reserved Instance usage, detect underutilization, or facilitate resale on the RI Marketplace. AWS CloudTrail records API calls and account activity across an AWS environment for auditing and compliance purposes, and does not analyze Reserved Instance utilization or generate billing reduction recommendations.

## clf-c02/domain4/q314

Answer: C

AWS Cost and Usage Reports provide the most granular data available about AWS costs, breaking down charges by hour, service, resource, and tags for detailed analysis and auditing.
An Amazon Machine Image is a template containing the software configuration required to launch an EC2 instance, and has no connection to cost analysis or billing data. AWS Cost Explorer provides interactive visualisations of AWS spending patterns over time and supports filtering by service, account, tag, and time period, but provides less granular data than the Cost and Usage Report which includes hourly resource-level detail. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and while it can monitor some billing metrics it does not provide the detailed cost and usage breakdown that the Cost and Usage Report delivers.

## clf-c02/domain4/q318

Answer: A, E

Tags are key-value metadata pairs that let you quickly identify which resources belong to specific projects and track AWS spending across those resources for cost allocation and organizational clarity.
Quickly identifying software solutions on AWS describes browsing AWS Marketplace, which is unrelated to tagging resources within an account. Tracking API calls in an AWS account describes the function of AWS CloudTrail, which logs account activity rather than organizing resources by metadata. Quickly identifying deleted resources and their metadata is not a function of tagging, as tags are attached to existing resources and are removed when resources are deleted.

## clf-c02/domain4/q328

Answer: B

AWS Migration Evaluator helps organizations compare the cost of running workloads on-premises versus on AWS, factoring in infrastructure, labor, and operational expenses to support a migration business case.
AWS Cost Explorer is used to visualise and analyze spending on existing AWS usage, not to compare on-premises costs against AWS before migration. AWS Budgets is used to set spending thresholds and receive alerts on existing AWS accounts, not to evaluate migration cost savings. The AWS Pricing Calculator estimates monthly costs for a planned AWS architecture but does not compare those costs against on-premises infrastructure to produce a cost-benefit analysis.

## clf-c02/domain4/q334

Answer: B

Deleting unused Auto Scaling launch configurations does not generate AWS charges, so it is not a cost-saving practice. In contrast, unused EBS volumes, Elastic Load Balancers, and Elastic IPs all incur ongoing charges that should be cleaned up.
Deleting unused EBS volumes after terminating an EC2 instance is a recommended cost-saving practice because EBS volumes continue to incur storage charges even when no instance is attached to them. Deleting unused Elastic Load Balancers is a recommended cost-saving practice because load balancers incur an hourly charge regardless of whether they are serving traffic. Releasing unused Elastic IP addresses after terminating an EC2 instance is a recommended cost-saving practice because AWS charges for Elastic IPs that are allocated but not associated with a running instance.

## clf-c02/domain4/q335

Answer: A

AWS Cost Explorer provides interactive visualisations of AWS spending over time, allowing you to filter by service, account, tag, or time period to identify spending trends and anomalies across recent months.
The AWS Pricing Calculator estimates future costs for AWS services before you use them, and does not provide visualisation of historical spending. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a proactive cost governance tool rather than a historical spending visualisation service. AWS Organizations provides centralized management of multiple AWS accounts including consolidated billing and the ability to apply Service Control Policies, but does not itself provide visualisation of spending patterns.

## clf-c02/domain4/q339

Answer: C

Amazon EC2 offers per-second billing with a one-minute minimum, so customers pay only for the exact compute time they use rather than rounding up to the nearest hour, directly reducing costs.
Low monthly instance maintenance costs is not an AWS cost reduction benefit, as maintenance of the underlying physical infrastructure is AWS's responsibility under the shared responsibility model and is included in the standard pricing. Low-cost instance tagging refers to the use of resource tags for cost allocation, and while tags are free to apply they are a cost visibility mechanism rather than a mechanism that reduces the price of running EC2 instances. Low instance start-up fees is a fabricated pricing concept. Amazon EC2 On-Demand instances have no start-up fee and charge only for the time the instance runs.

## clf-c02/domain4/q340

Answer: B

AWS Professional Services is a team of experts that works directly with customers to help them achieve their desired business outcomes through cloud strategy, architecture guidance, and migration support.
The AWS Security Team manages AWS's own internal security posture and the responsible disclosure program for AWS infrastructure, and is not a customer-facing team that works with customers to achieve business outcomes on AWS. AWS Trusted Advisor inspects your AWS environment and provides automated recommendations across security, cost, performance, and fault tolerance, and is a self-service advisory tool rather than a professional services team that works directly with customers. The AWS Concierge Support Team is available to Enterprise Support customers for billing and account inquiries, providing dedicated account guidance rather than strategic business outcome or cloud migration support.

## clf-c02/domain4/q344

Answer: A

The All Upfront payment option for Reserved Instances provides the largest discount because you pay the entire term cost at the beginning, earning you the maximum savings.
All Reserved Instance payment options do not provide the same discount level. The three options, All Upfront, Partial Upfront, and No Upfront, each provide progressively lower discounts as the amount paid upfront decreases. Partial Upfront reservation splits the payment between an initial upfront amount and lower monthly fees, providing a moderate discount that is greater than No Upfront but less than All Upfront. No Upfront reservation provides the lowest discount among the three RI payment options because no initial payment is made, meaning AWS offers less incentive than with Partial or All Upfront options.

## clf-c02/domain4/q346

Answer: C

Amazon Linux instances are billed per second with a one-minute minimum, so 2 hours, 5 minutes, and 9 seconds is the exact billable time. CentOS instances on the AWS Marketplace are billed per hour rounded up, resulting in 5 hours.
Billing both instances at rounded-up hour increments would apply the old hourly billing model to the Linux instance, which would result in 3 hours rather than the exact per-second duration. Billing both instances at exact per-second precision would incorrectly apply the Linux per-second billing model to the CentOS instance, which is billed per hour rounded up. Billing the Linux instance at rounded-up hours and the CentOS at exact seconds reverses the correct billing models for each instance type.

## clf-c02/domain4/q347

Answer: C

The AWS Support API allows customers to create, update, and resolve support cases programmatically, enabling integration with internal ticketing systems and automated incident workflows.
AWS Trusted Advisor inspects your AWS environment and provides automated recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than a feature for managing support cases programmatically. AWS Operations Support is not a recognized AWS service or support feature name. AWS Health Dashboard provides a personalized view of AWS service events affecting your resources along with remediation guidance, and is an observability tool rather than a programmatic interface for managing support cases.

## clf-c02/domain4/q356

Answer: B

Amazon S3 uses a tiered pricing model where the per-GB storage cost decreases as your total usage increases, automatically providing volume discounts to customers who store more data.
Amazon VPC is a networking service that lets you provision isolated virtual networks within AWS, and while VPC itself is free the resources deployed within it such as NAT Gateways are charged individually without volume-based discounts. Amazon Lightsail is a simplified compute service with straightforward bundled pricing for virtual servers and web applications, and uses fixed pricing tiers rather than volume discounts based on usage. AWS Cost Explorer provides visualisation and analysis of AWS spending patterns over time, and is a cost management tool rather than an AWS service that applies volume-based pricing discounts.

## clf-c02/domain4/q360

Answer: C

AWS continuously reduces pricing as it achieves greater economies of scale, passing savings to customers, which widens the total cost of ownership gap compared to traditional on-premises infrastructure.
AWS does not help customers invest more in capital expenditures. On the contrary, AWS shifts infrastructure spending from capital expenditure to operational expenditure, reducing the need for large upfront hardware investments. AWS automates many infrastructure tasks through managed services and orchestration tools, but customers still incur human resources costs for cloud engineers and architects, and AWS does not eliminate all infrastructure operations requiring staff. AWS does secure its own infrastructure at no additional charge as part of its responsibilities under the shared responsibility model, but this has always been the case and is not the primary reason the TCO gap has widened over time.

## clf-c02/domain4/q364

Answer: B, D

Security groups and Hosted Zones do not factor into EC2 pricing. EC2 costs are determined by instance type, running time, number of instances, storage, and data transfer.
The amount of time instances will be running directly affects EC2 costs, as Linux instances are billed per second and all instances stop accruing compute charges only when stopped or terminated. Allocated Elastic IP addresses incur charges when they are allocated but not associated with a running instance, and are a cost associated with EC2 deployments that must be considered when estimating total costs. The number of EC2 instances directly determines the scale of compute costs, as each running instance accrues charges based on its type and running time.

## clf-c02/domain4/q370

Answer: D

For a Production System Down case on the Business or Enterprise Support plan, the expected response time is one hour, ensuring critical production outages receive rapid attention from AWS Support.
A 12-hour response time corresponds to the general guidance response target for Developer Support customers on a system-impaired case, not the production system-down response time for Business or Enterprise Support. A 15-minute response time is the SLA for business-critical system failures under the Enterprise Support plan, which is a faster tier than the one-hour production system-down SLA available starting at Business Support. A 24-hour response time is the general guidance response target for Developer Support customers on general guidance cases, and does not apply to production system outages at the Business or Enterprise Support level.

## clf-c02/domain4/q373

Answer: D

AWS Enterprise Support provides a 15-minute response time for business-critical system-down cases, which is the fastest response SLA available across all AWS Support plans.
AWS Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and includes no technical case support or any defined response time SLA for system failures. AWS Developer Support provides email access to Cloud Support Engineers during business hours with response times measured in hours rather than minutes, and does not include 24/7 access or a 15-minute response SLA. AWS Business Support provides 24/7 access to Cloud Support Engineers with a one-hour response SLA for production system-down cases, which does not meet the requirement for a response within 15 minutes.

## clf-c02/domain4/q379

Answer: D

For steady-state workloads with continual utilization throughout the year, Reserved Instances provide significant discounts over On-Demand pricing in exchange for a 1 or 3-year commitment, making them the most cost-effective option.
On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a web application that uses compute capacity continuously throughout the year. Dedicated Hosts provide a physical server dedicated entirely to a single customer for compliance and licensing purposes, and are priced at a premium over standard EC2 options rather than providing cost savings for a standard continuously running web application. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, making them unsuitable for a production web application that requires continual availability throughout the year.

## clf-c02/domain4/q382

Answer: B

AWS supports Bring Your Own License, allowing customers to reuse existing third-party software licenses on AWS, which avoids paying for new licenses and reduces migration costs.
Using servers instead of managed services typically increases operational costs by requiring customers to manage and maintain the underlying operating systems, databases, and software, rather than reducing them through the efficiency of AWS managed services. Migrating production workloads to AWS edge locations instead of AWS Regions is not a valid migration strategy, as edge locations are designed for content caching and delivery rather than hosting production compute workloads. Using AWS Outposts to run all workloads does not save migration costs, as Outposts are designed for workloads that must remain on-premises due to latency or data residency requirements, and involve additional costs for dedicated AWS-managed hardware in the customer's facility.

## clf-c02/domain4/q386

Answer: B

AWS Pricing Calculator lets you estimate costs for AWS services before you use them, allowing you to model configurations for S3 storage and CloudFront distribution to forecast monthly expenses.
AWS Cost Explorer provides visualisation and analysis of existing AWS spending patterns over time and requires active usage data to generate analysis rather than providing pre-deployment cost estimates for services not yet in use. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a service for estimating future costs before deploying new services. The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a cost estimation service for planned deployments.

## clf-c02/domain4/q394

Answer: A, C

The Business Support plan includes 24/7 access to customer service via phone, chat, and email, and access to Infrastructure Event Management for an additional fee to support planned events like launches.
Access to Cloud Support Engineers via email only during business hours is a feature of the Developer Support plan, not Business Support, which provides 24/7 access via phone, email, and chat. 24/7 access to a dedicated Technical Account Manager is an Enterprise Support feature and is not included in the Business Support plan. Partial access to the core Trusted Advisor checks is incorrect because Business Support customers have access to the full suite of Trusted Advisor checks, not just the seven core checks that Basic and Developer Support customers receive.

## clf-c02/domain4/q402

Answer: C

EC2 Spot Instances offer up to 90% discounts by using spare AWS capacity, making them the most cost-effective option for workloads that are flexible on timing and can tolerate interruptions, like batch image and video processing.
EC2 On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for this type of flexible, non-time-critical batch workload. EC2 Reserved Instances with No Upfront payment provide a discount for steady-state workloads over a 1 or 3-year commitment, but are not cost-effective for workloads that run only periodically and do not require continuous capacity. EC2 Reserved Instances with All Upfront payment provide the deepest Reserved Instance discount through full prepayment, but require a long-term commitment and are not the most cost-effective option for periodic workloads that qualify for Spot pricing.

## clf-c02/domain4/q411

Answer: D

AWS Cost Explorer uses historical spending data to generate highly accurate cost forecasts for up to 12 months ahead, helping organizations plan budgets and anticipate future AWS spending.
Cost comparisons between AWS Cloud environments and on-premises environments are produced by the AWS Pricing Calculator, which allows customers to model AWS configurations and compare projected costs against on-premises infrastructure spending. Accurate estimates of AWS service costs based on expected usage are produced by the AWS Pricing Calculator, which is designed for pre-deployment cost modeling rather than analyzing historical usage. Consolidated billing is a feature of AWS Organizations that combines usage and invoices from multiple accounts into a single bill, and is not a capability of AWS Cost Explorer.

## clf-c02/domain4/q413

Answer: D

Stopping On-Demand EC2 instances halts compute charges while preserving the instance and its EBS volumes, so you can restart later without losing your configuration or data.
Deleting all EBS volumes attached to the instances would destroy all data stored on those volumes, which is an irreversible action that eliminates your development environment rather than simply reducing charges while it is not in use. On-Demand instances can be stopped to reduce charges, so the claim that charges cannot be minimized is incorrect. Stopping an instance is the recommended approach for development environments that are used intermittently. Terminating the instances permanently destroys them along with any instance store data, and while it does stop all charges it is an irreversible action that would require rebuilding the development environment from scratch.

## clf-c02/domain4/q415

Answer: A, C

Amazon EBS pricing is based on the size of provisioned volumes per gigabyte per month and the amount of data stored in EBS snapshots, which are incremental backups stored in Amazon S3 and billed separately.
The compute capacity you consume is an EC2 pricing factor based on instance type and size, not an EBS pricing factor. Compute time is billed through EC2 instance pricing rather than EBS volume pricing, which charges for provisioned storage regardless of whether the instance is running. The number of AWS Snowball devices requested affects Snow Family pricing and is entirely unrelated to Amazon EBS volume or snapshot costs.

## clf-c02/domain4/q417

Answer: A, D

Compute charges and Data Transfer Out charges are typically the two largest cost drivers in AWS. Data Transfer In is free, and IAM roles have no associated cost.
The number of AWS services used does not directly determine cost impact. A single heavily used service can cost far more than dozens of lightly used services, so cost impact is driven by usage and pricing rates rather than the count of services consumed. Data Transfer In charges to AWS are free for all data ingested into the AWS network from the internet or from on-premises environments, making inbound data transfer one of the few cost components that does not contribute to the bill. The number of IAM roles provisioned incurs no charges. IAM roles are free to create and there is no per-role cost, so provisioning additional roles has no impact on your AWS bill.

## clf-c02/domain4/q418

Answer: D

Reserved, Standard, All Upfront instances provide the deepest discount because Standard RIs offer larger savings than Convertible RIs, and paying everything upfront gives the maximum reduction over partial or no upfront options.
On-Demand, Convertible, Partial Upfront is not a valid purchasing combination as On-Demand instances do not have Convertible or upfront payment options. On-Demand pricing simply charges for compute time used with no commitment. Reserved, Convertible, All Upfront provides a meaningful discount through a long-term commitment with full prepayment, but Convertible RIs offer less discount than Standard RIs in exchange for the flexibility to exchange attributes. Reserved, Standard, No Upfront provides a discount through the long-term commitment of Standard RIs but without any upfront payment, which yields a smaller total discount than options that include upfront payment.

## clf-c02/domain4/q419

Answer: D

Reserved Instances allow you to pay upfront in exchange for lower hourly rates over a 1 or 3-year term, providing predictable savings for steady-state workloads.
The ability to bid for a lower hourly cost describes Spot Instances, which are priced based on spare EC2 capacity through a market-based mechanism rather than a commitment-based model. The ability to register EC2 instances to get volume discounts on every hour they are running is not a real EC2 purchasing option. Volume discounts in AWS apply through mechanisms such as consolidated billing or S3 storage tiers rather than through instance registration. The ability to buy Dedicated Instances for up to 90% discount is incorrect on two counts: Dedicated Instances are priced at a premium rather than a discount, and the 90% discount figure applies to Spot Instances rather than Dedicated Instances.

## clf-c02/domain4/q423

Answer: D

AWS Migration Evaluator is designed specifically for organizations comparing on-premises costs to AWS, providing a detailed cost-benefit analysis even before they have an AWS account.
AWS Cost Explorer is used to visualise and analyze spending patterns on existing AWS accounts, and requires an active AWS account to use. AWS Pricing Calculator estimates monthly costs for a planned AWS architecture but does not compare those costs against on-premises infrastructure. AWS Budgets is used to set spending thresholds and receive alerts on an existing AWS account, and has no capability to evaluate migration cost savings.

## clf-c02/domain4/q430

Answer: C

Chat support is available starting from the Business Support plan, so upgrading to at least Business tier is the minimum requirement to access the chat feature in the AWS Support Center.
AWS support does have a chat feature, but it is only available on Business and Enterprise plans, making this option factually incorrect. The chat feature is not available as an add-on for an additional fee on lower-tier plans, as it is an included feature of the Business and Enterprise support tiers only. The Developer Support plan provides access to AWS Support engineers via email only, and upgrading from Basic to Developer does not unlock the chat feature.

## clf-c02/domain4/q432

Answer: D

The Pay-As-You-Go model replaces large upfront capital expenses with low variable payments based on actual consumption, so you only pay for the resources you use.
Replacing low upfront expenses with large variable payments inverts the AWS pricing model, which specifically eliminates large upfront capital costs rather than introducing new large variable costs. Replacing low upfront expenses with large fixed payments describes neither the on-premises nor the AWS model accurately. On-premises typically has large upfront expenses, and AWS replaces those with low variable costs rather than fixed ones. Replacing large upfront expenses with low fixed payments partially captures the idea of reducing upfront costs, but AWS pricing is variable rather than fixed, scaling directly with actual resource consumption.

## clf-c02/domain4/q434

Answer: A

Using tags to group and label AWS resources by project, department, or environment enables detailed cost analysis and allocation through AWS Cost Explorer and Cost and Usage Reports.
Using AWS CloudFormation to automate the deployment of resources improves operational efficiency and repeatability, but automating deployments does not itself provide visibility into how costs are distributed across different parts of the organization. Deploying resources of the same type in different regions may be necessary for latency or compliance reasons, but distributing resources geographically does not help analyze which projects or teams are driving specific costs without tags to identify resource ownership. Configuring Amazon Inspector to automatically analyze costs is incorrect because Amazon Inspector is an automated security assessment service that scans for software vulnerabilities and unintended network exposure, and has no capability to analyze AWS costs or generate billing reports.

## clf-c02/domain4/q445

Answer: C, E

S3 pricing depends on the storage class used and the total size of all objects stored. Creating buckets, using encryption, and EBS volumes do not affect S3 storage charges.
Using default encryption for S3 buckets does not incur additional S3 storage charges. Server-side encryption with S3-managed keys is provided at no extra cost, and encrypting objects does not increase the storage charge beyond the standard price for the storage class used. The number of EBS volumes attached to your EC2 instances is a separate billing item for block storage and has no effect on S3 object storage charges. Creating and deleting S3 buckets does not incur any charges. AWS does not charge for the creation, management, or deletion of S3 buckets themselves, only for the data stored within them and requests made against them.

## clf-c02/domain4/q448

Answer: A

The AWS Cost and Usage Report provides the most comprehensive view of your actual AWS costs, breaking down charges by service, resource, and time period so you can see exactly what you are being charged for.
AWS Cost Explorer provides interactive visualisations and analysis of AWS spending patterns over time and is well-suited for exploring costs, but the Cost and Usage Report provides the most granular and complete raw data for detailed cost review. The AWS Pricing Calculator is used to estimate future costs for AWS services before provisioning them, and does not display actual charges already applied to your account. The Amazon VPC dashboard is a networking console for managing virtual private clouds, subnets, and network configuration, and has no connection to cost viewing or billing information.

## clf-c02/domain4/q449

Answer: A, E

Standard Reserved Instances provide the highest discount but are locked to a specific instance family, while Convertible Reserved Instances offer flexibility to change instance types at a slightly lower discount. Both are valid RI types.
Expedited is a retrieval speed option for Amazon S3 Glacier that provides faster access to archived data, and is not a Reserved Instance type. Bulk is also a retrieval tier for Amazon S3 Glacier that provides the lowest-cost but slowest data retrieval, and is not a Reserved Instance type. Spot is a separate EC2 purchasing model that uses spare AWS capacity at significant discounts and can be interrupted by AWS at any time, and is not a type of Reserved Instance.

## clf-c02/domain4/q456

Answer: B

Architecture Optimization involves regularly reviewing and refining workloads to ensure they use the most efficient AWS resource types, sizes, and configurations, directly reducing costs while maintaining performance.
Tagging Enforcement is a cost governance practice that requires resources to be labeled with specific tags before they can be created or used, which improves cost visibility and attribution but is a compliance and visibility mechanism rather than a practice focused on refining workloads to better utilize existing resources. Budgeting Processes involve setting cost and usage thresholds and tracking actual spending against those budgets, which helps manage financial expectations but does not itself involve reviewing and optimizing underlying resource configurations. Resource Controls restrict which resources users can provision or how they can be configured, and while they prevent unnecessary resource creation they are a governance guardrail rather than a practice of regularly reviewing existing workloads.

## clf-c02/domain4/q472

Answer: A, B

Amazon CloudFront pricing is based on the number of requests served and the geographic distribution of traffic, as different edge location regions have different pricing tiers.
The number of EBS volumes attached to EC2 instances is a separate billing item for block storage and has no effect on CloudFront pricing, which is based entirely on content delivery and request activity. The EC2 instance type running your origin servers may affect compute costs, but it does not factor into CloudFront's content delivery pricing, which charges for data transfer out and requests at the edge. The S3 storage class used for objects at the origin affects S3 storage costs but does not directly factor into CloudFront pricing, which is based on the delivery of content to end users.

## clf-c02/domain4/q477

Answer: B

Basic and Developer Support plans provide access to only the seven core Trusted Advisor checks. The full set of Trusted Advisor checks requires a Business or Enterprise Support plan.
Business and Enterprise Support plans both provide access to the full suite of Trusted Advisor checks rather than only the seven core checks, so this option describes the plans with the most Trusted Advisor access rather than those limited to seven checks. Developer and Enterprise Support is an incorrect pairing because Developer Support is limited to the seven core checks while Enterprise Support has access to the full suite, meaning they are at opposite ends of the Trusted Advisor access spectrum. Developer and Business Support is an incorrect pairing because Business Support provides the full suite of Trusted Advisor checks while Developer Support is limited to the seven core checks, so only Developer Support belongs in this limited-access category.

## clf-c02/domain4/q482

Answer: A, E

AWS Organizations enables centralized control over AWS service access using Service Control Policies, and consolidates billing from multiple accounts into a single payment.
Helping organizations design and maintain an accelerated path to successful cloud adoption describes the AWS Cloud Adoption Framework, which is a guidance framework created by AWS Professional Services rather than a capability of AWS Organizations. Managing your organization's payment methods is handled through the AWS Billing and Cost Management console at the individual account level, and is not a specific feature provided by AWS Organizations. Helping organizations achieve their desired business outcomes with AWS describes AWS Professional Services, which works directly with customers on cloud strategy and implementation rather than being a function of AWS Organizations.

## clf-c02/domain4/q484

Answer: C

AWS Marketplace is a digital catalog where customers can find, buy, and deploy third-party software solutions that run on AWS, including AMIs, SaaS applications, and data products.
AWS Application Discovery Service collects information about on-premises servers and workloads to help plan cloud migrations, and is a migration planning tool with no capability to purchase or deploy third-party software. AWS Cost Explorer provides visualisation and analysis of AWS spending and usage patterns over time, and is a cost management tool rather than a software procurement platform. AWS Resource Groups organizes AWS resources into logical groups based on tags or CloudFormation stacks for easier management, and has no role in discovering or purchasing third-party software solutions.

## clf-c02/domain4/q489

Answer: C

The AWS Health Dashboard at status.aws.amazon.com provides real-time and historical information about the availability and operational health of all AWS services across all Regions.
The AWS Billing Dashboard is accessed through the AWS Management Console and displays cost and usage summaries for your account, and is not accessible at the status.aws.amazon.com URL. AWS Cost Explorer is a cost management tool for visualising and analyzing AWS spending patterns over time, and is accessed through the billing section of the AWS Management Console rather than the public status URL. AWS Security Hub provides a centralized view of security alerts and compliance status across an AWS environment, and is a security posture management tool accessed through the AWS Management Console rather than the public status URL.

## clf-c02/domain4/q492

Answer: C

Cost allocation tags are key-value metadata that you apply to AWS resources, enabling you to segment and categorize costs by project, department, or environment in Cost Explorer and billing reports.
The AWS Pricing Calculator is used to estimate future costs for new AWS service configurations before deploying them, and does not monitor or categorize actual spending incurred by active workloads. Amazon Aurora is a fully managed relational database service compatible with MySQL and PostgreSQL, and is a database engine with no capability to forecast AWS spending or categorize costs by department. The AWS Price List API provides programmatic access to AWS service pricing data for building custom pricing tools, and delivers pricing information rather than automatically updating billing categories based on department usage.

## clf-c02/domain4/q495

Answer: B

Adding standalone accounts to an AWS Organization with Consolidated Billing aggregates usage across all accounts, enabling volume discounts through combined usage tiers and simplifying payment through a single bill.
Removing unnecessary AWS accounts may reduce spend but does not unlock volume discounts or address the structural billing inefficiency of running separate accounts. Tracking AWS charges incurred by member accounts is a cost visibility activity and does not reduce charges on its own. AWS tiered pricing is applied automatically based on usage volume and cannot be manually enabled before provisioning resources.

## clf-c02/domain4/q497

Answer: A, D

The Business Support plan provides access to the full set of Trusted Advisor checks across all five categories, and the AWS Support API for programmatic management of support cases.
The Support Concierge Service is available exclusively to Enterprise Support customers for dedicated billing and account guidance, and is not included in the Business Support plan. A response time of less than 15 minutes for business-critical system failures is an Enterprise Support feature. Business Support provides a one-hour response SLA for production system-down cases. Proactive Technical Account Management is an Enterprise Support feature. Business Support does not include a designated Technical Account Manager who provides ongoing proactive guidance.

## clf-c02/domain4/q501

Answer: A, C

AWS pay-as-you-go pricing requires no upfront fees or long-term contracts. You pay only for the individual services you use with no minimum commitments.
Customers do retain responsibility for third-party software license costs when running applications on AWS, unless they use AWS-provided licenses through services such as Amazon RDS. AWS does not take on software licensing obligations on the customer's behalf. For some services AWS does offer a startup fee, and Reserved Instances require upfront payment. However, the pay-as-you-go model for On-Demand services requires no startup fee. AWS does offer reservations such as Reserved Instances and Savings Plans that provide discounts in exchange for usage commitments, so the claim that there are no reservations on AWS is incorrect.

## clf-c02/domain4/q506

Answer: B, E

AWS Lambda pricing is based on the number of requests to your functions and the compute time consumed, measured in GB-seconds of execution duration, with a generous free tier for both dimensions.
Storage consumed is not a Lambda pricing factor in the same way. While Lambda functions have temporary storage available in the execution environment, Lambda pricing is based on requests and compute duration rather than storage consumption. The number of volumes is an Amazon EBS pricing concept for block storage attached to EC2 instances, and has no bearing on how Lambda functions are charged. Placement groups are a feature for controlling how EC2 instances are placed on underlying hardware to optimize network performance or fault tolerance, and are an EC2 concept with no connection to Lambda pricing.

## clf-c02/domain4/q508

Answer: C, D

Deleting unnecessary EBS snapshots removes the storage costs for backups you no longer need, and changing to a more cost-effective volume type such as moving from gp2 to gp3 reduces the per-gigabyte cost for the same capacity.
Deleting unused buckets is an Amazon S3 action that reduces S3 storage costs, but S3 buckets are entirely separate from EBS volumes and deleting them has no effect on EBS pricing. Using reservations is not a pricing mechanism available for EBS volumes. EBS pricing is based on provisioned storage and snapshot data rather than commitment-based reservations. Distributing requests to multiple volumes may improve performance by reducing I/O contention, but spreading data across more volumes increases total provisioned storage and therefore increases rather than reduces EBS costs.

## clf-c02/domain4/q511

Answer: D

AWS tags are key-value metadata pairs attached to resources, making it easy to categorize, filter, search, and manage resources by project, environment, owner, or any other custom criteria.
Amazon CloudWatch is a monitoring and observability service for collecting metrics, logs, and alarms on AWS resources, not a resource categorization or filtering tool. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal deployment, not for tagging or filtering existing resources. AWS Directory Service provides managed Microsoft Active Directory for user authentication and access management, unrelated to resource categorization or metadata management.

## clf-c02/domain4/q515

Answer: C, E

The Business and Enterprise Support plans both provide 24/7 access to Cloud Support Engineers via phone, email, and chat, making them the two plans that meet this requirement.
Developer Support provides email access to Cloud Support Engineers during business hours only, and does not include 24/7 phone or chat access. Premium Support is not a real AWS support plan name. The actual AWS support tiers are Basic, Developer, Business, Enterprise On-Ramp, and Enterprise. Standard Support is not a real AWS support plan name. It does not correspond to any of the five AWS Support plan tiers.

## clf-c02/domain4/q520

Answer: D, E

AWS Marketplace offers flexible pricing options including hourly, monthly, annual, and bring-your-own-license models, and provides software solutions that can run on AWS or other cloud platforms, giving customers broad choice and cost flexibility.
AWS Marketplace does not perform periodic security checks on listed products. Responsibility for product security remains with the independent software vendors who list their products. Per-second billing is an EC2 pricing feature, not a benefit of AWS Marketplace. Providing cheaper options for purchasing EC2 on-demand instances is not a function of AWS Marketplace, which is a catalog for third-party software, not a mechanism for discounting AWS compute pricing.

## clf-c02/domain4/q522

Answer: D

On-Demand Instances are the best choice for short-term, unpredictable workloads where downtime is unacceptable, providing guaranteed availability for the campaign period without any risk of interruption.
Savings Plans provide discounts in exchange for a commitment to a consistent usage level over one or three years, and are designed for steady-state long-term workloads rather than a short-term weekend advertising campaign. Spot Instances use spare AWS capacity at significant discounts but can be interrupted by AWS at any time, making them unsuitable for a campaign where downtime cannot be afforded. Reserved Instances require a minimum one-year commitment, which would cost significantly more over a single weekend than paying On-Demand for that short period.

## clf-c02/domain4/q528

Answer: C, E

On-Demand Instances eliminate the need to pre-purchase safety net capacity for traffic spikes, and let you increase or decrease compute capacity at any time to match application demand.
On-Demand Instances do not provide free capacity for testing. All compute time is charged at the standard On-Demand rate, and there is no free usage tier specifically for testing with On-Demand instances beyond the general AWS free tier. On-Demand Instances are not cheaper than all other EC2 options. Spot Instances offer discounts of up to 90% and Reserved Instances offer up to 72% savings, both significantly cheaper than On-Demand for suitable workloads. On-Demand Instances do not require 1 to 2 days for setup and configuration. They can be launched within minutes through the AWS Management Console, CLI, or API with no lengthy provisioning process.

## clf-c02/domain4/q536

Answer: C

The AWS Cost and Usage Report provides the most granular billing data available, breaking down costs by hour, service, resource, and tags for detailed analysis and auditing.
AWS Cost Explorer provides interactive visualisations of AWS spending patterns over time with filtering and grouping capabilities, and while it is excellent for analysis and forecasting it provides less granular raw data than the Cost and Usage Report. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a granular billing data reporting service. The AWS Billing dashboard provides a high-level summary of your current month's charges and recent billing history, and offers a much less granular view of costs than the detailed hourly and resource-level data in the Cost and Usage Report.

## clf-c02/domain4/q543

Answer: D

AWS Quick Start reference deployments provide automated gold-standard templates that deploy popular IT solutions on AWS in minutes, giving administrators a fast path to production-ready environments built on AWS best practices.
AWS Well-Architected Framework documentation provides architectural guidance and best practices for designing cloud workloads across six pillars, but is a reference document rather than a deployment tool that can provision a solution immediately. Amazon CloudFront is a content delivery network that caches and distributes content to users at edge locations worldwide, and has no capability to deploy or provision IT solutions. AWS CodeCommit is a managed Git-based source control service for storing and versioning code repositories, and is a developer tool with no rapid deployment or solution provisioning capability.

## clf-c02/domain4/q551

Answer: C

AWS forums, blogs, and whitepapers are publicly available security resources that anyone can access at no cost, providing guidance on security best practices, architecture patterns, and compliance considerations.
Calling AWS Support for security-related technical assistance requires at minimum a Developer Support plan, which has an associated monthly fee, making phone and chat support with engineers a paid service rather than a free action. Contacting AWS Professional Services to request a workshop is a paid engagement. AWS Professional Services charges for consulting time and workshop delivery rather than providing these services at no cost. Attending AWS classes at a local university is not an AWS-provided service and incurs academic fees unrelated to AWS pricing. AWS does offer its own training through AWS Training and Certification, but instructor-led courses carry a cost.

## clf-c02/domain4/q566

Answer: A

AWS Billing and Cost Management is the central service for paying AWS bills, monitoring usage, and managing budgets, providing tools including Cost Explorer, Budgets, and billing alerts in one place.
Consolidated billing is a feature of AWS Organizations that combines usage and invoices from multiple accounts into a single bill, and is a billing aggregation feature rather than a standalone service used to pay bills and monitor usage. Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting, and while it can monitor billing metrics it is a monitoring service rather than the primary service for paying bills and managing budgets. Amazon QuickSight is a serverless business intelligence service for creating interactive dashboards and visualisations from business data, and is not used to pay AWS bills or manage AWS account budgets.

## clf-c02/domain4/q568

Answer: B

Consolidated billing through AWS Organizations combines usage across all member accounts, allowing the organization to reach higher volume tiers and qualify for usage-based discounts that individual accounts would not achieve independently.
Service Control Policies are permission guardrails applied through AWS Organizations that restrict which AWS services and actions are available within member accounts, and are a governance mechanism rather than a feature that enables usage tier benefits. All Upfront Reserved Instances are a purchasing commitment where you pay the full cost of the reservation at the start of the term in exchange for the maximum discount, and apply to a single account rather than aggregating usage across multiple accounts. AWS Cost Explorer provides interactive visualisations and analysis of AWS spending patterns over time, and is a cost analysis tool rather than a feature that aggregates usage across accounts to qualify for volume pricing tiers.

## clf-c02/domain4/q582

Answer: C

Creating an AWS Organization from the payer account and inviting other accounts to join enables consolidated billing, centralizing payment under a single invoice while maintaining each department's account independence.
Using AWS Budgets on each account to pay only to budget is a cost governance practice for individual accounts, and does not consolidate the separate payment methods across accounts into a unified billing structure. Contacting AWS Support for a monthly bill is not a self-service mechanism for enabling consolidated billing, which is set up directly through AWS Organizations rather than through a support request. Putting all invoices into an S3 bucket and loading data into Redshift to run a billing report creates a custom reporting solution that provides visibility into costs but does not consolidate the actual billing and payment methods into a single invoice.

## clf-c02/domain4/q591

Answer: B

AWS Organizations with consolidated billing combines usage across all member accounts, allowing the organization to qualify for volume pricing tiers and Reserved Instance sharing that individual accounts cannot achieve alone.
AWS Server Migration Service is a tool for migrating on-premises servers to AWS, and has no connection to combining usage across accounts or obtaining volume discounts. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a service that aggregates usage across accounts for volume discounts. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than a service that combines usage across multiple accounts.

## clf-c02/domain4/q629

Answer: A

AWS Health Dashboard sends proactive personalized alerts when AWS events may impact your specific resources, providing remediation guidance tailored to your account rather than showing general service status.
Amazon CloudWatch collects metrics, logs, and event data from AWS services and resources to provide operational monitoring and alerting for performance and health of your own workloads, but does not send personalized alerts about AWS service-level events that may affect your resources. AWS Trusted Advisor analyzes your AWS environment against best practice checks across cost, performance, security, and fault tolerance, but does not send alerts about AWS service events or infrastructure disruptions. AWS Infrastructure Event Management is a paid support program for planning large-scale events such as product launches, and is not an alerting service for AWS health events affecting your resources.

## clf-c02/domain4/q630

Answer: A, D

AWS Trusted Advisor provides recommendations across five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. Fault Tolerance and Performance are both official categories.
Instance Usage is not a Trusted Advisor category. Usage-related recommendations fall under Cost Optimization rather than a dedicated instance usage category. Infrastructure is not a Trusted Advisor category and does not correspond to any of the five defined recommendation areas. Storage Capacity is not a Trusted Advisor category. Storage-related checks appear within Cost Optimization or Fault Tolerance depending on the nature of the recommendation.

## clf-c02/domain4/q643

Answer: A

Spot Instances are ideal when there is flexibility in when an application needs to run, because they use spare EC2 capacity at discounts of up to 90% and can be interrupted when that capacity is needed elsewhere.
Mission-critical workloads require guaranteed availability and cannot tolerate the interruptions that Spot Instances may experience, making On-Demand or Reserved Instances more appropriate for those use cases. When dedicated capacity is needed, either Dedicated Hosts or Dedicated Instances are appropriate depending on the licensing and compliance requirements, as they provide physical isolation that Spot Instances running on shared infrastructure cannot guarantee. When an instance should not be stopped, Spot Instances are unsuitable because AWS may reclaim Spot capacity at any time with a two-minute warning, making On-Demand or Reserved Instances the correct choice for workloads that must remain continuously active.

## clf-c02/domain4/q645

Answer: D

AWS Lambda charges based on the number of requests and the compute resources consumed, measured in GB-seconds of execution duration, making it a true pay-per-use serverless pricing model.
Users bidding on the maximum price they are willing to pay per hour describes the Spot Instance purchasing model for EC2, not Lambda, which has fixed pay-per-use pricing rather than a bidding mechanism. Choosing a 1, 3, or 5-year upfront payment term describes the Reserved Instance pricing model for EC2 and RDS, not Lambda, which has no commitment-based pricing option. Paying for required permanent storage on a file system or in a database describes storage service pricing, not Lambda pricing, which is based on function execution rather than persistent storage consumption.

## clf-c02/domain4/q647

Answer: B

The AWS Pricing Calculator allows companies to model on-premises or current cloud configurations alongside projected AWS configurations to produce a detailed cost comparison, making it the purpose-built tool for performing a cost benefit analysis of migrating to AWS.
AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns with forecasting capability, and requires active AWS usage data to generate analysis rather than providing pre-migration cost benefit comparisons. The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a cost benefit comparison tool for evaluating a potential migration. AWS Trusted Advisor inspects your existing AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool for optimizing an existing deployment rather than a cost benefit analysis tool for a migration decision.

## clf-c02/domain4/q648

Answer: B

Linked accounts under consolidated billing in AWS Organizations automatically share Reserved Instance cost benefits across all member accounts, so unused RIs in one account apply to matching usage in another.
AWS Cost Explorer between AWS accounts provides visualisation and analysis of spending across linked accounts but does not itself enable the sharing of Reserved Instance benefits, which is a function of consolidated billing within AWS Organizations. The Amazon EC2 Reserved Instance Utilization Report shows how effectively your Reserved Instances are being used, providing visibility into RI utilization rather than being the mechanism that enables RI benefit sharing across accounts. Amazon EC2 Instance Usage Reports show historical usage patterns for EC2 instances within an account, and are a reporting tool rather than the mechanism that enables Reserved Instance benefit sharing between accounts.

## clf-c02/domain4/q649

Answer: B

AWS Organizations provides consolidated billing, combining multiple AWS accounts under a single payer account to simplify the billing process with a single invoice covering all member accounts.
AWS Cost and Usage Reports provide the most granular breakdown of actual AWS charges by service, resource, and time period, and are a billing analysis tool rather than a service that consolidates payment across multiple accounts. AWS Cost Explorer provides interactive visualisations of AWS spending patterns and supports filtering and forecasting, and is a cost analysis tool rather than a service that simplifies billing by consolidating multiple accounts. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a billing consolidation service.

## clf-c02/domain4/q655

Answer: B, D

Creating separate AWS accounts per department isolates costs naturally as all charges within each account belong to that department, and applying tags to resources allows cost allocation by department within shared accounts through Cost Explorer reports.
Enabling multi-factor authentication for the AWS account root user is a security best practice for protecting account access, and has no connection to identifying or attributing costs by department. Using Reserved Instances reduces compute costs through long-term commitments, and while this benefits the overall bill it does not provide a mechanism for identifying or separating costs by department. Paying bills using purchase orders is a payment method for settling AWS invoices, and has no connection to identifying which department incurred which costs.

## clf-c02/domain4/q668

Answer: D

AWS Organizations provides centralized management of multiple AWS accounts, including Service Control Policies that restrict which services and actions are available within member accounts, enabling governance of access across the entire organization.
AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal use and self-service provisioning, and is a product and portfolio management tool rather than a service for centrally governing access across multiple accounts. AWS Config continuously tracks and records the configuration of AWS resources to assess compliance and detect changes, and is a configuration auditing tool rather than a service for managing access permissions across multiple accounts. AWS Trusted Advisor inspects your AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool that operates within a single account rather than providing centralized access management across multiple accounts.

## clf-c02/domain4/q669

Answer: B

AWS Budgets lets you set custom spending thresholds and sends alert notifications via email or SNS when your actual or forecasted costs approach or exceed those thresholds, making it the purpose-built alerting tool for cost management.
AWS Cost and Usage Reports provide the most granular breakdown of actual AWS charges by service, resource, and time period, and are a billing data and analysis tool rather than a threshold-based alerting service. AWS Cost Explorer provides interactive visualisations of AWS spending patterns and supports cost forecasting, and is an analysis tool for understanding spending trends rather than a service that sends alerts when spending approaches a defined limit. AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance including checks for underutilized resources, but does not send custom threshold-based alerts when account spending approaches a dollar amount you define.

## clf-c02/domain4/q670

Answer: A

The Enterprise Support plan is the minimum tier that includes a designated Technical Account Manager who provides proactive guidance, acts as a primary support contact, and coordinates AWS resources on behalf of the customer.
Business Support provides 24/7 access to Cloud Support Engineers via phone, email, and chat along with a one-hour response SLA for production system-down cases, but does not include a designated Technical Account Manager. Developer Support provides business-hours email access to Cloud Support Engineers for general technical questions, and does not include a Technical Account Manager or 24/7 dedicated support resources. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and includes no dedicated support personnel, technical case support, or account management.

## clf-c02/domain4/q673

Answer: A

On-Demand Instances are most cost-efficient for a short, uninterruptible workload that runs once a year, since there is no long-term commitment and you pay only for the 24 hours of actual usage.
Reserved Instances require a minimum one-year commitment, so purchasing a reservation for a workload that only runs for 24 hours once a year would result in paying for an entire year of capacity while using only a single day of it. Spot Instances use spare AWS capacity at significant discounts but can be interrupted by AWS at any time, making them unsuitable for a workload that must remain active and uninterrupted for its entire 24-hour duration. Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options, making them more expensive than On-Demand Instances for this simple use case.

## clf-c02/domain4/q677

Answer: B

The AWS Pricing Calculator allows companies to model the configuration of equivalent workloads on AWS and compare the projected costs against their current on-premises spending, making it the purpose-built tool for this type of cost comparison.
The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a tool for comparing projected AWS costs against on-premises spending. The AWS Billing and Cost Management console provides access to billing information, invoices, and cost management tools for active AWS accounts, and does not provide a structured way to compare on-premises infrastructure costs against projected AWS spending. AWS Cost Explorer provides interactive visualisations of existing AWS spending patterns and supports forecasting for active workloads, and requires active AWS usage data rather than providing a comparison against on-premises costs for a workload not yet on AWS.

## clf-c02/domain4/q685

Answer: B

A Technical Account Manager is exclusively available with the Enterprise Support plan, providing dedicated proactive guidance, coordinating AWS support resources, and acting as a primary ongoing contact for the account.
A Technical Project Manager is not an AWS Support resource. AWS does not offer a Technical Project Manager role through any support plan, making this an invalid option that does not correspond to a real AWS support benefit. Access to Cloud Support Engineers via phone, email, and chat is available with Business and Enterprise Support plans, and is not an exclusive benefit of Enterprise Support. Access to a Solutions Architect for architectural guidance is available to Enterprise Support customers through the TAM and architectural reviews, but Solutions Architects also engage with customers across other programs and are not exclusively an Enterprise Support benefit.

## clf-c02/domain4/q688

Answer: D

The full set of AWS Trusted Advisor checks across all five categories is available with Enterprise and Business Support plans. Developer and Basic Support plans provide access to only the seven core checks.
Business and Developer Support is an incorrect pairing because Developer Support provides only the seven core checks while Business Support provides the full suite, placing them at opposite levels of Trusted Advisor access. Business and Basic Support is an incorrect pairing because Basic Support provides only the seven core checks while Business Support provides the full suite, so they are not equivalent in Trusted Advisor access. Enterprise and Developer Support is an incorrect pairing because Developer Support is limited to the seven core checks while Enterprise Support provides the full suite, so they do not share the same level of Trusted Advisor access.

## clf-c02/domain4/q693

Answer: B

The AWS Pricing Calculator allows you to model AWS service configurations and estimate the monthly costs of running a new project before any resources are deployed, making it the purpose-built tool for pre-deployment cost estimation.
AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns, and requires active AWS usage data to generate analysis rather than providing cost estimates for new projects not yet deployed. The AWS Cost Explorer API provides programmatic access to the same historical cost and usage data that the Cost Explorer console displays, and like the console it requires existing usage data rather than supporting pre-deployment project cost estimation. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool for active workloads rather than a pre-deployment cost estimation service.

## clf-c02/domain4/q695

Answer: B

Amazon CloudWatch can monitor estimated AWS charges and trigger billing alarms when costs exceed thresholds you define, sending notifications through Amazon SNS to alert you before your bill reaches unexpected levels.
AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance and detect configuration changes, and has no capability to generate alerts based on estimated monthly billing amounts. AWS X-Ray is a distributed tracing service that analyzes and debugs application performance by mapping requests as they flow through application components, and is a performance tool with no connection to billing monitoring or cost alerts. AWS CloudTrail records API calls and account activity for auditing and compliance purposes, and while it logs billing-related API actions it does not generate alerts based on estimated monthly billing thresholds.

## clf-c02/domain4/q706

Answer: A, E

Reserved Instances provide significant discounts over On-Demand pricing of up to 72%, and they allow you to reserve capacity in a specific Availability Zone, ensuring that capacity is available when you need it.
Reserved Instances do not provide access to additional instance types beyond what is available on On-Demand. The instance types available to you are the same regardless of how you purchase them. Reserved Instances do not provide additional networking capability. Network performance is determined by the instance type and configuration rather than the purchasing model. Customers cannot upgrade Reserved Instance types as new types become available unless they hold Convertible RIs, which allow exchanges. Standard RIs are locked to the specific instance type purchased.

## clf-c02/domain4/q707

Answer: B

Amazon Linux EC2 instances are billed per second with a one-minute minimum, so the customer is billed for the exact duration of 3 hours, 5 minutes, and 6 seconds.
Billing for 3 hours and 5 minutes would omit the 6 seconds of actual usage, which would be incorrect under per-second billing where the exact duration including seconds is charged. Billing for 3 hours and 6 minutes would round the 5 minutes and 6 seconds up to the next full minute, which was the old per-hour billing approach and does not apply to Linux instances under current per-second billing. Billing for 4 hours would apply full-hour rounding to the entire session, which is the old billing model that predates per-second billing and would significantly overcharge compared to the actual usage time.

## clf-c02/domain4/q714

Answer: D

The AWS Pricing Calculator allows you to model the configuration of a web application on AWS and compare the projected costs against the equivalent traditional hosting environment costs, making it the purpose-built tool for this type of comparison.
AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns, and requires active AWS usage data to generate analysis rather than providing comparisons against traditional hosting costs for workloads not yet on AWS. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool for active workloads rather than a comparison tool for evaluating migration economics. The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a tool for comparing projected AWS costs against traditional hosting expenses.

## clf-c02/domain4/q715

Answer: A, B

AWS Marketplace offers flexible hourly or monthly licensing for third-party software, and enables one-click deployment that automates the launch of pre-configured software stacks without manual installation.
AWS Marketplace data encryption is not managed by a third-party vendor on behalf of the customer. Data encryption remains the customer's responsibility under the shared responsibility model regardless of whether software is sourced from Marketplace. AWS Marketplace does not eliminate the need to upgrade to newer software versions. Vendors release updated versions in Marketplace and customers must choose to subscribe to or upgrade to newer listings. Users cannot deploy third-party Marketplace software without testing. Thorough testing remains an important step in any software deployment to ensure compatibility and security, regardless of whether the software comes from Marketplace.

## clf-c02/domain4/q725

Answer: C

AWS Trusted Advisor is an online tool that runs automated checks against your AWS environment and provides actionable recommendations across cost optimization, performance, security, fault tolerance, and service limits.
AWS Trusted Advisor is an automated online tool rather than an AWS staff member. It does not involve human advisors providing personalized recommendations, and operates through automated checks rather than individual consultations. Trusted Advisor is an AWS-owned automated service rather than a network of AWS partners. The AWS Partner Network is a separate program of external consulting and technology firms, not a component of the Trusted Advisor service. Trusted Advisor is a self-service automated tool accessible through the AWS Management Console, and is entirely distinct from Technical Account Managers, who are dedicated human support professionals available only on Enterprise Support plans.

## clf-c02/domain4/q726

Answer: B

AWS Cost Explorer provides interactive visualisations that let you understand, analyze, and manage your AWS costs and usage over time, with filtering, grouping, and forecasting capabilities.
AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a proactive cost governance and alerting tool rather than a service for visualising and analyzing historical spending patterns. AWS Organizations provides centralized management of multiple AWS accounts including consolidated billing and Service Control Policies, and is an account governance service rather than a cost visualisation tool. Consolidated billing is a feature of AWS Organizations that combines usage and invoices from multiple accounts into a single bill, and is a billing aggregation feature rather than a tool for visualising and managing costs over time.

## clf-c02/domain4/q732

Answer: A

Pay-as-you-go pricing reduces capital expenditures by eliminating the need to purchase hardware upfront. Instead of large investments before deployment, costs are variable and based on actual consumption.
The pay-as-you-go model does not require upfront payment for AWS services. On-Demand pricing charges only after resources are consumed, which is the opposite of requiring payment before use. Pay-as-you-go pricing applies broadly across AWS services including compute, storage, databases, networking, and many others, and is not limited to EC2, S3, and RDS. Pay-as-you-go pricing reduces capital expenditures rather than operational expenditures. AWS usage fees are themselves operational expenses, so while the model shifts spending from capital to operational it does not reduce operational expenditures overall.

## clf-c02/domain4/q734

Answer: B

AWS Organizations enables consolidated billing across multiple accounts, providing a single payment method and combined usage that can qualify for volume discounts.
Amazon QuickSight is a serverless business intelligence service for creating dashboards and visualisations from business data, and has no capability to consolidate billing across multiple AWS accounts. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance tool rather than a service that consolidates billing across accounts. Amazon Forecast is a machine learning service that generates time-series predictions such as demand or inventory forecasts, and is an AI analytics service with no connection to billing consolidation across AWS accounts.

## clf-c02/domain4/q737

Answer: D

All upfront payment for a Dedicated Host reservation provides the largest discount because paying the full cost at the start of the term reduces AWS's billing risk and earns the maximum savings over the reservation period.
No upfront payment provides the lowest discount among the three payment options for Dedicated Host reservations. Without any initial payment, AWS offers less incentive compared to partial or full upfront options. Hourly on-demand payment is the most expensive option for Dedicated Hosts as it has no commitment and no discount, equivalent to standard On-Demand pricing rather than the reserved pricing tiers. Partial upfront payment splits the cost between an initial payment and ongoing monthly charges, providing a moderate discount that is greater than no upfront but less than the maximum available through all upfront payment.

## clf-c02/domain4/q738

Answer: B

The AWS Pricing Calculator allows users to model AWS service configurations and generate detailed cost estimates before any resources are deployed, making it the most appropriate tool to direct a user to when they need to estimate the cost of a new application.
Informing the user that AWS uses on-demand pricing is accurate but does not help them estimate actual costs for a specific application, as it provides no tool or mechanism for calculating projected spend. Amazon QuickSight is a serverless business intelligence service for creating dashboards and visualisations from business data, and is not a tool for analyzing on-premises spending or estimating AWS costs. Amazon AppStream 2.0 is a fully managed application streaming service that delivers desktop applications to users through a browser, and has no capability for real-time pricing analytics or cost estimation.

## clf-c02/domain4/q747

Answer: B

Using separate AWS accounts for production and non-production workloads isolates costs at the account level, allowing billing to naturally reflect each environment's consumption and making it straightforward to attribute and review costs independently.
Creating IAM roles for production and non-production workloads controls who can access each environment's resources but does not isolate or separately track the costs incurred by each environment, as IAM roles are access control constructs rather than billing boundaries. Using Amazon EC2 for non-production and other services for production workloads segments the infrastructure by service type rather than by environment boundary, which does not provide clean cost isolation and makes cost tracking more complex rather than simpler. Using Amazon CloudWatch to monitor service usage provides operational visibility into resource consumption and can trigger cost-related alerts, but monitoring usage is not the same as isolating costs between environments; CloudWatch does not create billing boundaries between production and non-production workloads.

## clf-c02/domain4/q758

Answer: A, C

AWS Lambda charges are based on the execution time of the function measured in GB-seconds and the number of requests made to trigger the function, with both dimensions incurring charges once the free tier is exceeded.
The number of versions of a specific Lambda function does not affect pricing. Lambda versions are used for deployment management and rollback purposes, and maintaining multiple versions does not increase charges. The programming language used for a Lambda function does not affect its cost. Lambda charges the same rate per GB-second of execution regardless of whether the function is written in Python, Node.js, Java, or any other supported runtime. The total number of Lambda functions in an AWS account does not affect pricing. Lambda charges based on actual invocations and execution duration rather than the number of functions defined in the account.

## clf-c02/domain4/q762

Answer: B, C

AWS Marketplace allows vendors to sell their software solutions to other AWS users, and allows buyers to purchase and deploy third-party software that runs on AWS infrastructure. Both are core functions of the platform.
Selling unused Amazon EC2 Spot Instances is not a function of AWS Marketplace. Spot Instance capacity is made available by AWS itself through the EC2 console based on unused compute capacity, and individual customers cannot list or sell their own Spot Instances. Purchasing AWS security and compliance documents describes AWS Artifact, which provides on-demand access to AWS compliance reports and security agreements, and is not a function of AWS Marketplace. Ordering AWS Snowball is done directly through the AWS console as part of the Snow Family service request process, and is not a procurement action available through AWS Marketplace.

## clf-c02/domain4/q768

Answer: C

AWS Organizations provides automated account creation and centralized management of multiple AWS accounts, including consolidated billing, Service Control Policies, and organizational units.
AWS QuickSight is a serverless business intelligence service for creating dashboards and visualisations from business data, and has no capability to create or manage AWS accounts. Amazon Lightsail is a simplified compute service for deploying virtual servers and web applications with straightforward pricing, and is a compute service rather than an account management tool. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is a customer engagement service with no connection to AWS account creation or management.

## clf-c02/domain4/q775

Answer: D

AWS Marketplace is a digital catalog of thousands of software products from independent software vendors that customers can find, subscribe to, and immediately deploy into their AWS environment, often with flexible licensing models including pay-as-you-go and BYOL.
AWS Config is a service that continuously monitors and records resource configurations and evaluates them against compliance rules, providing governance and change management capabilities rather than a software procurement catalog. AWS Service Catalog allows organizations to create and manage approved portfolios of IT services for internal use, enabling governance and self-service deployment of pre-approved resources, but it is an internal governance tool rather than an external marketplace where customers can find and purchase third-party software solutions. AWS Partner Network is the global partner program for companies that build with or sell AWS, providing training, certification, and co-selling benefits, and is a partner ecosystem program rather than a place for customers to purchase and deploy software solutions.

## clf-c02/domain4/q787

Answer: C, D

AWS Professional Services provides hands-on migration guidance and Landing Zone setup, and AWS Partner Network partners offer specialized migration consulting and implementation support, both providing the direct hands-on assistance the company needs.
The AWS Marketplace team provides a platform for discovering and purchasing third-party software and services, and does not perform migrations directly into customer accounts. AWS Support cases are used to resolve technical issues and service-related problems, not to engage hands-on project delivery teams for migration work. Amazon Connect is a cloud-based contact center service for managing customer communications, and has no function related to submitting proposals or engaging migration expertise.

## clf-c02/domain4/q788

Answer: C

The AWS Enterprise Support Concierge team specializes in answering billing and account inquiries, helping Enterprise customers navigate complex billing questions and manage account-level issues with dedicated expertise.
Supporting application development is the domain of AWS Developer Support, Solutions Architects, and Professional Services rather than the Concierge team, which focuses specifically on billing and account matters. Providing architecture guidance is the function of AWS Solutions Architects and the Technical Account Manager included in the Enterprise Support plan, not the Concierge team which handles billing and account inquiries. Answering questions regarding technical support cases is the role of Cloud Support Engineers, who handle technical issues via phone, email, and chat, rather than the Concierge team which is dedicated to billing and account topics.

## clf-c02/domain4/q791

Answer: C

The AWS Pricing Calculator allows you to model the configuration of an application on AWS and compare the projected costs against the equivalent on-premises running costs, making it the purpose-built tool for this comparison.
AWS Trusted Advisor inspects your existing AWS environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool for optimizing an active deployment rather than a cost comparison tool. The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a tool for comparing projected AWS costs against on-premises expenses. AWS Cost Explorer provides interactive visualisations of existing AWS spending and usage patterns with forecasting capability, and requires active AWS usage data to generate analysis rather than providing comparisons against on-premises costs.

## clf-c02/domain4/q792

Answer: A

To restrict Reserved Instance benefits to a single account, purchase the RIs from the master payer account and turn off Reserved Instance sharing in the billing settings, preventing the discounts from applying to other member accounts.
Enabling billing alerts in the AWS Billing and Cost Management console creates notifications when spending exceeds thresholds, and has no effect on how Reserved Instance benefits are shared or restricted across accounts in an organization. Purchasing the Reserved Instances in individual linked accounts and turning off RI sharing from the payer level would apply RI restrictions organization-wide rather than limiting benefits to a single specific account. Enabling Reserved Instance sharing in the AWS Billing and Cost Management console would expand RI benefit sharing across all member accounts, which is the opposite of restricting the benefit to a single account.

## clf-c02/domain4/q797

Answer: B

AWS Budgets supports Reserved Instance utilization budgets that send alerts when the utilization of Reserved Instances drops below a defined percentage threshold, helping customers ensure they are getting value from their RI commitments.
Preventing a given user from creating a resource is an access control function achieved through IAM policies or Service Control Policies in AWS Organizations, not through AWS Budgets. AWS Budgets is an alerting and monitoring tool and cannot enforce hard limits or prevent resource creation, making setting resource limits to prevent overspending an incorrect description of its capabilities. Splitting an AWS bill across multiple forms of payment is a billing and payment method configuration handled through the AWS Billing Console, and is not a feature of AWS Budgets.

## clf-c02/domain4/q799

Answer: A, C

AWS Trusted Advisor checks S3 bucket permissions to identify those with overly permissive public access that could expose data, and verifies that MFA is enabled on the root user account, both falling under its Security checks category.
AWS service outages are tracked by the AWS Health Dashboard, which provides real-time and historical status information about AWS services across all Regions, and are not a category of checks performed by Trusted Advisor. Available software patches for EC2 instance operating systems are identified by Amazon Inspector and AWS Systems Manager Patch Manager, and are not a category of recommendations provided by Trusted Advisor. The number of users in the account is visible through the IAM console and IAM credential reports, and is not a recommendation category in Trusted Advisor, which focuses on security, cost, performance, fault tolerance, and service limits.

## clf-c02/domain4/q817

Answer: A, D

The AWS Cost and Usage Report provides the most comprehensive view of actual AWS costs broken down by service, resource, and time period, and billing alerts combined with Amazon CloudWatch alarms proactively notify you when actual or forecasted spend exceeds defined thresholds. Both are purpose-built tools for monitoring AWS costs and expenses.
AWS product pages describe the features, use cases, and pricing of individual AWS services, and are a reference resource rather than a tool for actively monitoring costs and expenses in your account. AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance including checks for underutilized resources, but is an advisory tool rather than a direct cost and expense monitoring service. The AWS Price List API provides programmatic access to AWS service pricing data for building custom pricing tools, and is a pricing data source rather than a tool for monitoring actual costs and expenses in your account.

## clf-c02/domain4/q820

Answer: A

AWS Marketplace offers free trials and flexible pay-as-you-go pricing for third-party software solutions, allowing companies to evaluate an ecommerce platform before committing to long-term use.
AWS Partner Network is a program for consulting and technology partners who build and sell AWS-based solutions, not a platform for trialling third-party software. AWS Managed Services provides operational management of AWS infrastructure on behalf of customers and does not offer third-party software trials. AWS Service Catalog allows organizations to create and manage approved catalogs of IT services for internal use, not for discovering or trialling third-party commercial software.

## clf-c02/domain4/q821

Answer: C

Amazon CloudWatch can create billing alarms that monitor your estimated AWS charges and send notifications through Amazon SNS when costs exceed thresholds you define, making it the service used to set up billing alerts.
AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance, and while it includes checks for underutilized resources it does not create billing alarms that alert on spending thresholds in real time. AWS CloudTrail records API calls and account activity across your AWS environment for auditing and compliance purposes, and does not create billing alarms or monitor estimated charges. Amazon QuickSight is a serverless business intelligence service for creating dashboards and visualisations from business data, and has no capability to create or manage billing alarms based on AWS spending thresholds.

## clf-c02/domain4/q832

Answer: B

Creating a new AWS account and configuring AWS Organizations allows you to invite existing accounts to join, enabling centralized governance through Service Control Policies and consolidated billing under a single payer account.
Forwarding monthly invoices and creating IAM roles for cross-account access addresses reporting and permissions separately, but does not centralize governance or consolidate payments into a single billing structure under a payer account. AWS Organizations can only have one management account within an organization, and configuring it in multiple existing accounts simultaneously is not possible. The correct approach is to configure it in a single management account and then invite others to join. Using Cost Explorer to combine cost views and replicating IAM policies across accounts provides some visibility and consistency, but does not centralize governance through SCPs or consolidate payments into a single invoice the way AWS Organizations does.

## clf-c02/domain4/q836

Answer: C

AWS Cost Explorer provides cost forecasting capabilities that use historical spending data to project future AWS expenses, helping organizations anticipate and plan for upcoming costs.
AWS Trusted Advisor analyzes your environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool for optimizing existing deployments rather than a forecasting service for future spending. AWS Organizations provides centralized account management with consolidated billing and governance controls, and is an account structure and governance service rather than a tool for forecasting future AWS spending. Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security tool with no cost forecasting capability.

## clf-c02/domain4/q847

Answer: A

Opening a detailed billing support case with AWS Support is the appropriate action to resolve billing issues, as AWS Support can investigate the specific charges, clarify billing discrepancies, and apply corrections where appropriate.
Uploading data describing the issue to a private Amazon S3 bucket stores the information but does not submit it to anyone who can investigate or resolve the billing issue, as S3 is a storage service rather than a support channel. Creating a pricing application and deploying it to an EC2 instance for more information introduces unnecessary complexity and cost rather than addressing the billing issue through the appropriate AWS Support channel. Proceeding to create a new dashboard in Amazon QuickSight would visualise billing data but does not resolve the underlying billing issue, as QuickSight is an analytics tool rather than a support or dispute resolution mechanism.

## clf-c02/domain4/q848

Answer: B

The AWS Pricing Calculator allows users to model AWS service configurations and estimate monthly costs based on projected usage, helping customers forecast AWS spending before deploying resources.
Comparing on-premises costs to colocation environments is a function outside the scope of the AWS Pricing Calculator, which focuses on estimating the cost of AWS services rather than comparing third-party hosting options. Estimating power consumption at existing data centers is not a function of the AWS Pricing Calculator. Electricity and physical infrastructure costs are an on-premises concern that AWS abstracts away entirely for customers. Estimating CPU utilization of running instances is a function of Amazon CloudWatch, which collects and monitors performance metrics from active AWS resources, rather than the Pricing Calculator which estimates costs before deployment.

## clf-c02/domain4/q852

Answer: D

AWS Support handles billing inquiries and account reactivation requests. Users should submit an account and billing support case through the AWS Support Center, which is accessible even without an active support plan.
The AWS Support forum is a community-driven resource where customers and AWS staff exchange questions and answers, and is not the appropriate channel for resolving account suspension or submitting official billing requests. AWS Abuse handles reports of AWS resources being used for malicious activity such as spam, hacking, or unauthorised use, and is not the correct contact for billing inquiries or account reactivation. An AWS Solutions Architect provides architectural guidance and design support for building on AWS, and does not handle billing inquiries or account reactivation requests.

## clf-c02/domain4/q856

Answer: B, C

AWS Cost Management tools break down costs by day, service, and linked account for detailed analysis, and allow you to create budgets and receive notifications when actual or forecasted usage exceeds defined thresholds.
Terminating all AWS resources automatically if budget thresholds are exceeded is not a standard function of AWS Cost Management tools. AWS Budgets can trigger automated actions such as applying IAM policies to restrict further provisioning, but does not automatically terminate existing resources. Switching automatically to Reserved Instances or Spot Instances based on which is more cost-effective is not a function of AWS Cost Management tools. Instance purchasing decisions require deliberate configuration rather than automatic switching based on price comparisons. Moving data stored in S3 to a more cost-effective storage class is managed through S3 Lifecycle policies configured on individual buckets, and is a storage management feature rather than a function of the AWS Cost Management toolset.

## clf-c02/domain4/q863

Answer: A

EC2 Dedicated Hosts provide visibility into the physical server's sockets and cores, allowing you to use existing per-core or per-socket software licenses under the Bring Your Own License model.
On-Demand Instances run on shared infrastructure where the underlying physical server details are abstracted away, providing no visibility into socket or core topology required for per-core software license compliance. Spot Instances use spare AWS capacity on shared infrastructure and can be interrupted at any time, providing neither the physical server visibility required for per-core licensing nor the consistent availability needed for production database workloads. Reserved Instances are a pricing commitment model that reduces costs over a one or three-year term, but they run on standard shared infrastructure without host-level visibility and do not satisfy per-core or per-socket software license requirements.

## clf-c02/domain4/q868

Answer: D, E

AWS Organizations implements consolidated billing to combine multiple accounts under one payment method, and enforces governance through Service Control Policies that restrict which services and actions are available within member accounts.
Establishing real-time communications between members of an internal team is the function of collaboration tools such as Amazon Chime or AWS Wickr, not AWS Organizations, which manages account structure and billing. Facilitating the use of NoSQL databases is the function of services such as Amazon DynamoDB, which provides managed NoSQL database capabilities, rather than AWS Organizations which is an account management service. Providing automated security checks is the function of services such as Amazon Inspector, AWS Security Hub, and Amazon GuardDuty, rather than AWS Organizations which focuses on account governance and billing consolidation.

## clf-c02/domain4/q870

Answer: B

Consolidated billing through AWS Organizations combines previously independent accounts under a single payer, simplifying payment with a single invoice and enabling volume discounts through combined usage.
Detailed billing reports provide a historical breakdown of charges within an individual account, and are a reporting tool rather than a mechanism for combining the billing of previously separate accounts. The AWS Cost and Usage Report provides the most granular breakdown of actual charges by service, resource, and time period, and is a billing analysis tool rather than a feature for combining billing across independent accounts. A cost allocation report breaks down charges by tagged resources to support chargeback and attribution, and is a cost categorization tool rather than a mechanism for consolidating billing from independent accounts.

## clf-c02/domain4/q871

Answer: B

The AWS Pricing Calculator is used to model AWS service configurations and estimate costs, enabling customers to compare projected AWS spending against their current on-premises infrastructure costs to understand potential savings.
Receiving reports that break down AWS Cloud compute costs by duration, resource, or tags is the function of the AWS Cost and Usage Report, which provides granular historical billing data rather than pre-deployment cost estimates. Monitoring actual AWS costs compared to estimated costs describes a combination of AWS Budgets and AWS Cost Explorer, which track real spending against targets rather than providing pre-deployment estimates. Enabling billing alerts when spending exceeds a defined threshold is the function of AWS Budgets combined with Amazon CloudWatch billing alarms, not the AWS Pricing Calculator which is used before resources are deployed.

## clf-c02/domain4/q874

Answer: C

The Business Support plan is the minimum tier that provides access to the AWS Support API, enabling programmatic management of support cases and integration with existing service management systems.
Developer Support provides business-hours email access to Cloud Support Engineers but does not include the AWS Support API, limiting case management to the console and email rather than programmatic access. Enterprise Support also provides access to the AWS Support API along with a dedicated TAM and faster response times, but it is a higher-cost plan than Business Support and therefore not the minimum required. Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and does not include the AWS Support API or the ability to open technical support cases.

## clf-c02/domain4/q877

Answer: C

On-Demand Instances are ideal for workloads that run only when needed but must not be interrupted, since they have no long-term commitment and provide guaranteed availability for the duration of the process.
Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options, making them more expensive than On-Demand for a simple use case without isolation requirements. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, directly violating the requirement that the instance must remain active for the full duration of the process. Reserved Instances require a minimum one-year commitment, which is not appropriate for a workload that only runs occasionally when needed rather than continuously over a long term.

## clf-c02/domain4/q878

Answer: B

AWS Health Dashboard provides personalized and timely information about AWS events that may affect your specific resources, proactive notifications for scheduled maintenance activities, and guidance to help you manage events in progress.
Amazon CloudWatch dashboard displays metrics and alarms for your own AWS resources and applications, and is an operational monitoring tool for your workloads rather than a source of personalized notifications about AWS service events and scheduled infrastructure changes. AWS Trusted Advisor analyzes your environment against best practice checks across cost, performance, security, and fault tolerance, and provides advisory recommendations rather than real-time event notifications or proactive alerts about scheduled AWS infrastructure activities. AWS Systems Manager dashboard provides operational visibility and management tools for your AWS infrastructure including patch compliance, inventory, and automation status, and is a management console for your resources rather than a notification service for AWS service events.

## clf-c02/domain4/q882

Answer: D

The Enterprise Support plan provides access to architectural and operational reviews including Well-Architected reviews, and 24/7 access to Senior Cloud Support Engineers via email, chat, and phone.
Basic Support provides access to documentation, whitepapers, and the seven core Trusted Advisor checks, and does not include architectural reviews or 24/7 access to Senior Cloud Support Engineers. Business Support provides 24/7 access to Cloud Support Engineers and a one-hour response SLA for production system-down cases, but does not include architectural and operational reviews which are exclusive to Enterprise Support. Developer Support provides business-hours email access to Cloud Support Engineers for general technical questions, and does not include 24/7 access, phone support, or architectural and operational reviews.

## clf-c02/domain4/q892

Answer: C

Creating a separate AWS account for each department provides the cleanest cost separation, as all charges within each account belong exclusively to that department and appear as a distinct line item on a consolidated bill.
Adding department-specific tags to each resource enables cost attribution within shared accounts through Cost Explorer, but tagging relies on consistent human application and does not provide the hard billing boundaries that separate accounts create. Creating a separate VPC for each department isolates network resources and can improve security, but VPCs do not create separate invoices or cost boundaries as all VPC resources still appear on the same AWS account bill. Using AWS Organizations provides account governance and consolidated billing but does not itself separate costs by department. It enables visibility across accounts but the cost separation comes from having distinct accounts rather than from Organizations itself.

## clf-c02/domain4/q893

Answer: B

Consolidated billing combines usage across all member accounts in an AWS Organization, qualifying the organization for volume pricing tiers that individual accounts might not reach on their own.
Access to AWS Health Dashboard is available to all AWS customers regardless of whether they use consolidated billing, and is not a benefit that consolidated billing specifically enables. Improved account security is not a direct benefit of consolidated billing. Security posture is governed through IAM, Service Control Policies, and security configurations rather than through billing structure. Centralized AWS IAM is not a benefit of consolidated billing. IAM operates at the individual account level, and centralized access management across accounts is handled through AWS Organizations policies and IAM roles rather than through consolidated billing.

## clf-c02/domain4/q894

Answer: B

AWS Budgets lets you set custom cost and usage thresholds with configurable alerts that notify you via email or SNS when actual or forecasted spending exceeds your defined limits.
AWS Organizations provides centralized account management with consolidated billing and governance controls, and is an account structure service rather than a service for setting custom cost thresholds and sending alerts when those limits are breached. AWS Cost Explorer provides interactive visualisations of AWS spending patterns and supports cost forecasting, and is an analysis and planning tool rather than a threshold-based alerting service. AWS Trusted Advisor inspects your environment and provides recommendations across security, cost, performance, and fault tolerance, and is an advisory tool rather than a service for setting and monitoring custom spending limits.

## clf-c02/domain4/q896

Answer: B

AWS Trusted Advisor includes checks that monitor your usage against AWS service limits and alerts you when you are approaching or have reached a limit, helping you avoid service disruptions caused by limit exhaustion.
The AWS Pricing Calculator is used to estimate future costs for AWS services before provisioning them, and does not monitor current service usage against limits. AWS Health Dashboard provides personalized alerts about AWS events and scheduled maintenance that may affect your resources, and while it can notify you about limit-related events it is not the primary tool for actively monitoring service limit usage. AWS Cost and Usage Reports provide granular data about actual AWS spending broken down by service, resource, and time period, and are a billing analysis tool rather than a service limit monitoring tool.

## clf-c02/domain4/q902

Answer: B

Spot Instances offer up to 90% savings over On-Demand pricing and are ideal for applications with flexible start and end times, since they can be interrupted and restarted to take advantage of spare capacity pricing.
On-Demand Instances charge the full hourly rate and while they provide guaranteed availability, they do not take advantage of the cost savings available for workloads that can flex their timing around spare capacity availability. Reserved Instances require a one or three-year commitment and are designed for steady-state workloads with predictable usage, making them poorly suited for workloads with flexible schedules that do not require continuous capacity. Dedicated Hosts provide a physical server dedicated entirely to a single customer for compliance and licensing purposes, and are priced at a premium over standard EC2 options rather than providing cost savings for flexible workloads.

## clf-c02/domain4/q904

Answer: C

Spot Instances provide the deepest discounts for workloads that are infrequently executed and can be interrupted, making them the most cost-effective option when timing flexibility and interruption tolerance are present.
On-Demand Instances charge the full hourly rate with no discount, making them significantly more expensive than Spot Instances for a workload that qualifies for Spot pricing due to its interruptible and flexible nature. Reserved Instances provide discounts through long-term commitments of one or three years, but are designed for steady-state workloads running continuously rather than infrequently executed workloads where the commitment would result in paying for unused capacity. Dedicated Hosts provide a physical server dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options rather than providing cost savings for infrequent, interruptible workloads.

## clf-c02/domain4/q907

Answer: A

With a Developer Support plan, the developer should contact AWS Support by opening a support case through the AWS Management Console, which provides email-based assistance from Cloud Support Engineers during business hours.
AWS Professional Services is a team of experts that works with customers on cloud strategy, architecture, and migration engagements, and is not the appropriate channel for resolving a technical connectivity issue with an existing AWS service. A Technical Account Manager provides proactive guidance and is a dedicated contact for Enterprise Support customers only, and is not available to customers on the Developer Support plan. AWS consulting partners are external professional services firms in the AWS Partner Network, and are not the appropriate contact for technical support issues with AWS services under an active AWS Support plan.

## clf-c02/domain4/q911

Answer: A, D

AWS Trusted Advisor provides recommendations across five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. Cost Optimization and Performance are both official Trusted Advisor categories.
Auditing is not a Trusted Advisor category. Audit trail and compliance monitoring is handled by services such as AWS CloudTrail and AWS Config rather than being a category within the Trusted Advisor recommendation framework. Serverless architecture is not a Trusted Advisor category. Serverless design guidance is available through AWS documentation and the Well-Architected Framework rather than through automated Trusted Advisor checks. Scalability is not a Trusted Advisor category. While some Trusted Advisor checks address resource limits that could constrain scaling, scalability as a concept is addressed through the AWS Well-Architected Framework's Performance Efficiency pillar rather than as a dedicated Trusted Advisor category.

## clf-c02/domain4/q914

Answer: A

Using multiple AWS accounts, one per environment, provides completely separate invoices for development, testing, and production since all charges within each account are billed independently under consolidated billing.
Using resource tagging allows cost allocation by environment within a shared account through Cost Explorer, but tags rely on consistent application and do not create separate invoices. All tagged resources still appear on the same account's bill. Using multiple VPCs isolates network resources for each environment within the same account, but VPCs do not create separate invoices as all resources across all VPCs in an account are billed together on a single invoice. AWS Cost Explorer provides visualisation and analysis of spending patterns and supports filtering by tag or service, but is an analysis tool that reads from existing billing data rather than a mechanism for generating separate invoices per environment.

## clf-c02/domain4/q916

Answer: A, D

Spot Instances provide deep discounts for flexible, stateless workloads that can tolerate interruptions, and Reserved Instances offer significant savings for sustained workloads with predictable usage through long-term commitments. Both directly reduce the cost of running EC2 instances.
Memory optimized instances are designed for workloads that process large datasets in memory such as in-memory databases and real-time processing, and selecting the right instance type improves performance efficiency but does not itself reduce cost unless it right-sizes an over-provisioned instance. On-Demand Instances charge the full hourly rate with no discount, making them the most expensive EC2 purchasing option and not a mechanism for reducing costs compared to reserved or spot pricing. Spend limits set using AWS Budgets alert you when spending exceeds a threshold but do not themselves reduce the cost of running EC2 instances. Budgets are a governance and visibility tool rather than a pricing mechanism.

## clf-c02/domain4/q922

Answer: A

AWS Budgets sends alert notifications when actual or forecasted spending exceeds custom thresholds you define, enabling proactive cost management before bills grow unexpectedly.
AWS Cost Explorer provides interactive visualisations of historical AWS spending and usage patterns with forecasting capability, and is an analysis and planning tool rather than a service that sends automated threshold-based alerts. AWS Cost Allocation Tags are key-value labels applied to AWS resources that enable cost attribution by project, team, or environment in billing reports, and are a cost categorization mechanism rather than an alerting service. AWS Organizations provides centralized account management with consolidated billing and governance controls, and is an account structure and governance service rather than a service that sends spending threshold alerts.

## clf-c02/domain4/q926

Answer: C

On-Demand Instances are best for short-term, spiky, or unpredictable workloads that cannot be interrupted, since they have no long-term commitment, no upfront cost, and no risk of capacity interruption.
Spot Instances use spare AWS capacity at significant discounts but can be interrupted by AWS at any time, making them unsuitable for workloads that cannot be interrupted during execution. Dedicated Hosts provide a physical server dedicated to a single customer for compliance and licensing purposes, and are priced at a premium over standard EC2 options, making them more expensive and unnecessary for workloads without isolation requirements. Reserved Instances require a minimum one-year commitment and are designed for predictable, steady-state workloads. Committing to a reservation for a short-term, spiky, or unpredictable workload would result in paying for capacity beyond actual usage.

## clf-c02/domain4/q930

Answer: A

Tagging resources with key-value pairs such as department names enables cost allocation tracking through AWS Cost Explorer and billing reports, allowing each resource's costs to be attributed to the appropriate business unit.
Limiting who can create resources is an IAM and Service Control Policy governance practice that controls access permissions, and while it prevents unauthorised resource creation it does not itself allocate or attribute costs to specific business units. Adding a secondary payment method changes how AWS bills are paid rather than how costs are categorized or attributed across the organization, and has no effect on cost allocation reporting. Running all operations on a single AWS account consolidates billing into one place but does not provide cost allocation by department without tags or other attribution mechanisms to distinguish which resources belong to which business unit.

## clf-c02/domain4/q934

Answer: C

To unlink a member account from AWS Organizations, the account must meet the requirements of a standalone account, including having valid payment information, a support plan, and contact information configured independently.
Active compliance with AWS System and Organization Controls is not a requirement for unlinking a member account from AWS Organizations. SOC compliance is an AWS certification program rather than a precondition for account separation. Both the payer and the linked account are not required to create AWS Support cases to request unlinking. The process of removing a member account is performed directly through the AWS Organizations console by the management account or by the member account itself. The payer account can remove a linked account from the organization through the management console, but the member account itself can also leave the organization directly, so it is not strictly required that the payer account initiates the removal.

## clf-c02/domain4/q940

Answer: A, B

Using tags on resources enables cost allocation by department through Cost Explorer reports, and using multiple AWS accounts per department creates hard billing boundaries with separate invoices that cleanly separate costs.
Using an account manager refers to a support relationship rather than a technical mechanism for identifying costs by department, and does not provide a method for attributing or separating AWS resource costs across business units. Using AWS Trusted Advisor inspects your environment for best practice recommendations across cost, performance, security, and fault tolerance, but does not provide a mechanism for identifying or attributing costs to specific departments. Using consolidated billing combines usage from multiple accounts into a single invoice, which is the billing aggregation mechanism that enables the separation achieved by multiple accounts to be viewed together, rather than being an identification mechanism on its own.

## clf-c02/domain4/q942

Answer: A

AWS Organizations provides consolidated billing and Service Control Policies for effective cost management across multiple AWS accounts, enabling volume discounts through combined usage and governance controls to prevent overspending.
AWS Trusted Advisor inspects your existing AWS environment and provides recommendations across security, cost, performance, and fault tolerance, but operates primarily within individual accounts rather than providing a centralized cost management structure across multiple accounts. AWS Direct Connect provides a dedicated private network connection between on-premises infrastructure and AWS, and is a networking service with no capability for managing costs across multiple AWS accounts. Amazon Connect is a cloud contact center service for managing customer communications via voice and chat, and is a customer engagement service entirely unrelated to AWS account cost management.

## clf-c02/domain4/q943

Answer: C

On-Demand Instances are appropriate for a one-month pilot because they require no long-term commitment, the customer-facing application cannot risk interruption from Spot reclamation, and the short duration does not justify a Reserved Instance term.
Reserved Instances require a minimum one-year commitment, making them entirely unsuitable for a one-month pilot where the reservation term would far exceed the intended usage period. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, which is unacceptable for a customer-facing application that must remain consistently available throughout the pilot period. Dedicated Hosts provide physical server isolation for compliance and licensing purposes, and are priced at a premium over standard EC2 options, making them unnecessarily expensive for a standard one-month pilot application.

## clf-c02/domain4/q944

Answer: D

AWS Cost Explorer uses historical spending data and machine learning to automatically generate cost forecasts for up to 12 months ahead, making it the AWS tool that automatically forecasts future costs.
AWS Support Center is the portal for creating, viewing, and managing AWS support cases, and has no connection to cost forecasting or financial analysis. The AWS Cost and Usage Report provides the most granular breakdown of actual AWS charges already incurred, and is a historical billing analysis tool rather than a forecasting service. The AWS Pricing Calculator allows users to model AWS service configurations and estimate costs for new deployments, but requires manual input and does not automatically generate forecasts based on existing usage patterns the way Cost Explorer does.

## clf-c02/domain4/q946

Answer: D

AWS Organizations enables a master payer account to view consolidated billing reports across all member accounts, providing a unified view of spending and usage with the ability to apply governance policies.
AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than the service that enables consolidated billing report access through a master payer account. Amazon Macie is a data security service that uses machine learning to discover and protect sensitive data stored in Amazon S3, and is a security service with no connection to consolidated billing or master payer account reporting. Amazon QuickSight is a serverless business intelligence service for creating dashboards and visualisations from business data, and while it can visualise billing data it is not itself the service that enables consolidated billing through a master payer account structure.

## clf-c02/domain4/q949

Answer: A

Convertible Reserved Instances can be exchanged for other Convertible RIs from a different instance family, as long as the new RI has an equal or higher value, providing flexibility to adapt to changing needs.
Convertible RIs are Region-specific and cannot be exchanged for RIs in a different AWS Region. Only Standard Reserved Instances can be listed on the AWS Reserved Instance Marketplace, not Convertible RIs. Merging Convertible RIs to shorten their term is not a supported feature, as RI terms are fixed at one or three years and cannot be modified by combining reservations.

## clf-c02/domain4/q950

Answer: C

The AWS Pricing Calculator allows you to model the specific configuration of your EC2 instances, Elastic Load Balancer, and RDS database to generate a detailed and accurate monthly cost estimate before deployment.
Opening an AWS Support case to request a cost estimation is unnecessarily complex and time-consuming when a self-service tool like the AWS Pricing Calculator provides instant, detailed estimates without requiring support engagement. Collecting published prices and calculating manually is possible but error-prone and inefficient compared to the AWS Pricing Calculator, which automatically accounts for all pricing dimensions including data transfer, storage, and regional pricing variations. The AWS Cost and Usage Report provides granular data about actual AWS charges already incurred on active resources, and cannot be used to estimate the monthly cost of an architecture that has not yet been deployed.

## clf-c02/domain4/q956

Answer: B

Reserved Instances provide the most cost-effective pricing for a 3-year stateful workload with predictable, steady-state usage, offering up to 72% discount over On-Demand through a long-term commitment.
On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a workload running continuously for three years where the cost reduction from Reserved Instances would be substantial. Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing purposes, and are priced at a premium over standard EC2 options rather than providing cost savings for a standard stateful workload. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, making them unsuitable for a stateful workload that must remain continuously active and retain its state throughout the three-year period.

## clf-c02/domain4/q957

Answer: A

On-Demand Instances are most suitable for a short 7-hour task that cannot be interrupted, providing guaranteed availability with no long-term commitment and no risk of interruption during execution.
Reserved Instances require a minimum one-year commitment, making them entirely unsuitable for a single 7-hour task where the commitment period would vastly exceed the actual usage duration. Dedicated Hosts provide physical server isolation for compliance and licensing purposes, and are priced at a premium over standard EC2 options, making them unnecessarily expensive for a straightforward 7-hour task without isolation requirements. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, directly violating the requirement that the instance must run for 7 hours without interruptions.

## clf-c02/domain4/q958

Answer: C, D

AWS Trusted Advisor detects underutilized resources such as idle EC2 instances and unused load balancers to help reduce costs, and proactively monitors the AWS environment for security vulnerabilities and misconfigurations, making both cost optimization and security improvement core benefits of the service.
Providing high-performance container orchestration describes Amazon ECS or Amazon EKS, which are compute services for running containerised workloads, and is entirely unrelated to Trusted Advisor. Creating and rotating encryption keys describes AWS Key Management Service, which manages cryptographic keys for data protection, and is not a function of Trusted Advisor. Implementing enforced tagging across AWS resources describes a governance capability achieved through AWS Organizations Service Control Policies or AWS Config rules, and is not something Trusted Advisor can enforce.

## clf-c02/domain4/q965

Answer: D

The AWS Pricing Calculator is publicly accessible without an AWS account, allowing anyone to model AWS service configurations and generate cost estimates for almost all AWS services before committing to any deployment.
AWS Cost Explorer provides visualisation and analysis of actual AWS spending patterns and requires an active AWS account with usage history to generate meaningful data. The AWS Cost and Usage Report provides granular billing data for active AWS accounts, and requires an AWS account to be configured and generating charges before it can provide any data. AWS Budgets requires an active AWS account to set up cost and usage thresholds and send alerts, and cannot be used by someone without an account to estimate costs for AWS services.

## clf-c02/domain4/q967

Answer: C

A Partial Upfront Reserved Instance for one year provides meaningful savings over On-Demand while requiring less cash upfront than All Upfront, making it a cost-effective option for a database that must remain online continuously for a year.
Spot Instances can be interrupted by AWS when spare capacity is reclaimed, making them entirely unsuitable for a database server that must remain online continuously for a full year. On-Demand Instances charge the full hourly rate with no discount, making them significantly more expensive than Reserved Instances for a workload running continuously for a year with a predictable steady-state usage pattern. No Upfront Reserved Instances also provide a discount over On-Demand for a one-year commitment, but the discount is shallower than Partial Upfront because AWS does not receive any payment at the start of the term and therefore offers less incentive.

## clf-c02/domain4/q973

Answer: C

Sending an invitation from AnyCompany's AWS Organizations master account to Example Corp adds them to the organization, enabling consolidated billing under a single invoice and combined usage for volume discounts.
Requesting that an AWS solutions architect or TAM link accounts is not the self-service process for joining AWS Organizations. Account consolidation is configured directly through the AWS Organizations console without requiring AWS staff intervention. Creating a new support case requesting that both bills be combined is not the process for enabling consolidated billing, which is configured through AWS Organizations rather than through support requests. Migrating Example Corp's VPCs, EC2 instances, and other resources into AnyCompany's account would merge the infrastructure into a single account, which is a complex and disruptive migration entirely unnecessary when AWS Organizations can combine billing while keeping accounts separate.

## clf-c02/domain4/q974

Answer: B

AWS Budgets creates alerts when actual or forecasted costs exceed defined thresholds, sending notifications via email or SNS to help you manage spending proactively before bills reach unexpected levels.
AWS Cost Explorer provides interactive visualisations and analysis of historical AWS spending patterns with forecasting capability, and is an analysis tool rather than a threshold-based alerting service that sends notifications when costs exceed limits. The AWS Cost and Usage Report provides the most granular breakdown of actual charges by service, resource, and time period, and is a historical billing data tool rather than a service that creates and sends cost threshold alerts. AWS CloudTrail records API calls and account activity across your AWS environment for auditing and compliance purposes, and does not monitor billing or send alerts when spending exceeds defined cost thresholds.

## clf-c02/domain4/q976

Answer: A

All AWS users, including those on the Basic free support plan, have access to the seven core Trusted Advisor checks covering security and service limits, providing a baseline level of advisory guidance regardless of support tier.
Access to all Trusted Advisor checks requires a Business or Enterprise Support plan. Basic and Developer Support users are limited to the seven core checks and cannot access the full suite of recommendations across all five categories. Cost optimization checks are part of the full Trusted Advisor suite that requires Business or Enterprise Support, and are not available to all AWS users on the Basic plan. Fault tolerance checks are part of the full Trusted Advisor suite that requires Business or Enterprise Support, and are not available to all AWS users. Only the seven core checks spanning basic security and service limits are universally available.

## clf-c02/domain4/q982

Answer: D

Reserved Instances are the most cost-effective option for a consistent, long-running workload, providing significant discounts of up to 72% over On-Demand pricing in exchange for a one or three-year commitment.
Dedicated Hosts provide physical server isolation for compliance and licensing purposes, and are priced at a premium over standard EC2 options, making them more expensive rather than minimizing cost for a standard consistent workload. On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a workload running continuously at a consistent level where Reserved Instance savings would be substantial over time. Spot Instances can be interrupted by AWS when spare capacity is reclaimed, and the question specifies that compute resources must remain available, making Spot Instances unsuitable despite their lower cost.

## clf-c02/domain4/q983

Answer: A

AWS Health Dashboard provides personalized proactive notifications about scheduled maintenance, infrastructure changes, and lifecycle events that may affect your specific AWS resources, making it the purpose-built tool for identifying planned changes to AWS infrastructure.
AWS Trusted Advisor analyzes your AWS environment against best practice checks across cost, performance, security, and fault tolerance, and provides advisory recommendations rather than notifications about scheduled AWS infrastructure changes. The Billing Dashboard displays cost and usage summaries for your AWS account, and is a financial reporting tool with no connection to identifying scheduled infrastructure changes. AWS Config continuously tracks and records the configuration state of your AWS resources to assess compliance and detect changes you make, and does not provide information about scheduled changes to the AWS infrastructure itself.

## clf-c02/domain4/q986

Answer: A

AWS Budgets sends notifications when AWS costs or usage exceed custom-defined thresholds, enabling proactive spending management with alerts delivered via email or Amazon SNS.
AWS Cost Explorer provides visualisation and analysis of historical AWS spending and usage patterns with forecasting capability, and is an analysis tool rather than a threshold-based notification service that alerts when spending exceeds defined limits. AWS CloudTrail records API calls and account activity for auditing and compliance purposes, and does not monitor billing thresholds or send notifications when spending exceeds defined cost or usage limits. Amazon Macie is a data security service that uses machine learning to discover and protect sensitive data stored in Amazon S3, and is a security service entirely unrelated to cost monitoring or spending threshold notifications.

## clf-c02/domain4/q988

Answer: D

Spot Instances allow customers to purchase unused EC2 capacity at discounts of up to 90% compared to On-Demand pricing, with the trade-off that AWS may reclaim that capacity when needed.
Reserved Instances provide discounts through long-term commitments of one or three years and guarantee that capacity is available for the duration of the reservation, making them designed for steady predictable workloads rather than for purchasing unused spare capacity. On-Demand Instances are charged at the standard AWS rate with no discount, as they are the baseline pricing model that customers pay for guaranteed access to compute capacity on demand. Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing isolation purposes, and are priced at a premium over standard EC2 options rather than providing access to unused capacity at a discount.

## clf-c02/domain4/q1000

Answer: C

EC2 Reserved Instances provide the maximum savings for a steady-state 3-year workload, offering up to 72% discount over On-Demand pricing through a long-term commitment that matches the predictable usage pattern of a self-managed Oracle database.
EC2 Dedicated Instances run on hardware dedicated to a single customer for compliance and licensing purposes, and are priced at a premium over standard EC2 options rather than maximizing savings for a long-running database workload. EC2 Spot Instances can be interrupted by AWS when spare capacity is reclaimed, making them entirely unsuitable for a production Oracle database that must remain continuously available for steady-state operations. EC2 On-Demand Instances charge the full hourly rate with no discount, making them the most expensive option for a workload running continuously for three years where the substantial Reserved Instance savings would be foregone.

## clf-c02/domain4/q1002

Answer: A, C

Consolidated billing provides volume discounts by aggregating usage across all accounts to qualify for tiered pricing, and delivers a single combined invoice covering all member accounts in the organization.
A minimal additional fee for use is incorrect because consolidated billing itself is provided at no additional charge by AWS Organizations. The billing consolidation feature does not carry a separate per-account or per-usage fee. Instalment payment options are not a feature of consolidated billing. AWS charges are billed monthly based on actual usage, and there are no instalment or deferred payment arrangements associated with consolidated billing. Custom cost and usage budget creation is a feature of AWS Budgets, which is a separate cost management service that allows you to set spending thresholds and receive alerts, not a benefit of consolidated billing itself.

## clf-c02/domain4/q1003

Answer: A

On-Demand Instances are best for short-term traffic spikes that cannot be interrupted, providing maximum flexibility with no commitment and no risk of capacity interruption during the surge period.
Spot Instances use spare AWS capacity at significant discounts but can be interrupted at any time, directly violating the requirement that the application cannot be interrupted during the traffic spike. Reserved Instances require a one or three-year commitment and are designed for steady-state predictable workloads, making them a poor fit for handling an unexpected short-term traffic spike where the commitment would far exceed the actual usage period. Dedicated Hosts provide physical server isolation for compliance and licensing purposes at a premium price, and are unnecessary for handling a temporary traffic spike that has no isolation or licensing requirements.

## clf-c02/domain4/q1009

Answer: B

AWS enables expense control through auto-scaling, which automatically adjusts resources up or down based on actual demand, ensuring that you only pay for what is actually needed as usage changes unpredictably.
AWS does not refund the cost difference if a customer moves to larger servers. Instance resizing is a configuration change that affects future charges, and there is no refund mechanism for moving between instance sizes. Spot Instances are not automatically used when their price is lower than On-Demand. Using Spot Instances requires deliberate configuration through launch templates, Auto Scaling groups, or Spot Fleet requests rather than automatic switching. Amazon CloudWatch monitors metrics and can trigger scaling actions through Auto Scaling policies, but does not itself automatically predict or provision the specific resources needed. Prediction requires configuring predictive scaling or target tracking policies rather than being a default CloudWatch behavior.

## clf-c02/domain4/q1019

Answer: C

AWS Compute Optimizer uses machine learning to analyze historical utilization metrics and provide recommendations for optimal EC2 instance types, right-sizing suggestions, and configuration improvements to reduce costs while maintaining performance.
AWS Trusted Advisor provides recommendations across security, cost, performance, and fault tolerance based on best practice checks, and while it can flag underutilized instances it does not use machine learning to analyze detailed utilization patterns for granular right-sizing recommendations. AWS Cost Explorer provides visualisation and analysis of spending and usage patterns with forecasting capability, and while it includes a right-sizing recommendation feature it is primarily a cost analysis tool rather than a machine learning-based resource optimization service. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a machine learning-based service for analyzing resource configuration and utilization.

## clf-c02/domain4/q1020

Answer: B

AWS Compute Optimizer recommends optimal AWS resource configurations by analyzing utilization data using machine learning models, providing specific instance type recommendations based on actual CPU, memory, and network usage patterns.
Amazon Inspector is an automated security assessment service that scans EC2 instances and container images for software vulnerabilities and unintended network exposure, and is a security tool with no capability to analyze utilization metrics or recommend optimal instance types. AWS Config continuously tracks and records the configuration state of AWS resources to assess compliance against desired settings, and focuses on configuration compliance rather than analyzing performance metrics to recommend right-sized instance types. AWS Cost Explorer provides visualisation and analysis of spending and usage patterns and includes a basic right-sizing recommendation feature, but is primarily a cost management tool rather than a dedicated machine learning-based service for EC2 instance optimization.

## clf-c02/domain4/q1021

Answer: B

AWS Cost Anomaly Detection uses machine learning to continuously monitor cost and usage patterns and detect unusual spending that deviates from expected norms, sending alerts when anomalies are identified without requiring manual threshold configuration.
AWS Budgets allows you to set custom spending and usage thresholds and receive alerts when those thresholds are exceeded, but requires you to manually define the expected spending levels rather than automatically detecting anomalies using machine learning. AWS Trusted Advisor provides best practice recommendations across security, cost, performance, and fault tolerance, and while it flags some cost inefficiencies it does not continuously monitor spending patterns to automatically detect unusual cost anomalies. Amazon GuardDuty is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity and anomalous behavior using machine learning, and is a security threat detection service rather than a cost anomaly monitoring service.

## clf-c02/domain4/q1022

Answer: C

AWS Cost Anomaly Detection automatically learns your spending patterns and uses machine learning to identify unexpected cost increases without requiring users to define specific thresholds, sending alerts when anomalies are detected.
AWS Cost Explorer provides interactive visualisations and analysis of historical spending with forecasting capability, and while it shows spending trends it does not automatically detect anomalies or send alerts without user-defined thresholds. AWS Budgets requires users to define specific cost and usage thresholds before it can send alerts, meaning it cannot identify unexpected changes without prior manual configuration of expected spending levels. The AWS Pricing Calculator is used to estimate future costs for planned AWS deployments before resources are provisioned, and has no capability to monitor active spending patterns or detect unexpected cost changes.

## clf-c02/domain4/q1040

Answer: C

AWS Savings Plans offer flexible pricing with up to 72% savings on compute usage in exchange for a one or three-year commitment to a consistent spend level, applying automatically across EC2 instance families, sizes, operating systems, and tenancy.
Reserved Instances provide significant discounts but are locked to a specific instance family, size, operating system, and region unless they are Convertible RIs, making them less flexible than Savings Plans which apply automatically across these dimensions. Spot Instances offer discounts of up to 90% by using spare AWS capacity, but can be interrupted by AWS at any time and do not provide the consistent availability or flexibility across instance families that Savings Plans offer. Dedicated Hosts provide physical server isolation for compliance and licensing purposes, and are priced at a premium over standard EC2 options rather than providing the flexible compute savings that Savings Plans are designed to deliver.

## clf-c02/domain4/q1041

Answer: B

Compute Savings Plans provide flexibility across instance families, sizes, operating systems, tenancy, and regions, while Standard Reserved Instances are locked to a specific instance type, operating system, and region.
Savings Plans are available with one or three-year commitments, not a five-year commitment. Both Savings Plans and Reserved Instances are available with the same one and three-year term options. Reserved Instances do not offer greater discounts than Savings Plans as a general rule. Both can offer similar discount levels, and Compute Savings Plans can match or exceed the discounts of many Reserved Instance configurations while offering greater flexibility. Savings Plans apply to EC2 instances, AWS Fargate, and AWS Lambda compute usage, not exclusively to EC2. Reserved Instances are also available for services beyond EC2 including RDS and ElastiCache, so neither option is exclusively limited to EC2.

## clf-c02/domain4/q1055

Answer: B

AWS Cost Categories allows you to create custom groupings of your cost and usage data by mapping costs into meaningful categories aligned with your business structure, enabling chargeback and showback reporting for internal departments.
AWS Cost Explorer provides interactive visualisations and analysis of spending patterns with filtering capabilities, and while it can display costs by tag it does not provide a dedicated mechanism for creating custom named cost categories for chargeback mapping. AWS Cost Allocation Tags enable you to label individual resources with department metadata so their costs appear separately in billing reports, but tags operate at the resource level and require consistent application rather than providing a higher-level category mapping framework. AWS Budgets lets you set custom cost and usage thresholds and receive alerts when those thresholds are exceeded, and is a cost governance and alerting tool rather than a service for creating custom cost category structures for chargeback purposes.

## clf-c02/domain4/q1089

Answer: C

Under the AWS Business Support plan, a production system impaired case, where the workload is experiencing degraded performance but has not completely stopped, has a target initial response time of less than 4 hours, reflecting the elevated urgency of an affected production environment that has not yet reached the highest severity level.
Less than 24 hours is the target response time for general guidance cases under the Business Support plan, which apply to questions and requests that do not involve any impact to a running production system and represent the lowest priority level. Less than 12 hours is the target response time for a system impaired case under the AWS Developer Support plan, and is not the correct SLA for production system impaired cases under the Business Support plan, which provides faster response times than Developer Support for production-affecting issues. Less than 1 hour is the target response time for a production system down case under the Business Support plan, which applies when a production workload has completely stopped functioning and represents a higher severity level than production system impaired.

## clf-c02/domain4/q1090

Answer: B

AWS Business Support provides 24/7 access to Cloud Support Engineers through phone, email, and chat channels, while AWS Developer Support provides access to Cloud Support Associates only during business hours and only via email, making round-the-clock multi-channel technical support a key differentiator of the Business plan.
A Technical Account Manager (TAM) is exclusively available to customers on the AWS Enterprise Support and Enterprise On-Ramp plans and is not included in either Developer or Business Support, so this does not describe a difference between these two plans. Access to the full set of AWS Trusted Advisor checks is a feature of Business, Enterprise On-Ramp, and Enterprise Support plans; Developer Support provides access to only the seven core Trusted Advisor checks, meaning Business Support offers broader Trusted Advisor coverage than Developer Support, not narrower. AWS Business Support is available to any AWS customer who chooses to purchase it regardless of AWS Partner status, and is not restricted to members of the AWS Partner Network.

## clf-c02/domain4/q1091

Answer: D

AWS Enterprise Support is the only plan that provides a target response time of less than 15 minutes for business-critical system down cases, where a production system supporting critical business operations has become completely unavailable, reflecting the highest urgency level in the AWS support tier structure.
AWS Developer Support targets a response time of less than 12 hours for system impaired cases and does not offer a production or business-critical system down severity category, making it insufficient for any workload requiring guaranteed sub-hour response times. AWS Business Support targets a response time of less than 1 hour for production system down cases, which is faster than Developer Support but does not meet the sub-15-minute guarantee that only the most premium support tiers provide. AWS Enterprise On-Ramp Support targets a response time of less than 30 minutes for business-critical system down cases, which is faster than Business Support but still does not achieve the sub-15-minute response guarantee that only the full AWS Enterprise Support plan provides.

## clf-c02/domain4/q1115

Answer: C

Service Quotas is a centralized service that allows customers to view their current service limits across AWS services, track utilization against those limits, and request quota increases directly from the console, providing a single place to manage all resource limits.
AWS Trusted Advisor includes a service limits check that flags when usage approaches certain default limits, but it only monitors a subset of limits and does not provide the ability to view all quotas or submit increase requests directly. AWS Organizations is an account management service for governing multiple AWS accounts through policies and consolidated billing, and does not provide visibility into or management of individual service resource limits. AWS Config records and evaluates the configuration of AWS resources against compliance rules, and monitors resource settings rather than tracking or managing service-level resource limits.

## clf-c02/domain4/q1116

Answer: B

Service Quotas allows customers to view their current quota values for AWS services, monitor usage against those quotas, and submit requests to increase specific limits such as the maximum number of VPCs per Region, all from a single console.
AWS Support can be used to submit a support case to request limit increases, but Service Quotas provides a more direct and self-service approach specifically designed for viewing and managing resource limits without needing to create a support case. AWS Config tracks the configuration state of AWS resources and evaluates compliance against rules, but it does not monitor or manage service quota limits or provide the ability to request increases. AWS Budgets is a cost management tool for setting spending and usage thresholds and receiving alerts when those thresholds are approached, and has no capability to view or manage service resource limits.

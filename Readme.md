# 题目三

## 已完成部分

*   用python实现简单的nmap功能，多线程扫描打开的端口

*   根据端口查找服务（没有版本信息）

## 需要商量的部分

*   python集成nmap功能

    *   主机存活状态:根据目标的反应来确定它是否处于开机并联网的状态

    *   开放的端口扫描∶根据目标端口的反应来判断它是否开放

    *   服务及版本检测:检测它运行服务的服务类型和版本

    *   操作系统检测:识别主机的操作系统

*   python-nmap其实只是一个库，但是有了这个库甚至可以不需要指纹算法

## 未完成部分

*   主机操作系统的扫描

*   服务对应的版本信息（python-nmap）可以完成

*   应用服务、服务开发框架、中间件、虚拟化软件的扫描

*   硬件扫描

*   扫描路由器和路由器下的其他IP和端口

*   网络拓扑图，前端页面+echarts（或者其他思路）

*   指纹识别算法的接口实现（用来计算版本）

*   关联开放数据库
## 测试用例
*   现在如果想直接跑通的话，先只看main.py和scan_port.py，其余在开发中。
*   ![image](https://user-images.githubusercontent.com/92193510/187325128-871f6c0f-f72e-41ac-9aaa-4b3631f4ea3c.png)
*   ![image](https://user-images.githubusercontent.com/92193510/187325198-b87e3fc6-65be-451c-b3b9-37d62f3f306a.png)

*   ![image](https://user-images.githubusercontent.com/92193510/187325164-7ae5706b-1873-4e04-ae00-87c63fa35d19.png)


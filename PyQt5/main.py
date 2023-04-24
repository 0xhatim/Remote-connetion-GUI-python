from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal
import sys, socket
from app import Ui_Dialog
import threading
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import datetime
import autopy

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ip = ""
        self.port = ""
        self.server_socket = None
        self.client_socket = None
        self.connected_ips = {}

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Controller | Connection Info IP:PORT")
        self.ui.tabWidget.tabBar().setVisible(False)
        self.ui.ConnectButton.clicked.connect(self.connect)
        self.ui.pushButton.clicked.connect(self.SendCommand)
        self.ui.pushButton_2.clicked.connect(self.sendAlll)

                # create the table view and set its model
        self.ui.tableView 
        self.model = QStandardItemModel()
        self.ui.tableView .setModel(self.model)

        # add columns to the model
        self.model.setColumnCount(2)
        self.model.setHorizontalHeaderLabels(['IP', 'Datetime'])

    def SendCommand(self):
        IDDD = int(self.ui.comboBox.currentText())

        cmd = self.ui.lineEdit_3.text()
        x = self.connected_ips[IDDD]

        for key,value in x.items():
            ip = value
            client_var = key
        threading.Thread(target=self.send_message, args=(cmd,ip,client_var,)).start()

        #self.send_message(cmd,ip,client_var)
    def sendAlll(self):
        cmd = self.ui.lineEdit_3.text()
        threading.Thread(target=self.send_all, args=(cmd,)).start()

        #self.send_all(cmd)
    def connect(self):
        self.ip = self.ui.lineEdit.text()
        try:

            self.port = int(self.ui.lineEdit_2.text())
        except ValueError:
            self.ui.status_label.setText("Invalid Port")
            return   
   # Check if IP and port are valid
        if not self.ip or not self.port:
            self.ui.status_label.setText("Invalid IP or Port")
            return

        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5) # Queue 5 
        print(f"Server listening on {self.ip}:{self.port}")

        # start thread to accept incoming connections
        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()



        self.ui.status_label.setText("Connecting...")
        self.ui.ConnectButton.setEnabled(False)
        self.on_connected()

    def accept_connections(self):
        
        while True:
            self.client_socket , address = self.server_socket.accept() # address for ip 
            connection_varible = self.client_socket
            print(f"Connection established from {address}")
            IDD = len(self.connected_ips)+1
            self.connected_ips[IDD] = {connection_varible:address[0]}
            row1 = [QStandardItem(f'{address[0]}'), QStandardItem(f'{datetime.datetime.now()}')]
            self.model.appendRow(row1)
            row1 =[]
            self.ui.comboBox.addItem(f"{IDD}")


    def send_all(self, message):
        
  
        for i in self.connected_ips.keys():
            i = self.connected_ips[i]

            for key,value in i.items():
                ip = value
                client_var = key

            self.send_message(message,ip,client_var)
    def send_message(self, message, ip,client_varible):

        client_varible.sendto(bytes(message, "utf-8"), (ip, self.port))
        print(f"Sent message: {message} to {ip}")
        response = self.client_socket.recv(1024).decode()
        autopy.alert.alert(response,"Controller Message")
        self.ui.label_6.setText(f"successefuly send command to {ip}")


    def on_connected(self):
        print("connect thread done ")
        self.setWindowTitle(f"Controller | Listen : {self.port} ")
        self.ui.status_label.setText("Connected")
        self.ui.ConnectButton.hide()
        self.ui.tabWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

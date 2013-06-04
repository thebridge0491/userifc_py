import QtQuick 1.1

Rectangle {
	id: rectangle1
	width: 150; height: 75
	color: "light gray"

	function on_button1_clicked() {
		//if (process.env.HANDLERUSE_JAVASCRIPT) {
		if ("undefined" == typeof handler) {
			//console.log("grey button clicked");
			simplebutton1.opacity = 0;
			entry1.text = "";
			simpleentry1.opacity = 1;
			entry1.focus = 1;
		} else {
			handler.on_button1_clicked();
		}
	}
	
	function on_entry1_returnPressed() {
		//if (process.env.HANDLERUSE_JAVASCRIPT) {
		if ("undefined" == typeof handler) {
			//console.log("entry accepted");
			simpleentry1.opacity = 0;
			simplebutton1.opacity = 1;
			textview1.text = "Hello, " + entry1.text + ".";
		} else {
			handler.on_entry1_returnPressed();
		}
	}
	
	Grid {
		id: grid1
		width: parent.width; height: parent.height
		columns: 1
		spacing: 5
		
		Rectangle {
			id: simplelabel1
			color: "dark gray"
			width: parent.width; height: parent.height / 3
			radius: 10
			
			Text {
        id: label1
        text: "label1"
        width: parent.width; height: parent.height
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
			}
		}
		
		Rectangle {
			id: simplebutton1
			objectName: "simplebutton1"
			color: "grey"
			width: parent.width; height: parent.height / 3
			opacity: 1
			radius: 10
			 
			Text {
				id: button1
				objectName: "button1"
				text: "button1"
				width: parent.width; height: parent.height
				horizontalAlignment: Text.AlignHCenter
				verticalAlignment: Text.AlignVCenter
			}
			
			MouseArea {
				anchors.fill: parent
				onClicked: on_button1_clicked();
				//onClicked: handler.on_button1_clicked();
			}
		}
		
		Rectangle {
			id: simpleentry1
			objectName: "simpleentry1"
			width: parent.width; height: 20; radius: 10
			opacity: 0
			
			TextInput {
				id: entry1
				objectName: "entry1"
				focus: true
				onAccepted: on_entry1_returnPressed();
				//onAccepted: handler.on_entry1_returnPressed();
			}
		}

		TextEdit {
			id: textview1
			objectName: "textview1"
			width: parent.width; height: parent.height / 3
			
			Keys.onReturnPressed: {
				//console.log("return pressed")
			}
			//onTextChanged: console.log("text changed")
		}
	}
}

// preview: [QT_QUICK_BACKEND=software] qmlscene helloForm-qt4.qml

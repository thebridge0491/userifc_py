#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <QtGui>
#include <QApplication>

#include "ui_helloForm-qt.h"

//#define QStringLiteral(str) QString::fromUtf8("" str "", sizeof(str) - 1)

class HelloQtDemo : public QStackedWidget {
    Q_OBJECT

public:
    HelloQtDemo(QStackedWidget *parent = 0);
    
    //virtual ~HelloQtDemo(void);

    QWidget *form1;
    QWidget *dialog1;
    QLabel *label1;
    QPushButton *button1;
    QPlainTextEdit *textview1;
    QLineEdit *entry1;
    QBoxLayout *vertLayout1;
    QBoxLayout *vertLayout2;

private slots:
    void on_button1_clicked(void);
    void on_entry1_textChanged(QString);
    void on_entry1_returnPressed(void);

private:
    Ui::stackedWidget1 ui;
};

HelloQtDemo::HelloQtDemo(QStackedWidget *parent) : QStackedWidget(parent) {
    /*form1 = new QWidget;
    dialog1 = new QWidget;
    label1 = new QLabel("label1", form1);
    button1 = new QPushButton("button1", form1);
    textview1 = new QPlainTextEdit(form1);
    entry1 = new QLineEdit(dialog1);
    vertLayout1 = new QBoxLayout(QBoxLayout::Direction::TopToBottom, form1);
    vertLayout2 = new QBoxLayout(QBoxLayout::Direction::TopToBottom, dialog1);

    vertLayout1->addWidget(label1);
    vertLayout1->addWidget(button1);
    vertLayout1->addWidget(textview1);
    vertLayout2->addWidget(entry1);
    this->addWidget(form1);
    this->addWidget(dialog1);

    this->setWindowTitle("HelloQtDemo");
    this->setWindowModality(Qt::NonModal);
    this->resize(274, 278);
    this->setEnabled(1);
    */
    ui.setupUi(this);

    form1 = ui.form1;
    dialog1 = ui.dialog1;
    textview1 = ui.textview1;
    entry1 = ui.entry1;
    
    /*QObject::connect(button1, SIGNAL(clicked()), this, 
        SLOT(on_button1_clicked()));
    QObject::connect(entry1, SIGNAL(textChanged(QString)), this, 
        SLOT(on_entry1_textChanged(QString)));
    QObject::connect(entry1, SIGNAL(returnPressed()), this, 
        SLOT(on_entry1_returnPressed()));*/
    //form1->connect(button1, SIGNAL(clicked()), this,
    //    SLOT(on_button1_clicked()));
    dialog1->connect(entry1, SIGNAL(textChanged(QString)), this,
        SLOT(on_entry1_textChanged(QString)));
    dialog1->connect(entry1, SIGNAL(returnPressed()), this,
        SLOT(on_entry1_returnPressed()));

    this->show();
    this->setCurrentIndex(this->indexOf(form1));
}

//HelloQtDemo::~HelloQtDemo(void) {
//    
//}

void HelloQtDemo::on_button1_clicked(void) {
    entry1->setText("");
    entry1->setFocus();
    this->setCurrentIndex(this->indexOf(dialog1));
}

void HelloQtDemo::on_entry1_textChanged(QString) {
    this->textview1->setPlainText("Hello, " + entry1->text() + ".");
}

void HelloQtDemo::on_entry1_returnPressed(void) {
    this->setCurrentIndex(this->indexOf(form1));
}

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    
    char pretextBuf[256];
    snprintf(pretextBuf, sizeof(pretextBuf) - 1,
        "(GCC %d.%d) Qt version: %s\n", __GNUC__, 
        __GNUC_MINOR__, qVersion());

    HelloQtDemo gui;
    gui.textview1->setPlainText(pretextBuf);

    exit(app.exec());
}

#include "moc_HelloQtDemo.cpp"


// uic helloForm-qt.ui -o build/ui_helloForm-qt.h
// moc HelloQtDemo.cpp -o build/moc_HelloQtDemo.cpp
// c++ -fPIC -I build HelloQtDemo.cpp -o build/main-HelloQtDemo `pkg-config --cflags --libs QtCore QtGui QtWidgets opengl`
// build/main-HelloQtDemo

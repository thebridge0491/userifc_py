#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <QtGui>
#include <QtQml>
#include <QQmlApplicationEngine>
//#include <QDeclarativeView>
//#include <QDeclarativeEngine>
#include <QApplication>

//#define QStringLiteral(str) QString::fromUtf8("" str "", sizeof(str) - 1)

class HelloQtquickDemo : public QObject {
    Q_OBJECT

public:
    explicit HelloQtquickDemo(QObject *parent = 0);
    
    //virtual ~HelloQtquickDemo(void);
    
    QQmlApplicationEngine *engine;
    QObject *rootObject;
    QWindow *decl_view;
    
    QObject *button1;
    QObject *entry1;
    QObject *textview1;
    QObject *simplebutton1;
    QObject *simpleentry1;

public slots:
    void on_button1_clicked(void);
    void on_entry1_textChanged(QString);
    void on_entry1_returnPressed(void);

private:
    
};

HelloQtquickDemo::HelloQtquickDemo(QObject *parent) : QObject(parent) {
    std::string rsrc_path = getenv("RSRC_PATH") ? getenv("RSRC_PATH") : 
        "resources";
    //QT_VERSION_MAJOR depends on compile: Qt5Core or Qt4Core
    std::string uiform = rsrc_path + "/" + ((4 == QT_VERSION_MAJOR) ? 
        "qt/helloForm-qt4.qml" : "qt/helloForm-qt5.qml");
    
    if (4 != QT_VERSION_MAJOR) {
        //this->engine = new QQmlApplicationEngine(uiform.c_str());
        //this->engine = new QQmlApplicationEngine(
        //    QUrl::fromLocalFile(QStringLiteral(uiform)));
        this->engine = new QQmlApplicationEngine();
        //this->engine->load(QUrl::fromLocalFile(
        //    QStringLiteral(uiform.c_str())));
        this->engine->load(QUrl::fromLocalFile(uiform.c_str()));
        this->rootObject = engine->rootObjects().first();
        this->decl_view = (QWindow*)this->rootObject;
    } else {
        /*//this->decl_view = new QDeclarativeView(uiform.c_str());
        this->decl_view = new QDeclarativeView(
            QUrl::fromLocalFile(QStringLiteral(uiform)));
        this->decl_view->setResizeMode(
            QDeclarativeView::SizeRootObjectToView);
        this->rootObject = this->decl_view->rootObject();
        this->engine = this->decl_view->engine();*/
    }
    
    this->button1 = this->rootObject->findChild<QObject*>("button1");
    this->entry1 = this->rootObject->findChild<QObject*>("entry1");
    this->textview1 = this->rootObject->findChild<QObject*>("textview1");
    this->simplebutton1 = this->rootObject->findChild<QObject*>(
        "simplebutton1");
    this->simpleentry1 = this->rootObject->findChild<QObject*>(
        "simpleentry1");
    
    /*QObject::connect(button1, SIGNAL(clicked()), this, 
        SLOT(on_button1_clicked()));
    QObject::connect(entry1, SIGNAL(textChanged(QString)), this, 
        SLOT(on_entry1_textChanged(QString)));
    QObject::connect(entry1, SIGNAL(returnPressed()), this, 
        SLOT(on_entry1_returnPressed()));*/
    this->engine->rootContext()->setContextProperty("handler", this);
    
    this->decl_view->setGeometry(400, 300, 240, 160);
    this->decl_view->show();
}

//HelloQtquickDemo::~HelloQtquickDemo(void) {
//    ;
//}

void HelloQtquickDemo::on_button1_clicked(void) {
    this->simplebutton1->setProperty("opacity", 0);
    this->entry1->setProperty("text", "");
    this->simpleentry1->setProperty("opacity", 1);
    this->entry1->setProperty("focus", 1);
}

void HelloQtquickDemo::on_entry1_textChanged(QString) {
    this->textview1->setProperty("text", "Hello, " + 
        this->entry1->property("text").toString() + ".");
}

void HelloQtquickDemo::on_entry1_returnPressed(void) {
    this->simpleentry1->setProperty("opacity", 0);
    this->simplebutton1->setProperty("opacity", 1);
    this->textview1->setProperty("text", "Hello, " + 
        this->entry1->property("text").toString() + ".");
}

int main(int argc, char *argv[]) {
    //fprintf(stderr, "QT_VERSION_MAJOR: %d\n", QT_VERSION_MAJOR);
    setenv("QT_QUICK_BACKEND", getenv("QT_QUICK_BACKEND") ?
        getenv("QT_QUICK_BACKEND") : "software", 1);
    QApplication app(argc, argv);
    
    char pretextBuf[256];
    snprintf(pretextBuf, sizeof(pretextBuf) - 1,
        "(GCC %d.%d) Qt version: %s\n", __GNUC__, 
        __GNUC_MINOR__, qVersion());

    HelloQtquickDemo gui;
    //QObject::connect(gui.engine, SIGNAL(quit()), &app, SLOT(quit()));
    gui.textview1->setProperty("text", pretextBuf);

    exit(app.exec());
}

#include "moc_HelloQtquickDemo.cpp"


// moc HelloQtquickDemo.cpp -o build/moc_HelloQtquickDemo.cpp
// c++ -fPIC -I build HelloQtquickDemo.cpp -o build/main-HelloQtquickDemo `pkg-config --cflags --libs QtCore QtGui QtWidgets QtQml opengl`
// build/main-HelloQtquickDemo

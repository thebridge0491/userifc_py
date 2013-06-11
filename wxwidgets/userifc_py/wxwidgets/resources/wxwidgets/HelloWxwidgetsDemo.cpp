#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <unistd.h>
#include "wx/wx.h"
#include "wx/xrc/xmlres.h"
#include "wx/app.h"

class HelloWxwidgetsDemo {
public:
    HelloWxwidgetsDemo(const wxString& title = "HelloWxwidgetsDemo");
    //HelloWxwidgetsDemo(void);
    //HelloWxwidgetsDemo(HelloWxwidgetsDemo const &orig);
    //virtual ~HelloWxwidgetsDemo(void);
    
    void on_frame1_closed(wxCloseEvent& event);
    void on_dialog1_closed(wxCloseEvent& event);
    void on_button1_clicked(wxCommandEvent& event);
    void on_entry1_textChanged(wxCommandEvent& event);
    void on_entry1_returnPressed(wxCommandEvent& event);
    
    wxFrame* frame1;
    
private:
    //wxFrame* frame1;
    wxStaticText* label1;
    wxButton* button1;
    wxTextCtrl* textview1;
    wxDialog* dialog1;
    wxTextCtrl* entry1;
};

HelloWxwidgetsDemo::HelloWxwidgetsDemo(const wxString& title) {
    /*frame1 = new wxFrame(NULL, wxID_ANY, title, wxDefaultPosition,
        wxSize(219, 174), wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL);
    label1 = new wxStaticText(frame1, wxID_ANY, "label1");
    button1 = new wxButton(frame1, wxID_ANY, "button1");
    textview1 = new wxTextCtrl(frame1, wxID_ANY, "",
        wxDefaultPosition, wxSize(160, 80), wxTE_MULTILINE|wxTE_WORDWRAP);
    dialog1 = new wxDialog(NULL, wxID_ANY, "dialog1", wxDefaultPosition,
        wxSize(169, 73), wxDEFAULT_DIALOG_STYLE);
    entry1 = new wxTextCtrl(dialog1, wxID_ANY, "entry1", wxDefaultPosition,
        wxDefaultSize, wxTE_PROCESS_ENTER);
    frame1->SetSizer(new wxBoxSizer(wxVERTICAL));
    dialog1->SetSizer(new wxBoxSizer(wxVERTICAL));
    wxSizer *vbox1 = frame1->GetSizer();
    wxSizer *dialog_vbox1 = dialog1->GetSizer();
    vbox1->Add(label1, 0, wxALIGN_CENTER, 0);
    vbox1->Add(button1, 0, wxALIGN_CENTER, 0);
    vbox1->Add(textview1, 0, wxALIGN_CENTER, 0);
    dialog_vbox1->Add(entry1, 0, wxALIGN_CENTER, 0);
    frame1->Layout();
    dialog1->Layout();
    */
    std::string rsrc_path = getenv("RSRC_PATH") ? getenv("RSRC_PATH") : 
		"resources";
    std::string uiform = rsrc_path + "/" + 
        "wxwidgets/helloForm-wxwidgets.xrc";
    
    wxXmlResource::Get()->InitAllHandlers();
    wxXmlResource::Get()->SetFlags(wxXRC_USE_LOCALE | wxXRC_USE_ENVVARS);
    if (!wxXmlResource::Get()->Load(uiform))
        return;
    frame1 = wxXmlResource::Get()->LoadFrame(NULL, "frame1");
    frame1->SetTitle(title);
    label1 = XRCCTRL(*frame1, "label1", wxStaticText);
    button1 = XRCCTRL(*frame1, "button1", wxButton);
    textview1 = XRCCTRL(*frame1, "textview1", wxTextCtrl);
    dialog1 = wxXmlResource::Get()->LoadDialog(NULL, "dialog1");
    entry1 = XRCCTRL(*dialog1, "entry1", wxTextCtrl);
    
    frame1->Bind(wxEVT_CLOSE_WINDOW, &HelloWxwidgetsDemo::on_frame1_closed,
        this);
    dialog1->Bind(wxEVT_CLOSE_WINDOW, &HelloWxwidgetsDemo::on_dialog1_closed,
        this);
    button1->Bind(wxEVT_BUTTON, &HelloWxwidgetsDemo::on_button1_clicked,
        this);
    entry1->Bind(wxEVT_TEXT, &HelloWxwidgetsDemo::on_entry1_textChanged,
        this);
    entry1->Bind(wxEVT_TEXT_ENTER,
        &HelloWxwidgetsDemo::on_entry1_returnPressed, this);
    
    frame1->Show(true);
}

//HelloWxwidgetsDemo::HelloWxwidgetsDemo(const HelloWxwidgetsDemo& orig) {
//    ;
//}

//HelloWxwidgetsDemo::~HelloWxwidgetsDemo(void) {
//    ;
//}

void HelloWxwidgetsDemo::on_frame1_closed(wxCloseEvent& WXUNUSED(event)) {
    wxExit();
}

void HelloWxwidgetsDemo::on_dialog1_closed(wxCloseEvent& WXUNUSED(event)) {
    frame1->Close();
}

void HelloWxwidgetsDemo::on_button1_clicked(wxCommandEvent& WXUNUSED(event)) {
    frame1->Hide();
    dialog1->Show(true);
    entry1->SetFocus();
    entry1->SetValue("");
}

void HelloWxwidgetsDemo::on_entry1_textChanged(wxCommandEvent& WXUNUSED(event)) {
    ;
}

void HelloWxwidgetsDemo::on_entry1_returnPressed(wxCommandEvent& WXUNUSED(event)) {
    textview1->SetValue("Hello, " + entry1->GetValue() + ".");
    dialog1->Hide();
    frame1->Show(true);
}

class App : public wxApp {
public:
    virtual bool OnInit() wxOVERRIDE;
};

wxIMPLEMENT_APP_NO_MAIN(App);
int main(int argc, char** argv) {
    ////wxString wxVer(wxVERSION_STRING); //wxVer.mb_str().data()
    //const char *wxVer = (new wxString(wxVERSION_STRING))->mb_str().data();
    //fprintf(stderr, "(GCC %d.%d) WxGtk %s GUI\n", __GNUC__, 
	//	__GNUC_MINOR__, wxVer);
    
	wxEntryStart(argc, argv);
    wxTheApp->CallOnInit();
    wxTheApp->OnRun();
    //wxTheApp->MainLoop();
      
    exit(EXIT_SUCCESS);
}
//wxIMPLEMENT_APP(App);
wxIMPLEMENT_WX_THEME_SUPPORT;

bool App::OnInit() {
    if (!wxApp::OnInit())
        return false;
    //wxString wxVer(wxVERSION_STRING); //wxVer.mb_str().data()
    const char *wxVer = (new wxString(wxVERSION_STRING))->mb_str().data();
    char pretextBuf[256];
    snprintf(pretextBuf, sizeof(pretextBuf) - 1,
        "(GCC %d.%d) WxGtk %s GUI\n", __GNUC__, 
		__GNUC_MINOR__, wxVer);
    HelloWxwidgetsDemo *gui = new HelloWxwidgetsDemo("HelloWxwidgetsDemo");
    //this->SetTopWindow(gui->frame1);
    gui->textview1->SetValue(pretextBuf);
    
    return true;
}


// c++ HelloWxwidgetsDemo.cpp -o build/main-HelloWxwidgetsDemo `wx-config --cflags --libs core xrc`
// build/main-HelloWxwidgetsDemo

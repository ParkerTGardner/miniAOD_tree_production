#include "TH2D.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TPad.h"
#include "TProfile.h"
#include "TGraph.h"
#include <vector>
#include "math.h"
#include "TRandom3.h"
#include "TMath.h"
#include "TFile.h"
#include "TTree.h"
#include "TCutG.h"
#include <numeric>
#include "coordinateTools.h"

using TMath::ATan;
using TMath::Exp;


void Drawer()
{
    TFile *f = new TFile("equal_miniAOD.root");
  /*  
    TCanvas* cA = new TCanvas("cA","cA" , 1000, 1000);
    TCanvas* cB = new TCanvas("cB","cB" , 1000, 1000);
    TCanvas* cC = new TCanvas("cC","cC" , 1000, 1000);


    TH2D* h1 = (TH2D*)f->Get(Form("hSig_%d_%d",1,1));
    TH2D* h2 = (TH2D*)f->Get(Form("hBck_%d_%d",1,1));
    
    cA->cd();
    h1->DrawCopy("COLZ");
    cB->cd();
    h2->Draw("COLZ");

    h1->Divide(h2);
    cC->cd();
    h1->Draw("COLZ");
  */

    TH1::SetDefaultSumw2(kFALSE);
    TH2::SetDefaultSumw2(kFALSE);

	int trackbin = 3;
	int ptbin = 5;

    TCanvas* c1          = new TCanvas("c1","c1" , 1000, 1000);
    c1->Divide(ptbin,trackbin);
    TCanvas* c2          = new TCanvas("c2","c2" , 1000, 1000);
    c2->Divide(ptbin,trackbin);

    //TCanvas* c3          = new TCanvas("c3","c3" , 1000, 1000);
    //c3->Divide(ptbin,trackbin);
    //TCanvas* c4          = new TCanvas("c4","c4" , 1000, 1000);
    //c4->Divide(ptbin,trackbin);


    TCanvas* c1Y         = new TCanvas("c1Y","c1Y" , 1000, 1000);
    c1Y->Divide(ptbin,trackbin);
    //TCanvas* c1Y_sub     = new TCanvas("c1Y_sub","c1Y_sub" , 1000, 1000);
    //c1Y_sub->Divide(ptbin,trackbin);
    //TCanvas* c1X         = new TCanvas("c1X","c1X" , 1000, 1000);
    //c1X->Divide(5,3);
    //TCanvas* c1X_sub     = new TCanvas("c1X_sub","c1X_sub" , 1000, 1000);
    //c1X_sub->Divide(5,3);

    for(int wtrk =1; wtrk <trackbin+1; wtrk++){
        for(int wppt =1; wppt <ptbin+1; wppt++){
            TH2D* h1 = (TH2D*)f->Get(Form("hSig_%d_%d",wtrk,wppt));
            TH2D* h2 = (TH2D*)f->Get(Form("hBck_%d_%d",wtrk,wppt));
            //TH2D* h3 = (TH2D*)f->Get(Form("hSig_sub_%d_%d",wtrk,wppt));
            //TH2D* h4 = (TH2D*)f->Get(Form("hBck_sub_%d_%d",wtrk,wppt));
            //h1->SetDirectory(nullptr);
            //h2->SetDirectory(nullptr);
            //h3->SetDirectory(nullptr);
            //h4->SetDirectory(nullptr);

		h1->SetStats(kFALSE);
                h2->SetStats(kFALSE);
                //h3->SetStats(kFALSE);
                //h4->SetStats(kFALSE);

            int where = wppt + (wtrk-1)*(ptbin);

            //h1->Divide(h2);
            //c1->cd(where);
            //h1->ProjectionY()->DrawCopy();

            
            c1->cd(where);
            h1->DrawCopy("COLZ");

            c2->cd(where);
            h2->DrawCopy("COLZ");

            //h1->Divide(h2);
            //c3->cd(where);
            //h1->DrawCopy("COLZ");

            //h3->Divide(h4);
            //c4->cd(where);
            //h3->DrawCopy("COLZ");

/*
            c1->cd(where);
            h1->DrawCopy("COLZ");

            c2->cd(where);
            h2->DrawCopy("COLZ");
*/

            
            TH1D* hh1 = h1->ProjectionY("",1,39);
            TH1D* hh2 = h2->ProjectionY("",1,39);
            hh1->Divide(hh2);
            hh1->SetName(Form("hh1_%d_%d",wtrk,wppt));
            hh1->SetStats(kFALSE);


            //h1->Divide(h2);
            //h1->SetName(Form("h1_%d_%d",wtrk,wppt));
            //h1->SetStats(kFALSE);

            //h3->Divide(h4);
            //h3->SetName(Form("h3_%d_%d",wtrk,wppt));
            //h3->SetStats(kFALSE);

            //c1->cd(where);
            //h1->DrawCopy("COLZ");

            c1Y->cd(where);
            //h1->ProjectionY()->DrawCopy();
            hh1->DrawCopy();            


            //c1Y_sub->cd(where);
            //h1->ProjectionY("",27,39)->DrawCopy();

            //c1X->cd(where);
            //h1->ProjectionX()->DrawCopy();

            //c1X_sub->cd(where);
            //h1->ProjectionX("",1,15)->DrawCopy();

        }
    }
}


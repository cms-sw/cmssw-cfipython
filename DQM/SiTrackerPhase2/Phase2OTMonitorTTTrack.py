import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTTrack(**kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTTrack',
    TH1_NStubs = cms.PSet(
      Nbinsx = cms.int32(8),
      xmax = cms.double(8),
      xmin = cms.double(0)
    ),
    TH1_NTracks = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(399),
      xmin = cms.double(0)
    ),
    TH1_Track_Pt = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(100),
      xmin = cms.double(0)
    ),
    TH1_Track_Phi = cms.PSet(
      Nbinsx = cms.int32(60),
      xmax = cms.double(3.5),
      xmin = cms.double(-3.5)
    ),
    TH1_Track_D0 = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(5),
      xmin = cms.double(-5)
    ),
    TH1_Track_Eta = cms.PSet(
      Nbinsx = cms.int32(45),
      xmax = cms.double(3),
      xmin = cms.double(-3)
    ),
    TH1_Track_VtxZ = cms.PSet(
      Nbinsx = cms.int32(41),
      xmax = cms.double(20),
      xmin = cms.double(-20)
    ),
    TH1_Track_Chi2 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(50),
      xmin = cms.double(0)
    ),
    TH1_Track_Chi2R = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(10),
      xmin = cms.double(0)
    ),
    TH1_Track_Chi2_Probability = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(1),
      xmin = cms.double(0)
    ),
    TH1_Track_MVA1 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(1),
      xmin = cms.double(0)
    ),
    TH2_Track_Chi2R_NStubs = cms.PSet(
      Nbinsx = cms.int32(5),
      xmax = cms.double(8),
      xmin = cms.double(3),
      Nbinsy = cms.int32(15),
      ymax = cms.double(10),
      ymin = cms.double(0)
    ),
    TH2_Track_Chi2R_Eta = cms.PSet(
      Nbinsx = cms.int32(15),
      xmax = cms.double(3),
      xmin = cms.double(-3),
      Nbinsy = cms.int32(15),
      ymax = cms.double(10),
      ymin = cms.double(0)
    ),
    TH2_Track_Eta_NStubs = cms.PSet(
      Nbinsx = cms.int32(15),
      xmax = cms.double(3),
      xmin = cms.double(-3),
      Nbinsy = cms.int32(5),
      ymax = cms.double(8),
      ymin = cms.double(3)
    ),
    TopFolderName = cms.string('TrackerPhase2OTL1Track'),
    TTTracksTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    HQNStubs = cms.int32(4),
    HQChi2dof = cms.double(10),
    HQBendChi2 = cms.double(2.2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

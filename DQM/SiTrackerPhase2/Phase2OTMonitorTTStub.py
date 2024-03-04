import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTStub(**kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTStub',
    TH2TTStub_Position = cms.PSet(
      Nbinsx = cms.int32(960),
      xmax = cms.double(120),
      xmin = cms.double(-120),
      Nbinsy = cms.int32(960),
      ymax = cms.double(120),
      ymin = cms.double(-120)
    ),
    TH2TTStub_RZ = cms.PSet(
      Nbinsx = cms.int32(900),
      xmax = cms.double(300),
      xmin = cms.double(-300),
      Nbinsy = cms.int32(900),
      ymax = cms.double(120),
      ymin = cms.double(0)
    ),
    TH1TTStub_Eta = cms.PSet(
      Nbinsx = cms.int32(45),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    TH1TTStub_Phi = cms.PSet(
      Nbinsx = cms.int32(60),
      xmin = cms.double(-3.5),
      xmax = cms.double(3.5)
    ),
    TH1TTStub_R = cms.PSet(
      Nbinsx = cms.int32(45),
      xmin = cms.double(0),
      xmax = cms.double(120)
    ),
    TH1TTStub_bend = cms.PSet(
      Nbinsx = cms.int32(69),
      xmin = cms.double(-8.625),
      xmax = cms.double(8.625)
    ),
    TH1TTStub_isPS = cms.PSet(
      Nbinsx = cms.int32(2),
      xmin = cms.double(0),
      xmax = cms.double(2)
    ),
    TH1TTStub_Layers = cms.PSet(
      Nbinsx = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5)
    ),
    TH1TTStub_Discs = cms.PSet(
      Nbinsx = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    TH1TTStub_Rings = cms.PSet(
      Nbinsx = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    TH2TTStub_DisOf_Layer = cms.PSet(
      Nbinsx = cms.int32(6),
      xmax = cms.double(6.5),
      xmin = cms.double(0.5),
      Nbinsy = cms.int32(43),
      ymax = cms.double(10.75),
      ymin = cms.double(-10.75)
    ),
    TH2TTStub_DisOf_Disc = cms.PSet(
      Nbinsx = cms.int32(5),
      xmax = cms.double(5.5),
      xmin = cms.double(0.5),
      Nbinsy = cms.int32(43),
      ymax = cms.double(10.75),
      ymin = cms.double(-10.75)
    ),
    TH2TTStub_DisOf_Ring = cms.PSet(
      Nbinsx = cms.int32(16),
      xmax = cms.double(16.5),
      xmin = cms.double(0.5),
      Nbinsy = cms.int32(43),
      ymax = cms.double(10.75),
      ymin = cms.double(-10.75)
    ),
    TopFolderName = cms.string('TrackerPhase2OTStub'),
    TTStubs = cms.InputTag('TTStubsFromPhase2TrackerDigis', 'StubAccepted'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

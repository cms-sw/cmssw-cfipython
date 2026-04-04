import FWCore.ParameterSet.Config as cms

def Phase2OTValidateStub(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTValidateStub',
    TH2TTStub_RZ = cms.PSet(
      Nbinsx = cms.int32(900),
      xmax = cms.double(300),
      xmin = cms.double(-300),
      Nbinsy = cms.int32(900),
      ymax = cms.double(120),
      ymin = cms.double(0)
    ),
    TH1_2S_Res = cms.PSet(
      Nbinsx = cms.int32(99),
      xmax = cms.double(5.5),
      xmin = cms.double(-5.5)
    ),
    TH1_PS_Res = cms.PSet(
      Nbinsx = cms.int32(99),
      xmax = cms.double(2),
      xmin = cms.double(-2)
    ),
    TH1Phi_Res = cms.PSet(
      Nbinsx = cms.int32(599),
      xmax = cms.double(0.1),
      xmin = cms.double(-0.1)
    ),
    TH1Bend_Res = cms.PSet(
      Nbinsx = cms.int32(59),
      xmax = cms.double(5),
      xmin = cms.double(-5.5)
    ),
    TH1Effic_pt = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(100),
      xmin = cms.double(0)
    ),
    TH1Effic_pt_zoom = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(10),
      xmin = cms.double(0)
    ),
    TopFolderName = cms.string('TrackerPhase2OTStubV'),
    TTStubs = cms.InputTag('TTStubsFromPhase2TrackerDigis', 'StubAccepted'),
    trackingParticleToken = cms.InputTag('mix', 'MergedTrackTruth'),
    MCTruthStubInputTag = cms.InputTag('TTStubAssociatorFromPixelDigis', 'StubAccepted'),
    MCTruthClusterInputTag = cms.InputTag('TTClusterAssociatorFromPixelDigis', 'ClusterInclusive'),
    TP_minNStub = cms.int32(4),
    TP_minNLayersStub = cms.int32(4),
    TP_minPt = cms.double(1.5),
    TP_maxEta = cms.double(2.4),
    TP_maxVtxZ = cms.double(15),
    TP_maxD0 = cms.double(1),
    TP_maxLxy = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def Phase2OTValidateTrackingParticles(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTValidateTrackingParticles',
    TH1TrackParts_Eta = cms.PSet(
      Nbinsx = cms.int32(45),
      xmax = cms.double(3),
      xmin = cms.double(-3)
    ),
    TH1TrackParts_Phi = cms.PSet(
      Nbinsx = cms.int32(60),
      xmax = cms.double(3.1415926535897931),
      xmin = cms.double(-3.1415926535897931)
    ),
    TH1TrackParts_Pt = cms.PSet(
      Nbinsx = cms.int32(45),
      xmax = cms.double(100),
      xmin = cms.double(0)
    ),
    TH1Res_ptRel = cms.PSet(
      Nbinsx = cms.int32(200),
      xmax = cms.double(0.5),
      xmin = cms.double(-0.5)
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
    TH1Effic_eta = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(2.5),
      xmin = cms.double(-2.5)
    ),
    TH1Effic_d0 = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(2),
      xmin = cms.double(-2)
    ),
    TH1Effic_VtxR = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(5),
      xmin = cms.double(-5)
    ),
    TH1Effic_VtxZ = cms.PSet(
      Nbinsx = cms.int32(50),
      xmax = cms.double(30),
      xmin = cms.double(-30)
    ),
    TH1Res_pt = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(0.2),
      xmin = cms.double(-0.2)
    ),
    TH1Res_eta = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(0.01),
      xmin = cms.double(-0.01)
    ),
    TH1Res_phi = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(0.01),
      xmin = cms.double(-0.01)
    ),
    TH1Res_VtxZ = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(1),
      xmin = cms.double(-1)
    ),
    TH1Res_d0 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmax = cms.double(0.05),
      xmin = cms.double(-0.05)
    ),
    TopFolderName = cms.string('TrackerPhase2OTL1TrackV'),
    trackingParticleToken = cms.InputTag('mix', 'MergedTrackTruth'),
    MCTruthStubInputTag = cms.InputTag('TTStubAssociatorFromPixelDigis', 'StubAccepted'),
    MCTruthTrackInputTag = cms.InputTag('TTTrackAssociatorFromPixelDigis', 'Level1TTTracks'),
    MCTruthClusterInputTag = cms.InputTag('TTClusterAssociatorFromPixelDigis', 'ClusterAccepted'),
    L1Tk_minNStub = cms.int32(4),
    L1Tk_maxChi2dof = cms.double(25),
    TP_minNStub = cms.int32(4),
    TP_minNLayersStub = cms.int32(4),
    TP_minPt = cms.double(2),
    TP_maxEta = cms.double(2.4),
    TP_maxVtxZ = cms.double(15),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

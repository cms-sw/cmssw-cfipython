import FWCore.ParameterSet.Config as cms

def Phase2OTValidateTracks(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTValidateTracks',
    TH1TrackParts_Eta = cms.PSet(
      Nbinsx = cms.int32(45),
      xmin = cms.double(-3),
      xmax = cms.double(3)
    ),
    TH1TrackParts_Phi = cms.PSet(
      Nbinsx = cms.int32(60),
      xmin = cms.double(-3.1415926535897931),
      xmax = cms.double(3.1415926535897931)
    ),
    TH1TrackParts_Pt = cms.PSet(
      Nbinsx = cms.int32(45),
      xmin = cms.double(0),
      xmax = cms.double(100)
    ),
    n_trackParticles = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(600)
    ),
    TH1Effic_pt = cms.PSet(
      Nbinsx = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(100)
    ),
    TH1Effic_pt_zoom = cms.PSet(
      Nbinsx = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    TH1Effic_eta = cms.PSet(
      Nbinsx = cms.int32(50),
      xmin = cms.double(-2.5),
      xmax = cms.double(2.5)
    ),
    TH1Effic_d0 = cms.PSet(
      Nbinsx = cms.int32(101),
      xmin = cms.double(-0.15),
      xmax = cms.double(0.15)
    ),
    TH1DisEffic_d0 = cms.PSet(
      Nbinsx = cms.int32(101),
      xmin = cms.double(-10),
      xmax = cms.double(10)
    ),
    TH1Effic_Lxy = cms.PSet(
      Nbinsx = cms.int32(25),
      xmin = cms.double(0),
      xmax = cms.double(1)
    ),
    TH1displacedEffic_Lxy = cms.PSet(
      Nbinsx = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(10)
    ),
    TH1Effic_z0 = cms.PSet(
      Nbinsx = cms.int32(40),
      xmin = cms.double(-16),
      xmax = cms.double(16)
    ),
    TH1Res_ptRel = cms.PSet(
      Nbinsx = cms.int32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(0.5)
    ),
    TH1Res_pt = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(-0.2),
      xmax = cms.double(0.2)
    ),
    TH1Res_eta = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(-0.01),
      xmax = cms.double(0.01)
    ),
    TH1Res_phi = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(-0.01),
      xmax = cms.double(0.01)
    ),
    TH1Res_z0 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(-1),
      xmax = cms.double(1)
    ),
    TH1Res_d0 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(-0.05),
      xmax = cms.double(0.05)
    ),
    TH1Resdisplaced_d0 = cms.PSet(
      Nbinsx = cms.int32(101),
      xmin = cms.double(-2),
      xmax = cms.double(2)
    ),
    TH1Track_pt = cms.PSet(
      Nbinsx = cms.int32(50),
      xmin = cms.double(0),
      xmax = cms.double(25)
    ),
    TH1NTracks_pt2 = cms.PSet(
      Nbinsx = cms.int32(400),
      xmin = cms.double(0),
      xmax = cms.double(400)
    ),
    TH1NTracks_pt3 = cms.PSet(
      Nbinsx = cms.int32(300),
      xmin = cms.double(0),
      xmax = cms.double(300)
    ),
    TH1NTracks_pt10 = cms.PSet(
      Nbinsx = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(100)
    ),
    TopFolderName = cms.string('TrackerPhase2OTL1TrackV'),
    trackingParticleToken = cms.InputTag('mix', 'MergedTrackTruth'),
    MCTruthStubInputTag = cms.InputTag('TTStubAssociatorFromPixelDigis', 'StubAccepted'),
    MCTruthTrackInputTag = cms.InputTag('TTTrackAssociatorFromPixelDigis', 'Level1TTTracks'),
    MCTruthTrackExtendedInputTag = cms.InputTag('TTTrackAssociatorFromPixelDigisExtended', 'Level1TTTracks'),
    MCTruthClusterInputTag = cms.InputTag('TTClusterAssociatorFromPixelDigis', 'ClusterInclusive'),
    L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    L1TrackExtendedInputTag = cms.InputTag('l1tTTTracksFromExtendedTrackletEmulation', 'Level1TTTracks'),
    L1Tk_minNStub = cms.int32(4),
    L1Tk_maxChi2dof = cms.double(25),
    TP_minNStub = cms.int32(4),
    TP_minNLayersStub = cms.int32(4),
    TP_minPt = cms.double(1.5),
    TP_maxEta = cms.double(2.4),
    TP_maxZ0 = cms.double(15),
    TP_maxLxy = cms.double(1),
    TP_maxD0 = cms.double(0.1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

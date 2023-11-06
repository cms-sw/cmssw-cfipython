import FWCore.ParameterSet.Config as cms

trackTypeMonitor = cms.EDProducer('TrackTypeMonitor',
  ModuleName = cms.untracked.string('TrackTypeMonitor'),
  FolderName = cms.untracked.string('highPurityTracks'),
  verbose = cms.untracked.bool(False),
  muonInputTag = cms.untracked.InputTag('muons'),
  electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
  trackInputTag = cms.untracked.InputTag('generalTracks'),
  offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
  vertexTag = cms.untracked.InputTag('offlinePrimaryVertices'),
  trackQuality = cms.untracked.string('highPurity'),
  TrackChi2bynDOFPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(0),
    Xmax = cms.double(10)
  ),
  TrackEtaPar = cms.PSet(
    Xbins = cms.int32(60),
    Xmin = cms.double(-3),
    Xmax = cms.double(3)
  ),
  TrackPPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(0),
    Xmax = cms.double(100)
  ),
  TrackPhiPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(-4),
    Xmax = cms.double(4)
  ),
  TrackPtPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(0),
    Xmax = cms.double(100)
  ),
  TrackPterrPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(0),
    Xmax = cms.double(100)
  ),
  TrackdzPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(-100),
    Xmax = cms.double(100)
  ),
  TrackqOverpPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(-10),
    Xmax = cms.double(10)
  ),
  nTracksPar = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(-0.5),
    Xmax = cms.double(99.5)
  ),
  mightGet = cms.optional.untracked.vstring
)

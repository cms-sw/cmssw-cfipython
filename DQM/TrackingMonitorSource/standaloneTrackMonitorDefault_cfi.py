import FWCore.ParameterSet.Config as cms

standaloneTrackMonitorDefault = cms.EDProducer('StandaloneTrackMonitor',
  moduleName = cms.untracked.string('StandaloneTrackMonitor'),
  folderName = cms.untracked.string('highPurityTracks'),
  isRECO = cms.untracked.bool(False),
  trackInputTag = cms.untracked.InputTag('generalTracks'),
  offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
  vertexTag = cms.untracked.InputTag('offlinePrimaryVertices'),
  puTag = cms.untracked.InputTag('addPileupInfo'),
  clusterTag = cms.untracked.InputTag('siStripClusters'),
  PFJetsCollection = cms.untracked.InputTag('ak4PFJetsCHS'),
  trackQuality = cms.untracked.string('highPurity'),
  doPUCorrection = cms.untracked.bool(False),
  doTrackCorrection = cms.untracked.bool(False),
  isMC = cms.untracked.bool(False),
  haveAllHistograms = cms.untracked.bool(False),
  puScaleFactorFile = cms.untracked.string('PileupScaleFactor.root'),
  trackScaleFactorFile = cms.untracked.string('PileupScaleFactor.root'),
  MVAProducers = cms.required.untracked.vstring,
  TrackProducerForMVA = cms.required.untracked.InputTag,
  TCProducer = cms.required.untracked.InputTag,
  AlgoName = cms.required.untracked.string,
  verbose = cms.untracked.bool(False),
  trackEtaH = cms.PSet(
    Xbins = cms.int32(60),
    Xmin = cms.double(-3),
    Xmax = cms.double(3)
  ),
  trackPtH = cms.PSet(
    Xbins = cms.int32(60),
    Xmin = cms.double(0),
    Xmax = cms.double(100)
  ),
  trackPhiH = cms.PSet(
    Xbins = cms.int32(100),
    Xmin = cms.double(-3.1415926535897931),
    Xmax = cms.double(3.1415926535897931)
  ),
  mightGet = cms.optional.untracked.vstring
)

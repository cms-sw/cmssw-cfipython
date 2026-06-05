import FWCore.ParameterSet.Config as cms

def SiStripHitEfficiencyWorker(*args, **kwargs):
  mod = cms.EDProducer('SiStripHitEfficiencyWorker',
    dqmDir = cms.string('AlCaReco/SiStripHitEfficiency'),
    UseOnlyHighPurityTracks = cms.bool(True),
    cutOnTracks = cms.bool(False),
    doMissingHitsRecovery = cms.bool(False),
    useAllHitsFromTracksWithMissingHits = cms.bool(False),
    useFirstMeas = cms.bool(False),
    useLastMeas = cms.bool(False),
    ClusterTrajDist = cms.double(64),
    ResXSig = cms.double(-1),
    StripsApvEdge = cms.double(10),
    combinatorialTracks = cms.InputTag('generalTracks'),
    commonMode = cms.InputTag('siStripDigis', 'CommonMode'),
    lumiScalers = cms.InputTag('scalersRawToDigi'),
    metadata = cms.InputTag('onlineMetaDataDigis'),
    siStripClusters = cms.InputTag('siStripClusters'),
    siStripDigis = cms.InputTag('siStripDigis'),
    trackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    trajectories = cms.InputTag('generalTracks'),
    ClusterMatchingMethod = cms.int32(0),
    Layer = cms.int32(0),
    trackMultiplicity = cms.uint32(100),
    Debug = cms.untracked.bool(False),
    ShowRings = cms.untracked.bool(False),
    ShowTOB6TEC9 = cms.untracked.bool(False),
    addCommonMode = cms.untracked.bool(False),
    addLumi = cms.untracked.bool(True),
    BunchCrossing = cms.untracked.int32(0),
    BadModulesFile = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

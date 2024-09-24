import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronSeedProducer(*args, **kwargs):
  mod = cms.EDProducer('LowPtGsfElectronSeedProducer',
    tracks = cms.InputTag('generalTracks'),
    pfTracks = cms.InputTag('lowPtGsfElePfTracks'),
    ecalClusters = cms.InputTag('particleFlowClusterECAL'),
    hcalClusters = cms.InputTag('particleFlowClusterHCAL'),
    EBRecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
    BeamSpot = cms.InputTag('offlineBeamSpot'),
    Fitter = cms.ESInputTag('', 'GsfTrajectoryFitter_forPreId'),
    Smoother = cms.ESInputTag('', 'GsfTrajectorySmoother_forPreId'),
    TTRHBuilder = cms.ESInputTag('', 'WithAngleAndTemplate'),
    ModelNames = cms.vstring(),
    ModelWeights = cms.vstring(),
    ModelThresholds = cms.vdouble(),
    PassThrough = cms.bool(False),
    UsePfTracks = cms.bool(True),
    MinPtThreshold = cms.double(1),
    MaxPtThreshold = cms.double(15),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

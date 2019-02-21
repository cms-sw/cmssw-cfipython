import FWCore.ParameterSet.Config as cms

lowPtGsfElectronSeeds = cms.EDProducer('LowPtGsfElectronSeedProducer',
  tracks = cms.InputTag('generalTracks'),
  pfTracks = cms.InputTag('lowPtGsfElePfTracks'),
  ecalClusters = cms.InputTag('particleFlowClusterECAL'),
  hcalClusters = cms.InputTag('particleFlowClusterHCAL'),
  EBRecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  EERecHits = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  BeamSpot = cms.InputTag('offlineBeamSpot'),
  Fitter = cms.string('GsfTrajectoryFitter_forPreId'),
  Smoother = cms.string('GsfTrajectorySmoother_forPreId'),
  TTRHBuilder = cms.string('WithAngleAndTemplate'),
  ModelNames = cms.vstring(),
  ModelWeights = cms.vstring(),
  ModelThresholds = cms.vdouble(),
  PassThrough = cms.bool(False),
  UsePfTracks = cms.bool(True),
  MinPtThreshold = cms.double(1),
  MaxPtThreshold = cms.double(15)
)

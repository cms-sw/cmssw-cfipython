import FWCore.ParameterSet.Config as cms

produceLowPtGsfElectronSeeds = cms.EDProducer('LowPtGsfElectronSeedProducer',
  tracks = cms.InputTag('generalTracks'),
  pfTracks = cms.InputTag('lowPtGsfElePfTracks'),
  ecalClusters = cms.InputTag('particleFlowClusterECAL'),
  hcalClusters = cms.InputTag('particleFlowClusterHCAL'),
  EBRecHits = cms.InputTag('reducedEcalRecHitsEB'),
  EERecHits = cms.InputTag('reducedEcalRecHitsEE'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  BeamSpot = cms.InputTag('offlineBeamSpot'),
  Fitter = cms.string('GsfTrajectoryFitter_forPreId'),
  Smoother = cms.string('GsfTrajectorySmoother_forPreId'),
  TTRHBuilder = cms.string('WithAngleAndTemplate'),
  ModelNames = cms.vstring(),
  ModelWeights = cms.vstring(),
  ModelThresholds = cms.vdouble(),
  PassThrough = cms.bool(False),
  UsePfTracks = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15)
)

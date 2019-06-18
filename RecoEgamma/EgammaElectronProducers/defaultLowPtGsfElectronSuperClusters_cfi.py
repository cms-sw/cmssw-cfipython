import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronSuperClusters = cms.EDProducer('LowPtGsfElectronSCProducer',
  gsfPfRecTracks = cms.InputTag('lowPtGsfElePfGsfTracks'),
  ecalClusters = cms.InputTag('particleFlowClusterECAL'),
  hcalClusters = cms.InputTag('particleFlowClusterHCAL'),
  MaxDeltaR2 = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)

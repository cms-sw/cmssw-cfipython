import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronSeedValueMaps = cms.EDProducer('LowPtGsfElectronSeedValueMapsProducer',
  electrons = cms.InputTag('lowPtGsfElectrons'),
  preIdsValueMap = cms.InputTag('lowPtGsfElectronSeeds'),
  ModelNames = cms.vstring('default')
)

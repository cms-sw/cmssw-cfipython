import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronSeedValueMaps = cms.EDProducer('LowPtGsfElectronSeedValueMapsProducer',
  gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
  preIdsValueMap = cms.InputTag('lowPtGsfElectronSeeds'),
  ModelNames = cms.vstring()
)

import FWCore.ParameterSet.Config as cms

lowPtGsfElectronSeedValueMaps = cms.EDProducer('LowPtGsfElectronSeedValueMapsProducer',
  gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
  preIdsValueMap = cms.InputTag('lowPtGsfElectronSeeds'),
  ModelNames = cms.vstring(
    'unbiased',
    'ptbiased'
  ),
  mightGet = cms.optional.untracked.vstring
)

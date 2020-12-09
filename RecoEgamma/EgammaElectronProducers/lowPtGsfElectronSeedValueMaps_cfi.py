import FWCore.ParameterSet.Config as cms

lowPtGsfElectronSeedValueMaps = cms.EDProducer('LowPtGsfElectronSeedValueMapsProducer',
  gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
  preIdsValueMap = cms.InputTag('lowPtGsfElectronSeeds'),
  ModelNames = cms.vstring(
    'unbiased',
    'ptbiased'
  ),
  rekey = cms.bool(False),
  gsfElectrons = cms.InputTag(''),
  floatValueMaps = cms.VInputTag()
)

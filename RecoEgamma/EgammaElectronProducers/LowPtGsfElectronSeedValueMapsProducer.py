import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronSeedValueMapsProducer(**kwargs):
  mod = cms.EDProducer('LowPtGsfElectronSeedValueMapsProducer',
    gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
    preIdsValueMap = cms.InputTag('lowPtGsfElectronSeeds'),
    ModelNames = cms.vstring(
      'unbiased',
      'ptbiased'
    ),
    rekey = cms.bool(False),
    gsfElectrons = cms.InputTag(''),
    floatValueMaps = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

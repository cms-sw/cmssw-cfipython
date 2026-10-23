import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronSeedValueMapsProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

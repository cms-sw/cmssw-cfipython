import FWCore.ParameterSet.Config as cms

def ElectronMVAValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronMVAValueMapProducer',
    src = cms.InputTag(''),
    keysForValueMaps = cms.InputTag(''),
    mvaConfigurations = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

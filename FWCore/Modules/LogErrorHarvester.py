import FWCore.ParameterSet.Config as cms

def LogErrorHarvester(**kwargs):
  mod = cms.EDProducer('LogErrorHarvester',
    excludeModules = cms.untracked.vstring(),
    includeModules = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

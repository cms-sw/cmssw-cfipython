import FWCore.ParameterSet.Config as cms

def LogErrorHarvester(*args, **kwargs):
  mod = cms.EDProducer('LogErrorHarvester',
    excludeModules = cms.untracked.vstring(),
    includeModules = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

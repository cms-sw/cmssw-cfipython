import FWCore.ParameterSet.Config as cms

def ElectronShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def AcquireIntProducer(*args, **kwargs):
  mod = cms.EDProducer('AcquireIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

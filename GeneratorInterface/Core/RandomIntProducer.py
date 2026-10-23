import FWCore.ParameterSet.Config as cms

def RandomIntProducer(*args, **kwargs):
  mod = cms.EDProducer('RandomIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def NonProducer(*args, **kwargs):
  mod = cms.EDProducer('NonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

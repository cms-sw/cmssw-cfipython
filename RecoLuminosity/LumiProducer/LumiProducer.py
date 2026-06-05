import FWCore.ParameterSet.Config as cms

def LumiProducer(*args, **kwargs):
  mod = cms.EDProducer('LumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

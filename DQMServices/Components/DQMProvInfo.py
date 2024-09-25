import FWCore.ParameterSet.Config as cms

def DQMProvInfo(*args, **kwargs):
  mod = cms.EDProducer('DQMProvInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

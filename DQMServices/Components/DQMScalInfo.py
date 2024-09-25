import FWCore.ParameterSet.Config as cms

def DQMScalInfo(*args, **kwargs):
  mod = cms.EDProducer('DQMScalInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DQMSourcePi0(*args, **kwargs):
  mod = cms.EDProducer('DQMSourcePi0',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

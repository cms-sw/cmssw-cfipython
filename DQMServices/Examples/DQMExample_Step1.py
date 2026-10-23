import FWCore.ParameterSet.Config as cms

def DQMExample_Step1(*args, **kwargs):
  mod = cms.EDProducer('DQMExample_Step1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

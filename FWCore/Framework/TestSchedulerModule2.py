import FWCore.ParameterSet.Config as cms

def TestSchedulerModule2(**kwargs):
  mod = cms.EDProducer('TestSchedulerModule2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

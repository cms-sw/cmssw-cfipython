import FWCore.ParameterSet.Config as cms

def TestSchedulerModule1(**kwargs):
  mod = cms.EDProducer('TestSchedulerModule1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

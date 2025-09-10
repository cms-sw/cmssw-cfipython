import FWCore.ParameterSet.Config as cms

def TestSchedulerModule2(*args, **kwargs):
  mod = cms.EDProducer('TestSchedulerModule2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

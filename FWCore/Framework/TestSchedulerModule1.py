import FWCore.ParameterSet.Config as cms

def TestSchedulerModule1(*args, **kwargs):
  mod = cms.EDProducer('TestSchedulerModule1',
    module_name = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

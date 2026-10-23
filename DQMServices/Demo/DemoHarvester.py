import FWCore.ParameterSet.Config as cms

def DemoHarvester(*args, **kwargs):
  mod = cms.EDProducer('DemoHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

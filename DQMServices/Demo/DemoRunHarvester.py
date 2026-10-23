import FWCore.ParameterSet.Config as cms

def DemoRunHarvester(*args, **kwargs):
  mod = cms.EDProducer('DemoRunHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DemoRunHarvester(**kwargs):
  mod = cms.EDProducer('DemoRunHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

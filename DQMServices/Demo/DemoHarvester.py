import FWCore.ParameterSet.Config as cms

def DemoHarvester(**kwargs):
  mod = cms.EDProducer('DemoHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

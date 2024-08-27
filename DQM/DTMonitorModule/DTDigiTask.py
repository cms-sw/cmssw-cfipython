import FWCore.ParameterSet.Config as cms

def DTDigiTask(**kwargs):
  mod = cms.EDProducer('DTDigiTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

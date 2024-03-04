import FWCore.ParameterSet.Config as cms

def ESTimingTask(**kwargs):
  mod = cms.EDProducer('ESTimingTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

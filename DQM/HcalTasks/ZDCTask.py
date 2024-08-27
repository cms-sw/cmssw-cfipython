import FWCore.ParameterSet.Config as cms

def ZDCTask(**kwargs):
  mod = cms.EDProducer('ZDCTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

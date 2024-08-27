import FWCore.ParameterSet.Config as cms

def WriteMath(**kwargs):
  mod = cms.EDProducer('WriteMath',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HiL1Subtractor(**kwargs):
  mod = cms.EDProducer('HiL1Subtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def L1TdeGCT(**kwargs):
  mod = cms.EDProducer('L1TdeGCT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

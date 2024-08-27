import FWCore.ParameterSet.Config as cms

def L1TCompare(**kwargs):
  mod = cms.EDProducer('L1TCompare',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

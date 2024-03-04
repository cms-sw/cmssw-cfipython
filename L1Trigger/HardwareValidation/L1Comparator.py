import FWCore.ParameterSet.Config as cms

def L1Comparator(**kwargs):
  mod = cms.EDProducer('L1Comparator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

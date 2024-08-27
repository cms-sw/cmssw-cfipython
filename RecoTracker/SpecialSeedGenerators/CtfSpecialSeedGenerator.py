import FWCore.ParameterSet.Config as cms

def CtfSpecialSeedGenerator(**kwargs):
  mod = cms.EDProducer('CtfSpecialSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

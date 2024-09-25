import FWCore.ParameterSet.Config as cms

def CtfSpecialSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('CtfSpecialSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

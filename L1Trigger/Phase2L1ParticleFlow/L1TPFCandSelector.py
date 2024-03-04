import FWCore.ParameterSet.Config as cms

def L1TPFCandSelector(**kwargs):
  mod = cms.EDFilter('L1TPFCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def L1TPFCandSelector(*args, **kwargs):
  mod = cms.EDFilter('L1TPFCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
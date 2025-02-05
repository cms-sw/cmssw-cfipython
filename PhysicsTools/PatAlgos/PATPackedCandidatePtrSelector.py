import FWCore.ParameterSet.Config as cms

def PATPackedCandidatePtrSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPackedCandidatePtrSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

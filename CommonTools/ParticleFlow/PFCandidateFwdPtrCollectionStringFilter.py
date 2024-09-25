import FWCore.ParameterSet.Config as cms

def PFCandidateFwdPtrCollectionStringFilter(*args, **kwargs):
  mod = cms.EDFilter('PFCandidateFwdPtrCollectionStringFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

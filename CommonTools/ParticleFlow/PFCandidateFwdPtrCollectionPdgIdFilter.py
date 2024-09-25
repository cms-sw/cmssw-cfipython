import FWCore.ParameterSet.Config as cms

def PFCandidateFwdPtrCollectionPdgIdFilter(*args, **kwargs):
  mod = cms.EDFilter('PFCandidateFwdPtrCollectionPdgIdFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

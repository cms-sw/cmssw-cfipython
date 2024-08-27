import FWCore.ParameterSet.Config as cms

def PFCandidateFwdPtrCollectionStringFilter(**kwargs):
  mod = cms.EDFilter('PFCandidateFwdPtrCollectionStringFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

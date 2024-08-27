import FWCore.ParameterSet.Config as cms

def PFCandidateFwdPtrCollectionPdgIdFilter(**kwargs):
  mod = cms.EDFilter('PFCandidateFwdPtrCollectionPdgIdFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

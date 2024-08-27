import FWCore.ParameterSet.Config as cms

def PtMinPFCandidateSelector(**kwargs):
  mod = cms.EDFilter('PtMinPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

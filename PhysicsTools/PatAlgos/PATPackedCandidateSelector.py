import FWCore.ParameterSet.Config as cms

def PATPackedCandidateSelector(**kwargs):
  mod = cms.EDFilter('PATPackedCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

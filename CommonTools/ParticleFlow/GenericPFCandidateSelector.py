import FWCore.ParameterSet.Config as cms

def GenericPFCandidateSelector(**kwargs):
  mod = cms.EDFilter('GenericPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

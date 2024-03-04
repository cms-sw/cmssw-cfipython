import FWCore.ParameterSet.Config as cms

def PdgIdPFCandidateSelector(**kwargs):
  mod = cms.EDFilter('PdgIdPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

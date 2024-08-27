import FWCore.ParameterSet.Config as cms

def MuonIDPFCandidateSelector(**kwargs):
  mod = cms.EDFilter('MuonIDPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def InconsistentMuonPFCandidateFilter(**kwargs):
  mod = cms.EDFilter('InconsistentMuonPFCandidateFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def GreedyMuonPFCandidateFilter(**kwargs):
  mod = cms.EDFilter('GreedyMuonPFCandidateFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

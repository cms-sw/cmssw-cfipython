import FWCore.ParameterSet.Config as cms

def GreedyMuonPFCandidateFilter(*args, **kwargs):
  mod = cms.EDFilter('GreedyMuonPFCandidateFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

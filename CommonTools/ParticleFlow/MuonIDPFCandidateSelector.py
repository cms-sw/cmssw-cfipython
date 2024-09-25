import FWCore.ParameterSet.Config as cms

def MuonIDPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('MuonIDPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

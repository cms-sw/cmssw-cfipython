import FWCore.ParameterSet.Config as cms

def IsolatedPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('IsolatedPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

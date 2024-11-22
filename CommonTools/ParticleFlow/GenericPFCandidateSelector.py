import FWCore.ParameterSet.Config as cms

def GenericPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('GenericPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

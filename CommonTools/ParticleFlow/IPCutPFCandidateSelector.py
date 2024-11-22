import FWCore.ParameterSet.Config as cms

def IPCutPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('IPCutPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

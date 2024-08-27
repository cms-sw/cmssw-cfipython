import FWCore.ParameterSet.Config as cms

def IPCutPFCandidateSelector(**kwargs):
  mod = cms.EDFilter('IPCutPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PdgIdPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdPFCandidateSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def CandidateBVertexFilter(*args, **kwargs):
  mod = cms.EDFilter('CandidateBVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def CandidateBVertexFilter(**kwargs):
  mod = cms.EDFilter('CandidateBVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

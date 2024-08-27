import FWCore.ParameterSet.Config as cms

def VertexSelector(**kwargs):
  mod = cms.EDFilter('VertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

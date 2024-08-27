import FWCore.ParameterSet.Config as cms

def SimVertexSelector(**kwargs):
  mod = cms.EDFilter('SimVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

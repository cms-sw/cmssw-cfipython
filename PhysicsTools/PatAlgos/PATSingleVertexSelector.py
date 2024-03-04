import FWCore.ParameterSet.Config as cms

def PATSingleVertexSelector(**kwargs):
  mod = cms.EDFilter('PATSingleVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

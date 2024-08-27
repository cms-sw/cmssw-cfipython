import FWCore.ParameterSet.Config as cms

def PdgIdAndStatusCandSelector(**kwargs):
  mod = cms.EDFilter('PdgIdAndStatusCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

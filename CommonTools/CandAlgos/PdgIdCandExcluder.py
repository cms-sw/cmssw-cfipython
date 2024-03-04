import FWCore.ParameterSet.Config as cms

def PdgIdCandExcluder(**kwargs):
  mod = cms.EDFilter('PdgIdCandExcluder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

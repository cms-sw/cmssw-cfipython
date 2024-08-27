import FWCore.ParameterSet.Config as cms

def PdgIdCandViewSelector(**kwargs):
  mod = cms.EDFilter('PdgIdCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PdgIdCandRefSelector(**kwargs):
  mod = cms.EDFilter('PdgIdCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

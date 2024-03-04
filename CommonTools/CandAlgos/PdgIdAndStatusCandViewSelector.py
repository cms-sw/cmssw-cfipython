import FWCore.ParameterSet.Config as cms

def PdgIdAndStatusCandViewSelector(**kwargs):
  mod = cms.EDFilter('PdgIdAndStatusCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

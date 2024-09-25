import FWCore.ParameterSet.Config as cms

def PdgIdCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

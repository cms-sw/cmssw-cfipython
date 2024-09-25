import FWCore.ParameterSet.Config as cms

def PdgIdCandRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdCandRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PdgIdAndStatusCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdAndStatusCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TMTFilter(*args, **kwargs):
  mod = cms.EDFilter('TMTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

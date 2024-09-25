import FWCore.ParameterSet.Config as cms

def LHEVpTFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEVpTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

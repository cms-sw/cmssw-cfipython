import FWCore.ParameterSet.Config as cms

def SeedChargeSelector(*args, **kwargs):
  mod = cms.EDFilter('SeedChargeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

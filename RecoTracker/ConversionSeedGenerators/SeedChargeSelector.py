import FWCore.ParameterSet.Config as cms

def SeedChargeSelector(**kwargs):
  mod = cms.EDFilter('SeedChargeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

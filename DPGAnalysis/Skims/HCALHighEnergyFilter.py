import FWCore.ParameterSet.Config as cms

def HCALHighEnergyFilter(*args, **kwargs):
  mod = cms.EDFilter('HCALHighEnergyFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

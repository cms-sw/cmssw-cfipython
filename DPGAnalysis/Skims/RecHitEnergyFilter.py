import FWCore.ParameterSet.Config as cms

def RecHitEnergyFilter(*args, **kwargs):
  mod = cms.EDFilter('RecHitEnergyFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
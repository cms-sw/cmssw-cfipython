import FWCore.ParameterSet.Config as cms

def Phase2GCTBarrelToCorrelatorLayer1(*args, **kwargs):
  mod = cms.EDProducer('Phase2GCTBarrelToCorrelatorLayer1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

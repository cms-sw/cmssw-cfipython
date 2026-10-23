import FWCore.ParameterSet.Config as cms

def FixedGridRhoProducer(*args, **kwargs):
  mod = cms.EDProducer('FixedGridRhoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

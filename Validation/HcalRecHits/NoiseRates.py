import FWCore.ParameterSet.Config as cms

def NoiseRates(*args, **kwargs):
  mod = cms.EDProducer('NoiseRates',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

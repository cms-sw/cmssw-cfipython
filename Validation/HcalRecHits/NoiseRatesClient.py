import FWCore.ParameterSet.Config as cms

def NoiseRatesClient(*args, **kwargs):
  mod = cms.EDProducer('NoiseRatesClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

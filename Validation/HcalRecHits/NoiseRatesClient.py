import FWCore.ParameterSet.Config as cms

def NoiseRatesClient(**kwargs):
  mod = cms.EDProducer('NoiseRatesClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

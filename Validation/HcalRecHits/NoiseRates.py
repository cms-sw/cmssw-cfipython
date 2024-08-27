import FWCore.ParameterSet.Config as cms

def NoiseRates(**kwargs):
  mod = cms.EDProducer('NoiseRates',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

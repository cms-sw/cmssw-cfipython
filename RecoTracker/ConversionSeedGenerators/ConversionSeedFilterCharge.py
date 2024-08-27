import FWCore.ParameterSet.Config as cms

def ConversionSeedFilterCharge(**kwargs):
  mod = cms.EDProducer('ConversionSeedFilterCharge',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

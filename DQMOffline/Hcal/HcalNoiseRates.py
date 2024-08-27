import FWCore.ParameterSet.Config as cms

def HcalNoiseRates(**kwargs):
  mod = cms.EDProducer('HcalNoiseRates',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

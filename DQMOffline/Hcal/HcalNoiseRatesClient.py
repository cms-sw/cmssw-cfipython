import FWCore.ParameterSet.Config as cms

def HcalNoiseRatesClient(**kwargs):
  mod = cms.EDProducer('HcalNoiseRatesClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

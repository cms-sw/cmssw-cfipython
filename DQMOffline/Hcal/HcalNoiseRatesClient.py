import FWCore.ParameterSet.Config as cms

def HcalNoiseRatesClient(*args, **kwargs):
  mod = cms.EDProducer('HcalNoiseRatesClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

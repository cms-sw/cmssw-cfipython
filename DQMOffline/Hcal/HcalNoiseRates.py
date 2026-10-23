import FWCore.ParameterSet.Config as cms

def HcalNoiseRates(*args, **kwargs):
  mod = cms.EDProducer('HcalNoiseRates',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

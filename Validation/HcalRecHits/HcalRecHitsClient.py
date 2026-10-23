import FWCore.ParameterSet.Config as cms

def HcalRecHitsClient(*args, **kwargs):
  mod = cms.EDProducer('HcalRecHitsClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

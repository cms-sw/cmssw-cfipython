import FWCore.ParameterSet.Config as cms

def EcalPreshowerRecHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalPreshowerRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

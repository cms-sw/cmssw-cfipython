import FWCore.ParameterSet.Config as cms

def EcalEndcapRecHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalEndcapRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

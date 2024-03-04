import FWCore.ParameterSet.Config as cms

def EcalEndcapRecHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalEndcapRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

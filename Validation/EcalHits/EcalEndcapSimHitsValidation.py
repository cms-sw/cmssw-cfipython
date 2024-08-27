import FWCore.ParameterSet.Config as cms

def EcalEndcapSimHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalEndcapSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

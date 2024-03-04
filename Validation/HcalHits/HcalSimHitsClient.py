import FWCore.ParameterSet.Config as cms

def HcalSimHitsClient(**kwargs):
  mod = cms.EDProducer('HcalSimHitsClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

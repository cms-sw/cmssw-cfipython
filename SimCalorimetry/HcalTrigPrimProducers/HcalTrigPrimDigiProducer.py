import FWCore.ParameterSet.Config as cms

def HcalTrigPrimDigiProducer(**kwargs):
  mod = cms.EDProducer('HcalTrigPrimDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

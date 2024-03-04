import FWCore.ParameterSet.Config as cms

def HcalTTPTriggerRecord(**kwargs):
  mod = cms.EDProducer('HcalTTPTriggerRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

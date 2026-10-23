import FWCore.ParameterSet.Config as cms

def HcalTTPTriggerRecord(*args, **kwargs):
  mod = cms.EDProducer('HcalTTPTriggerRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

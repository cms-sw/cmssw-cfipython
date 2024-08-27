import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDEtaLessByDR(**kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDEtaLessByDR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

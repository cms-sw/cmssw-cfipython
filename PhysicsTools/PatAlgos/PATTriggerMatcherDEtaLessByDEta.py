import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDEtaLessByDEta(**kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDEtaLessByDEta',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

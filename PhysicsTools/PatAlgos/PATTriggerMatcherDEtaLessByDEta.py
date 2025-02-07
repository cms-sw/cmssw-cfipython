import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDEtaLessByDEta(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDEtaLessByDEta',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRLessByPt(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRLessByPt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

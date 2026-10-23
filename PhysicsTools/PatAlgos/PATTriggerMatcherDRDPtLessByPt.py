import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRDPtLessByPt(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRDPtLessByPt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

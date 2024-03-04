import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRLessByPt(**kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRLessByPt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

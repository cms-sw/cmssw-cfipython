import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRDPtLessByPt(**kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRDPtLessByPt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

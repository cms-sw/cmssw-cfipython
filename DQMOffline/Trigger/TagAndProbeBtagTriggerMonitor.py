import FWCore.ParameterSet.Config as cms

def TagAndProbeBtagTriggerMonitor(**kwargs):
  mod = cms.EDProducer('TagAndProbeBtagTriggerMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

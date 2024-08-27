import FWCore.ParameterSet.Config as cms

def HLTObjectsMonitor(**kwargs):
  mod = cms.EDProducer('HLTObjectsMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

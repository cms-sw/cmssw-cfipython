import FWCore.ParameterSet.Config as cms

def PhysicsObjectsMonitor(**kwargs):
  mod = cms.EDProducer('PhysicsObjectsMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

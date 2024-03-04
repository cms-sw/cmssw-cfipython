import FWCore.ParameterSet.Config as cms

def BeamMonitor(**kwargs):
  mod = cms.EDProducer('BeamMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

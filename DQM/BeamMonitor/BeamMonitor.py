import FWCore.ParameterSet.Config as cms

def BeamMonitor(*args, **kwargs):
  mod = cms.EDProducer('BeamMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

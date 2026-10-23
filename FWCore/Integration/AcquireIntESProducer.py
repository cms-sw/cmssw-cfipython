import FWCore.ParameterSet.Config as cms

def AcquireIntESProducer(*args, **kwargs):
  mod = cms.ESProducer('AcquireIntESProducer',
    numberOfIOVsToAccumulate = cms.untracked.uint32(8),
    secondsToWaitForWork = cms.untracked.uint32(1),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

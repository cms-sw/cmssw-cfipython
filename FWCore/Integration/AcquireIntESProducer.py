import FWCore.ParameterSet.Config as cms

def AcquireIntESProducer(**kwargs):
  mod = cms.ESProducer('AcquireIntESProducer',
    numberOfIOVsToAccumulate = cms.untracked.uint32(8),
    secondsToWaitForWork = cms.untracked.uint32(1),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

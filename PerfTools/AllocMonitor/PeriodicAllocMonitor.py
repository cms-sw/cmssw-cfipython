import FWCore.ParameterSet.Config as cms

def PeriodicAllocMonitor(**kwargs):
  mod = cms.Service('PeriodicAllocMonitor',
    filename = cms.untracked.string('timing.log'),
    millisecondsPerMeasurement = cms.untracked.uint64(1000)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

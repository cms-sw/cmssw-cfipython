import FWCore.ParameterSet.Config as cms

def EventProcessingAllocMonitor(**kwargs):
  mod = cms.Service('EventProcessingAllocMonitor')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def SimpleAllocMonitor(**kwargs):
  mod = cms.Service('SimpleAllocMonitor')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

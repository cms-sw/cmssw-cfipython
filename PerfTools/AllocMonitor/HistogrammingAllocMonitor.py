import FWCore.ParameterSet.Config as cms

def HistogrammingAllocMonitor(**kwargs):
  mod = cms.Service('HistogrammingAllocMonitor')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

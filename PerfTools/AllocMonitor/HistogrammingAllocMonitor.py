import FWCore.ParameterSet.Config as cms

def HistogrammingAllocMonitor(*args, **kwargs):
  mod = cms.Service('HistogrammingAllocMonitor')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

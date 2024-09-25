import FWCore.ParameterSet.Config as cms

def LoadableDummyFinder(*args, **kwargs):
  mod = cms.ESSource('LoadableDummyFinder')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

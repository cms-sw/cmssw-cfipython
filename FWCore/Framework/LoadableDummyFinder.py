import FWCore.ParameterSet.Config as cms

def LoadableDummyFinder(**kwargs):
  mod = cms.ESSource('LoadableDummyFinder')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

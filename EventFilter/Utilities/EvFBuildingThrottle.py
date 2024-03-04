import FWCore.ParameterSet.Config as cms

def EvFBuildingThrottle(**kwargs):
  mod = cms.Service('EvFBuildingThrottle')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

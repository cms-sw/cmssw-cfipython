import FWCore.ParameterSet.Config as cms

def EvFBuildingThrottle(*args, **kwargs):
  mod = cms.Service('EvFBuildingThrottle')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

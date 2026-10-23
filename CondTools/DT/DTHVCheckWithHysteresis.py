import FWCore.ParameterSet.Config as cms

def DTHVCheckWithHysteresis(*args, **kwargs):
  mod = cms.Service('DTHVCheckWithHysteresis')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

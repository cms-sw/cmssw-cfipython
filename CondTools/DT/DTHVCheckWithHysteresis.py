import FWCore.ParameterSet.Config as cms

def DTHVCheckWithHysteresis(**kwargs):
  mod = cms.Service('DTHVCheckWithHysteresis')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def FWFFHelper(**kwargs):
  mod = cms.Service('FWFFHelper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

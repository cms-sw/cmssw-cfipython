import FWCore.ParameterSet.Config as cms

def FWFFHelper(*args, **kwargs):
  mod = cms.Service('FWFFHelper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

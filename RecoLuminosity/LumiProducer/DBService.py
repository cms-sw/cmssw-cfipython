import FWCore.ParameterSet.Config as cms

def DBService(*args, **kwargs):
  mod = cms.Service('DBService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

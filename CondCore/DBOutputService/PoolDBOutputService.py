import FWCore.ParameterSet.Config as cms

def PoolDBOutputService(*args, **kwargs):
  mod = cms.Service('PoolDBOutputService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

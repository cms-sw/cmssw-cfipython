import FWCore.ParameterSet.Config as cms

def PoolDBOutputService(**kwargs):
  mod = cms.Service('PoolDBOutputService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

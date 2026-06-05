import FWCore.ParameterSet.Config as cms

def AsyncService(*args, **kwargs):
  mod = cms.Service('AsyncService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

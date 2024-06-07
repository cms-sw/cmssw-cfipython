import FWCore.ParameterSet.Config as cms

def AsyncService(**kwargs):
  mod = cms.Service('AsyncService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

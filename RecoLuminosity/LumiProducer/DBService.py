import FWCore.ParameterSet.Config as cms

def DBService(**kwargs):
  mod = cms.Service('DBService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

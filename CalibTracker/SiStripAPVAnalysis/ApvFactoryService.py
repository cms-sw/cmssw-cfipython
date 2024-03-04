import FWCore.ParameterSet.Config as cms

def ApvFactoryService(**kwargs):
  mod = cms.Service('ApvFactoryService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

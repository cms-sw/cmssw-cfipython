import FWCore.ParameterSet.Config as cms

def WaitingService(**kwargs):
  mod = cms.Service('WaitingService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

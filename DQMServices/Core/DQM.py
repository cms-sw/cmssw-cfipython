import FWCore.ParameterSet.Config as cms

def DQM(**kwargs):
  mod = cms.Service('DQM')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

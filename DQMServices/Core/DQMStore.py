import FWCore.ParameterSet.Config as cms

def DQMStore(**kwargs):
  mod = cms.Service('DQMStore')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

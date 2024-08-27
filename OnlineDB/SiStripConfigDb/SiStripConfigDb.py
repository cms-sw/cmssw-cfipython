import FWCore.ParameterSet.Config as cms

def SiStripConfigDb(**kwargs):
  mod = cms.Service('SiStripConfigDb')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

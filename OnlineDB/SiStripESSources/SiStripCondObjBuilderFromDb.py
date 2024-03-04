import FWCore.ParameterSet.Config as cms

def SiStripCondObjBuilderFromDb(**kwargs):
  mod = cms.Service('SiStripCondObjBuilderFromDb')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

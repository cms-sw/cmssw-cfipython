import FWCore.ParameterSet.Config as cms

def SiStripCondObjBuilderFromDb(*args, **kwargs):
  mod = cms.Service('SiStripCondObjBuilderFromDb')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

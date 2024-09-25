import FWCore.ParameterSet.Config as cms

def SiStripConfigDb(*args, **kwargs):
  mod = cms.Service('SiStripConfigDb')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

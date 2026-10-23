import FWCore.ParameterSet.Config as cms

def SiStripDetVOffBuilder(*args, **kwargs):
  mod = cms.Service('SiStripDetVOffBuilder')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

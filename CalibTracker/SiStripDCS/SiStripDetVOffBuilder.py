import FWCore.ParameterSet.Config as cms

def SiStripDetVOffBuilder(**kwargs):
  mod = cms.Service('SiStripDetVOffBuilder')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

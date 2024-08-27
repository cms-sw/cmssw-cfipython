import FWCore.ParameterSet.Config as cms

def PathsAndConsumesOfModulesTestService(**kwargs):
  mod = cms.Service('PathsAndConsumesOfModulesTestService',
    modulesAndConsumes = cms.VPSet(
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

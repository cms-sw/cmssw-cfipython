import FWCore.ParameterSet.Config as cms

def PathsAndConsumesOfModulesTestService(*args, **kwargs):
  mod = cms.Service('PathsAndConsumesOfModulesTestService',
    modulesAndConsumes = cms.VPSet(
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

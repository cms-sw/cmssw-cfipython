import FWCore.ParameterSet.Config as cms

def PathsAndConsumesOfModulesTestService(*args, **kwargs):
  mod = cms.Service('PathsAndConsumesOfModulesTestService',
    modulesAndConsumes = cms.VPSet(
      template = cms.PSetTemplate(
        key = cms.required.string,
        value = cms.required.vstring
      )
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ResourceInformationService(*args, **kwargs):
  mod = cms.Service('ResourceInformationService',
    verbose = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

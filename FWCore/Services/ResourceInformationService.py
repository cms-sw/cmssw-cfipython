import FWCore.ParameterSet.Config as cms

def ResourceInformationService(**kwargs):
  mod = cms.Service('ResourceInformationService',
    verbose = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

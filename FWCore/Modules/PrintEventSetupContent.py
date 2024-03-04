import FWCore.ParameterSet.Config as cms

def PrintEventSetupContent(**kwargs):
  mod = cms.EDAnalyzer('PrintEventSetupContent',
    compact = cms.untracked.bool(False),
    printProviders = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

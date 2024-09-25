import FWCore.ParameterSet.Config as cms

def PrintEventSetupContent(*args, **kwargs):
  mod = cms.EDAnalyzer('PrintEventSetupContent',
    compact = cms.untracked.bool(False),
    printProviders = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

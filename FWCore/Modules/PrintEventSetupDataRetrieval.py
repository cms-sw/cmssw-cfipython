import FWCore.ParameterSet.Config as cms

def PrintEventSetupDataRetrieval(*args, **kwargs):
  mod = cms.EDAnalyzer('PrintEventSetupDataRetrieval',
    printProviders = cms.untracked.bool(False),
    checkDuringBeginRun = cms.untracked.bool(False),
    checkDuringBeginLumi = cms.untracked.bool(False),
    checkDuringEvent = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

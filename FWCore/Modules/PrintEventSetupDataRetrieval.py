import FWCore.ParameterSet.Config as cms

def PrintEventSetupDataRetrieval(**kwargs):
  mod = cms.EDAnalyzer('PrintEventSetupDataRetrieval',
    printProviders = cms.untracked.bool(False),
    checkDuringBeginRun = cms.untracked.bool(False),
    checkDuringBeginLumi = cms.untracked.bool(False),
    checkDuringEvent = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

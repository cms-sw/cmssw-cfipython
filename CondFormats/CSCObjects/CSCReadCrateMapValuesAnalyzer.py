import FWCore.ParameterSet.Config as cms

def CSCReadCrateMapValuesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadCrateMapValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

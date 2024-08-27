import FWCore.ParameterSet.Config as cms

def CSCReadCrateMapValuesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadCrateMapValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

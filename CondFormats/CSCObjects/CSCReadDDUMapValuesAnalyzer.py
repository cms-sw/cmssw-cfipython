import FWCore.ParameterSet.Config as cms

def CSCReadDDUMapValuesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadDDUMapValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def CSCReadDDUMapValuesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadDDUMapValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

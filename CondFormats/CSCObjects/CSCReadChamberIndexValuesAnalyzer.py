import FWCore.ParameterSet.Config as cms

def CSCReadChamberIndexValuesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberIndexValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

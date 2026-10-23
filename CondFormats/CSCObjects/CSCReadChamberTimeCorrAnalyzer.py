import FWCore.ParameterSet.Config as cms

def CSCReadChamberTimeCorrAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberTimeCorrAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

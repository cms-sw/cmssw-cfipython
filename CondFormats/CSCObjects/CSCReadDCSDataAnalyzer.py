import FWCore.ParameterSet.Config as cms

def CSCReadDCSDataAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadDCSDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

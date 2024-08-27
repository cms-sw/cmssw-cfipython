import FWCore.ParameterSet.Config as cms

def CSCReadDCSDataAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadDCSDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

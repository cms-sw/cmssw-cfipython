import FWCore.ParameterSet.Config as cms

def CSCReadBadStripsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadBadStripsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

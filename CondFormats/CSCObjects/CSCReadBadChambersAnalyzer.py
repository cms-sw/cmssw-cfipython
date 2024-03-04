import FWCore.ParameterSet.Config as cms

def CSCReadBadChambersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadBadChambersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

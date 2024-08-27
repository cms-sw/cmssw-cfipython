import FWCore.ParameterSet.Config as cms

def CSCReadBadWiresAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadBadWiresAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

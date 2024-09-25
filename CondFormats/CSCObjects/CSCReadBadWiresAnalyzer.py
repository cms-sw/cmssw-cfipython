import FWCore.ParameterSet.Config as cms

def CSCReadBadWiresAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadBadWiresAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

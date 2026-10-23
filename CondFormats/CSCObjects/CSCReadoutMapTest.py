import FWCore.ParameterSet.Config as cms

def CSCReadoutMapTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadoutMapTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

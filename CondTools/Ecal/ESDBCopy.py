import FWCore.ParameterSet.Config as cms

def ESDBCopy(*args, **kwargs):
  mod = cms.EDAnalyzer('ESDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

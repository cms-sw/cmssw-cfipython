import FWCore.ParameterSet.Config as cms

def ESDBCopy(**kwargs):
  mod = cms.EDAnalyzer('ESDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

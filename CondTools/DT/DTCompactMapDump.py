import FWCore.ParameterSet.Config as cms

def DTCompactMapDump(**kwargs):
  mod = cms.EDAnalyzer('DTCompactMapDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

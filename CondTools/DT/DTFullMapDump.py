import FWCore.ParameterSet.Config as cms

def DTFullMapDump(**kwargs):
  mod = cms.EDAnalyzer('DTFullMapDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

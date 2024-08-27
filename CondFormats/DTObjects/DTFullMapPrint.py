import FWCore.ParameterSet.Config as cms

def DTFullMapPrint(**kwargs):
  mod = cms.EDAnalyzer('DTFullMapPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

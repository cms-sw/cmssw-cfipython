import FWCore.ParameterSet.Config as cms

def DTMapPrint(**kwargs):
  mod = cms.EDAnalyzer('DTMapPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

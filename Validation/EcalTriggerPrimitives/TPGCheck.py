import FWCore.ParameterSet.Config as cms

def TPGCheck(**kwargs):
  mod = cms.EDAnalyzer('TPGCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

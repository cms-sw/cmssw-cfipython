import FWCore.ParameterSet.Config as cms

def DTTtrigPrint(**kwargs):
  mod = cms.EDAnalyzer('DTTtrigPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

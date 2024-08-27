import FWCore.ParameterSet.Config as cms

def corrResps(**kwargs):
  mod = cms.EDAnalyzer('corrResps',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

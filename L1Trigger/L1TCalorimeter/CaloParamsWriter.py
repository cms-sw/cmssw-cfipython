import FWCore.ParameterSet.Config as cms

def CaloParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('CaloParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

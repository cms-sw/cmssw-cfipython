import FWCore.ParameterSet.Config as cms

def DTTPGParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('DTTPGParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

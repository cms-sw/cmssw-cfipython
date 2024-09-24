import FWCore.ParameterSet.Config as cms

def CaloParamsWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
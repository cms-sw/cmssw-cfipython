import FWCore.ParameterSet.Config as cms

def ZdcTBAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ZdcTBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

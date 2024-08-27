import FWCore.ParameterSet.Config as cms

def CaloSimParametersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CaloSimParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

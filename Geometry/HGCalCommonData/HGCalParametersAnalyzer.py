import FWCore.ParameterSet.Config as cms

def HGCalParametersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HGCalParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

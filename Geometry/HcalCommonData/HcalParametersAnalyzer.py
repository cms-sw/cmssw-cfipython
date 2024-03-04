import FWCore.ParameterSet.Config as cms

def HcalParametersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

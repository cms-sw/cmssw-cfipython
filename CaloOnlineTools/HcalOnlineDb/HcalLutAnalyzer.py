import FWCore.ParameterSet.Config as cms

def HcalLutAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalLutAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

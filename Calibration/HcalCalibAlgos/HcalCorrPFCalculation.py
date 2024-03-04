import FWCore.ParameterSet.Config as cms

def HcalCorrPFCalculation(**kwargs):
  mod = cms.EDAnalyzer('HcalCorrPFCalculation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

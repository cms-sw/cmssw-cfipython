import FWCore.ParameterSet.Config as cms

def HcalPulseContainmentTest(**kwargs):
  mod = cms.EDAnalyzer('HcalPulseContainmentTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

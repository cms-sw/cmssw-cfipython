import FWCore.ParameterSet.Config as cms

def HcalDigitizerTest(**kwargs):
  mod = cms.EDAnalyzer('HcalDigitizerTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

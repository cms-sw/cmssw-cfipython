import FWCore.ParameterSet.Config as cms

def HcalDigiAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

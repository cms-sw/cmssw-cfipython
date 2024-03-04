import FWCore.ParameterSet.Config as cms

def HcalSevLvlAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalSevLvlAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

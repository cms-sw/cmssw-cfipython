import FWCore.ParameterSet.Config as cms

def HcalRecoParamsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HcalLongRecoParamsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalLongRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

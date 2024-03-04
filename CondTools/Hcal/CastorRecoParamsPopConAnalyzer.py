import FWCore.ParameterSet.Config as cms

def CastorRecoParamsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

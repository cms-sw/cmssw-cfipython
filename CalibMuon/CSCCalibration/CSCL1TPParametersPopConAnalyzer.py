import FWCore.ParameterSet.Config as cms

def CSCL1TPParametersPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCL1TPParametersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

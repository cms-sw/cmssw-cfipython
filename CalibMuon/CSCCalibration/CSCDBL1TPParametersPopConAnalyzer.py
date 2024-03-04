import FWCore.ParameterSet.Config as cms

def CSCDBL1TPParametersPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCDBL1TPParametersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

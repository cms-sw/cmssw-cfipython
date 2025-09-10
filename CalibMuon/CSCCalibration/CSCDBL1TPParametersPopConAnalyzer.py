import FWCore.ParameterSet.Config as cms

def CSCDBL1TPParametersPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCDBL1TPParametersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def CSCL1TPParametersPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCL1TPParametersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

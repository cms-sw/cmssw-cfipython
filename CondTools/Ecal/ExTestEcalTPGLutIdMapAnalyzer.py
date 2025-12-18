import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLutIdMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLutIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLutIdMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLutIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

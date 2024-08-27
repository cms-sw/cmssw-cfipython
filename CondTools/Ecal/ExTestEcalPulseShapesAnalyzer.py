import FWCore.ParameterSet.Config as cms

def ExTestEcalPulseShapesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPulseShapesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

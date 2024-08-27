import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainStripEEAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainStripEEAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainStripEEAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainStripEEAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

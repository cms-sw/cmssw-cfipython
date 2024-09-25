import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainTowerEEAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainTowerEEAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

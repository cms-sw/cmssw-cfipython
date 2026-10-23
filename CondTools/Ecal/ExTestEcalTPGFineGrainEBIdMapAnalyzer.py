import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainEBIdMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainEBIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

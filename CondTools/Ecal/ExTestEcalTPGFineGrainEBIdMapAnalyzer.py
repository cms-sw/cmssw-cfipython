import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainEBIdMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainEBIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

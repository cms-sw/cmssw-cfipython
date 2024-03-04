import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainTowerfromFile(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainTowerfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainStripfromFile(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainStripfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPedfromFile(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPedfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

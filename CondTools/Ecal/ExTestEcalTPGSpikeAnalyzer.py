import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGSpikeAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGSpikeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

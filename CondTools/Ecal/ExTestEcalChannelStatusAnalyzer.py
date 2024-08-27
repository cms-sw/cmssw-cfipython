import FWCore.ParameterSet.Config as cms

def ExTestEcalChannelStatusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalChannelStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

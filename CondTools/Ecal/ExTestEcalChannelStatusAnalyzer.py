import FWCore.ParameterSet.Config as cms

def ExTestEcalChannelStatusAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalChannelStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalGraphDumperModule(**kwargs):
  mod = cms.EDAnalyzer('EcalGraphDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

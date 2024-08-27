import FWCore.ParameterSet.Config as cms

def EcalPnGraphDumperModule(**kwargs):
  mod = cms.EDAnalyzer('EcalPnGraphDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

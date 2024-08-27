import FWCore.ParameterSet.Config as cms

def EcalHexDumperModule(**kwargs):
  mod = cms.EDAnalyzer('EcalHexDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

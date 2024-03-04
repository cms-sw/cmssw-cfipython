import FWCore.ParameterSet.Config as cms

def EcalDigiDumperModule(**kwargs):
  mod = cms.EDAnalyzer('EcalDigiDumperModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalSimpleTBAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalSimpleTBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

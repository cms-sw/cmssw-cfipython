import FWCore.ParameterSet.Config as cms

def EcalSimple2007H4TBAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalSimple2007H4TBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalObjectAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalObjectAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

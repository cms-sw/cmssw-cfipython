import FWCore.ParameterSet.Config as cms

def EcalTPInputAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTPInputAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

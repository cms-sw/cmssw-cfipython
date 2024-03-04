import FWCore.ParameterSet.Config as cms

def EcalHexDisplay(**kwargs):
  mod = cms.EDAnalyzer('EcalHexDisplay',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

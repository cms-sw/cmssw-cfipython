import FWCore.ParameterSet.Config as cms

def EcalDisplaysByEvent(**kwargs):
  mod = cms.EDAnalyzer('EcalDisplaysByEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

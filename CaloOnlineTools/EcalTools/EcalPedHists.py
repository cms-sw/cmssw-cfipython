import FWCore.ParameterSet.Config as cms

def EcalPedHists(**kwargs):
  mod = cms.EDAnalyzer('EcalPedHists',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

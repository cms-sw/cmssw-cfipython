import FWCore.ParameterSet.Config as cms

def EcalPedOffset(**kwargs):
  mod = cms.EDAnalyzer('EcalPedOffset',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

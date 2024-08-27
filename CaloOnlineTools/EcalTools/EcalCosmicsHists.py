import FWCore.ParameterSet.Config as cms

def EcalCosmicsHists(**kwargs):
  mod = cms.EDAnalyzer('EcalCosmicsHists',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

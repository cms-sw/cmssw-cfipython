import FWCore.ParameterSet.Config as cms

def EcalPerEvtMatacqAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalPerEvtMatacqAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

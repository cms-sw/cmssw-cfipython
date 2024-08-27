import FWCore.ParameterSet.Config as cms

def EcalDCSTowerStatusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalDCSTowerStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

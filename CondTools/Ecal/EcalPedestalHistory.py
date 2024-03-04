import FWCore.ParameterSet.Config as cms

def EcalPedestalHistory(**kwargs):
  mod = cms.EDAnalyzer('EcalPedestalHistory',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

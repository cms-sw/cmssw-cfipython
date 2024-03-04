import FWCore.ParameterSet.Config as cms

def ECALMultifitAnalyzer_HI(**kwargs):
  mod = cms.EDProducer('ECALMultifitAnalyzer_HI',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

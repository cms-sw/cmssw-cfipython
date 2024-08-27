import FWCore.ParameterSet.Config as cms

def TTbar_GenLepAnalyzer(**kwargs):
  mod = cms.EDProducer('TTbar_GenLepAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

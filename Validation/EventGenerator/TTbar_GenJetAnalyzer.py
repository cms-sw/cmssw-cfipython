import FWCore.ParameterSet.Config as cms

def TTbar_GenJetAnalyzer(**kwargs):
  mod = cms.EDProducer('TTbar_GenJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

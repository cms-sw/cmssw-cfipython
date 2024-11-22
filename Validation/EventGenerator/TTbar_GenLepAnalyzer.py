import FWCore.ParameterSet.Config as cms

def TTbar_GenLepAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('TTbar_GenLepAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

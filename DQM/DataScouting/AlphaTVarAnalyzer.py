import FWCore.ParameterSet.Config as cms

def AlphaTVarAnalyzer(**kwargs):
  mod = cms.EDProducer('AlphaTVarAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

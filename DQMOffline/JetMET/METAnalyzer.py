import FWCore.ParameterSet.Config as cms

def METAnalyzer(**kwargs):
  mod = cms.EDProducer('METAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

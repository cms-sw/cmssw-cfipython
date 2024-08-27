import FWCore.ParameterSet.Config as cms

def MiniAODTaggerAnalyzer(**kwargs):
  mod = cms.EDProducer('MiniAODTaggerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

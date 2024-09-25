import FWCore.ParameterSet.Config as cms

def MiniAODTaggerAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MiniAODTaggerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MiniAODTagInfoAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MiniAODTagInfoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MiniAODSVAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MiniAODSVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

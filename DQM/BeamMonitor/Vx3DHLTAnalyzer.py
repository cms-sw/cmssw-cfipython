import FWCore.ParameterSet.Config as cms

def Vx3DHLTAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('Vx3DHLTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

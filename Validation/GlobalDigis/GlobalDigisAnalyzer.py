import FWCore.ParameterSet.Config as cms

def GlobalDigisAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('GlobalDigisAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

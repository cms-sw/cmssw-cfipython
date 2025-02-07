import FWCore.ParameterSet.Config as cms

def METAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('METAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

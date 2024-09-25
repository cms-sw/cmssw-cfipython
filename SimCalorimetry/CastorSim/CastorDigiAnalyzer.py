import FWCore.ParameterSet.Config as cms

def CastorDigiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

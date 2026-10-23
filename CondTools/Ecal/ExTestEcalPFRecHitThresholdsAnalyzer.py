import FWCore.ParameterSet.Config as cms

def ExTestEcalPFRecHitThresholdsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPFRecHitThresholdsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

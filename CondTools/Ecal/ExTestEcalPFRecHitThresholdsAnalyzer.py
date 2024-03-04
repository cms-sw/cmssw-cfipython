import FWCore.ParameterSet.Config as cms

def ExTestEcalPFRecHitThresholdsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPFRecHitThresholdsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

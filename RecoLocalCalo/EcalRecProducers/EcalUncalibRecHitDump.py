import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitDump(**kwargs):
  mod = cms.EDAnalyzer('EcalUncalibRecHitDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

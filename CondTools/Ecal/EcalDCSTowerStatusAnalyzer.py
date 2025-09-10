import FWCore.ParameterSet.Config as cms

def EcalDCSTowerStatusAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDCSTowerStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

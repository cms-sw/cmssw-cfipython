import FWCore.ParameterSet.Config as cms

def EcalContainmentCorrectionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalContainmentCorrectionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

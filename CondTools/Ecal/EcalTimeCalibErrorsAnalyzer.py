import FWCore.ParameterSet.Config as cms

def EcalTimeCalibErrorsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTimeCalibErrorsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

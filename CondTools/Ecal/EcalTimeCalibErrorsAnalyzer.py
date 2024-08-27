import FWCore.ParameterSet.Config as cms

def EcalTimeCalibErrorsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTimeCalibErrorsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

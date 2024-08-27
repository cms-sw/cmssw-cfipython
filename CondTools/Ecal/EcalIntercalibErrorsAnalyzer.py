import FWCore.ParameterSet.Config as cms

def EcalIntercalibErrorsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibErrorsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

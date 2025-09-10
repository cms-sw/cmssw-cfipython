import FWCore.ParameterSet.Config as cms

def EcalIntercalibErrorsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibErrorsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

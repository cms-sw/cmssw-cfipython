import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

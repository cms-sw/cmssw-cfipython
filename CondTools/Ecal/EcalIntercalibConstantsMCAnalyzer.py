import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsMCAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsMCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

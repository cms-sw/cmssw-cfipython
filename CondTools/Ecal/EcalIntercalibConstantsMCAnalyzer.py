import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsMCAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsMCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

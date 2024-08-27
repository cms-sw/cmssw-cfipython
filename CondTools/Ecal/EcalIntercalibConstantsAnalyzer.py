import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

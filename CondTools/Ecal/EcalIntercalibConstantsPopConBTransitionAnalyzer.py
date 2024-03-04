import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsPopConBTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

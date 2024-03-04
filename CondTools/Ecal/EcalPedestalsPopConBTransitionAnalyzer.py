import FWCore.ParameterSet.Config as cms

def EcalPedestalsPopConBTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalPedestalsPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

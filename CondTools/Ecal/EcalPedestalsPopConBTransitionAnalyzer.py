import FWCore.ParameterSet.Config as cms

def EcalPedestalsPopConBTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPedestalsPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

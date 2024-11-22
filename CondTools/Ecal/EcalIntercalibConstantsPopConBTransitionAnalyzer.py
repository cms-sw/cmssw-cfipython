import FWCore.ParameterSet.Config as cms

def EcalIntercalibConstantsPopConBTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalIntercalibConstantsPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

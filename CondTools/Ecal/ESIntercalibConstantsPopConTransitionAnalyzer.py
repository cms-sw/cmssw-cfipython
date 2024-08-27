import FWCore.ParameterSet.Config as cms

def ESIntercalibConstantsPopConTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ESIntercalibConstantsPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

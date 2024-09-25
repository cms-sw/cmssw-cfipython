import FWCore.ParameterSet.Config as cms

def EcalMatacqHist(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalMatacqHist',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalPerEvtMatacqAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPerEvtMatacqAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

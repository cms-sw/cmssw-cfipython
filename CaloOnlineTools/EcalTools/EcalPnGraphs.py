import FWCore.ParameterSet.Config as cms

def EcalPnGraphs(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPnGraphs',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

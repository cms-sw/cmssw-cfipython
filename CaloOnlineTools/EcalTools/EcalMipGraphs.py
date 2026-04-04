import FWCore.ParameterSet.Config as cms

def EcalMipGraphs(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalMipGraphs',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

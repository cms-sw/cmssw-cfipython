import FWCore.ParameterSet.Config as cms

def EcalMipGraphs(**kwargs):
  mod = cms.EDAnalyzer('EcalMipGraphs',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

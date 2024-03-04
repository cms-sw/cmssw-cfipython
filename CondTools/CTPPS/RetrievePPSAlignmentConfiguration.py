import FWCore.ParameterSet.Config as cms

def RetrievePPSAlignmentConfiguration(**kwargs):
  mod = cms.EDAnalyzer('RetrievePPSAlignmentConfiguration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

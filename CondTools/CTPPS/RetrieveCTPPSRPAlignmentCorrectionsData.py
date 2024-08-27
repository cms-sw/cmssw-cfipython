import FWCore.ParameterSet.Config as cms

def RetrieveCTPPSRPAlignmentCorrectionsData(**kwargs):
  mod = cms.EDAnalyzer('RetrieveCTPPSRPAlignmentCorrectionsData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

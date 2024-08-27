import FWCore.ParameterSet.Config as cms

def WritePPSAlignmentConfiguration(**kwargs):
  mod = cms.EDAnalyzer('WritePPSAlignmentConfiguration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

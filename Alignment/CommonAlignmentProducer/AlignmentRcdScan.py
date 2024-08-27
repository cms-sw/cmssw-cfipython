import FWCore.ParameterSet.Config as cms

def AlignmentRcdScan(**kwargs):
  mod = cms.EDAnalyzer('AlignmentRcdScan',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

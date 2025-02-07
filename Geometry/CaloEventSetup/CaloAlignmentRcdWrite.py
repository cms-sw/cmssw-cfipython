import FWCore.ParameterSet.Config as cms

def CaloAlignmentRcdWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloAlignmentRcdWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

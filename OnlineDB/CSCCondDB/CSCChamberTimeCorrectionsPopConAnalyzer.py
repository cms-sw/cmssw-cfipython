import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCChamberTimeCorrectionsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
